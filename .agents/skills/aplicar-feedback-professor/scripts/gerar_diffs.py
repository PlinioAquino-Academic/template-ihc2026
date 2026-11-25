#!/usr/bin/env python3
"""Gera um HTML com os diffs de uma rodada de feedback, lado a lado, em markdown renderizado.

Cada commit aparece com o trecho literal do parecer do professor que o motivou.

Uso (na raiz do repositório):
    python3 .agents/skills/aplicar-feedback-professor/scripts/gerar_diffs.py spec.json saida.html

Formato do spec.json: veja references/diff-html.md. Requer `pip install markdown`;
ImageMagick (`convert`) é usado para comprimir imagens raster, se disponível.
"""
import base64, difflib, html, json, re, shutil, subprocess, sys
import markdown

SPEC_PATH, OUT = sys.argv[1:3]
SPEC = json.load(open(SPEC_PATH, encoding='utf-8'))
REPO = subprocess.run(['git', 'rev-parse', '--show-toplevel'], capture_output=True, text=True).stdout.strip() or '.'
BASE = SPEC['base']
TITLE = SPEC.get('titulo', 'Diffs do feedback')


def _gh_base():
    url = subprocess.run(['git', '-C', REPO, 'remote', 'get-url', 'origin'], capture_output=True, text=True).stdout.strip()
    m = re.search(r'github\.com[:/]+([^/]+/[^/]+?)(?:\.git)?$', url)
    if m:
        return f'https://github.com/{m.group(1)}/commit/'
    m = re.search(r'/git/([^/]+/[^/]+?)(?:\.git)?$', url)
    return f'https://github.com/{m.group(1)}/commit/' if m else ''


GH = _gh_base()


def git(*a, binary=False):
    r = subprocess.run(['git', '-C', REPO, *a], capture_output=True)
    if r.returncode != 0:
        return None
    return r.stdout if binary else r.stdout.decode('utf-8')


# ---------------------------------------------------------------- blocos
LIST_RE = re.compile(r'^(\s*)([-*+]|\d+\.)\s')


def split_blocks(text):
    """Divide o markdown em blocos. Linhas de tabela viram blocos próprios."""
    lines = text.split('\n')
    blocks = []
    cur = []
    i = 0

    def flush():
        nonlocal cur
        if cur:
            blocks.append({'kind': 'text', 'src': '\n'.join(cur)})
            cur = []

    while i < len(lines):
        ln = lines[i]
        if ln.strip() == '':
            flush(); i += 1; continue
        if ln.lstrip().startswith('|'):
            flush()
            tbl = []
            while i < len(lines) and lines[i].lstrip().startswith('|'):
                tbl.append(lines[i]); i += 1
            if len(tbl) >= 2 and re.match(r'^\s*\|[\s:|-]+\|\s*$', tbl[1]):
                header = tbl[0] + '\n' + tbl[1]
                # tabela só com cabeçalho: uma linha vazia mantém o cabeçalho visível no diff
                for r in tbl[2:] or ['']:
                    blocks.append({'kind': 'row', 'src': r, 'header': header})
            else:
                blocks.append({'kind': 'text', 'src': '\n'.join(tbl)})
            continue
        if ln.startswith('#'):
            flush(); blocks.append({'kind': 'text', 'src': ln}); i += 1; continue
        m = LIST_RE.match(ln)
        if m and len(m.group(1)) == 0 and cur:
            flush()
        cur.append(ln); i += 1
    flush()
    return blocks


# ---------------------------------------------------------------- diff de palavras
TOK = re.compile(r'!?\[[^\]\n]*\]\([^)\n]*\)|`[^`\n]*`|\*\*[^*\n]+\*\*|\s+|[^\s]+')
NOWRAP = re.compile(r'^(\||#+|>|[-*+]|\d+\.|\\-)$')


def tokens(s):
    return TOK.findall(s)


def mark(toks, spans, tag):
    out = []
    for i, t in enumerate(toks):
        on = spans[i]
        if on and not t.isspace() and not NOWRAP.match(t):
            out.append(f'<{tag}>{t}</{tag}>')
        else:
            out.append(t)
    return ''.join(out)


def word_diff(a, b):
    ta, tb = tokens(a), tokens(b)
    sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
    sa = [False] * len(ta)
    sb = [False] * len(tb)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op in ('replace', 'delete'):
            for k in range(i1, i2): sa[k] = True
        if op in ('replace', 'insert'):
            for k in range(j1, j2): sb[k] = True
    return mark(ta, sa, 'del'), mark(tb, sb, 'ins')


# ---------------------------------------------------------------- alinhamento
def ratio(a, b):
    return difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()


def align_group(old, new):
    """Alinhamento monótono por similaridade (DP)."""
    n, m = len(old), len(new)
    if n * m > 4000:
        pairs = [(o, None) for o in old] + [(None, x) for x in new]
        return pairs
    sim = [[0.0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if old[i]['kind'] == new[j]['kind']:
                r = ratio(old[i]['src'], new[j]['src'])
                sim[i][j] = r if r >= 0.3 else 0.0
    dp = [[0.0] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            best = max(dp[i + 1][j], dp[i][j + 1])
            if sim[i][j] > 0:
                best = max(best, sim[i][j] + dp[i + 1][j + 1])
            dp[i][j] = best
    pairs = []
    i = j = 0
    while i < n or j < m:
        if i < n and j < m and sim[i][j] > 0 and abs(dp[i][j] - (sim[i][j] + dp[i + 1][j + 1])) < 1e-9:
            pairs.append((old[i], new[j])); i += 1; j += 1
        elif i < n and (j >= m or dp[i][j] == dp[i + 1][j]):
            pairs.append((old[i], None)); i += 1
        else:
            pairs.append((None, new[j])); j += 1
    return pairs


def diff_pairs(old_text, new_text):
    ob, nb = split_blocks(old_text), split_blocks(new_text)
    sm = difflib.SequenceMatcher(None, [b['src'] for b in ob], [b['src'] for b in nb], autojunk=False)
    pairs = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            for k in range(i2 - i1):
                o, x = ob[i1 + k], nb[j1 + k]
                # mesma linha sob outro cabeçalho: a tabela mudou
                pairs.append(('eq' if o.get('header') == x.get('header') else 'ch', o, x))
        else:
            for o, x in align_group(ob[i1:i2], nb[j1:j2]):
                pairs.append(('ch', o, x))
    return pairs


# ---------------------------------------------------------------- renderização
MD = markdown.Markdown(extensions=['tables', 'sane_lists'])


def md(src):
    MD.reset()
    return MD.convert(src)


IMG_CACHE = {}
IMG_IDS = {}


def embed_images(h, rev, doc_path):
    base_dir = doc_path.rsplit('/', 1)[0] if '/' in doc_path else ''

    def repl(m):
        src = html.unescape(m.group(1))
        if src.startswith('http') or src.startswith('data:'):
            return m.group(0)
        parts = (base_dir + '/' + src).split('/') if base_dir else src.split('/')
        norm = []
        for p in parts:
            if p == '..':
                norm and norm.pop()
            elif p and p != '.':
                norm.append(p)
        path = '/'.join(norm).replace('%20', ' ')
        key = (rev, path)
        if key not in IMG_CACHE:
            data = git('show', f'{rev}:{path}', binary=True)
            if data is None:
                IMG_CACHE[key] = None
            else:
                if path.lower().endswith('.svg'):
                    IMG_CACHE[key] = 'data:image/svg+xml;base64,' + base64.b64encode(data).decode()
                elif shutil.which('convert'):
                    r = subprocess.run(['convert', '-', '-resize', '900x>', '-quality', '72', 'jpg:-'],
                                       input=data, capture_output=True)
                    IMG_CACHE[key] = 'data:image/jpeg;base64,' + base64.b64encode(r.stdout).decode()
                else:
                    ext = path.rsplit('.', 1)[-1].lower().replace('jpg', 'jpeg')
                    IMG_CACHE[key] = f'data:image/{ext};base64,' + base64.b64encode(data).decode()
        uri = IMG_CACHE[key]
        if uri is None:
            return f'src="" data-missing="{html.escape(path)}"'
        if uri not in IMG_IDS:
            IMG_IDS[uri] = f'i{len(IMG_IDS)}'
        return f'data-img="{IMG_IDS[uri]}" loading="lazy"'
    h = re.sub(r'src="([^"]+)"', repl, h)
    h = re.sub(r'<a href="(http[^"]+)"', r'<a target="_blank" rel="noopener" href="\1"', h)
    return h


def render_cell(blocks_src, rev, path):
    if not blocks_src:
        return ''
    h = md(blocks_src)
    # Python-Markdown acrescenta uma linha vazia a tabelas só com cabeçalho
    h = re.sub(r'\s*<tbody>\s*<tr>(?:\s*<td></td>)+\s*</tr>\s*</tbody>', '', h)
    return embed_images(h, rev, path)


def build_rows(pairs, old_rev, new_rev, path, ctx=1):
    n = len(pairs)
    show = [False] * n
    for i, (k, _, _) in enumerate(pairs):
        if k == 'ch':
            for d in range(-ctx, ctx + 1):
                if 0 <= i + d < n:
                    show[i + d] = True
    out = []
    i = 0
    while i < n:
        if not show[i]:
            j = i
            while j < n and not show[j]:
                j += 1
            hidden = pairs[i:j]
            # linhas de tabela ocultas: agrupa com o cabeçalho
            segs = []  # textos e [cabeçalho, linhas] de tabelas
            cur = None  # tabela em andamento
            for _, _, b in hidden:
                if b['kind'] == 'row':
                    if cur is None or cur[0] != b['header']:
                        cur = [b['header'], []]; segs.append(cur)
                    if b['src']:
                        cur[1].append(b['src'])
                else:
                    cur = None
                    segs.append(b['src'])
            segs = [sg if isinstance(sg, str) else '\n'.join([sg[0]] + sg[1]) for sg in segs]
            inner = render_cell('\n\n'.join(segs), new_rev, path)
            label = f'{j - i} bloco{"s" if j - i > 1 else ""} sem mudança'
            out.append(f'<details class="fold"><summary>⋯ {label}</summary><div class="md same">{inner}</div></details>')
            i = j
            continue
        k, o, x = pairs[i]
        # agrupa linhas de tabela consecutivas com os mesmos cabeçalhos (antigo e novo)
        if (o or x)['kind'] == 'row':
            j = i
            group = []
            ho = hn = None
            while j < n and show[j]:
                kk, oo, xx = pairs[j]
                if (oo or xx)['kind'] != 'row':
                    break
                if (oo and ho not in (None, oo['header'])) or (xx and hn not in (None, xx['header'])):
                    break
                ho = oo['header'] if oo else ho
                hn = xx['header'] if xx else hn
                group.append(pairs[j]); j += 1
            left_rows, right_rows = [], []
            changed = False
            for kk, oo, xx in group:
                if kk == 'eq':
                    left_rows.append(oo['src']); right_rows.append(xx['src'])
                else:
                    changed = True
                    if oo and xx:
                        a, b = word_diff(oo['src'], xx['src'])
                        left_rows.append(a); right_rows.append(b)
                    elif oo:
                        left_rows.append(mark_whole_row(oo['src'], 'del'))
                    else:
                        right_rows.append(mark_whole_row(xx['src'], 'ins'))
            hl, hr = ho, hn
            if ho and hn and ho != hn:
                hl, hr = header_diff(ho, hn)
            has_old = any(oo for _, oo, _ in group)
            has_new = any(xx for _, _, xx in group)
            L = render_table(hl, left_rows, old_rev, path) if has_old else ''
            R = render_table(hr, right_rows, new_rev, path) if has_new else ''
            out.append(row_html(L, R, 'tbl' + (' mod' if changed else ' ctx')))
            i = j
            continue
        if k == 'eq':
            h = render_cell(o['src'], new_rev, path)
            out.append(f'<div class="r ctx"><div class="md same full">{h}</div></div>')
        elif o and x:
            a, b = word_diff(o['src'], x['src'])
            out.append(row_html(render_cell(a, old_rev, path), render_cell(b, new_rev, path), 'mod'))
        elif o:
            out.append(row_html(render_cell(o['src'], old_rev, path), '', 'del'))
        else:
            out.append(row_html('', render_cell(x['src'], new_rev, path), 'add'))
        i += 1
    return '\n'.join(out)


def header_diff(old, new):
    """Destaca só a linha de títulos; a linha de separadores (|---|) fica intacta."""
    (ol, osep), (nl, nsep) = old.split('\n'), new.split('\n')
    a, b = word_diff(ol, nl)
    return a + '\n' + osep, b + '\n' + nsep


def render_table(hdr, rows, rev, path):
    return render_cell('\n'.join([hdr] + [r for r in rows if r]), rev, path)


def mark_whole_row(src, tag):
    if not src:
        return src
    cells = src.strip().strip('|').split('|')
    return '| ' + ' | '.join(f'<{tag}>{c.strip()}</{tag}>' if c.strip() else '' for c in cells) + ' |'


def row_html(L, R, cls):
    lc = 'md old' + ('' if L else ' empty')
    rc = 'md new' + ('' if R else ' empty')
    return f'<div class="r {cls}"><div class="{lc}">{L}</div><div class="{rc}">{R}</div></div>'


# ---------------------------------------------------------------- seções
def changed_files(a, b):
    out = git('diff', '--name-status', a, b)
    res = []
    for ln in out.strip().split('\n'):
        if not ln:
            continue
        st, *ps = ln.split('\t')
        res.append((st[0], ps[-1]))
    return res


def file_section(a, b, st, path):
    title = html.escape(path)
    if path.endswith('.md'):
        old = git('show', f'{a}:{path}') or '' if st != 'A' else ''
        new = git('show', f'{b}:{path}') or '' if st != 'D' else ''
        pairs = diff_pairs(old, new)
        nch = sum(1 for p in pairs if p[0] == 'ch')
        body = build_rows(pairs, a, b, path)
        return (f'<section class="file"><header><span class="fname">{title}</span>'
                f'<span class="badge">{nch} bloco{"s" if nch != 1 else ""} alterado{"s" if nch != 1 else ""}</span></header>'
                f'<div class="cols"><div>Antes</div><div>Depois</div></div>{body}</section>')
    if re.search(r'\.(png|jpe?g|gif)$', path, re.I) and st == 'A':
        data = git('show', f'{b}:{path}', binary=True)
        uri = 'data:image/png;base64,' + base64.b64encode(data).decode()
        if uri not in IMG_IDS:
            IMG_IDS[uri] = f'i{len(IMG_IDS)}'
        return (f'<section class="file"><header><span class="fname">{title}</span><span class="badge add">imagem nova</span></header>'
                f'<div class="r add"><div class="md old empty"></div><div class="md new"><p><img data-img="{IMG_IDS[uri]}" alt="{title}"></p></div></div></section>')
    if path.lower().endswith('.svg'):
        cells = []
        for rev, ok in ((a, st != 'A'), (b, st != 'D')):
            data = git('show', f'{rev}:{path}', binary=True) if ok else None
            if not data:
                cells.append('')
                continue
            uri = 'data:image/svg+xml;base64,' + base64.b64encode(data).decode()
            if uri not in IMG_IDS:
                IMG_IDS[uri] = f'i{len(IMG_IDS)}'
            cells.append(f'<p><img data-img="{IMG_IDS[uri]}" alt="{title}"></p>')
        return (f'<section class="file"><header><span class="fname">{title}</span><span class="badge">imagem SVG alterada</span></header>'
                f'<div class="cols"><div>Antes</div><div>Depois</div></div>{row_html(cells[0], cells[1], "mod")}</section>')
    return f'<section class="file"><header><span class="fname">{title}</span><span class="badge">{st}</span></header></section>'


PARECER = ''
if SPEC.get('parecer'):
    PARECER = git('show', f"{SPEC.get('parecer_rev', BASE)}:{SPEC['parecer']}") or ''


def citacao(c):
    """Trecho literal do parecer: de `inicio` até o fim de `fim`, ou a linha que começa em `linha`."""
    if 'linha' in c:
        i = PARECER.index(c['linha']); j = PARECER.find('\n', i)
        return PARECER[i:j if j >= 0 else None].strip()
    i = PARECER.index(c['inicio'])
    j = PARECER.index(c['fim'], i) + len(c['fim']) if c.get('fim') else PARECER.find('\n\n', i)
    return PARECER[i:j].strip()


def resolve(rev, what):
    full = (git('rev-parse', '--verify', '--quiet', f'{rev}^{{commit}}') or '').strip()
    if not full:
        sys.exit(f'Commit não encontrado ({what}): {rev}')
    return full


def conferir_rodada(base, fim, spec_items):
    """Garante que os commits de base..fim e os itens do spec sejam os mesmos e que cada item tenha citação ou nota."""
    erros = []
    commits = (git('rev-list', '--reverse', f'{base}..{fim}') or '').split()
    por_item = {resolve(it['commit'], 'item do spec'): it for it in spec_items}
    sem_item = [c for c in commits if c not in por_item]
    fora = [c for c in por_item if c not in commits]
    sem_origem = [c for c, it in por_item.items() if not it.get('citacoes') and not it.get('nota')]

    def lista(cs):
        return ''.join(f"\n  {c[:7]} {(git('log', '-1', '--format=%s', c) or '').strip()}" for c in cs)
    if sem_item:
        erros.append(f'{len(sem_item)} commit(s) de {base[:7]}..{fim[:7]} sem item no spec '
                     f'(acrescente um item com citação ou nota, ou mude `fim`):{lista(sem_item)}')
    if fora:
        erros.append(f'{len(fora)} item(ns) do spec fora de {base[:7]}..{fim[:7]} '
                     f'(confira `base`, `fim` e o campo `commit`):{lista(fora)}')
    if sem_origem:
        erros.append(f'{len(sem_origem)} item(ns) sem `citacoes` nem `nota`:{lista(sem_origem)}')
    if erros:
        sys.exit('A rodada do spec está inconsistente.\n' + '\n'.join(erros))


TIPOS = {'correcao': 'c', 'recomendacao': 'r', 'registro': 'm', 'pendencia': 'm', 'anotacao': 'm'}
FIM = resolve(SPEC['fim'], '`fim`') if SPEC.get('fim') else resolve(SPEC['itens'][-1]['commit'], 'último item')
if not SPEC.get('fim'):
    print(f'Aviso: spec sem `fim`; o Total termina no último item ({FIM[:7]}).', file=sys.stderr)
BASE = resolve(BASE, '`base`')
conferir_rodada(BASE, FIM, SPEC['itens'])
items = []
for it in SPEC['itens']:
    quotes = []
    for c in it.get('citacoes', []):
        try:
            quotes.append((c['onde'], citacao(c)))
        except ValueError:
            sys.exit(f"Âncora não encontrada no parecer para {it['commit']}: {c}")
    items.append({'h': git('rev-parse', '--short', it['commit']).strip(),
                  'cls': TIPOS.get(it.get('tipo', 'registro'), 'm'),
                  'lbl': it['rotulo'], 'title': it['titulo'],
                  'quotes': quotes, 'note': it.get('nota', '')})
sections = []
nav = []

# total
tot_files = changed_files(BASE, FIM)
stat = git('diff', '--shortstat', BASE, FIM).strip()
sections.append(('total', 'Total', f'Todas as mudanças ({BASE[:7]}..{FIM[:7]})', '',
                 ''.join(file_section(BASE, FIM, st, p) for st, p in tot_files), stat))
nav.append(('total', 'Total', 'Todas as mudanças', 't'))

def why_box(it):
    parts = []
    for where, q in it.get('quotes', []):
        parts.append(f'<div class="src">{html.escape(where)}</div><blockquote class="prof md">{md(q)}</blockquote>')
    if it.get('note'):
        parts.append(f'<p class="note"><b>Nota:</b> {html.escape(it["note"])}</p>')
    if not parts:
        return ''
    head = 'Comentário do professor que motivou esta mudança' if it.get('quotes') else 'Origem desta mudança'
    return f'<section class="why"><h3>💬 {head}</h3>{"".join(parts)}</section>'


index_rows = []
for it in items:
    h, cls, label, title = it['h'], it['cls'], it['lbl'], it['title']
    parent = git('rev-parse', f'{h}^').strip()
    files = changed_files(parent, h)
    body = why_box(it) + ''.join(file_section(parent, h, st, p) for st, p in files)
    st = git('diff', '--shortstat', parent, h).strip()
    sections.append((h, label, title, GH + h if GH else '', body, st))
    nav.append((h, label, title, cls))
    origem = '; '.join(w for w, _ in it.get('quotes', [])) or (it.get('note', '').split(':')[0] if it.get('note') else '')
    index_rows.append(f'<tr><td><a href="#s-{h}">{html.escape(label)}: {html.escape(title)}</a></td><td>{html.escape(origem)}</td><td><code>{h[:7]}</code></td></tr>')

tot = sections[0]
idx = ('<section class="why"><h3>🗺️ Qual comentário levou a cada commit</h3><div class="md"><table><thead><tr><th>Commit</th>'
       '<th>Trecho do parecer</th><th>Hash</th></tr></thead><tbody>' + ''.join(index_rows) + '</tbody></table></div></section>')
sections[0] = (tot[0], tot[1], tot[2], tot[3], idx + tot[4], tot[5])

nav_html = '\n'.join(
    f'<a href="#s-{sid}" class="k-{cls}"><span class="lbl">{html.escape(lbl)}</span>'
    f'<span class="ttl">{html.escape(t)}</span>{"" if sid == "total" else f"<code>{sid[:7]}</code>"}</a>'
    for sid, lbl, t, cls in nav)

sec_html = '\n'.join(
    f'<article id="s-{sid}"><h2><span class="lbl">{html.escape(lbl)}</span> {html.escape(t)}</h2>'
    f'<p class="meta">{"<a target=_blank href=" + url + ">" + sid[:7] + " no GitHub</a> · " if url else ""}{html.escape(st)}</p>{body}</article>'
    for sid, lbl, t, url, body, st in sections)

CSS = r"""
:root{--bg:#fbfaf8;--fg:#1d1d1f;--mut:#6b6b70;--card:#fff;--line:#e4e2dd;--del:#fde7e7;--delfg:#a3202a;--ins:#e3f5e6;--insfg:#17692b;
--delb:#f3b9bc;--insb:#a8dcb3;--acc:#3557d6;--code:#f2f1ee;--th:#f6f5f2}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#141416;--fg:#e8e6e3;--mut:#9a9aa0;--card:#1c1c1f;--line:#2e2e33;
--del:#3a1d20;--delfg:#ff9aa2;--ins:#173222;--insfg:#8be0a0;--delb:#6b2a30;--insb:#2b6a3f;--acc:#8aa4ff;--code:#26262a;--th:#222226}}
:root[data-theme="dark"]{--bg:#141416;--fg:#e8e6e3;--mut:#9a9aa0;--card:#1c1c1f;--line:#2e2e33;
--del:#3a1d20;--delfg:#ff9aa2;--ins:#173222;--insfg:#8be0a0;--delb:#6b2a30;--insb:#2b6a3f;--acc:#8aa4ff;--code:#26262a;--th:#222226}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
.wrap{display:grid;grid-template-columns:300px 1fr;min-height:100vh}
nav{position:sticky;top:0;height:100vh;overflow:auto;border-right:1px solid var(--line);padding:16px 12px;background:var(--card)}
nav h1{font-size:15px;margin:0 0 4px}
nav p{font-size:12px;color:var(--mut);margin:0 0 12px}
nav a{display:block;padding:7px 8px;border-radius:8px;color:var(--fg);text-decoration:none;font-size:13px;margin-bottom:2px}
nav a:hover{background:var(--code)}
nav .lbl{display:inline-block;font-size:10.5px;font-weight:600;text-transform:uppercase;letter-spacing:.03em;padding:1px 6px;border-radius:999px;margin-right:6px;background:var(--code);color:var(--mut)}
nav .k-c .lbl{background:#fde2c4;color:#8a4a00} nav .k-r .lbl{background:#dde6ff;color:#2a45a8}
nav .k-a .lbl{background:#e8ddff;color:#5b2fb0} nav .k-m .lbl{background:#d9f2e3;color:#1c6b3b} nav .k-t .lbl{background:var(--fg);color:var(--bg)}
nav code{display:block;font-size:11px;color:var(--mut);margin-top:2px}
nav .ttl{display:inline}
main{padding:20px 24px 80px;min-width:0}
.tools{position:sticky;top:0;z-index:5;background:var(--bg);padding:8px 0 10px;display:flex;gap:8px;align-items:center;border-bottom:1px solid var(--line);margin-bottom:12px}
.tools button{font:inherit;font-size:13px;padding:5px 10px;border:1px solid var(--line);background:var(--card);color:var(--fg);border-radius:8px;cursor:pointer}
.tools button[aria-pressed=true]{border-color:var(--acc);color:var(--acc)}
.tools .leg{font-size:12px;color:var(--mut);margin-left:auto}
.tools .leg del,.tools .leg ins{padding:0 4px}
article{margin:0 0 48px}
article h2{font-size:19px;margin:8px 0 2px}
article h2 .lbl{font-size:11px;vertical-align:middle;padding:2px 7px;border-radius:999px;background:var(--code);color:var(--mut);text-transform:uppercase}
.meta{color:var(--mut);font-size:12.5px;margin:0 0 12px}.meta a{color:var(--acc)}
.file{border:1px solid var(--line);border-radius:12px;background:var(--card);margin:0 0 18px;overflow:hidden}
.file>header{display:flex;justify-content:space-between;align-items:center;padding:9px 14px;border-bottom:1px solid var(--line);background:var(--th)}
.fname{font:600 13px ui-monospace,SFMono-Regular,Menlo,monospace}
.badge{font-size:11.5px;color:var(--mut)}
.cols{display:grid;grid-template-columns:1fr 1fr;font-size:11.5px;font-weight:600;color:var(--mut);text-transform:uppercase;letter-spacing:.04em;border-bottom:1px solid var(--line)}
.cols div{padding:5px 14px}.cols div+div{border-left:1px solid var(--line)}
.r{display:grid;grid-template-columns:1fr 1fr;border-bottom:1px solid var(--line)}
.r>.md{padding:6px 14px;min-width:0;overflow-x:auto}
.r>.md+.md{border-left:1px solid var(--line)}
.r.ctx{opacity:.62}.r.ctx .full{grid-column:1/3}
.r.del>.old{background:var(--del);box-shadow:inset 3px 0 var(--delb)}
.r.add>.new{background:var(--ins);box-shadow:inset 3px 0 var(--insb)}
.r.mod>.old{box-shadow:inset 3px 0 var(--delb)}.r.mod>.new{box-shadow:inset 3px 0 var(--insb)}
.md.empty{background:repeating-linear-gradient(135deg,transparent 0 6px,var(--code) 6px 7px)}
del{background:var(--del);color:var(--delfg);text-decoration:line-through;text-decoration-thickness:1px;border-radius:3px}
ins{background:var(--ins);color:var(--insfg);text-decoration:none;border-radius:3px}
.r.del del,.r.add ins{background:none}
details.fold{border-bottom:1px solid var(--line)}
details.fold>summary{cursor:pointer;padding:5px 14px;font-size:12px;color:var(--mut);background:var(--th);list-style:none}
details.fold>summary::-webkit-details-marker{display:none}
details.fold .md{padding:6px 14px;opacity:.75}
.md h1{font-size:20px}.md h2{font-size:18px}.md h3{font-size:16px}.md h4{font-size:15px}
.md h1,.md h2,.md h3,.md h4{margin:8px 0 6px}
.md p{margin:6px 0}.md ul,.md ol{margin:6px 0;padding-left:22px}
.md blockquote{margin:6px 0;padding:2px 12px;border-left:3px solid var(--line);color:var(--fg)}
.md table{border-collapse:collapse;font-size:12.5px;margin:6px 0;width:100%}
.md th,.md td{border:1px solid var(--line);padding:4px 7px;vertical-align:top;min-width:70px;overflow-wrap:anywhere}
.md th{background:var(--th)}
.md code{background:var(--code);padding:1px 4px;border-radius:4px;font-size:12.5px}
.md img{max-width:100%;height:auto;border-radius:6px;border:1px solid var(--line)}
.md a{color:var(--acc)}
.why{border:1px solid var(--line);border-left:4px solid var(--acc);border-radius:12px;background:var(--card);padding:10px 16px 12px;margin:0 0 18px}
.why h3{font-size:13px;text-transform:uppercase;letter-spacing:.04em;color:var(--acc);margin:4px 0 8px}
.why .src{font-size:12.5px;font-weight:600;color:var(--mut);margin:8px 0 4px}
.why blockquote.prof{margin:0 0 6px;padding:4px 14px;border-left:3px solid var(--acc);background:var(--code);border-radius:0 8px 8px 0;font-size:14px}
.why .note{font-size:13px;color:var(--mut);margin:8px 0 2px}
.why table{font-size:12.5px}.why td,.why th{max-width:520px}
body.only .r.ctx,body.only details.fold{display:none}
@media (max-width:900px){.wrap{grid-template-columns:1fr}nav{position:static;height:auto;border-right:0;border-bottom:1px solid var(--line)}
main{padding:12px 16px}}
"""

JS = r"""
document.querySelectorAll('img[data-img]').forEach(i=>{i.src=IM[i.dataset.img]});
const b=document.getElementById('only');
b.onclick=()=>{const on=document.body.classList.toggle('only');b.setAttribute('aria-pressed',on)};
"""

page = f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)}</title><style>{CSS}</style></head><body>
<div class="wrap"><nav><h1>{html.escape(TITLE)}</h1><p>Markdown renderizado, antes × depois. {html.escape(stat)}</p>{nav_html}</nav>
<main><div class="tools"><button id="only" aria-pressed="false">Só mudanças</button>
<span class="leg"><del>removido</del> <ins>acrescentado</ins> · blocos esmaecidos são contexto</span></div>
{sec_html}</main></div><script>const IM={json.dumps({v: k for k, v in IMG_IDS.items()})};{JS}</script></body></html>"""
open(OUT, 'w').write(page)
print(OUT, len(page) // 1024, 'KB')

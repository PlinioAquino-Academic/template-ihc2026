"""Gera o protótipo navegável da Entrega 11 (telas F01–F12) a partir da interface do TCC.

Uso (na raiz do repositório):
    python3 assets/11_figma/prototipo/gerar_prototipo.py            # index.html (navegável)
    python3 assets/11_figma/prototipo/gerar_prototipo.py --figma X  # X.html autocontido, todas as telas

O visual (cores, tipografia, painéis e mesa de luz) vem de `base_tcc.css`, cópia do CSS da interface
`codigo/interface/static/app.css` do TCC. `prototipo.css` acrescenta os signos revisados nas Entregas
6, 9 e 10. A radiografia é a imagem de teste do TCC (`testes/anomalia.png`) e o mapa de atenção é a
saída real do modelo de referência para essa imagem; caso, carga e responsável são fictícios.
"""
import base64
import sys
from pathlib import Path

DIR = Path(__file__).resolve().parent

CASO = {
    "id": "CASO-DEMO-0417",
    "unidade": "MSKU 000000-0",
    "carga": "Paletes de madeira",
    "peso": "18.400 kg",
}
RESP = "Gustavo Onofre"
COMENT = "Mancha mais densa no centro da carga, sem a forma regular dos paletes ao redor."
JUSTIF = "A região 1 é mais densa que o restante e não acompanha o empilhamento declarado de madeira."
REGIAO_MODELO = (299, 305, 78, 77)   # saída do modelo (305, 311, 66, 65) com margem de 6 px
MARCA = (290, 296, 96, 94)


# ---------------------------------------------------------------- blocos

def go(target, label, cls="btn"):
    return f'<a class="{cls}" href="#{target}">{label}</a>'


def topbar(com_caso=True, trocar="F11a"):
    if com_caso:
        caso = f"""
      <div class="case">
        <dl>
          <div><dt>Caso (S01)</dt><dd>{CASO['id']}</dd></div>
          <div><dt>Unidade de carga</dt><dd>{CASO['unidade']}</dd></div>
          <div><dt>Carga declarada (S13)</dt><dd>{CASO['carga']} · {CASO['peso']}</dd></div>
        </dl>
        <span class="src">Dados do caso demonstrativo · fictícios</span>
      </div>"""
        acao = go(trocar, "Trocar caso")
    else:
        caso = '<div class="case"><span class="case-empty">Nenhum caso aberto</span></div>'
        acao = ""
    return f"""
    <header class="topbar">
      <div class="brand">
        <svg class="brand-mark" viewBox="0 0 32 32" aria-hidden="true"><rect x="3" y="7" width="26" height="18" rx="1.5"/><path d="M9 7v18M15 7v18M21 7v18"/><path class="beam" d="M1 16h30"/></svg>
        <div><h1>Mesa de inspeção</h1><p class="file-name">{'anomalia.png · 640 × 640' if com_caso else 'Abra a radiografia de um caso'}</p></div>
      </div>
      {caso}
      <div class="topbar-actions">{acao}{go('F02', 'Abrir caso', 'btn btn-primary') if not com_caso else ''}</div>
    </header>"""


def tools(ativo=True, preset="Original"):
    chips = "".join(
        f'<span class="chip{" is-active" if p == preset else ""}">{p}</span>'
        for p in ("Original", "Penetração alta", "Penetração baixa", "Negativo", "Super realce"))

    def slider(nome, valor, pos=50):
        return f"""<div class="control"><label>{nome}</label><output>{valor}</output>
          <div style="grid-column:1/-1;position:relative;height:16px"><div style="position:absolute;top:6px;left:0;right:0;height:4px;border-radius:2px;background:var(--line)"></div>
          <div style="position:absolute;top:0;left:calc({pos}% - 8px);width:16px;height:16px;border-radius:50%;background:var(--text);box-shadow:0 0 0 1px var(--muted)"></div></div></div>"""

    return f"""
    <aside class="panel tools{'' if ativo else ' is-disabled'}" aria-label="Ajustes da imagem">
      <section class="group"><h2>Funções rápidas <span class="tag-cand">S17 · H43</span></h2><div class="presets">{chips}</div></section>
      <section class="group"><h2>Exposição</h2>{slider('Brilho','0')}{slider('Contraste','0')}{slider('Penetração','normal')}</section>
      <section class="group"><h2>Realce</h2>{slider('Realce local','0%',0)}{slider('Nitidez','0%',0)}{slider('Bordas','0%',0)}</section>
      <section class="group"><h2>Densidade e cor</h2>{slider('Faixa de densidade','tudo',0)}
        <div class="control"><label>Paleta</label><span class="field" style="grid-column:1/-1">Tons de cinza</span></div>
        <p class="note">Os ajustes mudam só a exibição; o original é preservado.</p></section>
    </aside>"""


def rx(img="rx_mapa.jpg", tam=640, regiao=True, marca=False, rascunho=False, rotulo=None, x=None):
    s = tam / 640
    svg = ""
    if regiao:
        rx_, ry, rw, rh = REGIAO_MODELO
        svg += f'<rect x="{rx_*s}" y="{ry*s}" width="{rw*s}" height="{rh*s}" fill="none" stroke="#f2a93b" stroke-width="2" stroke-dasharray="6 4"/>'
    if marca:
        mx, my, mw, mh = MARCA
        dash = ' stroke-dasharray="6 4"' if rascunho else ""
        svg += (f'<rect x="{mx*s}" y="{my*s}" width="{mw*s}" height="{mh*s}" fill="none" stroke="#e5654f" stroke-width="2.4"{dash}/>'
                f'<rect x="{mx*s}" y="{my*s-19}" width="21" height="19" fill="#e5654f"/>'
                f'<text x="{mx*s+10.5}" y="{my*s-5}" fill="#2b0b05" font-family="Barlow Semi Condensed" font-weight="600" font-size="13" text-anchor="middle">1</text>')
    pos = f' style="width:{tam}px;height:{tam}px' + (f';left:{x}' if x else "") + '"'
    lab = f'<span class="rx-label">{rotulo}</span>' if rotulo else ""
    return f'<div class="rx"{pos}>{lab}<img src="img/{img}" alt="Radiografia do contêiner do caso demonstrativo"><svg viewBox="0 0 {tam} {tam}">{svg}</svg></div>'


def toolbar(vista="sobreposta", ferramenta="mover", ativo=True):
    def tool(nome, alvo, icone):
        cls = "tool is-active" if ferramenta == nome.lower() else "tool"
        return f'<a class="{cls}" href="#{alvo}"><svg viewBox="0 0 24 24"><path d="{icone}"/></svg><span>{nome}</span></a>'

    def v(nome, alvo):
        return f'<a class="{"is-on" if vista == nome.lower() else ""}" href="#{alvo}">{nome}</a>'

    off = "" if ativo else ' is-disabled'
    return f"""
      <div class="stage-toolbar{off}">
        <div class="tool-set">
          {tool('Mover', 'F03', 'M12 3v18M3 12h18M12 3l-3 3M12 3l3 3M12 21l-3-3M12 21l3-3M3 12l3-3M3 12l3 3M21 12l-3-3M21 12l-3 3')}
          {tool('Lupa', 'F03', 'M10 4a6 6 0 1 0 0 12a6 6 0 1 0 0-12M14.5 14.5L20 20')}
          {tool('Marcar', 'F06', 'M4 8V4h4M16 4h4v4M20 16v4h-4M8 20H4v-4')}
        </div>
        <div class="tool-set">
          <span class="vista-label">Vista (S06)</span>
          <span class="vista">{v('Sobreposta', 'F03')}{v('Sem mapa', 'F04')}{v('Lado a lado', 'F05')}</span>
          <span class="icon-btn"><svg viewBox="0 0 24 24"><path d="M5 12h14"/></svg></span>
          <span class="zoom-level">100% <small style="opacity:.7">(S16)</small></span>
          <span class="icon-btn"><svg viewBox="0 0 24 24"><path d="M5 12h14M12 5v14"/></svg></span>
        </div>
      </div>"""


def resultado(estado="pronto"):
    if estado == "aguardando":
        corpo = '<div class="state">Análise (S03)</div><div class="cat neutral">Aguardando imagem do caso.</div>'
    elif estado == "analisando":
        corpo = '<div class="state">Análise (S03)</div><div class="cat neutral">Analisando imagem…</div><p>O resultado aparece aqui ao terminar. Os ajustes já podem ser usados.</p>'
    elif estado == "falha":
        corpo = '<div class="state">Análise (S03)</div><div class="cat neutral" style="color:#ff9b87">Sem resultado: a análise falhou.</div><p>Falha não significa “sem indício”.</p>'
    else:
        corpo = ('<div class="state">Indicação do modelo (S04) · análise concluída</div>'
                 '<div class="cat">Indício de atipicidade</div>'
                 '<p>Apoio à triagem: aponta onde a imagem diverge do esperado. '
                 'Não identifica ilícito nem substitui o seu exame.</p>')
    return f'<div class="result">{corpo}</div>'


def mapa_ctrl(mostrar=True, ativo=True):
    on = " on" if mostrar else ""
    return f"""<div class="{'' if ativo else 'is-disabled'}">
      <div class="legend-map"><i></i> mapa aproximado (S05) <b></b> maior atenção</div>
      <div class="switch{on}"><span class="box"></span>Mostrar onde o modelo olhou</div>
      <div class="switch{on}"><span class="box"></span>Destacar a região de maior atenção</div></div>"""


def regioes(estado="vazia"):
    if estado == "vazia":
        corpo = '<p class="note">Nenhuma região marcada. Use <b>Marcar</b> para registrar o que chamou sua atenção.</p>'
    else:
        txt = (f'<span class="mark-note ph">Descreva o que você viu nesta região…</span>' if estado == "sem_comentario"
               else f'<span class="mark-note">{COMENT}</span>')
        err = '<div class="err-msg">Comentário obrigatório para exportar a região.</div>' if estado == "sem_comentario" else ""
        corpo = f"""<ol class="marks"><li><div class="mark-head"><span class="mark-id">1</span><span>Região 1 · 96 × 94 px</span>
          <a href="#F03" title="Excluir região 1">Excluir</a></div><div style="margin-top:.35rem">{txt}</div>{err}
          <div class="mark-meta">Marcação humana (S07) · comentário (S08)</div></li></ol>"""
    return f'<section class="group"><h2>Regiões marcadas</h2>{corpo}</section>'


def parecer(conclusao=None, justif=None, resp=None, erros=False, ativo=True, botao=None):
    justif = bool(conclusao) if justif is None else justif
    resp = bool(conclusao) if resp is None else resp
    botao = botao or ("F08" if conclusao and justif and resp else "F10c")
    def opt(valor, cls):
        sel = " sel" if conclusao == valor else ""
        return f'<a class="decision-opt {cls}{sel}" href="#{"F11b" if valor == "Sem ressalvas na imagem" else "F07"}"><span>{valor}</span></a>'

    j = (f'<span class="field">{JUSTIF}</span>' if justif else
         f'<span class="field ph{" err" if erros else ""}">Por que esta conclusão?</span>')
    r = (f'<span class="field">{RESP}</span>' if resp else
         f'<span class="field ph{" err" if erros else ""}">Seu nome</span>')
    ej = '<div class="err-msg">Informe a justificativa.</div>' if erros and not justif else ""
    er = '<div class="err-msg">Informe o responsável.</div>' if erros and not resp else ""
    return f"""
      <section class="group final{'' if ativo else ' is-disabled'}">
        <h2>Conclusão da análise (S09)</h2>
        <div class="decision">{opt('Sem ressalvas na imagem', 'is-clear')}{opt('Suspeita apontada', 'is-hold')}</div>
        <div class="label-row"><span>Justificativa (S10)</span><span class="req">obrigatória</span></div>{j}{ej}
        <div class="label-row" style="margin-top:.5rem"><span>Responsável (S11)</span><span class="req">obrigatório</span></div>{r}{er}
        <a class="btn btn-primary btn-block" style="margin-top:.7rem" href="#{botao}">Revisar e emitir parecer</a>
        <p class="note" style="margin-top:.4rem">O parecer não libera nem retém a carga.</p>
      </section>"""


def verdict(res="pronto", mapa=True, reg="vazia", par=None, ativo=True, extra=""):
    par = par if par is not None else parecer(ativo=ativo)
    return f"""
    <aside class="panel verdict" aria-label="Análise e parecer">
      <section class="group"><h2>Análise do modelo</h2>{extra}{resultado(res)}{mapa_ctrl(mapa, ativo)}</section>
      {regioes(reg) if ativo else '<div class="is-disabled">' + regioes() + '</div>'}
      {par}
    </aside>"""


def sim(fid, links):
    itens = "".join(f'<a href="#{alvo}">{texto}</a>' for alvo, texto in links)
    return f'<div class="sim"><span class="tag">Simulação do protótipo</span>{itens}<span class="id">{fid}</span></div>'


def tela(fid, nome, corpo, links=()):
    return f'<section class="screen" id="{fid}" data-nome="{fid} — {nome}">{corpo}{sim(fid, links)}</section>'


def mesa(stage, verdict_html, tools_html=None, top=None, toolbar_html=None, overlay="", trocar="F01"):
    return f"""{top or topbar(trocar=trocar)}
    <main class="workspace">
      {tools_html or tools()}
      <section class="stage-wrap">{toolbar_html or toolbar()}<div class="stage">{stage}</div></section>
      {verdict_html}
    </main>{overlay}"""


def dialogo(titulo, texto, acoes, wide=False, extra=""):
    return f"""<div class="backdrop"><div class="dialog{' wide' if wide else ''}" role="dialog" aria-modal="true">
      <h3>{titulo}</h3>{texto}{extra}<div class="acts">{acoes}</div></div></div>"""


def previa():
    return f"""<div class="preview">
      <div class="thumb">{rx('rx_mapa.jpg', 300, regiao=False, marca=True)}</div>
      <dl>
        <dt>Caso (S01)</dt><dd>{CASO['id']} · {CASO['unidade']}</dd>
        <dt>Carga declarada</dt><dd>{CASO['carga']} · {CASO['peso']} (S13)</dd>
        <span class="sep"></span>
        <dt>Região 1 (S07)</dt><dd>{COMENT} (S08)</dd>
        <dt>Conclusão (S09)</dt><dd><b style="color:#ff9b87">Suspeita apontada</b></dd>
        <dt>Justificativa (S10)</dt><dd>{JUSTIF}</dd>
        <dt>Responsável (S11)</dt><dd>{RESP} · autoria declarada</dd>
        <dt>Data e hora (S18)</dt><dd>preenchidas na emissão (UTC−03:00)</dd>
        <span class="sep"></span>
        <dt>Modelo (S04/S05)</dt><dd>Indício de atipicidade; mapa de atenção aproximado. Separado da conclusão humana.</dd>
      </dl></div>"""


# ---------------------------------------------------------------- telas

def telas():
    t = []
    vazio_stage = """<label class="dropzone" style="cursor:pointer">
        <svg viewBox="0 0 48 48" aria-hidden="true"><rect x="6" y="12" width="36" height="24" rx="2"/><path d="M14 12v24M22 12v24M30 12v24M38 12v24"/></svg>
        <strong>Arraste a radiografia do caso para cá</strong>
        <span>ou clique para escolher um arquivo PNG ou JPEG (S02)</span>
        <span style="font-size:.8rem;color:#5b6a76;margin-top:.4rem">A identificação e a descrição da carga acompanham o caso demonstrativo.</span>
      </label>"""
    t.append(tela("F01", "Abrir caso (sem imagem)", mesa(
        f'<a href="#F02" style="position:absolute;inset:0">{vazio_stage}</a>',
        verdict("aguardando", ativo=False, par=parecer(ativo=False)),
        tools_html=tools(False), top=topbar(False), toolbar_html=toolbar(ativo=False)),
        [("F02", "Escolher anomalia.png → F02"), ("F10a", "Escolher arquivo inválido → F10a")]))

    t.append(tela("F02", "Analisando imagem", mesa(
        f"""<div class="dim">{rx('rx_original.jpg', regiao=False)}</div>
        <div class="busy"><div class="scanline"></div><p>Analisando imagem do caso… <a href="#F01" style="text-decoration:underline;margin-left:.6rem">Cancelar análise</a></p></div>""",
        verdict("analisando", mapa=False, ativo=False, par=parecer(ativo=False)), toolbar_html=toolbar(ativo=False)),
        [("F03", "Análise concluída → F03"), ("F10b", "Falha na análise → F10b"), ("F01", "Cancelar → F01")]))

    t.append(tela("F03", "Resultado — vista sobreposta", mesa(
        rx(), verdict()),
        [("F04", "Sem mapa → F04"), ("F05", "Lado a lado → F05"), ("F06", "Marcar região → F06"), ("F11b", "Concluir “Sem ressalvas” → F11b")]))

    t.append(tela("F04", "Comparar sem o mapa", mesa(
        rx("rx_original.jpg", regiao=False), verdict(mapa=False),
        toolbar_html=toolbar("sem mapa")),
        [("F03", "Sobreposta → F03"), ("F05", "Lado a lado → F05"), ("F06", "Marcar região → F06")]))

    lado = (rx("rx_original.jpg", 380, regiao=False, rotulo="Radiografia com os ajustes atuais", x="calc(25% + 6px)")
            + rx("rx_mapa.jpg", 380, rotulo="Mapa de atenção do modelo", x="calc(75% - 6px)"))
    t.append(tela("F05", "Comparar lado a lado", mesa(
        lado, verdict(), toolbar_html=toolbar("lado a lado")),
        [("F03", "Sobreposta → F03"), ("F04", "Sem mapa → F04"), ("F06", "Marcar região → F06")]))

    t.append(tela("F06", "Região marcada e comentada", mesa(
        rx(marca=True), verdict(reg="ok", par=parecer()), toolbar_html=toolbar(ferramenta="marcar"), trocar="F11a"),
        [("F07", "Preencher conclusão → F07"), ("F11a", "Trocar caso com registros → F11a"), ("F03", "Excluir região → F03")]))

    t.append(tela("F07", "Conclusão, justificativa e responsável", mesa(
        rx(marca=True), verdict(reg="ok", par=parecer("Suspeita apontada")), toolbar_html=toolbar(ferramenta="marcar"), trocar="F11a"),
        [("F08", "Revisar e emitir → F08"), ("F10c", "Emitir com campos vazios → F10c"), ("F11b", "Escolher “Sem ressalvas” → F11b")]))

    acoes = go("F07", "Voltar e corrigir") + go("F09", "Exportar PDF", "btn btn-primary")
    t.append(tela("F08", "Revisar o parecer antes de exportar", mesa(
        rx(marca=True), verdict(reg="ok", par=parecer("Suspeita apontada")), toolbar_html=toolbar(ferramenta="marcar"),
        overlay=dialogo("Revisar parecer (S12)", "<p>Confira o caso e o conteúdo. O PDF é salvo neste computador; o encaminhamento a quem decide segue o procedimento institucional, fora da Mesa.</p>",
                        acoes, wide=True, extra=previa()), trocar="F11a"),
        [("F09", "Exportação concluída → F09"), ("F10d", "Falha ao exportar → F10d"), ("F07", "Voltar → F07")]))

    ok = f"""<div class="banner ok"><span class="ico">✓</span><div><strong>Parecer exportado localmente</strong>
      parecer_{CASO['id']}.pdf · emitido em 17/11/2026 03:12 (UTC−03:00).<br>O envio a quem decide não é feito pela Mesa.
      <div class="acts">{go('F12', 'Ver documento', 'btn btn-sm')}{go('F01', 'Abrir outro caso', 'btn btn-sm')}</div></div></div>"""
    t.append(tela("F09", "Parecer exportado", mesa(
        rx(marca=True) + f'<div class="stage-top">{ok}</div>', verdict(reg="ok", par=parecer("Suspeita apontada")), toolbar_html=toolbar(ferramenta="marcar")),
        [("F12", "Ver o PDF → F12"), ("F01", "Abrir outro caso → F01")]))

    inval = f"""<div class="stage-msg error"><h3>Não foi possível abrir “manifesto.pdf”</h3>
      <p>A Mesa aceita radiografias PNG ou JPEG. Nada foi analisado e nenhum dado do caso foi alterado.</p>
      <p>Se a radiografia estiver corrompida, obtenha uma nova cópia no sistema de origem.</p>
      <div class="acts">{go('F01', 'Escolher outro arquivo', 'btn btn-primary btn-sm')}</div></div>"""
    t.append(tela("F10a", "Erro: arquivo inválido", mesa(
        vazio_stage + inval, verdict("aguardando", ativo=False, par=parecer(ativo=False)),
        tools_html=tools(False), top=topbar(False), toolbar_html=toolbar(ativo=False)),
        [("F01", "Escolher outro arquivo → F01")]))

    falha = f"""<div class="stage-msg error"><h3>Não foi possível analisar a imagem</h3>
      <p>O serviço de análise local não respondeu. Não há resultado do modelo para este caso: isso não equivale a “sem indício”.</p>
      <p>A radiografia continua aberta; você pode examiná-la com os ajustes enquanto decide.</p>
      <div class="acts">{go('F02', 'Tentar novamente', 'btn btn-primary btn-sm')}{go('F01', 'Cancelar e voltar', 'btn btn-sm')}</div></div>"""
    t.append(tela("F10b", "Erro: falha na análise", mesa(
        rx("rx_original.jpg", regiao=False) + falha, verdict("falha", mapa=False, ativo=False, par=parecer(ativo=False)),
        toolbar_html=toolbar(ativo=False)),
        [("F02", "Tentar novamente → F02"), ("F01", "Cancelar → F01")]))

    aviso = """<div class="banner error"><span class="ico">!</span><div><strong>Faltam 3 itens para emitir</strong>
      Comentário da região 1 · Justificativa · Responsável. Os demais dados foram mantidos.</div></div>"""
    t.append(tela("F10c", "Erro: parecer incompleto", mesa(
        rx(marca=True) + f'<div class="stage-top">{aviso}</div>', verdict(reg="sem_comentario", par=parecer("Suspeita apontada", justif=False, resp=False, erros=True, botao="F10c")),
        toolbar_html=toolbar(ferramenta="marcar"), trocar="F11a"),
        [("F07", "Completar os campos → F07")]))

    erro_exp = """<div class="banner error" style="margin:.2rem 0 .6rem"><span class="ico">!</span><div><strong>Falha ao exportar</strong>
      Não foi possível salvar o PDF na pasta escolhida (sem permissão ou sem espaço). Seus registros foram mantidos.</div></div>"""
    acoes_err = go("F07", "Voltar ao parecer") + go("F09", "Tentar novamente", "btn btn-primary")
    t.append(tela("F10d", "Erro: falha na exportação", mesa(
        rx(marca=True), verdict(reg="ok", par=parecer("Suspeita apontada")), toolbar_html=toolbar(ferramenta="marcar"),
        overlay=dialogo("Revisar parecer (S12)", erro_exp, acoes_err, wide=True, extra=previa()), trocar="F11a"),
        [("F09", "Tentar novamente → F09"), ("F07", "Voltar → F07")]))

    troca = dialogo("Trocar de caso?",
                    "<p>Este caso tem registros que ainda não foram exportados:</p><ul><li>1 região marcada com comentário</li><li>Conclusão e justificativa</li></ul><p>Ao trocar, esses registros serão descartados. A radiografia original não é alterada.</p>",
                    go("F06", "Manter caso", "btn btn-primary") + go("F01", "Descartar e trocar", "btn btn-danger"))
    t.append(tela("F11a", "Confirmar troca de caso", mesa(
        rx(marca=True), verdict(reg="ok", par=parecer("Suspeita apontada")), toolbar_html=toolbar(ferramenta="marcar"), overlay=troca, trocar="F11a"),
        [("F06", "Manter caso → F06"), ("F01", "Descartar → F01")]))

    div = dialogo("Sua conclusão difere da indicação do modelo",
                  "<p>Você escolheu <b>Sem ressalvas na imagem</b>, e o modelo indicou <b>indício de atipicidade</b> na região destacada.</p><p>Discordar é permitido: a conclusão é sua. Confirme que revisou a região e explique o motivo na justificativa.</p>",
                  go("F03", "Rever a imagem") + go("F07", "Confirmar e justificar", "btn btn-primary"))
    t.append(tela("F11b", "Confirmar conclusão divergente", mesa(
        rx(), verdict(par=parecer("Sem ressalvas na imagem", justif=False)), overlay=div, trocar="F11a"),
        [("F03", "Rever a imagem → F03"), ("F07", "Confirmar → F07")]))

    pdf = f"""
    <header class="reader-bar"><b>parecer_{CASO['id']}.pdf</b><span class="muted">Leitor de PDF do destinatário · externo à Mesa</span>
      <span class="muted" style="margin-left:auto">Página 1 de 2 · 100%</span></header>
    <div class="reader"><div class="page">
      <h1>Parecer técnico de apoio — análise de imagem de raio-X</h1>
      <p class="sub">Mesa de inspeção · protótipo demonstrativo do TCC · dados fictícios</p>
      <h4>Identificação</h4>
      <table><tr><td>Caso (S01)</td><td>{CASO['id']}</td></tr><tr><td>Unidade de carga</td><td>{CASO['unidade']}</td></tr>
        <tr><td>Carga declarada (S13)</td><td>{CASO['carga']} · {CASO['peso']}</td></tr>
        <tr><td>Responsável (S11)</td><td>{RESP} (autoria declarada, sem assinatura institucional)</td></tr>
        <tr><td>Emitido em (S18)</td><td>17/11/2026 03:12 (UTC−03:00), relógio da estação</td></tr></table>
      <h4>Achado registrado</h4>
      <div class="two"><div style="position:relative;width:210px;height:210px">{rx('rx_original.jpg', 210, regiao=False, marca=True)}</div>
        <div><b>Região 1 (S07)</b><br>{COMENT} (S08)<br><br><b>Conclusão da análise (S09):</b> Suspeita apontada<br>
        <b>Justificativa (S10):</b> {JUSTIF}</div></div>
      <h4>Apoio automático</h4>
      <p style="margin:0">Indicação do modelo (S04): indício de atipicidade. O mapa de atenção (S05) aparece na página 2 e é aproximado. O modelo não identifica o tipo de ilícito; a conclusão acima é do responsável.</p>
      <div class="limit"><b>Limites deste documento (S12).</b> Parecer de apoio: não é ato de despacho e não libera nem retém a carga. Dúvidas sobre o conteúdo devem ser tratadas com o emissor pelo canal institucional.</div>
    </div></div>"""
    t.append(tela("F12", "Parecer em PDF lido pelo destinatário (P02)", pdf,
                  [("F09", "Voltar à Mesa (P01) → F09")]))
    return t


def pagina(todas=False, embutir=False):
    css = (DIR / "fonts.css").read_text() + (DIR / "base_tcc.css").read_text() + (DIR / "prototipo.css").read_text()
    html = "\n".join(telas())
    if embutir:
        for nome in ("rx_mapa.jpg", "rx_original.jpg"):
            dado = base64.b64encode((DIR / "img" / nome).read_bytes()).decode()
            html = html.replace(f'src="img/{nome}"', f'src="data:image/jpeg;base64,{dado}"')
        css = css.replace('url("fonts/', 'url("' + (DIR / "fonts").as_uri() + "/")
    ids = [("F01", "F01"), ("F02", "F02"), ("F03", "F03"), ("F04", "F04"), ("F05", "F05"), ("F06", "F06"),
           ("F07", "F07"), ("F08", "F08"), ("F09", "F09"), ("F10a", "F10a"), ("F10b", "F10b"), ("F10c", "F10c"),
           ("F10d", "F10d"), ("F11a", "F11a"), ("F11b", "F11b"), ("F12", "F12")]
    nav = "".join(f'<a href="#{i}">{n}</a>' for i, n in ids)
    return f"""<!doctype html>
<html lang="pt-BR" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=1440">
<title>Mesa de inspeção — protótipo F01–F12</title>
<style>{css}</style>
</head>
<body class="{'todas' if todas else ''}">
{html}
<nav class="proto-nav"><b>Protótipo da Entrega 11.</b> Clique nos controles da tela ou na faixa “Simulação do protótipo”. Ir para: {nav}</nav>
<script>
  // Sem âncora, abre F01. Cada tela é uma âncora (#F03 etc.); os controles são links entre elas.
  if (!document.body.classList.contains("todas") && !location.hash) document.getElementById("F01").classList.add("is-default");
  addEventListener("hashchange", () => document.querySelectorAll(".is-default").forEach(e => e.classList.remove("is-default")));
</script>
</body>
</html>
"""


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--figma":
        Path(sys.argv[2]).write_text(pagina(todas=True, embutir=True))
    else:
        (DIR / "index.html").write_text(pagina())

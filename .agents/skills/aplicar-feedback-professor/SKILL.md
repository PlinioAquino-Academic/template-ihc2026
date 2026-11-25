---
name: aplicar-feedback-professor
description: Aplica o parecer do professor de uma entrega (feedbacks_professor/Feedback_Professor_EntregaNN_Equipe09.md) aos documentos do projeto, com plano prévio, um commit por item, anotações assinadas no parecer e um HTML de diffs renderizados que cita o comentário que motivou cada mudança. Use sempre que alguém da equipe (Kawan, Gabriel ou Alexandre) pedir para aplicar, tratar, responder ou corrigir o feedback, parecer ou comentários do professor de qualquer entrega, mesmo que não diga "skill" nem cite o arquivo.
---

# Aplicar feedback do professor

Aplique o parecer de uma entrega nas partes que cabem a quem está pedindo, deixe registrado no próprio parecer como cada comentário foi tratado e mostre as mudanças de forma que a pessoa consiga conferir cada uma contra o comentário que a motivou.

O fluxo foi construído aplicando os pareceres das Entregas 1 a 3. Os exemplos citados aqui estão no histórico da branch `aplicar-feedback`.

## 1. Identificar quem aplica e o que é de quem

Descubra quem está aplicando: pergunte se não estiver claro pela conversa. `git config user.name` ajuda, mas não substitui a confirmação. A pessoa assina as anotações com o próprio nome (`\- Kawan`, `\- Gabriel` ou `\- [Nome do usuário]`). O nome do usuário deve constar nos membros do projeto.

O escopo é **o trabalho individual de quem aplica e o trabalho de grupo**. O trabalho individual dos outros integrantes fica com eles: não reescreva, só registre no parecer o que ficou pendente e com quem.

Para atribuir autoria, use nesta ordem:

1. Campos `Autor(a):` e `Autor:` dentro do documento.
2. O próprio parecer, que costuma dizer quem responde por quê (por exemplo, "Kawan responde por P01").
3. A seção "Histórico de revisões" do documento e `git log --format='%h %ad %an %s' --date=short -- <arquivo>`.

Seções rotuladas "equipe" podem ter sido escritas por uma só pessoa. Quando a atribuição for ambígua, pergunte e dê uma recomendação. Um ajuste mínimo de coerência em material alheio é aceitável quando decorre de uma decisão de grupo, como trocar a linha "Tipo" de uma ficha após redefinir a composição das personas. Diga isso na anotação.

## 2. Levantar o estado atual

- Leia o parecer inteiro e o documento da entrega (`docs/NN_*.md`), além do que ele referencia: `RASTREABILIDADE.md`, entregas vizinhas e imagens e SVGs citados.
- Verifique se alguém já aplicou parte do parecer. Compare a data do commit que adicionou o parecer (`git log --format='%h %ad %s' -- feedbacks_professor/`) com os commits posteriores nos arquivos afetados. Commits anteriores ao parecer são o material avaliado, não correções.
- Procure pendências que pareceres anteriores deixaram para esta entrega, por exemplo uma hipótese reformulada na Entrega 1 que ainda aparece com a redação antiga.
- Confirme a branch de trabalho e sincronize com `git fetch`. Use a branch combinada com a equipe e não abra PR sem pedido.

## 3. Apresentar o plano antes de editar

Antes de mudar qualquer arquivo, mostre um panorama curto organizado por item do parecer (Correção 1, 2, ..., recomendações, pontos para as próximas entregas). Para cada item, diga o que vai mudar, onde, e se fica com outra pessoa. Separe o que é decisão de quem aplica, como escolher qual persona vira primária ou como tratar uma afirmação que não dá para comprovar, e ofereça opções com uma recomendação. Espere a confirmação.

Quando um comentário pedir algo que não pode ser verificado agora (um registro que não existe, um site bloqueado pela rede), prefira delimitar a afirmação e marcá-la `[?]` a inventar uma comprovação. Se usar busca na web no lugar do site oficial, diga isso à pessoa para que ela confira.

Detalhes inventados para proto-personas, como idade, trajetória e episódios, são aceitáveis quando o parecer pede caracterização, desde que fiquem marcados `[H]` como escolha da proto-persona. Proponha valores concretos no plano e destaque que a pessoa pode trocá-los.

## 4. Aplicar, um commit por item

Faça um commit por item do parecer, na ordem do plano, para que cada anotação aponte para um commit que trata só daquele comentário. Mensagem em português, no padrão `Entrega NN: <o que mudou>`, com um corpo curto dizendo o que mudou e por quê. Siga as regras de atribuição de commit do ambiente.

Convenções dos documentos, que valem para todo texto acrescentado:

- Português do Brasil. Marque cada afirmação com `[F]` fato, `[H]` hipótese ou `[?]` lacuna, como o resto do documento.
- Sem travessões (em-dash). Use ponto ou vírgula.
- O texto descreve o estado atual. Não escreva o que havia na versão anterior ("antes dizia...", "foi corrigido...") nem notas como "(revisado em DD/MM)" no meio do texto. A data da revisão fica só no cabeçalho e no histórico.
- Hipóteses novas recebem o próximo ID livre (`grep -o -E '^\| ?H[0-9]+' RASTREABILIDADE.md | tail -1`) e entram na tabela de `RASTREABILIDADE.md` com origem, estado, como investigar e decisão afetada. Não reaproveite IDs.
- Ao mudar um mapa de empatia ou outra figura que tenha versão textual, atualize a tabela e o SVG juntos e renderize o SVG para conferir (Playwright: `NODE_PATH=$(npm root -g) node` com `page.goto('file://...svg')` e `screenshot`).
- Mantenha âncoras estáveis: títulos como `### Persona P02 — Dr. Eduardo Resende (Auditor-Fiscal da Receita Federal)` são alvos de links em outros arquivos.

Feche a rodada com um commit de registro:

- No cabeçalho do documento, `**Data:** <original> (versão original)` e uma linha `**Revisão:** DD/MM/AAAA, aplicação do [feedback do professor](../feedbacks_professor/<arquivo>)`.
- Uma entrada no histórico de revisões do documento, se ele tiver um.
- Em `RASTREABILIDADE.md`, uma linha na tabela da seção 5 (registro de mudanças de escopo). As linhas da tabela da seção 5 ficam contíguas: uma linha em branco entre elas quebra a tabela.

## 5. Anotar o parecer

Depois dos commits de conteúdo, anote o arquivo do parecer em um commit separado. O texto do professor fica intacto; as anotações entram em blocos de citação. O formato está em [references/anotacoes.md](references/anotacoes.md): uma tabela de situação no topo e um bloco assinado após cada item, com o link do commit.

As anotações dependem dos hashes. Por isso, não reescreva commits já enviados (sem `rebase`, `amend` ou `push --force` depois do push). Se precisar corrigir algo, faça um commit novo e acrescente-o à anotação.

Envie com `git push -u origin <branch>`.

## 6. Gerar o HTML de diffs

Gere o HTML com os diffs renderizados (markdown à esquerda e à direita, palavras removidas e acrescentadas destacadas). No topo de cada commit vai o trecho literal do parecer que o motivou:

```bash
pip install markdown   # uma vez
python3 .agents/skills/aplicar-feedback-professor/scripts/gerar_diffs.py <spec.json> <saida.html>
```

O formato do `spec.json` e como escolher as âncoras das citações estão em [references/diff-html.md](references/diff-html.md), com um exemplo completo da Entrega 3 de outro projeto (as personas e os nomes do exemplo não são desta equipe). Informe no spec o `base` e o `fim` da rodada (o último commit, normalmente o das anotações). O script recusa gerar o HTML se algum commit desse intervalo ficar sem item. Salve o spec e o HTML fora do repositório (área temporária ou scratchpad): o HTML passa de 1 MB porque embute as imagens. Confira se nenhum commit ficou sem citação ou nota e envie o arquivo para a pessoa.

## 7. Fechar com a pessoa

Responda em poucas linhas:

- o que entrou, por item;
- o que ficou com outros integrantes;
- os pontos que ela precisa conferir, como detalhes inventados e conflitos com documentos de outros autores;
- o hash final enviado.

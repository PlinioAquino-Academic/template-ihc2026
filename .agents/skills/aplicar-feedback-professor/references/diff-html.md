# HTML de diffs com citações do parecer

`scripts/gerar_diffs.py` monta uma página com:

- uma aba "Total", com o diff de todos os commits da rodada (de `base` até `fim`) e um índice "qual comentário levou a cada commit";
- uma seção por commit, com o trecho literal do parecer que o motivou e o diff renderizado de cada arquivo alterado.

Nos arquivos `.md`, o diff é feito por blocos: parágrafos, itens de lista e linhas de tabela. Cada lado da tabela usa o próprio cabeçalho, e uma mudança só nos títulos das colunas conta como mudança e aparece em "Só mudanças". Dentro de cada bloco, palavras removidas e acrescentadas aparecem destacadas, e o markdown é renderizado nos dois lados. Imagens novas e SVGs alterados aparecem lado a lado. Há um botão "Só mudanças" que esconde o contexto.

## Formato do spec.json

```json
{
  "titulo": "Entrega 3: diffs do feedback",
  "base": "538c3dd",
  "fim": "25fc482",
  "parecer": "feedbacks_professor/Feedback_Professor_Entrega03_Equipe09.md",
  "parecer_rev": "1f73b32",
  "itens": [
    {
      "commit": "1dde02e",
      "tipo": "correcao",
      "rotulo": "Correção 1",
      "titulo": "P01 e P03 primárias; P02 persona atendida",
      "citacoes": [
        {"onde": "Correção prioritária 1: ...", "inicio": "Na seção de personas", "fim": "efetivamente serão apoiadas."},
        {"onde": "Recomendação de melhoria", "linha": "- Justifiquem a classificação"}
      ],
      "nota": "Opção escolhida por Gabriel: ..."
    }
  ]
}
```

| Campo | Significado |
|---|---|
| `base` | Commit anterior ao primeiro commit da rodada. |
| `fim` | Último commit da rodada, normalmente o das anotações. O "Total" compara `base..fim`, então o HTML não muda quando a branch recebe commits novos. Se faltar, vale o commit do último item e o script avisa. |
| `parecer_rev` | Um commit em que o parecer ainda não tem anotações, normalmente o último antes do commit de anotações. As citações saem dessa versão, para não citar as próprias anotações. |
| `tipo` | `correcao`, `recomendacao`, `pendencia`, `registro` ou `anotacao`. Define a cor do rótulo no menu. |
| `citacoes` | Trechos literais do parecer. Use `inicio` e `fim` (o trecho vai do começo de `inicio` até o fim de `fim`) ou `linha` (a linha inteira que contém o texto). |
| `nota` | Texto curto exibido abaixo das citações. Use para explicar decisões ou dizer quem ficou com o restante. Commits que não vêm do parecer, como o de anotações ou o de registro, levam só nota. |

O script confere a rodada antes de gerar o HTML. Todo commit de `base..fim` precisa ter um item no spec, e todo item precisa estar nesse intervalo e ter `citacoes` ou `nota`. Se algo faltar, o script lista os commits (hash e título) e não gera o arquivo. Um commit posterior à rodada fica de fora mudando o `fim`.

As âncoras precisam existir literalmente no parecer, com as mesmas aspas e acentos. O script interrompe com uma mensagem quando não encontra uma âncora. Copie o começo e o fim do trecho direto do arquivo.

Exemplo completo, que reproduz o HTML da Entrega 3 (`538c3dd..25fc482`, 9 itens): [exemplo-spec-entrega03.json](exemplo-spec-entrega03.json).

## Conferência

Abra o HTML e confira:

- se nenhuma imagem quebrou;
- se cada commit tem citação ou nota;
- se o console do navegador está sem erros.

Com Playwright, `NODE_PATH=$(npm root -g) node` e um script curto que abre o arquivo, conta `img[data-img]` sem `src` e coleta erros de `console` e `pageerror`.

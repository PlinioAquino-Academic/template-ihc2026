# Formato das anotações no parecer

O parecer anotado serve para o professor e para a equipe verem, comentário por comentário, o que foi feito e onde. O texto original do professor não muda. As anotações são blocos de citação (`>`) inseridos logo depois de cada item e terminam com a assinatura de quem aplicou.

Os links de commit usam a URL do repositório: `[`abc1234`](https://github.com/p4cs-974/projeto-ihc/commit/abc1234)`.

## Tabela de situação no topo

Logo abaixo do título `# Feedback do Professor > Entrega NN > Equipe 09`:

```markdown
> **Status da aplicação (DD/MM/AAAA):** esta revisão cobre <partes de quem aplica> e as partes de grupo da entrega: <seções>. <Partes individuais dos outros> ficam com seus autores. Cada comentário abaixo traz uma anotação com o link para o commit correspondente, na branch `aplicar-feedback`. O texto original do professor foi preservado; as anotações aparecem em blocos de citação logo após cada item.
>
> | Item do parecer | Situação | Commit(s) |
> |---|---|---|
> | Correção 1: <resumo> | aplicada | [`abc1234`](https://github.com/p4cs-974/projeto-ihc/commit/abc1234) |
> | Correção 2: <resumo> | aplicada em <parte>; <outra parte> fica com <nome> | [`def5678`](...) |
> | Recomendação: <resumo> | aplicada | [`...`](...) |
> | Pendência da Entrega N: <resumo> | aplicada | [`...`](...) |
>
> \- Gabriel
```

## Bloco depois de cada item

Escolha o tipo pelo resultado:

- `✅ Como foi tratado`: o item foi aplicado inteiro.
- `🟨 Tratado em parte`: uma parte foi aplicada e o resto fica com alguém.
- `⏭️ Fora desta revisão`: o item é inteiro de outro integrante.
- `ℹ️ Encaminhamento`: o item não pede mudança agora, como questões para entregas futuras.

```markdown
> **✅ Como foi tratado** ([`abc1234`](https://github.com/p4cs-974/projeto-ihc/commit/abc1234)): <o que mudou, onde, e qual decisão foi tomada>. <O que fica com quem, se for o caso>.
>
> \- Gabriel
```

Um item pode ter dois blocos dentro da mesma citação, separados por `>`, quando parte foi tratada e parte ficou com outra pessoa (`🟨` seguido de `⏭️`).

Itens em lista, como as recomendações, levam o bloco indentado com dois espaços, e uma linha em branco antes do próximo item da lista:

```markdown
- **Recomendação do professor.** Texto original.

  > **✅ Como foi tratado** ([`abc1234`](...)): ...
  >
  > \- Gabriel

- Próxima recomendação.
```

Depois da lista numerada da "Síntese das ações recomendadas", um bloco `**Situação:**` resume em uma ou duas frases o que foi aplicado e o que ficou com quem.

## Regras de escrita das anotações

- Escreva o que foi feito no estado atual dos documentos, com nomes de seções e IDs (`H39`, `RC05`, `P01`), não o que havia antes.
- Cite quem ficou com o quê pelo nome.
- A assinatura é `\- Nome`. A barra impede que o markdown transforme o hífen em lista.
- Sem travessões. Frases curtas.

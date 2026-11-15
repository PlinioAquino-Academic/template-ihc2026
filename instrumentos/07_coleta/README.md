# Instrumentos online da Entrega 7

Criados em **05/11/2026**. Os instrumentos estão publicados; não foram aplicados. A [Entrega 7](../../docs/07_coleta_dados.md) registra objetivos, público, ética, procedimentos e análise. As perguntas de I02 ficam exclusivamente no formulário online; o código local apenas consulta os links existentes.

| Instrumento | Acesso para leitura/preenchimento | Edição pela equipe |
|---|---|---|
| I02 — Questionário, Gabriel | [Abrir questionário](https://docs.google.com/forms/d/e/1FAIpQLSdSndNp5FioH8sv7jDSutkHYdAmeOqOeKNn247wJcviVF-Pkg/viewform) | [Editar](https://docs.google.com/forms/d/1oxMqGPpMAJ3TN2_hBkf4w9bmwdtfrLn6T1TFNv9LkFQ/edit) |
| I03 — Entrevista, Alexandre | [Abrir roteiro](https://docs.google.com/forms/d/e/1FAIpQLSfsc7UUP9KlAzQQzuqxQjVzSOzdyPg5rU0ag7LPhFXdi7pfGg/viewform) | [Editar](https://docs.google.com/forms/d/1_yuRgM6ilwdGepLaH4PZddhkT0oRkj6iZUr1WPa1Ku8/edit) |

Os links de edição exigem permissão da conta proprietária; conhecer o endereço não concede acesso. O roteiro I03 serve ao entrevistador para organizar notas, não substitui uma conversa conduzida por ele.

## Verificação

- Acesso às duas seções de cada formulário em sessão sem login.
- Conteúdo conferido com os roteiros do repositório; campos de explicação/correção são opcionais.
- Coleta de e-mail e limitação de uma resposta por conta desativadas.
- Consentimento inicial; o código configura a recusa para encerrar antes das perguntas.
- Nenhuma resposta enviada durante a conferência. Capturas vazias em [assets/07_coleta](../../assets/07_coleta/).

Uma eventual recusa enviada não deve contar como resposta válida. Antes de aplicação, a equipe deve definir o canal para pedidos de exclusão por código e restringir o acesso às respostas brutas. As respostas não devem ser publicadas no repositório.

## Manutenção

O [projeto no Apps Script](https://script.google.com/home/projects/1pnhS6OUvm2rhswMvrKRRakXRe-88Z5PIljkYtO9kIy4lLqHdVib6VcKg/edit) e os links de edição exigem permissão da conta proprietária. O arquivo local `criar_formularios.gs` contém somente `consultarInstrumentosEntrega7`, sem criação ou cópia das perguntas. Alterações do questionário devem ser feitas no próprio Forms; não recriar a versão antiga a partir do histórico Git.

Referência técnica: Google, [FormApp](https://developers.google.com/apps-script/reference/forms/form-app) e [Form](https://developers.google.com/apps-script/reference/forms/form).

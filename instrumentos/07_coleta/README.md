# Instrumentos online da Entrega 7

Criados em **05/11/2026**. Os instrumentos estão publicados; não foram aplicados. A [Entrega 7](../../docs/07_coleta_dados.md) registra objetivos, público, ética, procedimentos e análise. As perguntas de I02 ficam exclusivamente no formulário online; o código local apenas consulta os links existentes.

| Instrumento | Acesso para leitura/preenchimento | Edição pela equipe |
|---|---|---|
| I02 — Questionário, Gabriel | [Abrir questionário](https://docs.google.com/forms/d/e/1FAIpQLSdSndNp5FioH8sv7jDSutkHYdAmeOqOeKNn247wJcviVF-Pkg/viewform) | [Editar](https://docs.google.com/forms/d/1oxMqGPpMAJ3TN2_hBkf4w9bmwdtfrLn6T1TFNv9LkFQ/edit) |
| I03 — Entrevista, Alexandre | [Abrir roteiro](https://docs.google.com/forms/d/e/1FAIpQLSfsc7UUP9KlAzQQzuqxQjVzSOzdyPg5rU0ag7LPhFXdi7pfGg/viewform) | [Editar](https://docs.google.com/forms/d/1_yuRgM6ilwdGepLaH4PZddhkT0oRkj6iZUr1WPa1Ku8/edit) |

Os links de edição exigem permissão da conta proprietária; conhecer o endereço não concede acesso. O roteiro I03 serve ao entrevistador para organizar notas, não substitui uma conversa conduzida por ele.

## Verificação

- Acesso às duas seções de cada formulário em sessão sem login.
- Conferência original em 05/11/2026; não comprova atualização dos formulários após o feedback de 15/11/2026.
- Coleta de e-mail e limitação de uma resposta por conta desativadas.
- Consentimento inicial; o código configura a recusa para encerrar antes das perguntas.
- Nenhuma resposta enviada durante a conferência. Capturas vazias em [assets/07_coleta](../../assets/07_coleta/).

Uma eventual recusa não conta como resposta válida. As respostas brutas não devem ser publicadas no repositório.

## Pendências online após o feedback de 15/11/2026

- I02: inserir a prancha real `assets/06_prototipos/mesa_inspecao.png`, com ampliação e acesso durante as respostas, atualizar a abertura e operacionalizar o campo de código. Conteúdo de perguntas permanece exclusivamente online; a análise admite retirar/substituir score.
- I03: sincronizar abertura autossuficiente e orientações de aprofundamento com o protocolo da Entrega 7; continua ferramenta de notas do entrevistador.
- Confirmar contato privado da equipe para exclusão e informar data exata em cada convite, sem consolidar antes dela.
- Verificar os dois fluxos publicados sem login, sem enviar respostas de pesquisa, e preservar captura vazia da versão efetivamente revisada.

[F] O controle de navegador estava indisponível durante esta revisão. Nenhuma dessas alterações online foi declarada como executada. Capturas atuais são da versão original; não iniciar aplicação antes de concluir a verificação. O planejamento e o fluxo de exclusão estão na Entrega 7.

## Manutenção

O [projeto no Apps Script](https://script.google.com/home/projects/1pnhS6OUvm2rhswMvrKRRakXRe-88Z5PIljkYtO9kIy4lLqHdVib6VcKg/edit) e os links de edição exigem permissão da conta proprietária. O arquivo local `criar_formularios.gs` contém somente `consultarInstrumentosEntrega7`, sem criação ou cópia das perguntas. Alterações do questionário devem ser feitas no próprio Forms; não recriar a versão antiga a partir do histórico Git.

Referência técnica: Google, [FormApp](https://developers.google.com/apps-script/reference/forms/form-app) e [Form](https://developers.google.com/apps-script/reference/forms/form).

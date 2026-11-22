# Entrega 12 — Planejamento da avaliação de usabilidade (DECIDE)

**Data:** 12/11/2026  
**Status:** 🟨 em andamento
**Responsabilidade:** 1 solução por equipe

## Objetivo da atividade

Planejar a avaliação antes de executá-la, ligando perguntas de avaliação a métodos, participantes, tarefas, métricas, aspectos práticos, ética e forma de análise.

## O que está sendo avaliado

Em projetos cuja interface foi criada ou ampliada para a disciplina, o plano deve declarar explicitamente que a avaliação investiga **a qualidade da interação/protótipo**, não a validade científica ou o desempenho técnico do algoritmo/modelo do TCC.

Exemplos de perguntas:

- o DBA consegue localizar e comparar duas execuções?
- o analista entende o significado de um indicador?
- o administrador consegue alterar uma permissão sem risco de erro não percebido?
- o usuário compreende que o processamento está em andamento e consegue recuperar-se de uma falha?
- os filtros ajudam a localizar o histórico relevante?
- um relatório permite identificar a informação necessária para a decisão?

Se o protótipo utiliza dados ou resultados simulados, documente isso no plano.

## A. Método DECIDE

| Etapa | Aplicação no projeto |
|---|---|
| **D — Determine the goals** | **Qual é o objetivo do teste?** Descobrir em que ponto uma pessoa pode planejar a reposição com base em um valor mal interpretado ou corrigir o estoque sem evidência. Avaliar se ela conclui a tarefa, entende o resultado e consegue retomá-la após uma interrupção. |
| **E — Explore the questions** | **Que perguntas a avaliação deve responder?** Quem repõe o produto consegue dizer quantas unidades ainda pode vender e o que ficou registrado? Quem confere o estoque sabe quando corrigir a duplicidade e quando manter o caso em aberto? Que dificuldades e dúvidas surgem até chegar a essas decisões? A seção B indica a evidência para cada pergunta. |
| **C — Choose the evaluation paradigm and techniques** | Na Entrega 13, cada integrante inspecionará individualmente as telas e os estados disponíveis usando as dez heurísticas de Nielsen. Depois, a dupla consolidará os problemas. Na Entrega 14, observará participantes realizando tarefas e ouvirá suas explicações após cada tentativa. A inspeção antecipa dificuldades. A observação mostra quais delas ocorreram durante o uso. |
| **I — Identify the practical issues** | Na Entrega 13, os integrantes farão a inspeção individual e consolidarão os achados. Antes da Entrega 14, farão um piloto, identificarão a versão de coleta e convidarão uma pessoa por perfil. Paulo moderará a sessão de reposição e Victor a de conferência. Em cada sessão, o outro integrante registrará os dados. |
| **D — Decide how to deal with ethical issues** | Antes do pré-teste, explicar o uso da janela do Figma e da voz para avaliar a interação e obter aceite escrito. Usar os códigos U01 e U02 e dados fictícios. A pessoa pode recusar, interromper a gravação ou retirar a participação. Se recusar a gravação, agradecer e encerrar sem coleta. O termo informa quem terá acesso e o prazo de descarte. |
| **E — Evaluate, interpret and present the data** | A dupla reunirá as observações por tarefa e meta. Cada achado indicará o que ocorreu, a consequência para o trabalho e a mudança proposta. A versão avaliada acompanhará os resultados para permitir a repetição do caso após uma revisão. |


## B. Perguntas de avaliação

| ID | Pergunta | Método | Métrica/evidência | Critério esperado |
|---|---|---|---|---|
| QA01 | Quem faz reposição ou conferência consegue concluir e conferir o registro do seu item sem ajuda? | Observação da primeira tentativa do caso A de cada perfil | Desfecho, ajuda e registro final | MU01: ao menos 80% por tarefa. Com uma pessoa prevista por tarefa principal, a meta exige uma conclusão independente em uma tentativa avaliável (1 de 1). |
| QA02 | Quem decide a reposição explica quantas unidades estão livres, o que a estimativa informa e o que acontece ao salvar? | Perguntas abertas após os casos A e B de reposição | Explicação sobre disponibilidade, incerteza, ausência de previsão e efeito de salvar | MU02: todos os elegíveis explicam os quatro pontos, inclusive que previsão ausente não indica demanda zero e que a compra ainda depende de contato com o fornecedor. |
| QA03 | Quanto tempo cada pessoa leva para obter e conferir um desfecho? | Observação cronometrada | Tempo ativo da primeira tentativa independente do caso A | MU03: até 180 s na reposição e 300 s na conferência, por participante. |
| QA04 | Ao revisar uma correção, a pessoa consegue prever seu efeito no saldo? Se faltar a confirmação de que o saldo foi salvo, a tela indica como verificar o registro? | Inspeção do feedback, da prevenção e da recuperação em F12, F12E/F12F e F06E/F06R. Observação das decisões nos casos A e B. | Registrar a mensagem e a ação disponível na inspeção. Na sessão, anotar o desfecho escolhido, a evidência considerada e o efeito que a pessoa atribui ao registro. | MU04 exige zero erros críticos por tentativa. Os estados de falha ao salvar serão inspecionados. O plano não prevê provocar essa falha nas sessões. |
| QA05 | Como a pessoa avalia a experiência de realizar a tarefa e por quê? | Pergunta pós-tarefa | Nota de 1 a 5 e justificativa nas palavras do participante | MU05: nota mínima 4 por pessoa e tarefa. |
| QA06 | Ao receber outro produto em situação equivalente, a pessoa consegue repetir o trabalho sozinha? | Duas execuções sem instrução entre elas | Comparação de conclusão, ajuda e erro crítico | MU06 fica fora da coleta atual. Com variante equivalente, todos os elegíveis devem concluir a segunda execução sem ajuda e sem erro crítico. |
| QA07 | Após uma interrupção de balcão, a pessoa reconhece onde parou e o que precisa fazer? | Observação de execução separada com pausa | Tempo desde o retorno até identificar item, estado de salvamento e próxima ação. Observar eventual duplicação. | MU07: até 30 s após o retorno e nenhum registro duplicado. |


| Item | Planejamento |
|---|---|
| Perfis | Uma pessoa que decide reposições em pequeno comércio, preferencialmente com pouca familiaridade com sistemas de estoque, e uma pessoa que confere mercadorias e movimentações. |
| Critérios de inclusão/exclusão | Convidar adultos com experiência na atividade correspondente. Registrar familiaridade digital e contato prévio com o projeto. Integrantes da equipe e a pessoa do piloto ficam fora da amostra final. |
| Nº de participantes | Dois participantes finais previstos, um por integrante da equipe. Cada pessoa fará os casos da atividade que conhece. Recrutamento por conveniência a realizar antes das sessões; registrar apenas U01 e U02 no relatório público. Não é necessário publicar nomes de participantes para completar este plano. |
| Ambiente | Sessão presencial individual em sala tranquila, com notebook e os dois integrantes. Isso permite apresentar os mesmos dados e medir tempos com menos interferências. A pausa de balcão reproduz uma situação do comércio, mas a sessão não reproduz o movimento da loja nem a pressão de uma compra real. |
| Dispositivo | Planejado um notebook com navegador e mouse. Registrar dispositivo, zoom e eventuais adaptações de leitura. |
| Protótipo/versão | [Estoque Inteligente no Figma](https://www.figma.com/proto/jgB0Bk5BLQ3XM2W9tgZDmd/Estoque-Inteligente?page-id=0%3A1&node-id=2-2&starting-point-node-id=2%3A2&scaling=scale-down), versão da Entrega 11 de 11/11/2026. A referência corresponde aos 28 quadros documentados; o link pode mudar e não congela a versão. Após as correções da inspeção, Paulo preservará uma cópia identificada com data e revisão; a dupla verificará os caminhos no piloto. Registrar nas fichas a revisão efetivamente utilizada e manter essa versão nas duas sessões finais. A preservação e o piloto ainda serão executados. |
| Teste piloto | Antes da coleta, um integrante representará o participante e o outro conduzirá o roteiro. Verificar abertura das telas, legibilidade, neutralidade dos enunciados e cronometragem. Reservar 25–35 minutos por sessão e ajustar a previsão após o piloto. Em caso de falha de conexão, suspender o cronômetro e registrar o trecho inviabilizado. |
| Responsáveis e contato | Paulo Andre de Oliveira Hirata modera U01 e Victor Merker Binda observa; em U02, Victor modera e Paulo observa. Para dúvidas e retirada, utilizar o contato de Victor já confirmado na Entrega 7: victor.merker.bindaa@gmail.com. Victor enviará os convites e atenderá pedidos de esclarecimento ou retirada pelo endereço indicado no termo. |
| Recrutamento e agenda | A dupla convidará uma pessoa por perfil, verificará experiência na atividade e disponibilidade e agendará individualmente após o piloto. Datas e local exatos serão registrados nas fichas quando confirmados. Se o perfil for aproximado, justificar a escolha e sua limitação antes da sessão. |
| Armazenamento e descarte | Paulo guardará os vídeos e notas por código em pasta local protegida por senha, fora do GitHub. A dupla manterá aceites e chave de identificação separados. Apenas Paulo e Victor terão acesso aos registros individuais, com exibição privada da gravação ao docente se necessária para correção. Descartar vídeos, cópias de trabalho, notas, chave e aceites em até 30 dias após a divulgação da correção final. O repositório receberá somente a síntese desidentificada. |
| Modalidade de registro | Uma gravação por participante em sala virtual privada, durante a sessão presencial. Após o aceite e o pré-teste, o observador inicia a captura apenas da janela do Figma e do áudio do participante e do moderador, com câmeras desligadas. Gravar da leitura da primeira tarefa até o fim do pós-teste para conferir ações, ajudas, tempos e explicações. Pausar a pedido. O observador também preenche a ficha. |

Antes das sessões finais, a dupla registrará a revisão do Figma e ensaiará os dois fluxos. No piloto, reproduzirá um trecho com dados fictícios para conferir a leitura da tela, as duas vozes e o salvamento local. O moderador explicará o termo antes de abrir a gravação e o observador manterá as notificações e as câmeras desligadas.

## D. Lista de tarefas de avaliação

| ID | Cenário neutro entregue ao usuário | Objetivo oculto da avaliação | Critério de sucesso | Tempo-limite (se houver) |
|---|---|---|---|---|
| UT01 · T01-A | É segunda-feira. O fornecedor recebe pedidos até o meio-dia e prevê entregar na quinta. Veja a situação da garrafa térmica azul de 500 ml e deixe registrado como pretende proceder. | O01/M01. Observar como a pessoa identifica o item e fundamenta a decisão. | Reconhece 4 unidades disponíveis (6 físicas, 2 reservadas), considera o prazo e os dados de procura, explica o motivo e confere o registro. Aceitar 4 ou 6 unidades e outros desfechos disponíveis quando sustentados pela análise. | Meta de 3 min. Aos 6 min, oferecer ajuda ou encerramento, conforme a Entrega 8. |
| UT02 · T01-B | Em outro ciclo, você precisa decidir sobre a mesma garrafa. Use as informações disponíveis hoje e deixe registrado como dará continuidade ao trabalho. | O01/M01. Verificar interpretação de informação ausente. | Identifica a lacuna e registra o que precisa verificar antes de decidir. Confere a pendência salva. | Sem meta de tempo. |
| UT03 · T02-A | A loja está conferindo 14 registros. A proprietária quer saber por que há uma diferença no estoque do conjunto de três potes. Investigue o que aconteceu e diga a ela como ficou esse item. | O02/M02. Observar se a pessoa investiga a origem antes de ajustar o saldo. | Usa o conjunto como unidade. Confirma nas fontes a transcrição duplicada da mesma saída de 2 conjuntos, corrige apenas a duplicação, confere o saldo 10 e comunica o alcance parcial. | Meta de 5 min. Aos 10 min, oferecer ajuda ou encerramento, conforme a Entrega 8. |
| UT04 · T02-B | Em outra conferência do mesmo item, os registros e a contagem também divergem. Hoje você dispõe apenas dos documentos apresentados. Deixe o caso em condições de ser acompanhado pela proprietária. | O02/M02. Verificar como a pessoa atua com evidência insuficiente. | Preserva o saldo registrado, informa a dúvida e a próxima verificação. Comunica o que continua em aberto. | Sem meta de tempo. |
| UT05 · retomada | Você está no meio dessa atividade quando precisa atender alguém no balcão. Ao voltar, identifique onde parou e continue o trabalho. | O09/M01 ou M02. Observar reconhecimento do contexto. | Identifica o item, o estado do registro e a próxima ação. Retoma sem duplicar a operação. | Pausa de 30 s. Meta de retomada de até 30 s depois do retorno. |
| UT06 · repetição equivalente | Em outro ciclo, faça o mesmo trabalho para o item que recebeu agora. | MU06. Medir autonomia com outro produto e outros valores. | Conclui a segunda execução sem ajuda e sem erro crítico. | Sem meta de tempo. Requer variante equivalente. |

**Ordem e cobertura.** Na reposição, iniciar UT01 na visão geral (F01), abrir UT02 diretamente no caso sem previsão (F02B) e preparar UT05 na pausa de reposição (F02P). Na conferência, iniciar UT03 na visão geral (F01), abrir UT04 na identificação da divergência (F10) e preparar UT05 na pausa de conferência (F10P). Para cada perfil, reiniciar o cenário entre as três tentativas e medir a retomada separadamente. No Figma, a pausa disponível ocorre durante a análise dos dados (F02P ou F10P). O cronômetro da retomada começa quando a pessoa volta a ver esse estado. A versão atual tem apenas um produto por perfil. Por isso, **MU06 ficará não avaliada nesta versão**. Se a equipe preparar uma variante equivalente antes da coleta, inserir UT06 entre A e B, sem ensinar a solução entre as tentativas. Alterar apenas a quantidade planejada da mesma garrafa não produz essa variante.

## E. Instrumentos

Os instrumentos específicos já estão incorporados às Entregas 13 e 14. Serão usados diretamente, sem criar cópias genéricas nem arquivos adicionais de questionário ou planilha.

- [Termo de consentimento adaptado](../assets/14_testes/termo_consentimento.md): modelo do projeto para leitura, esclarecimento e aceite antes do pré-teste. O termo identifica Victor como responsável pelo convite e traz seu contato para dúvidas e retirada. O aceite abrange a captura da janela do Figma e do áudio conforme a seção C. Guardar a via assinada na pasta privada.
- [Roteiro e tarefas da Entrega 14](14_observacao_usuario.md#passo-5--tarefas): instruções neutras, estados de início, critérios, respostas da consulta simulada a Mariana, ordem e regras de cronometragem. U01 fará UT01, UT02 e UT05/M01; U02 fará UT03, UT04 e UT05/M02.
- [Protocolo do moderador](14_observacao_usuario.md#passo-6--protocolo-do-moderador): abertura, consentimento, condução, intervenções, perguntas posteriores e encerramento. Não exigir verbalização contínua; registrar falas espontâneas e perguntar após a tentativa, fora do tempo medido.
- [Pré-teste](14_observacao_usuario.md#passo-2--participantes) e [perguntas pós-tarefa/pós-teste](14_observacao_usuario.md#passo-6--protocolo-do-moderador): experiência, frequência, ferramentas e adaptações; compreensão dos dados e do desfecho; satisfação de 1 a 5 com justificativa; dúvidas e sugestões. A escala é própria do projeto, não SUS nem SEQ.
- [Fichas de resultados por participante](14_observacao_usuario.md#c-resultados--por-participante): usar as tabelas U01/U02 para sucesso, erros, ajudas, tempos, satisfação e evidências. Nas notas restritas, registrar data, versão, ambiente, início/fim, pausas, ações e intervenções. Consolidar nas seções D–G da mesma entrega.
- [Fichas de inspeção da Entrega 13](13_avaliacao_heuristica.md): usar as seções dos avaliadores A01 e A02 para identificação, cobertura H1–H10, violações, evidências, severidade e boas práticas. Consolidar somente depois das duas inspeções independentes, nas seções 7 e 8.

A dupla usará o mesmo termo, os mesmos critérios e as perguntas correspondentes ao perfil nas duas sessões.

## F. Plano de análise

- **Desfecho.** Sucesso total exige alcançar e conferir o resultado correto com autonomia. Registrar sucesso parcial quando houver progresso pertinente, mas faltar uma etapa essencial ou for preciso orientar a conclusão. Registrar falha quando houver erro crítico, desfecho incorreto ou abandono por dificuldade. Se a pessoa pedir orientação e preferir recebê-la, encerrar e cronometrar a tentativa independente antes de ajudar. Uma tentativa inviabilizada pelo equipamento ou por tela ausente será registrada como *não avaliada*. A retirada de consentimento será tratada conforme o termo.
- **Ocorrências.** Anotar dúvida quando a pessoa verbalizar incerteza. Contar como ajuda uma orientação do moderador que revele o próximo passo. Registrar consulta à ajuda da interface separadamente. Anotar abandono quando a pessoa decidir encerrar e distinguir dificuldade de interação de retirada de consentimento. Um desvio corrigido antes de salvar será classificado como erro recuperado. Um ajuste sem evidência, um registro duplicado, um produto ou unidade errados no registro final ou uma declaração indevida de conferência total serão erros críticos.
- **Tempo e satisfação.** Iniciar a contagem após a leitura do cenário e encerrar quando a pessoa conferir o desfecho ou interromper a tarefa. Guardar o tempo total e descontar do tempo ativo apenas pausas e esperas comprovadas. Registrar, por pessoa e tarefa, a nota de satisfação de 1 a 5 e o motivo apresentado. Fazer as perguntas de compreensão e satisfação após encerrar a cronometragem. Recusa de resposta será dado ausente.
- **Comparação.** Para MU01, informar sucessos independentes sobre primeiras tentativas avaliáveis do caso A, por tarefa. Incluir no denominador as tentativas assistidas ou malsucedidas. Mostrar, por exemplo, o resultado na forma “x de y”, com tempos individuais. Para MU02–MU07, confrontar cada observação com o critério da seção B. Em MU03, conclusão assistida ou interrupção por dificuldade conta como meta não atingida. Informar o tempo decorrido nessa tentativa. Com denominador zero, registrar a meta como não avaliada. Um resultado de 1/1 descreve apenas aquela sessão. Explicitar lacunas de cobertura antes de concluir sobre o fluxo.
- **Interpretação e prioridade.** Agrupar falas e ações por tema, como unidade, previsão, confirmação e retomada. Relacionar cada problema a uma evidência e à consequência no comércio. Dar prioridade a riscos de saldo incorreto, duplicação ou falsa conclusão. Depois, considerar bloqueios de tarefa, necessidade de ajuda e dificuldades recuperáveis. Na Entrega 13, registrar riscos previstos pela inspeção. Na Entrega 14, registrar ocorrências observadas e indicar o que deve ser revisto e testado novamente.
- **Qualidade da evidência e relato.** Para dar consistência à coleta, usar o mesmo roteiro por caso e comparar no piloto como a dupla classifica a mesma ocorrência. Para preservar a validade interna, distinguir ajuda de informação prevista no cenário e registrar esperas separadamente. Para interpretar a validade externa e a ecológica, indicar quem participou, em qual versão e o que a simulação reproduziu da loja. Ao apresentar cada pergunta da seção B, informar o resultado observado, a explicação dada pela pessoa e a decisão de projeto. Quando faltar evidência, registrar o que ficou sem resposta.
## Checklist

- [ ] As seis etapas DECIDE foram contextualizadas, não apenas expandidas por sigla.
- [ ] Perguntas de avaliação têm método e evidência correspondentes.
- [ ] O plano distingue avaliação de IHC de avaliação técnica/científica do TCC.
- [ ] Dados ou processamentos simulados no protótipo estão declarados.
- [ ] Tarefas vêm de objetivos/cenários relevantes.
- [ ] Critérios de sucesso foram definidos antes da coleta.
- [ ] Questões práticas e éticas estão resolvidas.
- [ ] Instrumentos estão prontos antes da Entrega 13/14.
- [ ] Plano diz como dados serão analisados e apresentados.

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
| **D — Decide how to deal with ethical issues** | **Como proteger quem participa?** Explicar o estudo e obter consentimento antes de anotar dados. Permitir pausa, recusa de resposta e desistência a qualquer momento. Usar dados fictícios e códigos U01 e U02. A equipe anotará ações e falas sem gravar áudio, vídeo ou tela. Guardará os aceites separadamente, restringirá o acesso aos registros individuais e os descartará após a correção da atividade. |
| **E — Evaluate, interpret and present the data** | A dupla reunirá as observações por tarefa e meta. Cada achado indicará o que ocorreu, a consequência para o trabalho e a mudança proposta. A versão avaliada acompanhará os resultados para permitir a repetição do caso após uma revisão. |

A inspeção da Entrega 13 terá finalidade **formativa**: localizar dificuldades enquanto ainda é possível alterar as telas. Na Entrega 14, a comparação com as metas terá finalidade **somativa** para a versão do protótipo usada na disciplina. Os três pontos destacados na tabela retomam o exercício proposto no encerramento da aula. 

## B. Perguntas de avaliação

| ID | Pergunta | Método | Métrica/evidência | Critério esperado |
|---|---|---|---|---|
| QA01 | Quem faz reposição ou conferência consegue concluir e conferir o registro do seu item sem ajuda? | Observação da primeira tentativa do caso A de cada perfil | Desfecho, ajuda e registro final | MU01: ao menos 80% por tarefa. Com um ou dois participantes elegíveis, todos devem concluir de forma independente. |
| QA02 | Quem decide a reposição explica quantas unidades estão livres, o que a estimativa informa e o que acontece ao salvar? | Perguntas abertas após os casos A e B de reposição | Explicação sobre disponibilidade, incerteza, ausência de previsão e efeito de salvar | MU02: todos os elegíveis explicam os quatro pontos, inclusive que previsão ausente não indica demanda zero e que a compra ainda depende de contato com o fornecedor. |
| QA03 | Quanto tempo cada pessoa leva para obter e conferir um desfecho? | Observação cronometrada | Tempo ativo da primeira tentativa independente do caso A | MU03: até 180 s na reposição e 300 s na conferência, por participante. |
| QA04 | Ao revisar uma correção, a pessoa consegue prever seu efeito no saldo? Se faltar confirmação de gravação, a tela deixa claro o que fazer? | Inspeção do feedback, da prevenção e da recuperação em F12, F12E/F12F e F06E/F06R. Observação das decisões nos casos A e B. | Registrar a mensagem e a ação disponível na inspeção. Na sessão, anotar o desfecho escolhido, a evidência considerada e o efeito que a pessoa atribui ao registro. | MU04 exige zero erros críticos por tentativa. Os estados de falha de gravação serão inspecionados. O plano não prevê provocar essa falha nas sessões. |
| QA05 | Como a pessoa avalia a experiência de realizar a tarefa e por quê? | Pergunta pós-tarefa | Nota de 1 a 5 e justificativa nas palavras do participante | MU05: nota mínima 4 por pessoa e tarefa. |
| QA06 | Ao receber outro produto em situação equivalente, a pessoa consegue repetir o trabalho sozinha? | Duas execuções sem instrução entre elas | Comparação de conclusão, ajuda e erro crítico | MU06 fica fora da coleta atual. Com variante equivalente, todos os elegíveis devem concluir a segunda execução sem ajuda e sem erro crítico. |
| QA07 | Após uma interrupção de balcão, a pessoa reconhece onde parou e o que precisa fazer? | Observação de execução separada com pausa | Tempo desde o retorno até identificar item, estado de salvamento e próxima ação. Observar eventual duplicação. | MU07: até 30 s após o retorno e nenhum registro duplicado. |

A aula de diretrizes orienta o que procurar nas telas. Em F02, verificar se “comprometidas” tem um sentido reconhecível para quem separa pedidos pagos. Em F12, verificar se o efeito de desfazer o segundo desconto aparece **antes** de confirmar. Em F06E/F06R, verificar se a mensagem permite distinguir “ainda sem resposta” de “gravação falhou” e escolher uma ação em cada situação. Esses são pontos a investigar na inspeção. [Expectativas do usuário, 8min53s](https://youtu.be/5FcSnJ4yrRE?t=533) · [Visibilidade e reconhecimento, 26min24s](https://youtu.be/5FcSnJ4yrRE?t=1584) · [Recuperação de erros, 31min47s](https://youtu.be/5FcSnJ4yrRE?t=1907) · *Princípios e Diretrizes para o Design de IHC*, PDF, pp. 3 e 12–16.

## C. Escopo e participantes

| Item | Planejamento |
|---|---|
| Perfis | Uma pessoa que decide reposições em pequeno comércio, preferencialmente com pouca familiaridade com sistemas de estoque, e uma pessoa que confere mercadorias e movimentações. |
| Critérios de inclusão/exclusão | Convidar adultos com experiência na atividade correspondente. Registrar familiaridade digital e contato prévio com o projeto. Integrantes da equipe e a pessoa do piloto ficam fora da amostra final. |
| Nº de participantes | Dois participantes finais previstos, um por integrante da equipe. Cada pessoa fará os casos da atividade que conhece. Nomes e recrutamento ainda não definidos. |
| Ambiente | Sessão presencial individual em sala tranquila, com notebook e os dois integrantes. Isso permite apresentar os mesmos dados e medir tempos com menos interferências. A pausa de balcão reproduz uma situação do comércio, mas a sessão não reproduz o movimento da loja nem a pressão de uma compra real. |
| Dispositivo | Planejado um notebook com navegador e mouse. Registrar dispositivo, zoom e eventuais adaptações de leitura. |
| Protótipo/versão | [Estoque Inteligente no Figma](https://www.figma.com/proto/jgB0Bk5BLQ3XM2W9tgZDmd/Estoque-Inteligente?page-id=0%3A1&node-id=2-2&starting-point-node-id=2%3A2&scaling=scale-down), versão da Entrega 11 de 11/11/2026. Usar a mesma versão nas duas sessões. Se houver alterações após a inspeção, registrar a revisão e reconferir os caminhos no piloto. |
| Teste piloto | Antes da coleta, um integrante representará o participante e o outro conduzirá o roteiro. Verificar abertura das telas, legibilidade, neutralidade dos enunciados e cronometragem. Reservar 25–35 minutos por sessão e ajustar a previsão após o piloto. Em caso de falha de conexão, suspender o cronômetro e registrar o trecho inviabilizado. |

## D. Lista de tarefas de avaliação

| ID | Cenário neutro entregue ao usuário | Objetivo oculto da avaliação | Critério de sucesso | Tempo-limite (se houver) |
|---|---|---|---|---|
| UT01 · T01-A | É segunda-feira. O fornecedor recebe pedidos até o meio-dia e prevê entregar na quinta. Veja a situação da garrafa térmica azul de 500 ml e deixe registrado como pretende proceder. | O01/M01. Observar como a pessoa identifica o item e fundamenta a decisão. | Reconhece 4 unidades disponíveis (6 físicas, 2 reservadas), considera o prazo e os dados de procura, explica o motivo e confere o registro. Aceitar 4 ou 6 unidades e outros desfechos disponíveis quando sustentados pela análise. | Meta de 3 min. Aos 6 min, oferecer ajuda ou encerramento, conforme a Entrega 8. |
| UT02 · T01-B | Em outro ciclo, você precisa decidir sobre a mesma garrafa. Use as informações disponíveis hoje e deixe registrado como dará continuidade ao trabalho. | O01/M01. Verificar interpretação de informação ausente. | Identifica a lacuna e registra o que precisa verificar antes de decidir. Confere a pendência salva. | Sem meta de tempo. |
| UT03 · T02-A | A loja está conferindo 14 registros. A proprietária quer saber por que há uma diferença no estoque do conjunto de três potes. Investigue o que aconteceu e diga a ela como ficou esse item. | O02/M02. Observar se a pessoa investiga a origem antes de ajustar o saldo. | Usa o conjunto como unidade. Confirma nas fontes a transcrição duplicada da mesma saída de 2 conjuntos, corrige apenas a duplicação, confere o saldo 10 e comunica o alcance parcial. | Meta de 5 min. Aos 10 min, oferecer ajuda ou encerramento, conforme a Entrega 8. |
| UT04 · T02-B | Em outra conferência do mesmo item, os registros e a contagem também divergem. Hoje você dispõe apenas dos documentos apresentados. Deixe o caso em condições de ser acompanhado pela proprietária. | O02/M02. Verificar como a pessoa atua com evidência insuficiente. | Preserva o saldo registrado, informa a dúvida e a próxima verificação. Comunica o que continua em aberto. | Sem meta de tempo. |
| UT05 · retomada | Você está no meio dessa atividade quando precisa atender alguém no balcão. Ao voltar, identifique onde parou e continue o trabalho. | O09/M01 ou M02. Observar reconhecimento do contexto. | Identifica o item, o estado do registro e a próxima ação. Retoma sem duplicar a operação. | Pausa de 30 s. Meta de retomada de até 30 s depois do retorno. |
| UT06 · repetição equivalente | Em outro ciclo, faça o mesmo trabalho para o item que recebeu agora. | MU06. Medir autonomia com outro produto e outros valores. | Conclui a segunda execução sem ajuda e sem erro crítico. | Sem meta de tempo. Requer variante equivalente. |

**Ordem e cobertura.** Por perfil, aplicar o caso A, depois o B e, em execução separada, UT05. No Figma, a pausa disponível ocorre durante a análise dos dados (F02P ou F10P). O cronômetro da retomada começa quando a pessoa volta a ver esse estado. A versão atual tem apenas um produto por perfil. Por isso, **MU06 ficará não avaliada nesta versão**. Se a equipe preparar uma variante equivalente antes da coleta, inserir UT06 entre A e B, sem ensinar a solução entre as tentativas. Alterar apenas a quantidade planejada da mesma garrafa não produz essa variante.

## E. Instrumentos

- [Termo de consentimento](../instrumentos/termo_consentimento_modelo.md) para leitura e aceite antes da sessão.
- [Roteiro de teste](../instrumentos/roteiro_teste_usabilidade.md) com os quadros de início e término e as respostas de Mariana para simular a consulta externa.
- [Planilha de observação](../instrumentos/planilha_observacao_modelo.md) para registro por tentativa.
- [Formulário de avaliação heurística](../instrumentos/formulario_heuristica_modelo.md) para inspeção independente e consolidação.
- [Questionário pré e pós-teste](../instrumentos/questionario_pre_pos.md) com perguntas de perfil, compreensão e satisfação.

## F. Plano de análise

- **Desfecho.** Sucesso total exige alcançar e conferir o resultado correto com autonomia. Registrar sucesso parcial quando houver progresso pertinente, mas faltar uma etapa essencial ou for preciso orientar a conclusão. Registrar falha quando houver erro crítico, desfecho incorreto ou abandono por dificuldade. Se a pessoa pedir orientação e preferir recebê-la, encerrar e cronometrar a tentativa independente antes de ajudar. Uma tentativa inviabilizada pelo equipamento ou por tela ausente será registrada como *não avaliada*. A retirada de consentimento será tratada conforme o termo.
- **Ocorrências.** Anotar dúvida quando a pessoa verbalizar incerteza. Contar como ajuda uma orientação do moderador que revele o próximo passo. Registrar consulta à ajuda da interface separadamente. Anotar abandono quando a pessoa decidir encerrar e distinguir dificuldade de interação de retirada de consentimento. Um desvio corrigido antes de salvar será classificado como erro recuperado. Um ajuste sem evidência, um registro duplicado, um produto ou unidade errados no registro final ou uma declaração indevida de conferência total serão erros críticos.
- **Tempo e satisfação.** Iniciar a contagem após a leitura do cenário e encerrar quando a pessoa conferir o desfecho ou interromper a tarefa. Guardar o tempo total e descontar do tempo ativo apenas pausas e esperas comprovadas. Registrar a nota de satisfação de cada participante e seu motivo. Recusa de resposta será dado ausente.
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

# Entrega 12 — Planejamento da avaliação de usabilidade (DECIDE)

**Data:** 18/11/2026  
**Status:** 🟩 planejamento concluído  
**Responsabilidade:** 1 solução por equipe.

**Integrantes**
- Gabriel Koiama de Rocha Lira — 22.125.067-3.
- João Pedro Lopes Santana Villas Bôas — 22.125.065-7.

## Objetivo da atividade

Planejar a avaliação da interface de configuração, execução e análise de simulações semafóricas, relacionando perguntas de avaliação, métodos, participantes, tarefas, métricas, aspectos práticos, ética e forma de análise.

O planejamento contempla os fluxos M01 e M02 e considera a atividade exploratória realizada em 15/11/2026 na aplicação funcional do TCC.

## O que está sendo avaliado

A avaliação investiga a qualidade da interação com a interface, incluindo a compreensão das opções de configuração, o reconhecimento dos estados da simulação e a consulta dos resultados.

O M01 abrange seleção do cenário, configuração do controlador, seed e modo de execução, validação e acompanhamento da simulação.

O M02 abrange localização dos registros, identificação das condições experimentais, interpretação das métricas e recuperação quando um resultado está indisponível.

A aplicação funcional do TCC executa as simulações com o SUMO. O Figma da Entrega 11 representa os fluxos de interação com processamento e resultados demonstrativos. A versão utilizada deve ser identificada no registro de cada atividade.

A avaliação técnica do algoritmo e de seu desempenho é documentada pelos experimentos do TCC.

### Contexto da atividade exploratória

Em 15/11/2026, domingo, Luiza Agatão e Flavio Agatão participaram de uma exploração presencial da aplicação funcional do TCC, conduzida por Gabriel em seu computador.

Os participantes exploraram a interface e executaram um teste no cenário R3, que representa uma réplica da região da Vila Mariana. Ambos concordaram em participar. A atividade ocorreu sem gravação e sem ensaio prévio.

O resultado da simulação foi salvo pela aplicação no computador. A atividade ficou sem anotações sistemáticas de tempo de interação, erros, ajudas e facilidade percebida.

Este documento foi consolidado em 18/11/2026 e apresenta também o roteiro para uma avaliação padronizada. Os critérios e instrumentos desse roteiro serão utilizados nas próximas sessões.

## A. Método DECIDE

| Etapa | Aplicação no projeto |
|---|---|
| **D — Determine the goals** | Avaliar a preparação correta da simulação, a recuperação de uma configuração inválida, a identificação do estado da execução e a consulta dos resultados. Relacionar as medidas às metas MU01–MU08 da Entrega 8. |
| **E — Explore the questions** | Verificar se os participantes entendem as opções de configuração, reconhecem erros e estados do sistema, localizam os registros solicitados e interpretam as métricas com seu contexto experimental. |
| **C — Choose the evaluation paradigm and techniques** | Combinar inspeção heurística na Entrega 13 com observação de usuários na Entrega 14. Usar a exploração de 15/11 como experiência preliminar e aplicar o roteiro padronizado para obter as medidas de usabilidade previstas. |
| **I — Identify the practical issues** | Utilizar computador com mouse ou touchpad. Conferir previamente os links, a versão da interface, os estados iniciais e os instrumentos. Gabriel prepara as tarefas do M01 e João prepara as tarefas do M02. Registrar o responsável pela condução de cada sessão. |
| **D — Decide how to deal with ethical issues** | Obter a concordância dos participantes, informar a possibilidade de interrupção e utilizar identificadores nas tabelas de resultados. Adotar anotações como forma de registro. Qualquer gravação dependerá de autorização específica. |
| **E — Evaluate, interpret and present the data** | Apresentar sucesso, tempo, erros, ajudas e facilidade percebida por participante e tarefa. Comparar as medidas com as metas da Entrega 8 e relacionar as dificuldades aos quadros da interface e aos achados da inspeção heurística. |

## B. Perguntas de avaliação

| ID | Pergunta | Método | Métrica/evidência | Critério esperado |
|---|---|---|---|---|
| QA01 | O participante prepara e revisa as condições corretas sem ajuda? | Observação, UT01 | Escolhas, sucesso e intervenções do moderador. | MU01 — 100% concluem a preparação sem ajuda. |
| QA02 | O participante identifica como corrigir a configuração inválida? | Observação, UT02 | Campo identificado e ação de recuperação. | MU02 — 100% identificam a ação correta de recuperação. |
| QA03 | Quanto tempo leva a preparação da simulação? | Observação, UT01 | Tempo até a conferência correta do resumo. | MU03 — mediana de até 5 minutos. |
| QA04 | O participante reconhece o estado da execução e o controlador utilizado? | Observação, UT03 | Resposta e informação consultada. | MU04 — 100% identificam ambos sem depender exclusivamente dos logs. |
| QA05 | O participante localiza a execução e identifica suas condições? | Observação, UT04 | Registro, cenário, controlador e seed. | MU05 — 100% identificam corretamente os dados solicitados. |
| QA06 | Quanto tempo leva para localizar uma execução? | Observação, UT04 | Tempo até abrir o registro correto. | MU06 — mediana de até 3 minutos. |
| QA07 | O participante compreende como comparar duas execuções? | Observação e pergunta pós-tarefa, UT05 | Consulta dos registros e explicação do procedimento. | MU08 — 100% reconhecem a consulta individual e a necessidade de reunir os dados externamente. |
| QA08 | O participante consegue continuar após encontrar um resultado indisponível? | Observação, UT06 | Reconhecimento do aviso e abertura de outro resultado. | Retornar ao histórico e abrir outro registro sem ajuda direta. |
| QA09 | Há problemas de feedback, consistência ou recuperação? | Inspeção heurística | Evidência, localização, heurística e severidade. | Registrar problemas reais e recomendações específicas. |
| QA10 | Qual é a facilidade percebida após cada tarefa? | Questionário pós-tarefa | Nota de 1 a 5 e justificativa. | MU07 — mediana de pelo menos 4 em 5. |

## C. Escopo e participantes

| Item | Planejamento e contexto |
|---|---|
| Participantes | U01 — Luiza Agatão e U02 — Flavio Agatão. |
| Perfis | Registrar no pré-teste a experiência com simulação, mobilidade urbana e interpretação de resultados. A experiência prévia dos participantes ficou sem registro na atividade exploratória. |
| Critérios de inclusão/exclusão | Participantes externos à equipe, com concordância para participar. Quando o perfil for aproximado ao público-alvo, registrar essa condição como limitação. |
| Nº de participantes | Dois participantes, conforme a quantidade prevista na Entrega 14. |
| Ambiente | Presencial. A atividade exploratória ocorreu no computador de Gabriel. |
| Dispositivo | Computador com mouse ou touchpad. Nas sessões padronizadas, registrar resolução, escala e versão da interface. |
| Interface utilizada em 15/11 | Aplicação funcional do TCC, com execução do cenário R3 — Vila Mariana. |
| Interface do roteiro padronizado | Protótipo Figma da Entrega 11, cobrindo M01 e M02. |
| Teste piloto | A atividade exploratória ocorreu sem ensaio prévio. Para a aplicação padronizada, verificar antes as instruções, os estados iniciais e a duração das transições do Figma. |
| Forma de registro | Na exploração, foi preservado o resultado da simulação. Nas sessões padronizadas, usar anotações por tarefa, sem gravação. |
| Armazenamento | Os resultados são salvos automaticamente pela aplicação do TCC no computador após cada teste. |
| Preservação | Os resultados técnicos serão mantidos por prazo indeterminado, permitindo consulta, reprodução dos experimentos e comparação posterior. |

**M01:** [Preparação e execução da simulação](https://www.figma.com/proto/YJJhBTujdrsjDY113Iefj4/Sem-t%C3%ADtulo?node-id=4-12&scaling=scale-down-width&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=4%3A12&show-proto-sidebar=1)

**M02:** [Histórico e resultados](https://www.figma.com/proto/YJJhBTujdrsjDY113Iefj4/Sem-t%C3%ADtulo?node-id=16-206&scaling=scale-down-width&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=16%3A206&show-proto-sidebar=1)

### Registro da concordância na atividade exploratória

| Participante | Identificador | Data da participação | Registro |
|---|---|---|---|
| Luiza Agatão | U01 | 15/11/2026 | Concordou em participar da exploração presencial da interface. A atividade ocorreu sem gravação. |
| Flavio Agatão | U02 | 15/11/2026 | Concordou em participar da exploração presencial da interface. A atividade ocorreu sem gravação. |

Gabriel conduziu a atividade e informou a concordância dos participantes. O registro acima foi consolidado pela equipe em 18/11/2026. A sessão ficou sem termo escrito de aceite.

Nas próximas sessões, o moderador deverá explicar o objetivo, as tarefas, os registros previstos e a possibilidade de interrupção antes de registrar a concordância.

## D. Lista de tarefas de avaliação

As tarefas abaixo compõem o roteiro padronizado do Figma. O cenário R2 corresponde aos quadros disponíveis nesse protótipo. Na atividade de 15/11, os participantes utilizaram o cenário R3 da aplicação funcional.

| ID | Cenário neutro entregue ao usuário | Objetivo oculto da avaliação | Critério de sucesso | Tempo-limite |
|---|---|---|---|---|
| UT01 | Prepare um experimento para Regional São Paulo, usando o controlador híbrido, seed 42 e execução sem abrir a janela gráfica do simulador. Confira as condições antes de iniciar. | Avaliar configuração e revisão. T01–T03, OBJ02–OBJ03, M01. | Chegar ao resumo com cenário R2, controlador híbrido, seed 42 e modo Headless. | Sem limite. Meta de mediana de até 5 minutos. |
| UT02 | Um colega preparou uma configuração. Ao tentar deixá-la pronta para execução, você encontra um problema. Descubra o que precisa corrigir. | Avaliar recuperação da seed ausente. T02/T04, OBJ03, M01. | Identificar a ausência da seed, recuperar o valor 42 e validar novamente. | Sem limite. |
| UT03 | O experimento já foi confirmado. Diga em que estado se encontra e qual estratégia está sendo usada. | Avaliar a percepção do estado. T05, OBJ04, M01. | Identificar corretamente o estado e o controlador. | Janela de observação conferida antes da sessão. |
| UT04 | Encontre R2-001 e identifique seu cenário, sua estratégia e sua seed. | Avaliar localização e contexto. T06, OBJ06, M02. | Abrir R2-001 e identificar Regional São Paulo, híbrido e seed 42. | Sem limite. Meta de mediana de até 3 minutos. |
| UT05 | Compare o tempo médio de espera de R2-001 e R2-002. Explique quais condições precisam ser conferidas antes de interpretar a diferença. | Avaliar interpretação e comparação. T06–T08, OBJ07–OBJ09, M02. | Identificar 28 s e 36 s nos registros corretos e explicar a verificação das condições e a comparação externa. | Sem limite. |
| UT06 | Consulte R2-003. Se encontrar um impedimento, explique o que aconteceu e continue com outro registro. | Avaliar recuperação de indisponibilidade. T06, OBJ06, M02. | Reconhecer o aviso, retornar ao histórico e abrir outro resultado. | Sem limite. |

> As instruções apresentam o objetivo da tarefa, preservando a descoberta do caminho pelo participante.

### Preparação e condução

1. Conferir a versão da interface e os estados iniciais.
2. Apresentar o objetivo da sessão e registrar a concordância.
3. Aplicar as perguntas de perfil.
4. Ler o mesmo enunciado para todos.
5. Registrar início, fim, ações, dificuldades e intervenções.
6. Aplicar a escala de facilidade após cada tarefa.
7. Fazer as perguntas finais e salvar as anotações com o identificador do participante.

Na UT02, começar com a seed vazia. Na UT03, verificar previamente se o estado Executando fica visível durante a pergunta. Se a transição impedir a observação, registrar o efeito sobre a medida.

Aplicar a UT04 antes das demais tarefas do M02 e considerar a familiarização do participante ao interpretar os resultados seguintes.

## E. Instrumentos

- [Modelo de termo de consentimento](../instrumentos/termo_consentimento_modelo.md)
- [Roteiro de teste](../instrumentos/roteiro_teste_usabilidade.md)
- [Planilha de observação](../instrumentos/planilha_observacao_modelo.md)
- [Formulário de avaliação heurística](../instrumentos/formulario_heuristica_modelo.md)

As perguntas e os campos abaixo especificam os instrumentos para as sessões padronizadas.

### Abertura e consentimento

O moderador deverá explicar que a sessão avalia a interface e apresentar as tarefas, a forma de registro e a possibilidade de interrupção.

O registro de concordância deverá conter identificador do participante, data, versão utilizada e responsável pela condução. A previsão é registrar por anotações, sem gravação.

### Pré-teste

- Você já configurou ou acompanhou uma simulação?
- Já utilizou tabelas ou gráficos para comparar resultados?
- Tem familiaridade com mobilidade urbana ou controle de tráfego?

### Planilha de observação

| Campo | Conteúdo a registrar |
|---|---|
| Identificação | U01 ou U02, data, versão da interface, moderador e dispositivo. |
| Tarefa | UT01 a UT06 e quadro inicial. |
| Tempo | Horário de início, horário de fim e duração. |
| Resultado | Sucesso total, sucesso parcial ou falha. |
| Ocorrências | Erros, dúvidas, ajudas e interrupções técnicas. |
| Evidência qualitativa | Ação, quadro, consequência e comentário relevante. |
| Facilidade | Nota de 1 a 5 e justificativa. |

### Pós-tarefa

Perguntar «Quão fácil ou difícil foi realizar esta tarefa?» e registrar a resposta.

| Nota | Significado |
|---|---|
| 1 | Muito difícil |
| 2 | Difícil |
| 3 | Nem fácil nem difícil |
| 4 | Fácil |
| 5 | Muito fácil |

Em seguida, perguntar «O que mais influenciou sua resposta?».

### Pós-teste

- Em qual momento foi mais difícil decidir como prosseguir?
- Que informação teria ajudado?
- Como você reuniria as informações para comparar as duas execuções?

## F. Plano de análise

| Item | Regra de registro e análise |
|---|---|
| Sucesso total | Cumprimento do critério sem orientação sobre a solução. |
| Sucesso parcial | Cumprimento de parte do critério ou conclusão após ajuda direta. |
| Falha | Encerramento sem atingir o critério, resultado incorreto ou abandono. |
| Erro | Ação que desvia do objetivo ou exige correção. Registrar quadro, ação e consequência. |
| Dúvida | Hesitação ou dificuldade verbalizada. |
| Ajuda | Intervenção que orienta a solução. Registrar separadamente a repetição do enunciado. |
| Tempo | Medir após a leitura da instrução até cumprir o critério ou encerrar a tentativa. Na UT01, parar na revisão. Na UT04, parar ao abrir o registro correto. |
| Facilidade percebida | Apresentar notas individuais, justificativas e mediana por tarefa. |
| Dados qualitativos | Agrupar dificuldades por configuração, recuperação, visibilidade do estado, localização e interpretação dos resultados. |
| Priorização | Priorizar problemas que bloqueiam a tarefa ou provocam configuração ou interpretação incorreta. |
| Metas | Comparar contagens e medianas com MU01–MU08. Apresentar os denominadores e justificar medidas indisponíveis. |
| Limitações | Considerar perfil dos participantes, amostra de duas pessoas, familiarização e restrições do protótipo. |

A atividade de 15/11 será apresentada como exploração da aplicação funcional e execução do cenário R3 pelos participantes. Seu resultado técnico poderá demonstrar a execução do cenário. As medidas de usabilidade serão apresentadas quando houver registro correspondente.

### Tratamento dos registros

A aplicação do TCC salva automaticamente os resultados dos testes no computador utilizado. Esses arquivos técnicos serão preservados por prazo indeterminado, pois documentam os experimentos e permitem verificar as condições de execução, reproduzir análises e comparar resultados.

A equipe decidiu manter os resultados técnicos sem exclusão programada.

Nas observações de usabilidade, as tabelas utilizarão U01 e U02. Eventuais registros de consentimento serão guardados separadamente, e os resultados públicos apresentarão apenas as informações necessárias à análise.

## Checklist

- [x] As seis etapas DECIDE foram contextualizadas.
- [x] As perguntas têm métodos e evidências correspondentes.
- [x] O plano identifica a qualidade da interação como objeto da avaliação.
- [x] Os dados e processamentos simulados do Figma foram declarados.
- [x] As tarefas são rastreáveis aos fluxos M01 e M02.
- [x] Os critérios de sucesso estão definidos para a avaliação padronizada.
- [x] Os participantes, o ambiente e o responsável pela atividade exploratória foram identificados.
- [x] A concordância dos participantes foi registrada com base no relato de Gabriel.
- [x] O roteiro, as perguntas e os campos de observação estão especificados neste plano.
- [x] As condições de armazenamento e preservação dos resultados técnicos foram definidas.
- [x] A ausência de ensaio prévio e de medidas sistemáticas na atividade de 15/11 foi registrada.
- [x] O plano define como os dados das próximas sessões serão analisados e apresentados.

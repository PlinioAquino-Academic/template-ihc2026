# Entrega 12 — Planejamento da avaliação de usabilidade (DECIDE)

**Data:** 18/11/2026  
**Status:** 🟨 plano elaborado, com preparação das sessões pendente  
**Responsabilidade:** 1 solução por equipe.  
**M01 — Preparação e execução da simulação:** Gabriel Koiama de Rocha Lira — 22.125.067-3.  
**M02 — Consulta e interpretação dos resultados:** João Pedro Lopes Santana Villas Bôas — 22.125.065-7.

## Objetivo da atividade

Planejar a avaliação antes de executá-la, ligando perguntas de avaliação a métodos, participantes, tarefas, métricas, aspectos práticos, ética e forma de análise.

## O que está sendo avaliado

A avaliação investiga a **qualidade da interação com o protótipo da Entrega 11**. A validade científica do algoritmo de controle semafórico e o desempenho técnico do SUMO pertencem ao TCC.

No **M01**, será avaliado se o participante consegue preparar e revisar uma simulação, recuperar-se de uma configuração inválida e reconhecer o estado da execução. O Figma simula a validação, o processamento, a conclusão e a falha. O tempo das transições do protótipo fica fora da medida de eficiência da preparação do experimento.

No **M02**, será avaliado se o participante consegue localizar um registro, identificar suas condições, interpretar uma métrica e recuperar-se quando um resultado está indisponível. Os registros, valores e gráficos são demonstrativos. O Figma apresenta uma execução de cada vez. A comparação e a síntese são feitas pelo participante fora da interface, usando as informações consultadas.

## A. Método DECIDE

| Etapa | Aplicação no projeto |
|---|---|
| **D — Determine the goals** | Avaliar, no M01, a preparação sem ajuda (MU01), a recuperação de erro (MU02), o tempo de preparação (MU03) e o reconhecimento do estado e do controlador (MU04). No M02, avaliar a identificação do registro e de seu contexto (MU05), o tempo de localização (MU06) e a compreensão de como comparar duas execuções na versão avaliada (MU08). Nos dois fluxos, medir a facilidade percebida (MU07). |
| **E — Explore the questions** | Investigar se a pessoa prepara as condições corretas, identifica como corrigir a seed, reconhece o andamento da execução, localiza o registro solicitado e mantém o contexto ao interpretar e comparar resultados. As perguntas e os critérios estão na seção B. |
| **C — Choose the evaluation paradigm and techniques** | Fazer duas inspeções heurísticas independentes na Entrega 13 para identificar problemas da interface. Na Entrega 14, observar os participantes realizando tarefas padronizadas e aplicar uma pergunta breve de facilidade após cada tarefa. |
| **I — Identify the practical issues** | Recrutar dois participantes externos à equipe, preparar o protótipo em navegador desktop e testar os links e os estados iniciais. Fazer um piloto antes da coleta. Gabriel prepara os cenários do M01 e João prepara os do M02. A dupla confirma o ambiente, as datas, os moderadores e a distribuição das sessões. |
| **D — Decide how to deal with ethical issues** | Apresentar o termo de consentimento antes da sessão, explicar a participação voluntária e permitir a interrupção a qualquer momento. Registrar as observações como P01 e P02, sem nomes na planilha. O registro previsto é por anotações. Qualquer gravação dependerá de autorização específica. A dupla define o local de armazenamento e o prazo de descarte antes da coleta. |
| **E — Evaluate, interpret and present the data** | Consolidar sucesso, erros, ajuda, tempo e facilidade percebida por tarefa. Comparar as observações com as metas da Entrega 8. Relacionar as dificuldades ao quadro do Figma, à ação e à consequência, e verificar quais delas também apareceram nas inspeções. |

## B. Perguntas de avaliação

| ID | Pergunta | Método | Métrica/evidência | Critério esperado |
|---|---|---|---|---|
| QA01 | O participante prepara e revisa as condições corretas sem ajuda? | Observação, UT01 | Sucesso, escolhas corretas e intervenções do moderador. | MU01 — 100% dos participantes observados na tarefa concluem sem ajuda. |
| QA02 | O participante reconhece a configuração inválida e identifica como corrigi-la? | Observação, UT02 | Campo identificado, ação de recuperação, resultado da nova validação e ajuda recebida. | MU02 — 100% dos participantes expostos ao erro identificam a ação correta. Registrar separadamente quem concluiu a correção. |
| QA03 | Quanto tempo leva a preparação e a revisão da simulação? | Observação, UT01 | Tempo entre o fim da instrução e a conferência correta do resumo. | MU03 — mediana de até 5 minutos. |
| QA04 | O participante identifica o estado da simulação e o controlador em uso? | Observação, UT03 | Resposta sobre estado e controlador e informação usada para responder. | MU04 — 100% identificam ambos sem depender exclusivamente dos logs. |
| QA05 | O participante localiza a execução solicitada e identifica suas condições? | Observação, UT04 | Registro aberto e identificação de cenário, controlador e seed. | MU05 — 100% localizam o registro correto e identificam os três dados. |
| QA06 | Quanto tempo leva para localizar uma execução no histórico? | Observação, UT04 | Tempo entre o fim da instrução e a abertura do registro correto. | MU06 — mediana de até 3 minutos. |
| QA07 | O participante consegue recuperar dois resultados e explicar como os compararia? | Observação e pergunta pós-tarefa, UT05 | Registros consultados, métrica e unidade identificadas, condições verificadas e explicação sobre a comparação externa. | MU08 — 100% identificam que a comparação exige consultar as execuções individualmente e reunir os dados fora da interface. |
| QA08 | O participante entende por que um resultado está indisponível e consegue prosseguir? | Observação, UT06 | Reconhecimento do aviso, retorno ao histórico e abertura de outro resultado. | Critério complementar do M02 — reconhecer a indisponibilidade e abrir outro registro com resultado sem ajuda direta. |
| QA09 | Há problemas de feedback, reconhecimento do contexto ou recuperação de erros? | Inspeção heurística, Entrega 13 | Achados com quadro, caminho, evidência, heurística e severidade. | O estado deve ser reconhecível, o contexto deve permanecer associado à execução e as mensagens de erro devem indicar como continuar. |
| QA10 | Quão fácil ou difícil foi realizar cada tarefa? | Questionário pós-tarefa, UT01–UT06 | Nota de 1 a 5 e justificativa breve. | MU07 — mediana de pelo menos 4 em 5. |

## C. Escopo e participantes

| Item | Planejamento |
|---|---|
| Perfis | Priorizar pessoas com familiaridade com mobilidade urbana, simulação de tráfego ou análise de resultados experimentais. Registrar a experiência de cada participante com configuração de simulações e interpretação de métricas. |
| Critérios de inclusão/exclusão | Participantes finais externos à equipe e com consentimento para participar. Se for necessário usar um perfil aproximado, justificar a escolha e registrar a limitação na interpretação. |
| Nº de participantes | Dois participantes finais, conforme a Entrega 14. Planejar que ambos realizem os dois fluxos com as mesmas condições iniciais. |
| Ambiente | Sessão moderada em desktop ou notebook, presencial ou remota. A modalidade e as datas serão confirmadas pela dupla antes da coleta. |
| Dispositivo | Computador com navegador e mouse ou touchpad. Usar a mesma escala de apresentação sempre que possível. Em sessão remota, verificar se o moderador consegue acompanhar a tela com o consentimento do participante. |
| Protótipo/versão | [M01 — Preparação e execução](https://www.figma.com/proto/YJJhBTujdrsjDY113Iefj4/Sem-t%C3%ADtulo?node-id=4-12&scaling=scale-down-width&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=4%3A12&show-proto-sidebar=1) e [M02 — Histórico e resultados](https://www.figma.com/proto/YJJhBTujdrsjDY113Iefj4/Sem-t%C3%ADtulo?node-id=16-206&scaling=scale-down-width&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=16%3A206&show-proto-sidebar=1). Registrar a data e a versão usada na coleta. |
| Teste piloto | Realizar uma sessão antes da coleta, fora da amostra final. Verificar as instruções, o cronômetro, a recuperação da seed vazia, a janela de observação do estado **Executando**, a abertura dos dois resultados, os retornos entre histórico, resultado e gráfico e a recuperação de indisponibilidade. Pessoa e data a confirmar pela dupla. |

## D. Lista de tarefas de avaliação

| ID | Cenário neutro entregue ao usuário | Objetivo oculto da avaliação | Critério de sucesso | Tempo-limite (se houver) |
|---|---|---|---|---|
| UT01 | Você precisa preparar um experimento para Regional São Paulo, usando o controlador híbrido, seed 42 e execução sem abrir a janela gráfica do simulador. Deixe as condições prontas para conferir antes de iniciar. | Avaliar seleção, configuração e conferência do resumo. T01–T03, OBJ02–OBJ03, M01. | Chegar à revisão com cenário R2, controlador híbrido, seed 42 e modo Headless e confirmar que as condições estão corretas. Registrar se houve ajuda. | Sem limite. Meta de mediana de até 5 minutos. |
| UT02 | A configuração de um experimento foi preparada por um colega. Ao tentar deixá-la pronta para execução, você encontra um problema. Descubra o que precisa ser corrigido e deixe a execução pronta para revisão. | Avaliar reconhecimento da seed ausente e recuperação. T02/T04, OBJ03, M01. | Identificar a ausência da seed, recuperar o valor 42 disponível no protótipo, validar novamente e chegar à revisão. | Sem limite. |
| UT03 | O experimento já foi confirmado. Enquanto ele roda, diga em que estado se encontra e qual estratégia de controle está sendo usada. | Avaliar visibilidade do andamento e do controlador. T05, OBJ04, M01. | Identificar corretamente o estado exibido e o controlador associado à execução. Registrar se houve ajuda ou dependência dos logs. | Janela de observação definida no piloto. |
| UT04 | Um colega pediu que você confira a execução R2-001. Encontre o registro e diga em qual cenário ela foi feita, qual estratégia de controle foi usada e qual seed foi registrada. | Avaliar localização do registro e reconhecimento do contexto. T06, OBJ06, M02. | Abrir R2-001 e identificar Regional São Paulo, controlador híbrido e seed 42. | Sem limite. Meta de mediana de até 3 minutos para abrir o registro correto. |
| UT05 | Você precisa comparar o tempo médio de espera das execuções R2-001 e R2-002. Encontre os dois valores e explique o que precisa conferir antes de interpretar a diferença e como faria a comparação. | Avaliar a interpretação do indicador, a recuperação sucessiva dos registros e a compreensão da comparação externa. T06–T08, OBJ07–OBJ09, M02. | Identificar os valores demonstrativos de 28 s e 36 s nos registros corretos, mencionar a verificação das condições experimentais e explicar que é preciso reunir os valores fora da interface. | Sem limite. |
| UT06 | Você recebeu a indicação de consultar o resultado da execução R2-003. Se encontrar um impedimento, diga o que aconteceu e continue a análise com outro registro disponível. | Avaliar o reconhecimento da indisponibilidade e a recuperação. T06, OBJ06, M02. | Reconhecer o aviso, retornar à lista e abrir o resultado de R2-001 ou R2-002 sem ajuda direta. | Sem limite. |

> Uma boa instrução descreve o objetivo do participante sem dizer **onde clicar** ou usar o rótulo exato do controle que está sendo testado.

### Preparação para o moderador

- **UT01:** iniciar no catálogo de cenários. Encerrar a medição ao conferir o resumo, antes de iniciar a simulação.
- **UT02:** iniciar na configuração com a seed vazia. A instrução ao participante deve preservar a descoberta de qual condição precisa ser corrigida.
- **UT03:** usar a apresentação padronizada no piloto para manter o estado **Executando** visível durante a pergunta. Se a transição impedir a observação, registrar a limitação do protótipo e informar que a medida ficou indisponível.
- **UT04 a UT06:** começar cada tarefa no histórico `F07`. Aplicar a UT04 antes das outras tarefas do M02 para que a medida de localização seja registrada antes de o participante explorar o histórico. Registrar essa ordem ao interpretar os resultados posteriores.
- Ler o mesmo enunciado para todos. Se houver intervenção, registrar quando ocorreu e qual orientação foi dada.

## E. Instrumentos

- [Modelo de termo de consentimento](../instrumentos/termo_consentimento_modelo.md)
- [Roteiro de teste](../instrumentos/roteiro_teste_usabilidade.md)
- [Planilha de observação](../instrumentos/planilha_observacao_modelo.md)
- [Formulário de avaliação heurística](../instrumentos/formulario_heuristica_modelo.md)

**Pré-teste.** Perguntar se a pessoa já configurou, acompanhou ou analisou uma simulação e quais informações costuma conferir ao preparar um experimento ou interpretar seus resultados.

**Pós-tarefa.** Perguntar «Quão fácil ou difícil foi realizar esta tarefa?» na escala de 1 a 5, em que 1 significa **muito difícil** e 5 significa **muito fácil**. Em seguida, perguntar «O que mais influenciou sua resposta?».

**Pós-teste.** Perguntar «Em qual momento foi mais difícil decidir como prosseguir?» e «Que informação teria ajudado nessa etapa?». Para o M02, acrescentar «Como você reuniria as informações para comparar as duas execuções?». Aplicar essa pergunta após as tarefas, sem orientar de antemão como a comparação deve ser feita.

## F. Plano de análise

| Item | Regra de registro e análise |
|---|---|
| Sucesso total | A pessoa cumpre o critério observável sem receber orientação sobre a solução. |
| Sucesso parcial | A pessoa cumpre parte do critério ou conclui após ajuda direta. Registrar o trecho cumprido e a ajuda recebida. |
| Falha | A pessoa encerra sem atingir o critério mínimo, chega a um resultado incorreto ou abandona. Registrar o motivo quando possível. |
| Erro e dúvida | Erro é uma ação que desvia da tarefa ou exige correção. Dúvida é hesitação ou dificuldade verbalizada. Registrar a ação, o quadro e o contexto, evitando duplicar a mesma ocorrência. |
| Ajuda e abandono | Ajuda é intervenção que orienta a solução. A repetição do enunciado original fica em campo separado. Abandono ocorre quando a pessoa declara que não consegue ou não deseja prosseguir. |
| Tempo | Iniciar após a leitura do enunciado. Na UT01, parar na conferência do resumo. Na UT04, parar o tempo de localização quando o registro correto for aberto e avaliar a identificação das condições separadamente. Nas demais tarefas, parar ao atingir o critério ou ao encerrar a tentativa. Registrar interrupções técnicas separadamente. |
| Facilidade percebida | Registrar nota de 1 a 5 e justificativa por tarefa. Apresentar as notas individuais e a mediana. |
| Registro qualitativo | Identificar participante, tarefa, quadro, ação e consequência. Agrupar as ocorrências por configuração, recuperação, visibilidade do estado, localização, compreensão da métrica ou interpretação do contexto. Usar apenas o código do participante nas citações. |
| Priorização | Priorizar dificuldades que bloqueiam a tarefa ou levam a confirmar condições incorretas, consultar o registro errado ou interpretar uma métrica fora de contexto. Relacionar os achados da observação com os da inspeção heurística, quando houver correspondência. |
| Comparação com as metas | Apresentar contagens com denominador, como `2/2 sem ajuda`, e as medianas previstas nas metas. Informar os casos não observáveis e suas causas. Interpretar os resultados considerando a amostra de dois participantes e o caráter demonstrativo do protótipo. |

A consolidação deve apresentar, para cada tarefa, o resultado observado, a meta correspondente, as dificuldades registradas e a tela envolvida. Nas tarefas de comparação, registrar se o participante reconheceu quais condições deveriam ser verificadas e se distinguiu a consulta individual da análise externa.

## Checklist

- [x] As seis etapas DECIDE foram contextualizadas.
- [x] As perguntas dos dois fluxos têm método e evidência correspondentes.
- [x] O plano distingue avaliação de IHC de avaliação técnica e científica do TCC.
- [x] Os dados e processamentos simulados foram declarados.
- [x] As tarefas são rastreáveis a objetivos, cenários e tarefas das entregas anteriores.
- [x] Os critérios de sucesso foram definidos antes da coleta.
- [ ] Recrutamento, ambiente, datas, divisão das sessões e armazenamento foram confirmados pela dupla.
- [ ] Os instrumentos, os links de início e o roteiro foram testados no piloto antes da coleta.
- [x] O plano define como os dados serão analisados e apresentados.

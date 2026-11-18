# Entrega 12 — Planejamento da avaliação de usabilidade (DECIDE)

**Data:** 18/11/2026  
**Status:** 🟨 em andamento  
**Responsabilidade:** 1 solução por equipe.  
**Contribuição nesta versão:** Gabriel Koiama de Rocha Lira — 22.125.067-3 — planejamento da avaliação do fluxo M01.

## Objetivo da atividade

Planejar a avaliação antes de executá-la, ligando perguntas de avaliação a métodos, participantes, tarefas, métricas, aspectos práticos, ética e forma de análise.

No M01, a avaliação verificará se o participante consegue selecionar o cenário, preparar e revisar as condições da simulação, corrigir uma configuração inválida e reconhecer o estado da execução.

## O que está sendo avaliado

O objeto da avaliação é a **qualidade da interação com o protótipo da Entrega 11**. A avaliação científica do algoritmo de controle semafórico e a medição do desempenho do SUMO pertencem ao TCC.

No M01, o Figma simula a validação dos parâmetros, a inicialização, a execução, a conclusão e a falha. A seed disponível para correção no protótipo é 42. As transições de processamento servem para apresentar os estados da interface. A medição de eficiência considera o tempo necessário para o participante cumprir a tarefa de interação.

**Escopo do M02 — João:** {{preencher}}.

## A. Método DECIDE

| Etapa | Aplicação no projeto |
|---|---|
| **D — Determine the goals** | No M01, avaliar a preparação e a revisão do experimento sem ajuda (MU01), a recuperação de uma configuração inválida (MU02), o tempo de preparação (MU03), o reconhecimento do estado e do controlador (MU04) e a facilidade percebida após cada tarefa (MU07). **M02:** {{preencher}}. |
| **E — Explore the questions** | Investigar se os participantes concluem a preparação, reconhecem o problema de validação, corrigem o campo indicado e identificam o estado da execução sem depender dos logs. As perguntas do M01 estão na seção B. **M02:** {{preencher}}. |
| **C — Choose the evaluation paradigm and techniques** | Usar inspeção heurística na Entrega 13 para examinar a visibilidade do estado, a prevenção de erros e o apoio à recuperação. Usar observação de usuários na Entrega 14 para registrar o que os participantes conseguem fazer e onde encontram dificuldade. |
| **I — Identify the practical issues** | No M01, preparar um computador com navegador, conferir a abertura do link e validar no piloto as rotas de configuração, erro e processamento. Cada tarefa deve começar no quadro indicado no roteiro do moderador. **Recrutamento, datas, ambiente final e divisão das sessões:** {{definir em dupla}}. |
| **D — Decide how to deal with ethical issues** | Propor consentimento antes da sessão, participação voluntária, possibilidade de interrupção e registro por identificadores sem nomes na planilha. Gabriel prevê registrar a tarefa por anotações. A gravação, se adotada pela dupla, dependerá de autorização específica. **Local de armazenamento, acesso e prazo de descarte:** {{definir em dupla}}. |
| **E — Evaluate, interpret and present the data** | Para o M01, reunir sucesso, erros, ajudas, tempo e facilidade percebida por tarefa. Comparar as observações com as metas da Entrega 8 e relacionar cada dificuldade ao quadro e à ação em que ocorreu. **Análise do M02 e consolidação dos dois fluxos:** {{preencher em dupla}}. |

## B. Perguntas de avaliação

| ID | Pergunta | Método | Métrica/evidência | Critério esperado |
|---|---|---|---|---|
| QA01 | O participante seleciona o cenário e revisa as condições corretas sem ajuda? | Observação, UT01 | Sucesso, escolhas corretas e intervenções do moderador. | MU01: 100% dos participantes observados nessa tarefa concluem sem ajuda. |
| QA02 | O participante reconhece a configuração inválida e identifica como corrigi-la? | Observação, UT02 | Campo identificado, correção realizada, resultado da nova validação e ajuda recebida. | MU02: 100% dos participantes expostos ao erro identificam a ação correta de recuperação. Registrar separadamente se a correção foi concluída. |
| QA03 | Quanto tempo o participante leva para preparar e revisar uma simulação em condição padronizada? | Observação, UT01 | Tempo entre o fim da instrução e a confirmação verbal de que o resumo está correto. | MU03: mediana de até 5 minutos. |
| QA04 | O participante identifica o estado da simulação e o controlador utilizado durante a execução? | Observação, UT03 | Resposta sobre o estado e o controlador, com indicação da informação usada. | MU04: 100% identificam corretamente o estado e a estratégia sem depender exclusivamente dos logs. |
| QA05 | Há problemas de visibilidade do estado ou de recuperação da configuração inválida? | Inspeção heurística | Achados com quadro, caminho, evidência e severidade. Aplicar as heurísticas de visibilidade do estado, prevenção de erros e recuperação de erros. | Os estados relevantes são distinguíveis, e a mensagem indica o campo a corrigir e como prosseguir. |
| QA06 | Qual é a facilidade percebida após cada tarefa do M01? | Questionário pós-tarefa | Nota de 1 a 5 e justificativa breve. | MU07: mediana de pelo menos 4 em 5. |
| {{ID do M02}} | {{pergunta do João}} | {{...}} | {{...}} | {{...}} |

## C. Escopo e participantes

| Item | Planejamento |
|---|---|
| Perfis | Para o M01, priorizar pessoas com familiaridade com simulação de tráfego, mobilidade urbana ou experimentos computacionais. |
| Critérios de inclusão/exclusão | Os participantes finais devem ser externos à equipe. Caso seja necessário usar um perfil aproximado, registrar sua experiência, a justificativa da escolha e a limitação para interpretar os resultados. |
| Nº de participantes | O modelo da Entrega 14 prevê dois participantes finais para a dupla. **Perfis recrutados e divisão das sessões:** {{definir em dupla}}. |
| Ambiente | {{definir em dupla se presencial ou remoto}} |
| Dispositivo | Computador desktop ou notebook com navegador e acesso ao protótipo. Usar mouse ou touchpad e manter as mesmas condições de apresentação entre as sessões. |
| Protótipo/versão | [Entrega 11 — Protótipo da equipe](https://www.figma.com/proto/YJJhBTujdrsjDY113Iefj4/Sem-t%C3%ADtulo?node-id=4-12&scaling=scale-down-width&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=4%3A12&show-proto-sidebar=1). Registrar a versão usada antes de iniciar a coleta. |
| Teste piloto | Para o M01, verificar se as instruções são compreensíveis, se a seed inválida pode ser corrigida e se o estado de execução fica visível por tempo suficiente para a pergunta da UT03. O piloto fica fora da amostra final. **Pessoa e data:** {{definir em dupla}}. |

## D. Lista de tarefas de avaliação

| ID | Cenário neutro entregue ao usuário | Objetivo oculto da avaliação | Critério de sucesso | Tempo-limite (se houver) |
|---|---|---|---|---|
| UT01 | Você precisa preparar um experimento para **Regional São Paulo**, usando o controlador híbrido, seed **42** e execução sem abrir a janela gráfica do simulador. Deixe as condições prontas para conferir antes de iniciar. | Avaliar seleção, configuração e conferência do resumo. T01–T03, OBJ02–OBJ03, M01. | Chegar à revisão com cenário R2, controlador híbrido, seed 42 e modo Headless, e confirmar verbalmente que as condições estão corretas. Registrar se houve ajuda. | Sem limite. Meta de mediana de até 5 minutos conforme MU03. |
| UT02 | A configuração de um experimento foi preparada por um colega. Ao tentar deixá-la pronta para execução, você encontra um problema. Descubra o que precisa ser corrigido e deixe a execução pronta para revisão. | Avaliar reconhecimento da seed ausente e recuperação. T02/T04, OBJ03, M01. O moderador começa a tarefa com a seed vazia. | Reconhecer que falta a seed, identificar como corrigir, recuperar o valor 42 disponível no protótipo e chegar à revisão após nova validação. | Sem limite. |
| UT03 | O experimento já foi confirmado. Enquanto ele roda, diga em que estado se encontra e qual estratégia de controle está sendo usada. | Avaliar visibilidade do andamento e do controlador. T05, OBJ04, M01. | Identificar corretamente o estado exibido e o controlador no contexto da execução. Registrar se foi necessário consultar detalhes técnicos ou receber ajuda. | Sem limite. O piloto deve validar uma janela de observação padronizada para todos. |
| {{ID do M02}} | {{instrução neutra do João}} | {{...}} | {{...}} | {{...}} |

> Uma boa instrução descreve o objetivo do participante sem dizer **onde clicar** ou usar o rótulo exato do controle que está sendo testado.

Na UT03, se a transição automática impedir o participante de observar o estado, registrar a ocorrência como limitação do protótipo. O piloto deve definir como manter o quadro **Executando** disponível durante a pergunta, seguindo o mesmo procedimento para todos os participantes.

## E. Instrumentos

- [Modelo de termo de consentimento](../instrumentos/termo_consentimento_modelo.md)
- [Roteiro de teste](../instrumentos/roteiro_teste_usabilidade.md)
- [Planilha de observação](../instrumentos/planilha_observacao_modelo.md)
- [Formulário de avaliação heurística](../instrumentos/formulario_heuristica_modelo.md)

**Pré-teste do M01.** Perguntar se a pessoa já configurou ou acompanhou uma simulação e quais informações costuma conferir antes de executá-la.

**Pós-tarefa do M01.** Perguntar «Quão fácil ou difícil foi realizar esta tarefa?» em escala de 1 a 5, em que 1 significa muito difícil e 5, muito fácil. Em seguida, perguntar «O que mais influenciou sua resposta?».

**Pós-teste do M01.** Perguntar «Em qual momento foi mais difícil decidir como prosseguir?» e «Que informação teria ajudado nessa etapa?».

**Questões e instrumentos específicos do M02:** {{preencher}}.

## F. Plano de análise

### Contribuição de Gabriel — M01

| Item | Regra para registro e análise |
|---|---|
| Sucesso total | O participante atinge o critério observável da tarefa sem receber orientação sobre a solução. |
| Sucesso parcial | O participante cumpre apenas parte do critério ou conclui após uma ajuda direta do moderador. Registrar o trecho concluído e a ajuda recebida. |
| Falha | O participante encerra sem atingir o critério mínimo, conclui com uma condição incorreta ou abandona a tarefa. Registrar o motivo quando possível. |
| Erro e dúvida | Erro é uma ação ou escolha que desvia do objetivo ou exige correção. Dúvida é uma hesitação ou dificuldade verbalizada. Uma mesma ocorrência pode ser registrada com seu contexto, evitando contar repetidamente a mesma ação. |
| Ajuda e abandono | Ajuda é uma intervenção que orienta a solução. Repetir a instrução original é registrado separadamente. Abandono ocorre quando o participante declara que não consegue ou não deseja prosseguir. |
| Tempo | Iniciar após a leitura da instrução e parar ao atingir o critério ou encerrar a tentativa. Na UT01, o cronômetro termina na conferência do resumo, antes de iniciar a simulação. Registrar interrupções técnicas separadamente. |
| Satisfação | Registrar a nota de 1 a 5 após cada tarefa e a justificativa. Apresentar a mediana junto das notas individuais, dado o tamanho da amostra. |
| Registro qualitativo | Identificar tarefa, quadro, ação e consequência. Classificar ocorrências por configuração, validação, confirmação ou percepção do estado. Citações devem estar associadas apenas ao identificador do participante. |
| Priorização | Dar prioridade às dificuldades que bloqueiam a tarefa ou levam à confirmação de condições incorretas. Relacionar cada achado ao quadro, à consequência e, quando houver, à evidência da inspeção heurística. |
| Comparação com as metas | Apresentar contagens e denominadores por tarefa, como `2/2 sem ajuda`, a mediana do tempo de preparação e a mediana das notas. Informar se cada meta foi atingida nas sessões observadas e indicar casos afetados por limitações do protótipo. |

### Contribuição de João — M02

{{preencher}}

### Consolidação dos dois fluxos

{{definir em dupla após completar o planejamento do M02}}

## Checklist

- [x] As seis etapas DECIDE foram contextualizadas para o M01.
- [x] As perguntas do M01 têm método e evidência correspondentes.
- [x] O plano distingue a avaliação de IHC da avaliação técnica/científica do TCC.
- [x] Os dados e processamentos simulados no M01 estão declarados.
- [x] As tarefas do M01 vêm de objetivos e cenários das entregas anteriores.
- [x] Os critérios de sucesso do M01 foram definidos antes da coleta.
- [ ] O planejamento do M02 foi acrescentado e consolidado com o M01.
- [ ] As questões práticas e éticas foram fechadas pela dupla.
- [ ] Os instrumentos e o roteiro estão prontos para as Entregas 13 e 14.
- [ ] O piloto foi realizado e as condições da sessão foram confirmadas.
- [x] O plano de análise do M01 define como registrar e apresentar os dados.

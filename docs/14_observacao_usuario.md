# Entrega 14 — Avaliação de usabilidade por observação de usuários

**Data do relatório:** 19/11/2026.  
**Status:** 🟩 relatório concluído — observações de U01 e U02 registradas, resultados consolidados e limitações documentadas.  
**Responsabilidade:** solução consolidada por equipe, com dois participantes finais externos à equipe.

## Objetivo da atividade

Observar participantes realizando tarefas representativas para avaliar eficácia, eficiência, compreensão e satisfação. O objeto é a interação com o protótipo Figma da Entrega 11, e não o desempenho científico do algoritmo ou do SUMO.

**Origem dos registros:** os dados de U01 foram fornecidos e validados por Gabriel, e os de U02 foram fornecidos e validados por João Pedro; ambos foram apresentados à equipe como resultados de sessões reais. A consolidação considera as anotações relatadas pelos moderadores, sem auditoria independente dos registros brutos. Os valores demonstrativos do próprio Figma não são resultados científicos reais de simulações do TCC.

A amostra final contém **dois participantes externos à equipe** (U01 e U02), ambos caracterizados como perfis aproximados (*proxy*), sem experiência profissional em controle de tráfego. Essa composição limita as conclusões sobre os perfis de pesquisadores e especialistas representados pelas proto-personas P01 e P02. Os moderadores não foram contabilizados como participantes.

## A. Fluxograma do processo — equipe

![Fluxograma da avaliação observacional](../assets/14_testes/fluxograma_avaliacao.svg)

O processo compreende: planejamento e definição da versão → recrutamento → consentimento → preparação e piloto → tarefas e observação → pós-teste → análise → recomendações.

As sessões de U01 e U02, assim como o piloto preparatório, foram relatadas como realizadas. O fluxograma definitivo está publicado em `assets/14_testes/fluxograma_avaliacao.svg`. A sequência do diagrama descreve o método adotado para planejar, observar, analisar, confrontar achados e propor melhorias, e não implica que todas as melhorias sugeridas já tenham sido implementadas.

## B. Procedimento de preparação e execução — equipe

### Passo 1 — Objetivos e versão avaliada

**Interface:** Figma da Entrega 11, fluxos M01 e M02.  
**Sessão U01:** 18/11/2026 — moderador Gabriel.  
**Sessão U02:** 19/11/2026 — moderador João Pedro.

- [Arquivo editável](https://www.figma.com/design/YJJhBTujdrsjDY113Iefj4/Sem-t%C3%ADtulo?node-id=4-12).
- [M01 — configuração e execução](https://www.figma.com/proto/YJJhBTujdrsjDY113Iefj4/Sem-t%C3%ADtulo?node-id=4-12&scaling=scale-down-width&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=4%3A12).
- [M02 — histórico e resultados](https://www.figma.com/proto/YJJhBTujdrsjDY113Iefj4/Sem-t%C3%ADtulo?node-id=16-206&scaling=scale-down-width&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=16%3A206).

Nas duas sessões, o quadro **Executando** foi apresentado de forma estável na UT03, conforme o procedimento de preparação documentado. Os resultados dessa tarefa avaliam o reconhecimento de estado e controlador nessa condição; não demonstram que as transições automáticas originais tenham duração suficiente para sua percepção.

O material consultado identifica os fluxos e os links do Figma, mas não oferece um identificador imutável da revisão histórica visualizada em cada sessão. Ambos os moderadores declararam utilizar o mesmo procedimento; não há registro de correções dos problemas HC01–HC07 entre as duas coletas. Por isso, os resultados são comparados com essa ressalva e **não** se presume que as violações heurísticas tenham sido corrigidas.

| Meta | Critério previsto | Fonte |
|---|---|---|
| MU01 | 100% preparam a configuração sem ajuda direta. | UT01 |
| MU02 | 100% identificam a ação correta de recuperação. | UT02 |
| MU03 | Mediana de preparação de até 5 minutos. | UT01 |
| MU04 | 100% reconhecem estado e controlador. | UT03 |
| MU05 | 100% identificam registro e condições solicitadas. | UT04 |
| MU06 | Mediana de localização de até 3 minutos. | UT04 |
| MU07 | Mediana de facilidade de pelo menos 4/5. | Pós-tarefa |
| MU08 | 100% compreendem consulta individual e comparação externa. | UT05 e pós-teste |

As metas são avaliadas na amostra efetivamente documentada (**N = 2**), mantendo resultados e limitações individuais. Para metas de 100%, sucesso significa 2/2 participantes no critério aplicável; um sucesso parcial não é computado como sucesso total. As medianas de tempo e facilidade são calculadas exclusivamente com medidas disponíveis e comparáveis.

R2-001 mostra 28 s e R2-002 mostra 36 s de espera média. Esses valores pertencem à demonstração do Figma e não são resultados reais de desempenho do algoritmo.

A exploração da aplicação funcional R3 em 15/11 permanece separada e é identificada nas documentações da Entrega 12 pelos códigos EX01 e EX02. Essa exploração não foi utilizada para preencher tempos, erros ou satisfação da avaliação padronizada.

Neste relatório, U01 e U02 identificam exclusivamente os participantes das sessões padronizadas do Figma, realizadas em 18 e 19/11/2026. Não se presume qualquer identidade entre os participantes das duas atividades, preservando a distinção metodológica e a privacidade dos envolvidos.

### Passo 2 — Participantes

| ID | Perfil e adequação | Responsável | Situação |
|---|---|---|---|
| U01 | Conhecimento básico do conceito de simulação, sem prática com SUMO; familiaridade com tabelas, gráficos de barras e indicadores; conhecimento básico de mobilidade urbana. Proxy com familiaridade parcial com análise, sem experiência profissional em controle de tráfego. | Gabriel Koiama de Rocha Lira — 22.125.067-3. | Sessão e resultados informados como reais pelo moderador. |
| U02 | Estudante de Engenharia de Computação, com experiência acadêmica básica em simulações e experiência intermediária com gráficos e dados, sem familiaridade prática com SUMO nem com sistemas de controle semafórico; proxy. | João Pedro Lopes Santana Villas Bôas — 22.125.065-7. | Sessão realizada em 19/11/2026; seis tarefas, pré-teste e pós-teste documentados. |

A familiaridade de U01 com gráficos fundamenta sua participação como perfil aproximado, sem torná-lo equivalente a um especialista. O relato de U01 não detalha seu uso anterior da aplicação ou do Figma; esse fator não será presumido ao interpretar os tempos. U02 relatou experiência intermediária com gráficos, conhecimento básico de simulações acadêmicas, baixa familiaridade com mobilidade urbana e nenhum uso anterior do protótipo avaliado. Os dois perfis são adequados para identificar dificuldades gerais de interação, **não para validar demandas de profissionais de tráfego**.

### Passo 3 — Consentimento, ambiente e privacidade

- **Instrumento:** [termo e procedimento de consentimento](../instrumentos/termo_consentimento_modelo.md).
- **Aceite de U01:** concordância voluntária prévia, conforme relato de Gabriel; o formato documental do aceite não foi especificado na síntese recebida.
- **Aceite de U02:** João relatou que apresentou objetivos, procedimentos, forma de registro e possibilidade de interrupção, obtendo concordância voluntária antes da sessão; não foi anexada cópia de termo assinado.
- **Registros utilizados:** planilhas de tarefas, descrições das ocorrências, tempos informados pelos moderadores e respostas pós-teste de cada participante.
- **Gravação:** não houve gravação das sessões de U01 e U02. Conforme confirmação verbal do professor relatada pela equipe, a gravação não é necessária para esta entrega. Os resultados foram registrados por anotações e planilhas de observação, de acordo com o procedimento adotado.
- **Identificação pública:** somente U01 e U02, sem nomes dos participantes.
- **Ambiente de U01:** local, equipamento, resolução, escala e horário não discriminados no registro resumido.
- **Ambiente de U02:** sala silenciosa, notebook Windows, navegador em resolução informada de 1920 × 1080; horário e escala do navegador não discriminados.
- **Guarda dos dados:** registros de observação e eventuais comprovantes de consentimento devem permanecer sob responsabilidade da equipe e fora do repositório público. Resultados técnicos de simulações e registros pessoais da avaliação têm finalidades e regras de preservação distintas.

### Passo 4 — Teste piloto

**Situação informada:** realizado antes da sessão de U01.  
**Responsável pelo relato:** Gabriel.  
**Data, executor e ambiente específicos do piloto:** não discriminados nos registros resumidos disponíveis. João informou que o procedimento preparatório foi reaproveitado na sua sessão.

| Verificação informada | Registro |
|---|---|
| Links M01 e M02 | Abertura correta. |
| UT02 | Configuração com seed ausente preparada. |
| UT03 | Estado Executando apresentado de forma estável para permitir a pergunta. |
| Instrumentação | Cronômetro e planilha conferidos. |
| Instruções | Mantidas padronizadas. |

**Ajuste informado e aplicado:** apresentar diretamente o quadro Executando durante UT03 para evitar que uma transição automática impedisse a observação. João relatou ter empregado a mesma apresentação estável com U02. Assim, a identificação do estado é comparável **nessa condição controlada**, mas não testa a duração padrão das transições.

O piloto não é contado na amostra final. A exploração de 15/11 não foi reclassificada como piloto.

### Passo 5 — Tarefas padronizadas

As instruções abaixo são as da Entrega 12 e do instrumento `roteiro_teste_usabilidade.md`. **O participante recebe apenas o enunciado**, não o critério de sucesso nem os caminhos esperados.

| ID | Instrução apresentada | Critério de sucesso do observador | Métricas | Rastreabilidade |
|---|---|---|---|---|
| UT01 | Prepare um experimento para Regional São Paulo, usando o controlador híbrido, seed 42 e execução sem abrir a janela gráfica do simulador. Confira as condições antes de iniciar. | Chegar ao resumo com cenário R2, controlador híbrido, seed 42 e modo Headless. | Sucesso, tempo até o resumo, erros, ajudas e facilidade. | T01–T03; OBJ02–OBJ03; M01; F01–F03. |
| UT02 | Um colega preparou uma configuração. Ao tentar deixá-la pronta para execução, você encontra um problema. Descubra o que precisa corrigir. | Identificar a seed ausente, recuperar 42 e validar novamente. | Sucesso, tempo, erros, ajudas e facilidade. | T02/T04; OBJ03; M01; F02/F02E/F03. |
| UT03 | O experimento já foi confirmado. Diga em que estado se encontra e qual estratégia está sendo usada. | Identificar o estado mostrado e o controlador. | Acerto, tempo de resposta, ajudas, facilidade e eventual interferência de transição. | T05; OBJ04; M01; F04/F04P/F05. |
| UT04 | Encontre R2-001 e identifique seu cenário, sua estratégia e sua seed. | Abrir R2-001 e informar Regional São Paulo, híbrido e seed 42. | Sucesso, tempo de localização, erros, ajudas e facilidade. | T06; OBJ06; M02; F07/F08. |
| UT05 | Compare o tempo médio de espera de R2-001 e R2-002. Explique quais condições precisam ser conferidas antes de interpretar a diferença. | Identificar 28 s e 36 s nos registros corretos, conferir condições e explicar a reunião externa dos valores. | Sucesso, valores e explicação, tempo, erros, ajudas e facilidade. | T06–T08; OBJ07–OBJ09; M02; F07/F08/F08B/F09/F09B. |
| UT06 | Consulte R2-003. Se encontrar um impedimento, explique o que aconteceu e continue com outro registro. | Reconhecer a indisponibilidade, retornar ao histórico e abrir outro resultado. | Sucesso, tempo, erros, ajudas e facilidade. | T06; OBJ06; M02; F07/F08E/F08. |

**Critérios de classificação e registro:**

- **Sucesso total:** critério cumprido sem orientação sobre a solução.
- **Sucesso parcial:** critério parcialmente cumprido ou conclusão após ajuda direta.
- **Falha:** critério não atingido, resposta incorreta ou abandono.
- **Erro:** ação que afasta o participante do objetivo ou exige correção; registrar o tipo e o contexto.
- **Ajuda direta:** intervenção do moderador indicando como resolver. A simples repetição do enunciado será registrada separadamente.
- **Tempo:** iniciar após a leitura da instrução e encerrar ao atingir o critério ou terminar a tentativa. Em UT01, parar na revisão do resumo; em UT04, medir o tempo de localização até abrir o registro, registrando separadamente o acerto das condições.
- **Facilidade percebida:** 1 = muito difícil; 2 = difícil; 3 = nem fácil nem difícil; 4 = fácil; 5 = muito fácil.
- **Limites:** não impor tempo-limite; comparar os registros com as metas apenas na análise posterior.

### Passo 6 — Condução das sessões U01 e U02

Gabriel moderou U01, e João Pedro moderou U02. Ambos relataram a utilização dos seis enunciados estabelecidos na E12 e no [roteiro padronizado](../instrumentos/roteiro_teste_usabilidade.md), com campos previstos na [planilha de observação](../instrumentos/planilha_observacao_modelo.md). Foram documentados desempenho por tarefa, facilidade percebida e respostas pós-teste. O participante recebe apenas o enunciado, sem o critério de sucesso reservado ao observador.

A classificação distingue erros corrigidos espontaneamente de ajuda direta. Em U01, UT02 exigiu orientação sobre campos obrigatórios e foi classificada como parcial. Em U02, as tarefas UT04 e UT06 exigiram intervenções, também classificadas como parciais. Erros corrigidos sem ajuda não impedem, por si só, sucesso total.

Os registros disponíveis incluem durações de tarefas, mas não horários individualizados de início e término nem anexos das fichas brutas. Em UT04, Gabriel registrou 01:34 como duração total de U01, sem separar o tempo de localização; João registrou 03:22 como tempo total de U02, com **02:58 até abrir R2-001**. Essa distinção será preservada na análise da meta MU06.

## C. Resultados — por participante

### U01 — Participante proxy sob responsabilidade de Gabriel

**Data informada:** 18/11/2026.  
**Moderador:** Gabriel Koiama de Rocha Lira — 22.125.067-3.  
**Interface:** Figma da Entrega 11; M01 e M02.  
**Consentimento:** concordância voluntária prévia, conforme relato do moderador.  
**Situação:** seis resultados e respostas pós-teste registrados a partir dos dados fornecidos.

| Tarefa | Grau de sucesso | Erros | Dificuldade ou ocorrência | Ajudas | Tempo | Facilidade | Evidência/observação |
|---|---|---:|---|---:|---|---:|---|
| UT01 | Total | 1 | Escolheu Visual inicialmente e corrigiu para Headless sem ajuda. | 0 | 02:42 | 4/5 | Resumo com R2, híbrido, seed 42 e Headless. |
| UT02 | Parcial | 1 | Procurou o problema nas opções do controlador antes de identificar a seed ausente. | 1 | 01:42 | 3/5 | Após orientação para examinar os campos obrigatórios, recuperou 42 e validou novamente. |
| UT03 | Total | 0 | Nenhuma dificuldade relatada na condição de apresentação estável. | 0 | 00:12 | 5/5 | Identificou Executando e o controlador híbrido. |
| UT04 | Total | 1 | Abriu R2-002 e corrigiu a seleção espontaneamente. | 0 | 01:34 | 4/5 | Abriu R2-001 e identificou cenário, controlador e seed. |
| UT05 | Parcial | 1 | Interpretou inicialmente o menor tempo como melhor desempenho antes de conferir as condições; não completou a explicação da reunião externa durante a tarefa. | 0 | 02:36 | 3/5 | Identificou corretamente 28 s e 36 s; a explicação mais completa surgiu no pós-teste. |
| UT06 | Total | 0 | Nenhuma dificuldade relatada na recuperação. | 0 | 01:15 | 4/5 | Reconheceu o aviso de indisponibilidade, voltou ao histórico e abriu outro resultado. |

#### Detalhamento das ocorrências

- **UT01:** o erro foi corrigido espontaneamente antes da confirmação. A existência de um erro corrigido não impede sucesso total, pois o critério foi atingido sem ajuda direta.
- **UT02:** a configuração inválida foi o estado inicial previsto. O erro contabilizado corresponde à investigação inicial do controlador; a necessidade de ajuda explica a classificação parcial.
- **UT03:** a condição estável permite avaliar identificação, mas limita conclusões sobre percepção de estados durante a execução temporizada original.
- **UT04:** a seleção incorreta foi recuperada sem ajuda. O registro de 01:34 não discrimina separadamente o momento de abertura de R2-001.
- **UT05:** sucesso parcial foi preservado para a execução da tarefa. A resposta posterior mais completa foi registrada separadamente e não altera retroativamente o desempenho observado.
- **UT06:** a recuperação foi concluída. Não foi informada a percepção do participante sobre o status de R2-003 antes da abertura.

#### Pós-teste

**Em qual momento foi mais difícil decidir como prosseguir?**

> Na parte de comparar os resultados. Eu conseguia encontrar os valores, mas fiquei em dúvida sobre quais informações precisava conferir para comparar as simulações corretamente.

**Que informação teria ajudado?**

> Uma explicação mais clara das métricas e uma escala numérica nos gráficos ajudariam a entender melhor os resultados.

**Como reuniria as informações para comparar duas execuções?**

> Eu consultaria cada execução no histórico, anotaria os valores e as condições do experimento e organizaria tudo em uma tabela para comparar depois.

As falas foram transcritas conforme o texto fornecido pelo moderador; não foram confrontadas com gravação.

#### Síntese individual

| Indicador | U01 |
|---|---|
| Sucesso total | 4/6 tarefas — 66,7%. |
| Sucesso parcial | 2/6 tarefas — 33,3%. |
| Falhas | 0/6 tarefas. |
| Erros | 4 ocorrências informadas. |
| Ajudas diretas | 1, em UT02. |
| Facilidade por tarefa | 4, 3, 5, 4, 3 e 4. |
| Mediana das seis notas de U01 | 4/5. |
| Menor facilidade | UT02 e UT05, ambas com 3/5. |

Essas proporções descrevem tarefas de um participante. Não equivalem à proporção de participantes que atende a cada meta na amostra completa. A mediana das seis notas de U01 também não substitui a análise por tarefa com os dois participantes.

### U02 — Participante sob responsabilidade de João Pedro

**Data da sessão:** 19/11/2026.  
**Moderador:** João Pedro Lopes Santana Villas Bôas — 22.125.065-7.  
**Participante:** U02 — pessoa externa à equipe, identificada anonimamente.  
**Interface:** Protótipo Figma da Entrega 11, fluxos M01 e M02.  
**Ambiente:** sala silenciosa, notebook Windows, navegador em tela de 1920 × 1080.  
**Registro:** planilha de observação e cronômetro, sem gravação.

#### 1. Perfil de U02

O participante é um estudante de Engenharia de Computação, familiarizado com softwares técnicos, análise de dados e utilização de gráficos, porém sem experiência direta com o simulador SUMO ou com a operação de sistemas de controle semafórico.

No pré-teste, informou:

- Experiência com simulações computacionais: básica, principalmente em atividades acadêmicas.
- Experiência com tabelas e gráficos: intermediária.
- Familiaridade com mobilidade urbana: baixa.
- Experiência prévia com o protótipo avaliado: nenhuma.

**Adequação ao público-alvo:** participante proxy. Sua experiência com tecnologia e interpretação de dados é relevante para avaliar aspectos gerais de interação, mas não representa integralmente as necessidades de especialistas em tráfego.

#### 2. Consentimento

Antes da sessão, o moderador apresentou o objetivo, a duração prevista, as tarefas, a forma de registro e o direito de interromper a participação.

O participante concordou voluntariamente com a avaliação e com o registro escrito de suas respostas.

**Aceite:** sim, antes do início das tarefas.  
**Gravação:** não realizada.  
**Identificação pública:** U02.

#### 3. Teste piloto

Foi realizado um piloto de preparação pela equipe antes da primeira sessão, com procedimento reaproveitado para U02.

Foram conferidos os links dos fluxos M01 e M02, as condições iniciais das tarefas e os recursos para registrar tempo, erros e ajudas.

Na UT02, a configuração foi preparada com a seed ausente. Na UT03, o estado Executando foi apresentado diretamente, permanecendo visível durante a pergunta, para evitar interferência das transições automáticas.

O procedimento adotado foi o mesmo documentado para U01, permitindo comparar os resultados sob condições semelhantes.

O piloto não foi contabilizado como participante final.

#### 4. Resultados das tarefas UT01–UT06

| Tarefa | Sucesso | Erros | Ajudas | Tempo | Facilidade |
|---|---|---:|---:|---|---:|
| UT01 | Total | 0 | 0 | 02:14 | 5/5 |
| UT02 | Total | 1 | 0 | 01:18 | 4/5 |
| UT03 | Total | 0 | 0 | 00:16 | 5/5 |
| UT04 | Parcial | 2 | 1 | 03:22 | 2/5 |
| UT05 | Total | 1 | 0 | 02:51 | 4/5 |
| UT06 | Parcial | 1 | 1 | 01:49 | 3/5 |

**Critérios:** sucesso total significa conclusão sem ajuda direta, mesmo que algum erro tenha sido corrigido espontaneamente. Sucesso parcial representa conclusão incompleta ou após ajuda direta. O tempo registra a duração da tentativa, salvo a medição específica descrita na UT04.

#### UT01 — Preparação do experimento

**Objetivo:** preparar um experimento no cenário R2, com controlador híbrido, seed 42 e execução Headless.

**Observação:**

O participante iniciou pelo catálogo, selecionou Regional São Paulo e avançou para a configuração. Identificou corretamente o controlador híbrido, definiu a seed 42 e selecionou Headless.

Antes de avançar, revisou as condições apresentadas e confirmou que correspondiam ao solicitado.

Não ocorreram erros ou solicitações de ajuda.

**Resultado:** sucesso total.  
**Tempo:** 02:14.  
**Erros:** 0.  
**Ajudas:** 0.  
**Facilidade:** 5/5.

**Interpretação:** a tarefa de preparação foi executada corretamente e sem intervenção, dentro do limite previsto para MU03.

#### UT02 — Recuperação de configuração inválida

**Objetivo:** identificar e corrigir uma configuração com seed ausente.

**Observação:**

Ao encontrar a mensagem de validação, o participante inicialmente verificou a seleção do controlador, supondo que a estratégia escolhida estivesse incorreta.

Após perceber que o controlador estava corretamente definido, examinou os demais campos, identificou a ausência da seed e informou o valor 42.

Realizou a validação novamente e conseguiu prosseguir sem intervenção do moderador.

**Resultado:** sucesso total.  
**Tempo:** 01:18.  
**Erros:** 1 — investigação inicial do campo incorreto.  
**Ajudas:** 0.  
**Facilidade:** 4/5.

**Interpretação:** houve dificuldade inicial, mas o participante conseguiu identificar e corrigir o erro de forma autônoma.

#### UT03 — Reconhecimento do estado de execução

**Objetivo:** identificar o estado atual do experimento e a estratégia de controle utilizada.

**Observação:**

Com o quadro Executando apresentado de maneira estável, o participante reconheceu imediatamente que a simulação estava em andamento.

Também identificou corretamente o controlador híbrido.

**Resultado:** sucesso total.  
**Tempo:** 00:16.  
**Erros:** 0.  
**Ajudas:** 0.  
**Facilidade:** 5/5.

**Interpretação:** o estado e o controlador foram reconhecidos sem dificuldades na condição controlada da tarefa. Isso não comprova que as transições automáticas originais sejam suficientemente longas.

#### UT04 — Localização de uma execução no histórico

**Objetivo:** encontrar R2-001 e identificar cenário, controlador e seed.

**Observação:**

O participante acessou o histórico, mas apresentou dificuldade para diferenciar os registros.

Inicialmente selecionou R2-003. Ao perceber que não correspondia ao identificador solicitado, voltou ao histórico e selecionou R2-002.

Depois de uma nova tentativa, solicitou ajuda ao moderador.

O moderador orientou que examinasse os identificadores dos registros, sem indicar diretamente qual deles selecionar.

Após a intervenção, o participante localizou R2-001 e identificou corretamente o cenário Regional São Paulo, o controlador híbrido e a seed 42.

**Resultado:** sucesso parcial.  
**Tempo total:** 03:22.  
**Tempo até abrir R2-001:** 02:58.  
**Erros:** 2 — seleção de registros incorretos.  
**Ajudas:** 1 — orientação direta para examinar os identificadores.  
**Facilidade:** 2/5.

**Interpretação:** a tarefa foi concluída, porém exigiu ajuda. O tempo de localização foi registrado separadamente para permitir avaliar MU06. A dificuldade sugere investigar a diferenciação dos registros no histórico.

#### UT05 — Interpretação e comparação de resultados

**Objetivo:** comparar os tempos médios de espera de R2-001 e R2-002, considerando as condições experimentais.

**Observação:**

O participante consultou o primeiro registro e encontrou o tempo médio de espera de 28 segundos.

Ao consultar o segundo, identificou o valor de 36 segundos. Inicialmente confundiu a associação entre o valor e o identificador, mas conferiu o cabeçalho e corrigiu espontaneamente a anotação.

Em seguida, explicou que, antes de afirmar que uma estratégia apresentou melhor desempenho, seria necessário verificar cenário, demanda, seed e demais condições relevantes do experimento.

Também explicou que reuniria as informações das duas execuções em uma tabela externa, já que o Figma não oferece comparação automática lado a lado.

**Resultado:** sucesso total.  
**Tempo:** 02:51.  
**Erros:** 1 — associação inicial incorreta de valor e registro.  
**Ajudas:** 0.  
**Facilidade:** 4/5.

**Interpretação:** mesmo com um erro corrigido espontaneamente, o participante conseguiu recuperar os valores, reconhecer a necessidade de condições comparáveis e explicar o procedimento de comparação externa.

#### UT06 — Recuperação de resultado indisponível

**Objetivo:** consultar R2-003 e continuar a navegação quando o resultado estiver indisponível.

**Observação:**

O participante selecionou R2-003 e identificou que o resultado não estava disponível.

Inicialmente tentou localizar outra ação dentro do mesmo quadro, em vez de retornar ao histórico.

Após solicitar ajuda, o moderador orientou que examinasse as opções de navegação disponíveis.

O participante encontrou a ação Voltar ao histórico e conseguiu abrir outro registro.

**Resultado:** sucesso parcial.  
**Tempo:** 01:49.  
**Erros:** 1 — tentativa de prosseguir por um caminho inadequado.  
**Ajudas:** 1 — orientação direta sobre a navegação.  
**Facilidade:** 3/5.

**Interpretação:** a recuperação foi possível, mas exigiu intervenção. O resultado sugere investigar a clareza e a visibilidade da ação de retorno.

#### 5. Respostas do pós-teste

**Pergunta 1 — Em qual momento foi mais difícil decidir como prosseguir?**

> Tive mais dificuldade para encontrar o registro certo no histórico. Os nomes das execuções eram parecidos e acabei abrindo outras opções antes de localizar a correta.

**Pergunta 2 — Que informação teria ajudado?**

> Acho que seria melhor se os identificadores das execuções ficassem mais destacados. Na tela de resultado indisponível, também poderia ficar mais claro como voltar e continuar.

**Pergunta 3 — Como reuniria as informações para comparar duas execuções?**

> Eu abriria os dois resultados separadamente, anotaria o tempo médio de espera e as informações de cada experimento e depois colocaria esses valores em uma planilha. Antes de comparar, verificaria se as condições dos testes são equivalentes.

#### 6. Síntese individual de U02

| Indicador | Resultado |
|---|---|
| Sucesso total | 4/6 tarefas — 66,7% |
| Sucesso parcial | 2/6 tarefas — 33,3% |
| Falhas | 0/6 tarefas |
| Erros | 5 |
| Ajudas diretas | 2 |
| Facilidade por tarefa | 5, 4, 5, 2, 4, 3 |
| Mediana das notas | 4/5 |
| Tarefa de maior dificuldade | UT04 — localização no histórico |
| Outra dificuldade | UT06 — recuperação após indisponibilidade |

#### 7. Achados da observação de U02

| ID provisório | Achado | Evidência | Recomendação |
|---|---|---|---|
| AU03 | Dificuldade de identificação dos registros no histórico. | UT04: dois erros, uma ajuda, facilidade 2/5. | Melhorar destaque e diferenciação dos identificadores na lista. |
| AU06 | Recuperação da consulta exigiu orientação. | UT06: um erro, uma ajuda, facilidade 3/5. | Tornar a ação Voltar ao histórico mais evidente na tela de indisponibilidade. |
| AU07 | Dúvida inicial sobre a causa de configuração inválida. | UT02: um erro, corrigido espontaneamente. | Verificar se a indicação do campo seed pode ficar mais clara. |

**Observação sobre os IDs:** AU03 já é utilizado no relatório de U01 para a dificuldade de seleção no histórico. O identificador foi reutilizado por se tratar do mesmo tipo de problema. AU06 e AU07 são identificadores novos, sujeitos à consolidação da equipe.

#### 8. Conclusão individual de João Pedro

A observação de U02 apresentou quatro tarefas concluídas integralmente e duas parcialmente. O participante cometeu cinco erros e precisou de duas intervenções diretas do moderador.

As maiores dificuldades ocorreram na localização de um registro específico e na recuperação após encontrar um resultado indisponível.

A preparação do experimento, o reconhecimento do estado de execução e a comparação de métricas foram concluídos corretamente, embora algumas tarefas tenham apresentado erros corrigidos espontaneamente.

Os resultados indicam a necessidade de priorizar melhorias na diferenciação dos registros do histórico e na visibilidade das ações de recuperação.

As conclusões individuais de U02 estão limitadas a um participante proxy e não podem ser generalizadas para profissionais de mobilidade urbana. Os resultados foram confrontados com os de U01 na consolidação da equipe apresentada nas seções D, E e F, permitindo identificar dificuldades recorrentes, avaliar as metas MU01–MU08 e relacionar os achados observacionais aos problemas heurísticos da Entrega 13.

## D. Consolidação por tarefa — equipe

### D.1. Resultados quantitativos comparados

A consolidação utiliza as **12 tentativas documentadas** (seis tarefas para cada um dos dois participantes). Considera-se sucesso total apenas a conclusão sem ajuda direta; a conclusão com ajuda é **parcial**, mesmo quando o objetivo foi alcançado ao final. A presença de erro corrigido espontaneamente não transforma automaticamente sucesso total em parcial. As medidas de tempo são durações de interação com o Figma, **não** tempos de execução de algoritmos do SUMO.

| Tarefa | U01 — sucesso / tempo / facilidade | U02 — sucesso / tempo / facilidade | Sucessos totais | Parciais | Erros (U01+U02) | Ajudas (U01+U02) | Mediana do tempo informado | Mediana da facilidade |
|---|---|---|---:|---:|---:|---:|---|---|
| UT01 | Total / 02:42 / 4 | Total / 02:14 / 5 | 2/2 | 0/2 | 1 | 0 | **02:28** | **4,5/5** |
| UT02 | Parcial / 01:42 / 3 | Total / 01:18 / 4 | 1/2 | 1/2 | 2 | 1 | **01:30** | **3,5/5** |
| UT03 | Total / 00:12 / 5 | Total / 00:16 / 5 | 2/2 | 0/2 | 0 | 0 | **00:14** | **5/5** |
| UT04 | Total / 01:34 / 4 | Parcial / 03:22 / 2 | 1/2 | 1/2 | 3 | 1 | **02:28** (duração total, não localização) | **3/5** |
| UT05 | Parcial / 02:36 / 3 | Total / 02:51 / 4 | 1/2 | 1/2 | 2 | 0 | **02:43,5** | **3,5/5** |
| UT06 | Total / 01:15 / 4 | Parcial / 01:49 / 3 | 1/2 | 1/2 | 1 | 1 | **01:32** | **3,5/5** |

O tempo mediano indicado para UT04 é calculado a partir das **durações totais** de ambas as tentativas. Não representa a mediana medida do tempo de localização exigido por MU06. O tempo de localização de U02 foi 02:58; para U01, sabe-se somente que a duração total foi 01:34, sem marcação separada da abertura de R2-001. A mediana exata de localização não pode ser reconstruída a partir desses registros.

### D.2. Indicadores gerais da amostra

| Indicador | U01 | U02 | Consolidação |
|---|---:|---:|---|
| Sucessos totais | 4/6 | 4/6 | **8/12 tentativas (66,7%)** |
| Sucessos parciais | 2/6 | 2/6 | **4/12 tentativas (33,3%)** |
| Falhas | 0/6 | 0/6 | **0/12 tentativas** |
| Erros informados | 4 | 5 | **9 ocorrências** |
| Ajudas diretas | 1 | 2 | **3 intervenções** |
| Mediana das seis notas individuais | 4/5 | 4/5 | **4/5** — mediana das 12 notas reunidas |

As proporções 8/12 e 4/12 representam **tentativas de tarefa**, não participantes distintos. Cada pessoa realizou seis tarefas; com apenas duas pessoas, porcentagens podem ocultar diferenças individuais. A leitura principal deve preservar as contagens por tarefa e as ocorrências descritas nas sessões.

### D.3. Verificação final de MU01–MU08

| Meta | Critério previsto na E8/E12 | Evidência das duas sessões | Resultado e ressalvas |
|---|---|---|---|
| **MU01** | 100% preparam corretamente o experimento sem ajuda direta. | UT01: U01 e U02 com sucesso total; 0 ajudas. | **Atingida na amostra (2/2).** |
| **MU02** | 100% identificam a ação correta para recuperar a configuração inválida. | UT02: U01 concluiu com uma ajuda direta; U02 corrigiu autonomamente. | **Não atingida em autonomia (1/2 sem ajuda).** O acerto final de 2/2 não equivale a recuperação autônoma de ambos. |
| **MU03** | Mediana de preparação de até cinco minutos. | UT01: 02:42 e 02:14; mediana **02:28**. | **Atingida na amostra.** |
| **MU04** | 100% identificam estado e controlador. | UT03: ambos responderam corretamente e sem ajuda. | **Atingida na apresentação estável (2/2).** Não avalia a duração das transições automáticas originais. |
| **MU05** | 100% localizam o registro e identificam as condições corretas. | UT04: ambos chegaram a R2-001 e identificaram cenário, controlador e seed; U02 precisou de ajuda. | **Atingida quanto ao acerto final (2/2), com ressalva de autonomia** (1/2 sem ajuda). |
| **MU06** | Mediana do tempo até abrir o registro correto de até três minutos. | U02: localização em **02:58**. U01: duração total de UT04 de **01:34**, sem instante de abertura isolado. | **Limiar de três minutos compatível com ambas as observações, mas mediana exata não mensurável.** Não utilizar 02:28 como mediana de localização. |
| **MU07** | Mediana de facilidade pós-tarefa de pelo menos 4/5. | Mediana global das 12 notas: **4/5**; medianas por tarefa: UT01 4,5; UT02 3,5; UT03 5; UT04 3; UT05 3,5; UT06 3,5. | **Atingida na agregação global**, mas UT02, UT04, UT05 e UT06 ficaram abaixo de 4/5 por tarefa. |
| **MU08** | 100% compreendem que comparar exige consultar resultados individuais e reunir dados externamente. | UT05: U02 explicou corretamente durante a tarefa; U01 teve sucesso parcial na tarefa, mas explicou a comparação externa no pós-teste. | **Compreensão final relatada em 2/2**, porém somente **1/2 concluiu integralmente UT05 durante a execução**. Não confundir entendimento posterior com desempenho autônomo na tarefa. |

**Interpretação:** a avaliação mostra pontos positivos na preparação e identificação controlada do estado, bem como dificuldades em validação, diferenciação de registros e continuidade da navegação. Não é metodologicamente correto declarar que todas as metas foram atingidas integralmente. As qualificações de MU05, MU06, MU07 e MU08 decorrem da diferença entre conclusão final, ajuda prestada, medida incompleta e agregação das notas.

## E. Achados e recomendações — consolidação de U01 e U02

A equipe confrontou os achados individuais com os relatos das seis tarefas de cada participante. Ocorrências semelhantes foram agrupadas sob **um único ID de problema**, preservando a origem de cada evidência. Os IDs AU01–AU05 já existiam na contribuição de U01; AU06 foi identificado em U02. O **AU07 provisório** do relatório individual de João, relativo à investigação inicial do controlador na UT02, foi incorporado a **AU02**, por tratar da mesma dificuldade geral de localizar a causa da validação, e **não** é contado como um sétimo problema distinto. O AU03 de U02 também corresponde ao AU03 registrado por U01.

| ID consolidado | Problema ou oportunidade de melhoria | Evidência U01 | Evidência U02 | Ocorrência por participante | Recomendação | Rastreabilidade |
|---|---|---|---|---|---|---|
| **AU01** | Diferenciação entre execução Visual e Headless. | UT01: uma escolha inicial incorreta, corrigida sem ajuda. | UT01: configuração correta, sem erro. | **1/2** | Melhorar rótulos/descrições dos modos; manter a conferência do resumo antes de iniciar. | T02/T03; M01; F02/F03; PG02/PG03. |
| **AU02** | Identificação da causa da configuração inválida (seed ausente). | UT02: um erro, uma ajuda, sucesso parcial, facilidade 3/5. | UT02: um erro inicial de investigação do controlador, corrigido sem ajuda; facilidade 4/5. | **2/2**, com gravidade distinta | Associar diretamente a mensagem ao campo seed e orientar a correção; preservar o retorno e a nova validação. | T02/T04; M01; F02E; PG04. |
| **AU03** | Diferenciação dos registros no histórico. | UT04: abriu R2-002 antes de R2-001 e corrigiu espontaneamente. | UT04: abriu R2-003 e R2-002 antes de R2-001; uma ajuda e facilidade 2/5. | **2/2**, com gravidade distinta | Destacar identificador e condições; tornar registros visualmente diferenciáveis e conferir consistência entre histórico e resultado. | T06; M02; F07; PG01. |
| **AU04** | Verificação contextual antes de interpretar/comparar resultados. | UT05: sucesso parcial e dúvida sobre a comparabilidade; esclarecimento posterior no pós-teste. | UT05: confundiu inicialmente associação valor–registro, corrigiu sem ajuda e explicou corretamente a comparação externa. | **2/2** com ocorrências diferentes | Evidenciar cenário, controlador, seed e demanda; fornecer orientação contextual sobre comparabilidade sem apresentar comparador automático inexistente. | T07/T08; M02; F08/F08B; PG06/PG07. |
| **AU05** | Necessidade de escala e explicações das métricas. | Pós-teste: pediu escala numérica e explicações mais claras. | Não houve comentário equivalente explícito. | **1/2** | Acrescentar escala identificada aos gráficos e definições contextuais dos indicadores; avaliar novamente. | T06/T08; F08/F09; PG02/PG06; HC04/HC07. |
| **AU06** | Visibilidade da ação de retorno após resultado indisponível. | UT06: recuperou a consulta sem erro ou ajuda. | UT06: um erro e uma ajuda para identificar a navegação; facilidade 3/5. | **1/2** | Destacar a ação **Voltar ao histórico**, com rótulo inequívoco e posição previsível. | T06; M02; F08E/F07; PG04. |

A contagem por participante indica a presença de pelo menos uma ocorrência pertinente ao achado, **não** o número de eventos (que é detalhado nas tabelas de tarefas). Com **N = 2**, a recorrência em 2/2 é apenas um sinal de prioridade no estudo exploratório, não uma estimativa estatística válida para o público profissional.

**Priorização proposta:**

1. **Recuperação da configuração e identificação do campo inválido (AU02):** foi observada nos dois participantes e exigiu ajuda de U01.
2. **Localização e identidade de registros (AU03):** observada nos dois participantes e exigiu ajuda de U02; se relaciona à necessidade de corrigir a inconsistência heurística HC02, embora os percursos alternativos de HC02 não tenham sido testados diretamente.
3. **Contexto de comparação e clareza das métricas (AU04/AU05):** evitar interpretação de resultados sob condições incompatíveis; tratar explicações e escalas.
4. **Recuperação de resultado indisponível (AU06):** observada em U02, com intervenção direta.
5. **Clareza dos modos Visual/Headless (AU01):** ocorrência pontual, com recuperação autônoma.

Essas recomendações são **propostas de melhoria**, não funcionalidades já implementadas ou alterações já verificadas no Figma.

## F. Comparação com a avaliação heurística — equipe

A inspeção da E13 registrou **12 achados individuais**, agrupados em **sete problemas consolidados (HC01–HC07)**. A observação da E14 não repetiu exaustivamente todos os percursos avaliados na inspeção. Um problema não encontrado na tarefa observacional **não é considerado corrigido**.

| Achado heurístico | Evidências de U01 | Evidências de U02 | Conclusão permitida |
|---|---|---|---|
| **HC01 — status de R2-003 não explícito previamente** | UT06: identificou indisponibilidade **depois de abrir** o registro; retorno bem-sucedido. | UT06: identificou indisponibilidade **depois de abrir**; precisou de ajuda para retornar. | Não houve registro do reconhecimento do status antes da abertura; **HC01 não foi comprovado nem descartado** pelo teste. A dificuldade de retorno de U02 corresponde a AU06, uma questão relacionada, mas distinta. |
| **HC02 — identidade inconsistente de R2-001 entre conclusões alternativas e histórico** | UT04: selecionou R2-002 inicialmente, depois R2-001. Caminhos alternativos de conclusão não foram documentados. | UT04: teve dificuldade com identificadores e precisou de ajuda. Não foram percorridas as conclusões alternativas. | **AU03 reforça a importância da identificação**, mas não comprova diretamente a inconsistência entre conclusão e histórico; **HC02 segue como problema da inspeção a corrigir**. |
| **HC03 — falha de processamento sem diagnóstico suficiente** | UT02 examinou validação de seed, não a falha F04E. | UT02 examinou validação de seed, não a falha F04E. | **Não exercitado** na observação; não confundir erro de entrada com falha de processamento. |
| **HC04 — gráficos sem escala numérica** | Pós-teste solicitou escala numérica para interpretar os gráficos. | Não relatou falta de escala explicitamente. | **Relação qualitativa parcial** com o achado, sem medida de efeito causal sobre tempos ou acertos. |
| **HC05 — Projeção regional sem explicação** | Configuração avançada não mencionada no relato. | Configuração avançada não mencionada no relato. | **Não exercitado** pelas tarefas relatadas. |
| **HC06 — ausência de acesso uniforme ao histórico nas conclusões alternativas** | Não há registro de teste das conclusões de Tempo fixo Visual e Max Pressure Headless. | Não há registro de teste dessas conclusões. | **Não exercitado**; a recuperação no histórico após F08E não testa esse problema. |
| **HC07 — Throughput sem definição contextual** | Comentário genérico pedindo explicações das métricas; sem menção específica a Throughput. | Não relatou dificuldade específica com Throughput. | **Não confirmado especificamente**, embora AU05 recomende ajuda contextual de indicadores. |

A lista de problemas heurísticos, especialmente os de **severidade 3 (HC02 e HC06)**, deve continuar no plano de melhorias mesmo onde não houve cobertura observacional. A E14 complementa a E13; não a substitui nem atesta correções que não foram implementadas e verificadas.

## G. Conclusão — equipe

### Síntese individual de U01 — Gabriel

U01 concluiu **quatro tarefas integralmente e duas parcialmente**, com quatro erros, uma ajuda direta e mediana individual de facilidade de **4/5**. Em UT02, a recuperação da configuração precisou de intervenção; em UT05, o participante identificou os valores corretos, mas não concluiu a explicação comparativa durante a tarefa, apresentando entendimento mais completo no pós-teste. O estado Executando foi apresentado de forma estável em UT03, e o tempo específico de localização em UT04 não foi separado de sua duração total.

### Síntese individual de U02 — João Pedro

U02 concluiu **quatro tarefas integralmente e duas parcialmente**, com cinco erros, duas ajudas diretas e mediana individual de facilidade de **4/5**. A preparação inicial (UT01), o reconhecimento de estado (UT03) e a comparação (UT05) foram concluídos sem ajuda direta. As maiores dificuldades ocorreram em UT04, na diferenciação dos registros do histórico, e em UT06, na recuperação após o resultado indisponível. Em UT04, João diferenciou o tempo total (**03:22**) do tempo até abrir R2-001 (**02:58**).

### Síntese consolidada e decisões

Na amostra de dois participantes externos à equipe foram observados **8 sucessos totais e 4 parciais em 12 tentativas**, com **9 erros, 3 ajudas diretas e nenhuma falha final**. A mediana global das 12 notas de facilidade foi de **4/5**. A organização da preparação e o reconhecimento do estado em apresentação estável mostraram resultados favoráveis; já a recuperação de configuração inválida, a distinção entre registros e o apoio à interpretação demandam aprimoramento.

A meta **MU02 não foi atingida quanto à recuperação autônoma por 100% dos participantes**. MU01, MU03 e MU04 tiveram resultado favorável na amostra; MU05 teve acerto final de 2/2, com uma ajuda; MU06 apresentou limiar individual compatível, mas mediana exata de localização indisponível; MU07 atingiu o valor global previsto, embora quatro tarefas tenham mediana inferior a 4/5; MU08 foi demonstrada no entendimento após a sessão por ambos, mas somente U02 concluiu integralmente a atividade de comparação durante a tentativa. Esses resultados não autorizam afirmar que todas as metas foram atendidas irrestritamente.

As recomendações de projeto são: **(1)** vincular melhor mensagens de validação aos campos que exigem correção; **(2)** tornar identificadores e condições de execução inequívocos no histórico e nos resultados; **(3)** explicitar critérios de comparabilidade, unidades e escalas dos gráficos; **(4)** tornar a recuperação de resultado indisponível mais evidente; e **(5)** verificar a consistência dos percursos alternativos de conclusão apontados na E13. A ordem sugerida considera impacto, intervenções e relação com os objetivos T01–T08, não uma estimativa de incidência populacional.

### Limitações e condições de interpretação

- **Amostra pequena:** apenas **dois participantes**, ambos perfis aproximados (*proxy*) e sem experiência profissional em controle de tráfego; não é possível extrapolar para especialistas em mobilidade ou afirmar validação de H01.
- **Protótipo demonstrativo:** o Figma reproduz percursos e resultados predefinidos; não executa SUMO nem comprova desempenho real dos controladores.
- **Controle da UT03:** o estado Executando permaneceu visível; esse procedimento reduz interferência da transição, mas não mede a adequação temporal do comportamento automático original.
- **Medição da UT04:** U01 não tem o instante separado de abertura do registro; MU06 não possui mediana exata reproduzível, embora o limiar de três minutos seja compatível com os registros disponíveis.
- **Versão da interface:** os links e fluxos usados estão identificados, porém a revisão imutável do Figma em cada sessão não foi informada; não foi registrada implementação de correções entre as coletas.
- **Evidência documental:** as conclusões foram redigidas a partir dos relatos e medidas fornecidos pelos moderadores, sem verificação independente das fichas originais ou dos comprovantes documentais de consentimento. João relatou consentimento voluntário de U02; Gabriel relatou o de U01. A equipe deve preservar os registros pertinentes em ambiente privado, sem expor dados pessoais no GitHub.
- **Gravação e orientação do docente:** o protocolo da equipe previa observação com anotações, sem gravação. Embora o material geral de fechamento da disciplina mencione gravação da interação, a equipe informou ter confirmado diretamente com o professor que ela não é necessária para esta entrega. Assim, a ausência de gravação não é tratada como pendência metodológica. Permanecem explicitados os limites dos registros escritos e da documentação de consentimento disponível.

**Conclusão:** a E14 documenta as duas sessões relatadas, apresenta resultados individuais e consolidados, confronta as metas MU01–MU08 e distingue problemas observados, achados heurísticos e melhorias propostas. O estudo fornece evidências formativas sobre a interação com a versão demonstrativa, preservando as limitações metodológicas e sem substituir a avaliação técnica do TCC.

## Checklist

- [x] Fluxos M01/M02, objetivos, tarefas UT01–UT06 e critérios de sucesso documentados e rastreados às E8–E12.
- [x] Protótipo Figma distinguido da interface funcional SUMO/TraCI e de resultados científicos reais do TCC.
- [x] Fluxograma definitivo publicado em `assets/14_testes/fluxograma_avaliacao.svg`.
- [x] Dois participantes externos identificados por U01/U02 e classificados como perfis aproximados (*proxy*).
- [x] Piloto preparatório relatado e apresentação estável da UT03 documentada nos dois casos.
- [x] Consentimento voluntário prévio relatado por ambos os moderadores, com limitação quanto ao comprovante documental.
- [x] Seis tarefas por participante registradas com sucesso, erros, ajudas, duração, facilidade e observações.
- [x] Respostas pós-teste e sínteses individuais registradas para U01 e U02.
- [x] Resultados consolidados por tarefa, com denominadores, medianas e ressalvas de medidas incompletas.
- [x] MU01–MU08 confrontadas com os resultados, sem equiparar sucesso parcial a total.
- [x] Achados AU01–AU06 consolidados com origem identificada; AU07 provisório agrupado em AU02.
- [x] Evidências observacionais comparadas com HC01–HC07, sem presumir confirmação ou correção de problemas não exercitados.
- [x] Conclusão de equipe, recomendações e limitações redigidas a partir dos dois registros.
- [x] A equipe confirmou com o professor que a gravação não é necessária; as sessões foram documentadas por anotações.
- [x] O consentimento voluntário prévio de U01 e U02 foi informado pelos respectivos moderadores, sem presumir a existência de termos assinados.
- [x] Conferir e preservar privadamente os registros ou comprovantes de consentimento efetivamente disponíveis e exigíveis.
- [x] `README.md` e `RASTREABILIDADE.md` foram atualizados com os resultados consolidados da E14, e o `CHECKLIST_FINAL.md` foi revisado para a conferência de encerramento.


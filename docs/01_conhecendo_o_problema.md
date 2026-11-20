# Entrega 1 — Conhecendo o projeto, o usuário e o problema

**Data:** 19/08/2026  
**Status:** `🟩 Concluido`  
**Responsabilidade:** 1 solução consolidada por equipe

## Objetivo da atividade

Reinterpretar o tema do TCC sob a perspectiva de Interação Humano-Computador e construir um **entendimento comum entre os integrantes da equipe**.

A disciplina utiliza preferencialmente o tema do TCC para os exercícios de IHC. Isso vale tanto para TCCs que já preveem uma interface quanto para trabalhos cujo resultado principal é algoritmo, modelo, API, biblioteca, análise de dados, infraestrutura, estudo experimental ou outro artefato técnico.

> **Importante:** a interface projetada na disciplina é um artefato de aprendizagem de IHC. Ela **não se torna automaticamente uma obrigação do TCC**. Sua incorporação ao trabalho de conclusão depende de decisão da equipe e do orientador.

Antes de preencher, leia [`../GUIA_ESCOPO_IHC.md`](../GUIA_ESCOPO_IHC.md).

Nesta primeira semana a equipe **não deve começar desenhando telas**. Primeiro deverá compreender:

- o que o TCC realmente produz;
- quem poderia obter valor dessa contribuição;
- quais pessoas interagem, administram, configuram, interpretam ou são afetadas;
- o que essas pessoas precisam alcançar;
- como atividades relacionadas acontecem hoje;
- problemas, limitações e contexto;
- alternativas existentes;
- qual recorte de interação fará sentido para a disciplina.

Ao final desta entrega, a equipe deve diferenciar:

- **tema do TCC** × **escopo formal do TCC** × **escopo de IHC da disciplina**;
- **objetivo do projeto** × **objetivo do usuário**;
- **problema do usuário** × **solução tecnológica**;
- **fato conhecido** × **hipótese** × **lacuna de conhecimento**;
- **capacidade técnica** × **forma de uso dessa capacidade**;
- **funcionalidade** × **atividade/resultado que o usuário precisa alcançar**;
- **usuário direto** × **stakeholders**.

---

## Como classificar as respostas

Sempre que a resposta fizer uma afirmação sobre usuários, problemas, atividades, necessidades, contexto ou mercado, use:

- **[F] Fato conhecido** — existe evidência/fonte.
- **[H] Hipótese** — afirmação plausível que ainda precisa ser investigada.
- **[?] Não sabemos ainda** — lacuna relevante.

Quando usar `[F]`, informe a origem. Hipóteses prioritárias devem receber IDs (`H01`, `H02`...) e também ser registradas em [`../RASTREABILIDADE.md`](../RASTREABILIDADE.md).

> **Exemplo:** `[H] H01 — DBAs considerariam útil comparar automaticamente o plano atual de execução com uma recomendação produzida pelo algoritmo.`

Uma hipótese explicitada é melhor do que uma suposição escondida.

---

# 0. Identificação do TCC e da equipe

## 0.1 Membros

| Nome completo | Matrícula | GitHub |
|---|---:|---|
| Gabriel Koiama de Rocha Lira | 22.125.067-3 | @koiamagabriel |
| João Pedro Lopes Santana Villas Bôas | 22.125.065-7 | @JPLopes05 |

## 0.2 Título atual do TCC

**Algoritmo Híbrido de Controle Semafórico Baseado em Max Pressure e Lógica Actuated em Ambiente de Simulação**

## 0.3 Orientador(a)

**Ricardo de Carvalho Destro**

## 0.4 Qual é o resultado principal atualmente previsto no TCC?

Marque e descreva:

- [ ] sistema/aplicação interativa;
- [x] algoritmo;
- [ ] modelo de IA/ML/LLM;
- [ ] biblioteca/API/framework;
- [ ] análise de dataset;
- [x] estudo/benchmark/avaliação experimental;
- [ ] infraestrutura/backend;
- [ ] componente embarcado/IoT;
- [ ] outro.

**Descrição:** O resultado principal previsto é o desenvolvimento e a avaliação experimental de um algoritmo híbrido de controle semafórico que combina o método Max Pressure com uma lógica do tipo actuated. O método será comparado com o controle de tempo fixo e com o Max Pressure convencional em diferentes cenários simulados.

## 0.5 O TCC já previa desenvolvimento de interface com usuário?

- [ ] Sim, a interface já faz parte do TCC.
- [x] Parcialmente; existe alguma interação, mas ainda não está bem definida.
- [ ] Não. O TCC é predominantemente técnico e não previa interface.

**Explique o que está formalmente previsto no TCC:**  
**[F]** A equipe já considerava o desenvolvimento de uma interface antes do início da disciplina de IHC. Entretanto, essa interface ainda não está formalmente detalhada no documento atual do TCC1, que concentra seu escopo na implementação e avaliação do algoritmo e do ambiente experimental.

**Fonte:** declaração da equipe e documento TCC1.

> Esta resposta serve para separar o compromisso do TCC do projeto da disciplina. Mesmo quando a opção for **não**, a equipe irá definir uma interface para exercitar IHC.

---

# 1. Entendendo a contribuição do projeto

## 1.1 Explique o TCC em uma frase, sem citar linguagem de programação, framework ou banco de dados.

Desenvolver e avaliar uma estratégia de controle semafórico capaz de adaptar a escolha e a duração das fases de acordo com as condições observadas do tráfego.

## 1.2 Qual situação, atividade ou problema do mundo real motivou o TCC?

**[F]** Sistemas semafóricos de tempo fixo não se adaptam às variações instantâneas da demanda de tráfego, podendo aumentar filas e tempos de espera e reduzir a eficiência da interseção.

**Fonte:** TCC1 — Introdução.

## 1.3 Qual é a **capacidade/contribuição central** produzida pelo TCC?

> “Nosso TCC produz, melhora, analisa ou permite `{{capacidade}}`.”

Nosso TCC permite **selecionar dinamicamente quais movimentos devem receber prioridade e controlar a permanência ou troca das fases verdes de acordo com o estado do tráfego**.

## 1.4 O que se espera que esteja diferente **para pessoas, organizações ou processos** se essa contribuição for bem-sucedida?

**[F]** O TCC pretende produzir evidências experimentais que permitam avaliar se a estratégia híbrida apresenta vantagens em relação ao tempo fixo e ao Max Pressure convencional.

**Fonte:** TCC1 — objetivos e metodologia.

**[H]** Em uma possível aplicação futura, resultados positivos poderiam apoiar pesquisadores e profissionais de mobilidade na avaliação de estratégias de controle mais adaptáveis às mudanças do tráfego.

## 1.5 O que é mérito técnico/científico do TCC e o que seria uma possível aplicação prática?

| Mérito/contribuição técnica | Possível aplicação/valor em uso |
|---|---|
| Combinação do Max Pressure com lógica actuated. | Avaliar uma estratégia de controle que considere tanto a prioridade das fases quanto sua duração. |
| Ambiente experimental para comparar estratégias de controle. | Permitir que pesquisadores e analistas testem diferentes métodos em cenários simulados. |
| Avaliação quantitativa por métricas de tráfego. | Apoiar a comparação do desempenho dos métodos em diferentes condições. |

---

# 2. Entendendo as pessoas envolvidas

## 2.1 Quem interage diretamente com o produto, se já existe interface prevista?

**[H] H01 —** O perfil inicialmente considerado como usuário direto é o **pesquisador ou analista de mobilidade urbana** que precisa configurar, executar e analisar experimentos de controle semafórico.

Esse perfil ainda deverá ser investigado nas próximas entregas.

## 2.2 Quem poderia **usar, configurar, administrar, operar, interpretar ou tomar decisões** a partir da contribuição técnica?

| Perfil | Relação com a contribuição | O que faria | Status/evidência |
|---|---|---|---|
| Pesquisador de mobilidade/tráfego | Utilizaria o ambiente para realizar estudos experimentais. | Configuraria cenários, executaria simulações e analisaria resultados. | H — H01 |
| Analista/engenheiro de tráfego | Poderia avaliar o comportamento de estratégias semafóricas. | Interpretaria métricas e compararia cenários. | H |
| Gestor de mobilidade | Poderia utilizar resultados consolidados de estudos. | Consultaria resultados para apoiar avaliações e decisões. | H |
| Equipe técnica/desenvolvedor | Desenvolve e mantém o ambiente experimental. | Configura componentes técnicos, algoritmos e experimentos. | F — desenvolvimento do TCC |

## 2.3 Existem pessoas afetadas que não usariam a interface diretamente?

| Stakeholder | Como é afetado | Usa interface? | Status/evidência |
|---|---|---|---|
| Motoristas | Poderiam ser beneficiados futuramente por um controle de tráfego mais eficiente. | não | H |
| Passageiros do transporte viário | Poderiam ser afetados por mudanças no fluxo e nos tempos de espera. | não | H |
| Órgãos responsáveis pelo trânsito | Poderiam utilizar estudos e resultados para avaliar estratégias. | possivelmente | H |
| Orientador e avaliadores acadêmicos | Avaliam metodologia, desenvolvimento e resultados do TCC. | não necessariamente | F — contexto acadêmico |

## 2.4 Que características desses perfis podem influenciar a interação?

**[H]** O usuário prioritário provavelmente possui conhecimento sobre tráfego, simulação ou análise de dados, mas não necessariamente conhece a implementação interna do algoritmo.

**[H]** Métricas, gráficos, parâmetros e comparação de cenários provavelmente fazem parte do vocabulário ou das atividades desse perfil.

**[?]** Ainda não sabemos qual é o nível de experiência desses usuários com ferramentas de simulação, quais termos são mais familiares ou quais necessidades específicas de acessibilidade precisam ser consideradas.

---

# 3. Entendendo objetivos e atividades

## 3.1 O que o usuário está tentando conseguir no mundo real?

**[H]** O usuário busca **avaliar como diferentes estratégias de controle semafórico se comportam em determinados cenários de tráfego e comparar seus resultados para apoiar uma análise técnica**.

## 3.2 Quais são as atividades mais importantes?

| ID | Atividade/objetivo | Quem realiza | Frequência/criticidade inicial | Status/evidência |
|---|---|---|---|---|
| A01 | Definir a malha e o cenário de tráfego a ser analisado. | Pesquisador/analista | recorrente / alta | H |
| A02 | Definir parâmetros e estratégia de controle do experimento. | Pesquisador/analista | recorrente / alta | H |
| A03 | Executar a simulação e acompanhar seu estado. | Pesquisador/analista | recorrente / média | H |
| A04 | Interpretar e comparar os resultados dos experimentos. | Pesquisador/analista | recorrente / alta | H |

## 3.3 Qual atividade parece mais frequente? Por quê?

**[H]** Configurar e executar experimentos tende a ser uma atividade recorrente, pois a metodologia do TCC prevê diferentes cenários, demandas e métodos de controle.

Essa frequência deverá ser confirmada com usuários ou especialistas.

## 3.4 Qual parece mais crítica? Que consequência existe se for mal executada?

**[H]** A configuração do experimento e a interpretação dos resultados parecem ser as atividades mais críticas.

Uma configuração inadequada pode prejudicar a comparabilidade entre experimentos, enquanto uma interpretação incorreta das métricas pode gerar conclusões equivocadas sobre o desempenho dos métodos.

---

# 4. Entendendo o problema ou processo atual

## 4.1 Como essas atividades são realizadas hoje, antes da interface imaginada na disciplina?

**[F]** No ambiente experimental descrito no TCC1, a rede viária, os veículos, os detectores e os semáforos são representados no simulador. O controlador externo processa as informações do tráfego e envia as decisões de controle durante a execução.

Os experimentos dependem da configuração dos cenários e parâmetros técnicos, e os resultados são obtidos a partir das saídas da simulação e dos registros produzidos pelo controlador.

**Fonte:** TCC1 — Metodologia.

## 4.2 O que é difícil, demorado, confuso, repetitivo, arriscado ou pouco transparente?

**[H] H02 —** A manipulação direta das configurações técnicas, parâmetros e resultados do ambiente experimental pode dificultar a realização dos experimentos por usuários que não participaram do desenvolvimento.

**[?]** Ainda não sabemos quais etapas específicas são consideradas mais difíceis, demoradas ou confusas por pesquisadores ou analistas externos à equipe.

## 4.3 Que informações o profissional precisa interpretar para tomar decisão?

**[F]** O protocolo experimental do TCC utiliza informações como:

- cenário e demanda utilizados;
- estratégia de controle executada;
- tempo médio de espera;
- tamanho médio das filas;
- throughput;
- número de trocas de fase.

**Fonte:** TCC1 — Estratégia de validação e Métricas de avaliação.

## 4.4 O que acontece quando a atividade falha ou quando o resultado é interpretado incorretamente?

**[H]** Uma configuração incorreta pode comprometer a comparação entre experimentos.

**[H]** Uma interpretação inadequada dos resultados pode levar a conclusões equivocadas sobre qual estratégia apresentou melhor desempenho nas condições analisadas.

Como o trabalho atual é realizado em simulação, esses erros não alteram diretamente semáforos reais, mas podem comprometer a validade da análise experimental.

## 4.5 Conte uma situação concreta.

**[H]** Um pesquisador deseja comparar diferentes estratégias de controle semafórico em uma interseção com demanda desbalanceada. Para isso, precisa definir o cenário e os parâmetros do experimento, executar cada estratégia sob condições equivalentes e posteriormente comparar métricas como filas, tempo de espera e throughput. Caso alguma configuração seja diferente entre as execuções ou os resultados sejam interpretados de maneira inadequada, a comparação pode não representar corretamente o comportamento dos métodos avaliados.

## 4.6 Que evidência existe hoje?

| Evidência/fonte | O que sustenta | Limitação |
|---|---|---|
| TCC1 — Introdução | Problema relacionado à rigidez do controle de tempo fixo. | Fundamenta o problema técnico, não a experiência de usuários. |
| TCC1 — Metodologia | Estrutura do ambiente experimental e processo de simulação. | Não avalia dificuldades de uso da interface. |
| TCC1 — Estratégia de validação | Necessidade de comparar métodos sob condições equivalentes. | Não define como o usuário prefere realizar a comparação. |
| Orientação do professor em aula | Possibilidade de organizar a interação em entrada, configuração/processamento e saída. | É uma direção inicial de projeto, não evidência de necessidade do usuário. |

---

# 5. Entendendo o contexto de uso

## 5.1 Onde e em quais situações a interação poderia ocorrer?

**[H]** A interação poderá ocorrer em ambientes acadêmicos, laboratoriais ou profissionais durante estudos e experimentos relacionados ao controle de tráfego.

## 5.2 Em quais dispositivos/equipamentos?

**[H]** A utilização provavelmente ocorrerá principalmente em computadores desktop ou notebooks, considerando a necessidade de trabalhar com mapas, parâmetros, gráficos e resultados.

**[?]** Essa escolha ainda deverá ser validada com o público priorizado.

## 5.3 Existem condições físicas relevantes?

**[?]** Até o momento não foram identificadas condições físicas específicas, como iluminação, ruído ou mobilidade, que sejam determinantes para a interação.

**[H]** A quantidade de informações apresentadas simultaneamente e o espaço disponível em tela podem influenciar a realização das tarefas.

## 5.4 Existem fatores sociais ou organizacionais?

**[F]** No contexto atual do TCC, o projeto é desenvolvido em equipe e acompanhado por um orientador.

**[H]** Em um contexto profissional, diferentes pessoas podem participar da configuração dos experimentos, análise dos resultados e tomada de decisão.

**[?]** Ainda não sabemos se serão necessárias permissões, aprovações ou diferentes níveis de acesso.

## 5.5 Existe necessidade de histórico, rastreabilidade ou auditoria?

**[?]** Ainda não sabemos se um histórico de execuções será uma necessidade prioritária do usuário.

A metodologia do TCC exige experimentos reproduzíveis, portanto registrar cenário, método e parâmetros utilizados pode ser relevante, mas a forma de interação deverá ser investigada antes de ser considerada requisito.

## 5.6 Um erro pode produzir consequência relevante? Qual?

**[H]** Sim. Erros na configuração ou interpretação podem comprometer a validade de um experimento ou gerar conclusões incorretas.

No escopo atual, a consequência é experimental e acadêmica, pois o sistema não controla diretamente uma interseção real.

---

# 6. Entendendo mercado e alternativas existentes

> Nesta entrega faça apenas um **levantamento inicial**. A análise aprofundada ocorre na Entrega 2.

## 6.1 Como pessoas resolvem problemas semelhantes hoje?

| Alternativa atual | Quem usa | Para quê | Status/evidência |
|---|---|---|---|
| SUMO | Pesquisadores e desenvolvedores | Modelar redes, veículos, semáforos e executar simulações de tráfego. | F — utilizado no TCC1 |
| Scripts/controladores externos integrados ao simulador | Pesquisadores e desenvolvedores | Implementar e testar estratégias personalizadas de controle. | F — abordagem adotada no TCC1 |
| CityFlow | Pesquisadores | Executar simulações de tráfego, especialmente em cenários de maior escala. | F — citado no TCC1 como alternativa |
| Outras ferramentas profissionais de simulação/análise | Pesquisadores e profissionais de mobilidade | Configurar, executar ou analisar estudos de tráfego. | ? — investigar na Entrega 2 |

## 6.2 Existem produtos que atuam na mesma área, mesmo sem serem equivalentes ao TCC?

**[F]** SUMO e CityFlow são ferramentas relacionadas à simulação de tráfego e aparecem no levantamento realizado no TCC1.

**[?]** Ainda é necessário investigar produtos e interfaces profissionais que atendam atividades próximas às definidas para o projeto de IHC.

## 6.3 Quais interfaces profissionais esse público já conhece?

**[?]** Ainda não sabemos quais interfaces e ferramentas são mais familiares ao público priorizado.

Esse ponto será investigado principalmente na **Entrega 2 — Público-alvo e análise de concorrência** e na **Entrega 3 — Personas, empatia, contexto e jornada**.

## 6.4 O que essas soluções parecem fazer bem?

**[?]** Ainda não foi realizada uma análise sistemática das interfaces existentes suficiente para afirmar seus principais pontos positivos.

Esse levantamento será aprofundado na Entrega 2.

## 6.5 O que parecem fazer mal, dificultar ou não atender?

**[?]** Ainda não existe evidência suficiente para afirmar quais problemas de interação estão presentes nas soluções existentes.

Esse levantamento será aprofundado na Entrega 2.

## 6.6 Que padrões de interface ou vocabulário parecem familiares a esse público?

**[?]** Ainda não há evidência suficiente para afirmar quais padrões de interface e termos são mais familiares ao público escolhido.

A análise de concorrentes e o contato com usuários deverão fornecer evidências para essa decisão.

---

# 7. Derivando o escopo de IHC da disciplina

## 7.1 Escolha o caminho do projeto

### Caminho A — TCC já possui interface

**Caminho adotado, com ressalva.**

**[F]** A equipe já havia planejado uma interface antes da disciplina de IHC, porém ela ainda não está formalmente detalhada no documento atual do TCC1.

Para a disciplina, será aprofundado um fluxo de interação relacionado ao ambiente de simulação, organizado inicialmente em três momentos:

1. **Entrada:** definição ou seleção da malha viária;
2. **Configuração e processamento:** definição dos parâmetros e execução da simulação;
3. **Saída:** visualização e comparação dos resultados.

Essa divisão foi discutida com o professor como uma forma inicial de representar onde, como e com quais resultados o usuário interage com a contribuição do TCC.

Ela ainda deverá ser validada e refinada ao longo das próximas entregas.

### Caminho B — TCC não possui interface prevista

**NÃO SE APLICA AO CAMINHO ADOTADO.**

A equipe já possuía uma proposta inicial de interface antes do início da disciplina.

## 7.2 Qual perfil será priorizado no projeto de IHC?

**[H] H01 — Pesquisador ou analista de mobilidade urbana.**

**Por que esse perfil foi escolhido?**  
Esse perfil possui relação plausível com as atividades centrais do projeto: definir condições experimentais, executar simulações e interpretar métricas de desempenho. Além disso, é coerente com o caráter experimental do TCC.

A adequação desse perfil ainda deverá ser investigada.

## 7.3 Qual objetivo desse usuário será priorizado?

**[H]** Avaliar o comportamento de diferentes estratégias de controle semafórico em cenários definidos, configurando experimentos e comparando seus resultados.

## 7.4 Que interface será explorada na disciplina?

> **Para fins da disciplina de IHC, será projetada uma interface que permita a `{{perfil}}` utilizar `{{capacidade/resultado do TCC}}` para `{{objetivo}}`, no contexto de `{{situação}}`.**

**Para fins da disciplina de IHC, será projetada uma interface que permita a um pesquisador ou analista de mobilidade utilizar o ambiente experimental e as estratégias de controle estudadas no TCC para configurar, executar e comparar simulações de controle semafórico em diferentes cenários de tráfego.**

O recorte inicial considera o seguinte fluxo:

**definir onde simular → configurar como simular → executar → interpretar os resultados.**

## 7.5 Qual é a relação dessa interface com o TCC?

- [ ] Já fazia parte do TCC de forma completamente definida.
- [x] É um aprofundamento de algo parcialmente previsto.
- [ ] É uma extensão conceitual criada para a disciplina.
- [ ] É um protótipo demonstrativo de aplicação potencial.
- [ ] Outra.

**Justificativa:** A intenção de desenvolver uma interface já existia antes da disciplina, porém seu usuário, tarefas, fluxo e requisitos de interação ainda não estavam formalmente definidos. A disciplina de IHC será utilizada para investigar e estruturar esses aspectos.

> **Declaração:** a interface desenvolvida nesta disciplina é um artefato de aprendizagem de IHC baseado no tema do TCC. Sua inclusão ou implementação no TCC somente ocorrerá se isso for posteriormente decidido pela equipe e pelo orientador.

---

# 8. Levantando possibilidades de interação — sem desenhar ainda

A equipe pode registrar possibilidades para investigação. **Não significa que todas serão implementadas.**

Marque apenas as que parecem plausíveis e explique o objetivo correspondente.

| Possibilidade | Pode fazer sentido? | Objetivo/tarefa que justificaria | Evidência atual |
|---|---|---|---|
| Dashboard/visão geral | sim, como hipótese inicial | Interpretar as principais métricas após a execução. | H03 — formato ainda precisa ser validado |
| Configuração/parametrização | sim | Definir as condições utilizadas no experimento. | F — os experimentos possuem parâmetros; interação ainda será definida |
| Entrada/upload/seleção de dados | sim | Definir a malha ou cenário utilizado na simulação. | H02 — recorte inicial discutido em aula |
| Acompanhamento de processamento | talvez | Saber se a simulação está em execução, concluída ou apresentou falha. | H |
| Relatório/resultados | sim, como hipótese inicial | Interpretar e comunicar os resultados do experimento. | H03 — métricas existem; formato ainda será validado |
| Histórico com busca/filtros | talvez | Recuperar experimentos anteriores e reproduzir comparações. | ? |
| Comparação de resultados | sim | Comparar o desempenho dos métodos sob condições equivalentes. | F — faz parte da metodologia do TCC |
| Explicabilidade/detalhamento | talvez | Investigar detalhes de uma execução ou resultado. | ? |
| Administração/configurações globais | não inicialmente | Não foi identificada uma atividade prioritária que justifique essa função. | ? |
| Usuários/perfis/permissões | não inicialmente | Não foi identificada necessidade de diferentes níveis de acesso. | ? |
| CRUD de entidade do domínio | não inicialmente | Nenhuma tarefa atual justifica a criação de um CRUD. | ? |
| Auditoria/logs | talvez | Investigar falhas ou reproduzir experimentos. | ? |
| Alertas/ocorrências | talvez | Informar problemas na configuração ou execução. | H |
| Ajuda/documentação | talvez | Auxiliar na compreensão de parâmetros e métricas. | H |

> **Atenção:** “login + dashboard + CRUD” não é uma solução universal. Cada padrão deve surgir de uma tarefa real.

---

# 9. Benefícios e ações iniciais

## 9.1 Qual benefício concreto o projeto de IHC pretende oferecer?

| Benefício esperado | Problema/necessidade | Usuário | Status/evidência |
|---|---|---|---|
| Facilitar a configuração dos experimentos. | Necessidade de definir corretamente cenário, parâmetros e método. | Pesquisador/analista | H — H02 |
| Facilitar a interpretação dos resultados. | Diferentes métricas precisam ser analisadas após cada execução. | Pesquisador/analista | H — H03 |
| Facilitar a comparação entre estratégias. | O TCC compara métodos sob condições equivalentes. | Pesquisador/analista | F/H |
| Reduzir a necessidade de interação direta com detalhes técnicos internos. | O ambiente experimental possui diferentes configurações e componentes técnicos. | Pesquisador/analista | H — H02 |

## 9.2 Que ações o usuário deverá conseguir realizar?

| ID | O usuário precisa conseguir... | Para alcançar... | Prioridade inicial |
|---|---|---|---|
| T01 | Definir ou selecionar a malha viária. | Estabelecer onde o experimento será realizado. | alta |
| T02 | Configurar parâmetros do experimento. | Definir as condições da simulação. | alta |
| T03 | Selecionar a estratégia de controle. | Determinar qual método será avaliado. | alta |
| T04 | Iniciar uma simulação. | Executar o experimento configurado. | alta |
| T05 | Verificar o estado da execução. | Saber se o experimento está em andamento, concluído ou apresentou problema. | média |
| T06 | Consultar as métricas obtidas. | Compreender o desempenho da execução. | alta |
| T07 | Comparar resultados. | Avaliar diferenças entre métodos ou cenários. | alta |
| T08 | Consultar ou gerar uma síntese dos resultados. | Registrar e comunicar os resultados do experimento. | média |

## 9.3 Tecnologias/restrições já definidas no TCC

A tecnologia aparece **agora**, depois do entendimento do uso.

| Tecnologia/restrição | Por que existe | Possível impacto na interação |
|---|---|---|
| SUMO | Representa a rede viária, os veículos, os detectores e os semáforos no ambiente de simulação. | A interface poderá abstrair parte da configuração técnica necessária para executar os experimentos. |
| Python | Implementa o controlador externo responsável pela lógica dos métodos avaliados. | A implementação poderá permanecer em segundo plano, expondo ao usuário apenas informações relevantes para sua tarefa. |
| TraCI | Realiza a comunicação entre o controlador externo e o SUMO. | Essa comunicação poderá ser transparente para o usuário. |
| Detectores virtuais E1 | Registram informações utilizadas para estimar o estado do tráfego. | Os dados técnicos deverão ser transformados em informações compreensíveis para análise. |
| Ambiente de simulação | O TCC está concentrado em desenvolvimento e validação experimental, não em implantação física. | A interface será voltada a experimentos simulados e não ao controle direto de semáforos reais. |
| Três estratégias de controle | Tempo fixo, Max Pressure e Max Pressure + actuated são comparados no TCC. | O usuário deverá conseguir identificar claramente qual estratégia foi utilizada em cada experimento. |
| Diferentes condições de demanda | O TCC pretende avaliar os controladores em diferentes cenários de tráfego. | A configuração do experimento precisa deixar claro quais condições estão sendo utilizadas. |
| Métricas de desempenho | Tempo médio de espera, fila média, throughput e trocas de fase são utilizadas na avaliação. | Os resultados devem ser apresentados de forma que permita interpretação e comparação. |

---

# 10. Hipóteses e dúvidas prioritárias

| ID | Hipótese/dúvida | Por que importa | Como poderá ser investigada |
|---|---|---|---|
| H01 | Pesquisadores ou analistas de mobilidade representam adequadamente o usuário prioritário da interface. | O perfil escolhido influencia tarefas, linguagem, contexto, personas e decisões de interação. | Entregas 2, 3 e 7 |
| H02 | Organizar a interação em definição da malha, configuração/execução e análise dos resultados facilita a realização dos experimentos em relação à interação direta com as ferramentas técnicas. | Esse fluxo é a base inicial do recorte de IHC e precisa ser validado. | Entregas 3, 5, 6 e 7 |
| H03 | Uma apresentação comparativa das métricas por meio de dashboard ou relatório facilita a interpretação do desempenho dos métodos. | A forma de apresentar os resultados influencia a comparação e compreensão dos experimentos. | Entregas 2, 6, 7 e 12–14 |

As hipóteses H01, H02 e H03 estão registradas em [`../RASTREABILIDADE.md`](../RASTREABILIDADE.md) e deverão ser atualizadas ao longo do semestre conforme novas evidências forem obtidas.

---

# 11. Síntese da equipe

| Pergunta | Síntese atual |
|---|---|
| Qual é a contribuição central do TCC? | Desenvolver e avaliar um controlador semafórico híbrido que combina Max Pressure para priorização das fases e lógica actuated para controle da permanência ou troca do verde. |
| O TCC já previa interface? | Parcialmente. A equipe já planejava uma interface antes da disciplina, mas ela ainda não está formalmente detalhada no TCC1. |
| Quem é o usuário prioritário de IHC? | [H] H01 — pesquisador ou analista de mobilidade urbana. |
| O que ele precisa alcançar? | Avaliar estratégias de controle semafórico por meio da configuração, execução e comparação de experimentos. |
| Qual problema/atividade será estudado? | O processo de definição, configuração, execução e análise de experimentos de controle semafórico. |
| Como isso acontece hoje? | Por meio do ambiente técnico de simulação, de suas configurações e dos registros e métricas produzidos durante os experimentos. |
| Qual é o contexto de uso? | [H] Ambiente computacional acadêmico, laboratorial ou profissional voltado à experimentação de estratégias de tráfego. |
| Que interface/recorte será explorado? | Definição da malha viária → configuração e execução da simulação → análise e comparação dos resultados. |
| Como a interface se relaciona ao TCC? | É um aprofundamento de uma interface já considerada pela equipe, utilizando como base o ambiente experimental e os resultados produzidos pelo TCC. |
| Quais pontos ainda são hipóteses? | H01 — usuário prioritário; H02 — adequação do fluxo de interação; H03 — adequação do dashboard/relatório para comparação dos resultados. |

### Delimitação

**Dentro do escopo de IHC:** investigar e projetar a interação necessária para definir a malha, configurar a simulação, selecionar estratégias de controle, executar experimentos e interpretar/comparar seus resultados.

**Fora do escopo de IHC:** desenvolvimento matemático do Max Pressure, implementação interna da lógica actuated, programação do controlador, funcionamento interno do TraCI, construção de sensores físicos e implantação do controlador em uma interseção real.

**Dentro do escopo formal do TCC:** desenvolvimento e avaliação do algoritmo híbrido Max Pressure + actuated, ambiente de simulação, integração entre controlador e simulador, obtenção dos dados de tráfego, cenários experimentais, comparação entre estratégias e análise dos resultados.

**Interface da disciplina será implementada no TCC?** **não definido** — a equipe já planejava desenvolver uma interface antes da disciplina, porém seu escopo final de implementação ainda deve permanecer separado das atividades de IHC e depende das decisões da equipe e do orientador.

---

# 12. Como esta entrega alimenta as próximas

- **Entrega 2:** verifica mercado, concorrentes e interfaces profissionais representativas.
- **Entrega 3:** detalha perfis e contexto.
- **Entrega 4:** aprofunda situações problemáticas.
- **Entrega 5:** modela tarefas centrais.
- **Entrega 6:** experimenta alternativas em baixa fidelidade.
- **Entrega 7:** investiga hipóteses com dados.
- **Entrega 8:** define restrições e metas de usabilidade.
- **Entregas 9–11:** transformam o recorte em modelo de interação e protótipo.
- **Entregas 12–14:** avaliam a interface construída na disciplina.

A Entrega 1 é uma **fotografia inicial do conhecimento**. Ela pode e deve ser revisada quando surgirem evidências.

---

# 13. Relação com INOVA e comunicação do projeto

Prepare uma explicação de até três frases:

1. **Problema/atividade humana:** Pesquisadores e analistas de mobilidade precisam avaliar como diferentes estratégias de controle semafórico se comportam em diferentes condições de tráfego.
2. **Contribuição técnica do TCC:** O TCC desenvolve e avalia um algoritmo híbrido que combina Max Pressure e lógica actuated para adaptar a escolha e a duração das fases semafóricas ao estado do tráfego.
3. **Como uma pessoa poderia utilizar essa contribuição:** Uma pessoa poderia definir o cenário e os parâmetros da simulação, executar diferentes estratégias de controle e comparar os resultados produzidos.

Essa síntese ajuda a apresentar o projeto para público não especializado sem reduzir seu mérito técnico.

---

# Checklist de qualidade

- [x] Está clara a diferença entre tema do TCC, escopo formal do TCC e escopo de IHC.
- [x] A equipe declarou se o TCC já previa interface.
- [x] Se não previa, foi derivado um usuário plausível e um objetivo de uso. *(Não se aplica diretamente, pois havia planejamento prévio de interface; o usuário prioritário foi registrado como hipótese.)*
- [x] A interface de IHC não foi apresentada como obrigação automática do TCC.
- [x] A contribuição do TCC foi descrita sem começar por tecnologias de implementação.
- [x] Usuários diretos e stakeholders foram diferenciados.
- [x] Foram considerados profissionais que configuram, administram, interpretam ou decidem, quando pertinente.
- [x] Objetivo do usuário não foi confundido com objetivo do projeto.
- [x] Processo/problema atual foi descrito antes da solução.
- [x] Existe situação concreta de uso/problema.
- [x] Contexto físico, social/organizacional, dispositivos e consequências de erro foram considerados.
- [x] Mercado/alternativas existentes foram levantados inicialmente.
- [x] Possibilidades como dashboard, relatório, histórico, filtros e CRUD foram tratadas como hipóteses de solução, não como requisitos automáticos.
- [x] Cada possibilidade de interface tem um objetivo/tarefa que poderia justificá-la.
- [x] Afirmações relevantes estão marcadas `[F]`, `[H]` ou `[?]`.
- [x] Hipóteses prioritárias receberam IDs e foram para a rastreabilidade.
- [x] O recorte de IHC é viável para modelar, prototipar e avaliar no semestre.
- [x] A equipe consegue explicar problema humano → contribuição computacional → forma de uso.

---

# Referências utilizadas nesta entrega

- LIRA, Gabriel Koiama de Rocha; VILLAS BÔAS, João Pedro Lopes Santana. **Algoritmo Híbrido de Controle Semafórico Baseado em Max Pressure e Lógica Actuated em Ambiente de Simulação**. Trabalho de Conclusão de Curso, Centro Universitário FEI, 2026.
- [Guia de uso, formatação e apresentação](../GUIA_DE_USO.md).
- [Guia para definir o escopo de IHC a partir do tema do TCC](../GUIA_ESCOPO_IHC.md).
- [Matriz de rastreabilidade de IHC](../RASTREABILIDADE.md).
- Orientações e discussão realizadas com o professor durante a disciplina de Interação Humano-Computador.

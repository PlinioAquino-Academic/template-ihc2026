# Entrega 4 — Cenários de análise/problema

**Data:** 16/09/2026  
**Status:** 🟩 Concluído  
**Responsabilidade:** 1 solução completa por integrante

## Objetivo da atividade

Descrever situações atuais em que o usuário tenta alcançar um objetivo e encontra dificuldades. O cenário de análise/problema deve tornar visível **o contexto, os atores, as ações e as rupturas**, sem antecipar a interface que será projetada.

> **Regra central:** cenário de problema é a “história do problema”. Se o texto já diz “o sistema mostra”, “o aplicativo resolve” ou descreve botões/telas futuras, provavelmente está misturando problema com solução.

Sempre que possível, o cenário deve aprofundar uma **situação concreta já registrada na Entrega 1**.

### Quando o TCC não possuía interface

O cenário continua sendo uma história de **problema/atividade humana**, não uma história do futuro sistema. Descreva como o profissional realiza hoje uma atividade semelhante ou como lida atualmente com dados, resultados, configurações, logs, decisões e limitações que o tema do TCC pretende apoiar.

Exemplo: em vez de “o DBA abre o novo dashboard e executa o algoritmo”, descreva “o DBA precisa investigar uma consulta lenta, reúne informações em ferramentas distintas, compara planos manualmente e tem dificuldade para estimar o impacto de uma mudança”.

A interface da disciplina aparecerá somente depois, nos cenários de interação.

Se o integrante escolher um novo problema/situação, explique por que ele passou a ser relevante e indique a evidência que motivou sua inclusão.

---

## Cenário C01 — Preparação e execução de experimentos sob condições comparáveis

**Autor(a):** Gabriel Koiama de Rocha Lira — 22.125.067-3  
**Persona(s) relacionada(s):** P01 — Marina Ribeiro  
**Necessidade relacionada:** R02 — definir corretamente as condições da simulação antes da execução; relacionada também a R01, R03 e R04  
**Situação concreta da Entrega 1 relacionada:** Entrega 1 — Seção 4.5, situação em que um pesquisador precisa comparar diferentes estratégias de controle semafórico em uma interseção com demanda desbalanceada  
**Hipóteses ainda presentes:** H01, H02

### 1. Cenário inicial

Marina Ribeiro é pesquisadora e analista de mobilidade e está realizando um estudo experimental para comparar o comportamento de diferentes estratégias de controle semafórico em uma interseção com demanda desbalanceada. Seu objetivo é executar o controle de tempo fixo, o Max Pressure convencional e o método híbrido Max Pressure + actuated em condições suficientemente equivalentes para que os resultados obtidos posteriormente possam ser comparados de forma válida.

Antes de iniciar cada experimento, Marina precisa definir ou conferir o cenário de tráfego, as condições de demanda e os parâmetros relevantes da simulação. Em seguida, precisa selecionar a estratégia de controle correspondente àquela execução. Como as estratégias são avaliadas separadamente, ela repete esse processo para cada método que deseja estudar, procurando alterar apenas aquilo que faz parte da comparação e preservar as demais condições experimentais.

Atualmente, essa atividade depende da manipulação das configurações técnicas do ambiente experimental e da conferência das informações utilizadas em cada execução. Marina precisa acompanhar quais condições foram utilizadas, qual estratégia está sendo executada e se a simulação foi concluída de forma adequada.

Esse processo exige atenção porque uma alteração não percebida em uma condição que deveria permanecer equivalente pode comprometer a comparação. Também existe o risco de Marina perceber uma configuração inadequada somente depois de executar a simulação, o que pode exigir que o experimento seja realizado novamente.

Como o estudo envolve diferentes estratégias e pode envolver várias execuções, a dificuldade não está apenas em iniciar uma simulação. Marina precisa garantir que cada execução realmente corresponda à condição experimental planejada e que seja possível reconhecer posteriormente em quais condições cada resultado foi produzido. Caso isso não aconteça, a comparação entre os métodos pode deixar de representar corretamente o comportamento das estratégias avaliadas.

### 2. Questões de refinamento

| # | Questão | Por que precisa ser respondida | Fonte/forma de obter resposta |
|---|---|---|---|
| Q1 | **Exploratória — Por que?** Por que as condições comuns do experimento precisam permanecer equivalentes entre as diferentes estratégias? | Esclarecer a consequência científica de alterar mais de uma condição ao mesmo tempo e justificar por que a comparabilidade é central para o cenário. | TCC1 — estratégia de validação; Entrega 1 — Seções 4.4 e 4.5. |
| Q2 | **Exploratória — O que é?** Quais informações caracterizam uma condição experimental e precisam ser conhecidas por Marina antes de considerar duas execuções comparáveis? | Identificar os dados que fazem parte da atividade e que precisam ser considerados durante a preparação dos experimentos. | TCC1 — metodologia e protocolo experimental; Entrega 1 — Seções 4.1 e 4.3. |
| Q3 | **Exploratória — Como?** Como Marina verifica atualmente se o cenário, a demanda e os parâmetros relevantes correspondem às condições que pretendia utilizar? | O cenário inicial afirma que a configuração precisa ser conferida, mas ainda não detalha como essa verificação é realizada na prática. | Observação do processo utilizado pela própria equipe no ambiente experimental e consulta à documentação técnica do experimento. |
| Q4 | **Exploratória — Como?** Como Marina identifica qual estratégia está associada a uma determinada execução e aos resultados produzidos por ela? | Revelar como é mantida a relação entre configuração, execução e resultado, necessária para a análise posterior. | TCC1 — metodologia; Entrega 1 — Seções 4.1 e 4.3; observação do processo experimental da equipe. |
| Q5 | **Exploratória — Como?** Como Marina determina se uma execução terminou de maneira adequada ou apresentou algum problema que comprometa seu uso posterior? | O cenário inicial menciona acompanhamento da execução, mas ainda não explica quais informações são usadas para avaliar seu término. | Observação do ambiente experimental, registros produzidos pela simulação e consulta à equipe técnica. |
| Q6 | **Exploratória — Por que?** O que acontece quando uma diferença de configuração é descoberta somente depois da conclusão de uma execução? | Aprofundar as consequências da ruptura e compreender o impacto de erros tardios sobre tempo, retrabalho e validade experimental. | Entrega 1 — Seção 4.4; experiência da equipe durante a realização dos experimentos. |
| Q7 | **Exploratória — O que é?** Quais informações de uma execução precisam permanecer disponíveis para que Marina consiga posteriormente reconhecer em quais condições o resultado foi produzido? | Determinar quais informações são necessárias para preservar a rastreabilidade experimental sem ainda definir como elas serão apresentadas em uma futura interface. | TCC1 — estratégia de validação e métricas; Entrega 1 — Seções 4.3 e 5.5. |
| Q8 | **Verificação** Uma execução pode ser considerada adequada para comparação quando Marina não consegue confirmar as condições em que ela foi realizada? | Verificar se a rastreabilidade das condições é realmente parte necessária do objetivo da atividade. | Discussão com a equipe, orientador e posteriormente com usuários ou especialistas do perfil representado por P01. |

### 3. Cenário refinado

Marina Ribeiro é pesquisadora e analista de mobilidade e está realizando um estudo experimental para comparar o comportamento do controle de tempo fixo, do Max Pressure convencional e do método híbrido Max Pressure + actuated em uma interseção com demanda desbalanceada.

Seu objetivo não é apenas executar os três métodos, mas produzir experimentos que possam ser comparados de maneira válida. **[NOVO: Para que essa comparação faça sentido, Marina precisa distinguir aquilo que deve permanecer comum entre as execuções das características que são modificadas propositalmente para avaliar cada estratégia.]**

Antes de cada execução, Marina define ou confere o cenário de tráfego, as condições de demanda e os parâmetros relevantes da simulação. Depois, identifica a estratégia que será utilizada naquela execução. **[NOVO: Essas informações caracterizam a condição experimental e precisam ser conhecidas antes que Marina possa considerar a execução adequada para comparação com as demais.]**

A atividade é repetida para cada estratégia avaliada. Como o ambiente experimental depende de configurações técnicas, Marina precisa conferir as condições utilizadas ao preparar cada execução e acompanhar seu andamento. **[NOVO: Além de reconhecer qual estratégia está sendo executada, ela precisa conseguir relacionar a execução às condições que a originaram e determinar se ela foi concluída de maneira adequada antes de utilizar seus resultados.]**

Durante esse processo podem ocorrer rupturas. Um parâmetro que deveria permanecer equivalente pode ser alterado sem que Marina perceba imediatamente, uma execução pode não corresponder às condições que ela pretendia avaliar ou a relação entre a configuração utilizada e o resultado obtido pode se tornar difícil de reconstruir posteriormente.

**[NOVO: Quando uma inconsistência é identificada somente depois da execução, Marina precisa verificar se aquele resultado ainda pode ser utilizado. Caso a diferença comprometa a equivalência experimental, a execução pode precisar ser descartada e realizada novamente, produzindo retrabalho e atrasando a análise.]**

Esse risco cresce à medida que diferentes estratégias e condições precisam ser avaliadas. Marina precisa lembrar e conferir várias informações para determinar se as execuções são realmente comparáveis. **[NOVO: Por isso, informações suficientes sobre cenário, demanda, parâmetros relevantes, estratégia executada e identificação da execução precisam permanecer associadas ao experimento para que sua origem possa ser reconhecida posteriormente.]**

Caso Marina compare resultados produzidos sob condições que não eram equivalentes, poderá atribuir à estratégia de controle uma diferença que, na realidade, foi causada pela configuração experimental. Nesse caso, o problema não afeta diretamente uma interseção real, pois o trabalho ocorre em simulação, mas pode comprometer a validade do estudo e levar a conclusões inadequadas sobre o comportamento dos métodos avaliados.

### 4. Elementos extraídos

| Elemento | Evidência no cenário |
|---|---|
| Ator(es) | P01 — Marina Ribeiro, pesquisadora/analista de mobilidade responsável por preparar, executar e posteriormente analisar os experimentos. A equipe técnica pode fornecer informações sobre o funcionamento do ambiente quando necessário, mas Marina é a atriz principal do cenário. |
| Objetivo(s) | Executar diferentes estratégias de controle semafórico sob condições comparáveis e produzir resultados cuja origem experimental possa ser reconhecida posteriormente. |
| Contexto | Estudo experimental de controle semafórico realizado em ambiente de simulação, utilizando uma interseção com demanda desbalanceada e comparando tempo fixo, Max Pressure e Max Pressure + actuated. |
| Recursos/informações | Cenário de tráfego, condições de demanda, parâmetros do experimento, estratégia de controle, informações sobre a execução e registros/resultados produzidos pelo ambiente experimental. |
| Ações | Definir ou conferir o cenário; verificar condições e parâmetros; identificar a estratégia; preparar e iniciar a execução; acompanhar seu andamento; verificar se a execução corresponde ao planejado; preservar a relação entre condições, execução e resultado. |
| Problemas/rupturas | Configuração diferente daquela planejada; alteração não percebida de uma condição que deveria permanecer equivalente; dificuldade de confirmar quais condições foram utilizadas; identificação tardia de erros; dificuldade de relacionar uma execução às condições que a produziram. |
| Consequências | Necessidade de repetir experimentos, aumento de retrabalho, atraso na análise, perda da comparabilidade entre execuções e possibilidade de conclusões experimentais inadequadas sobre as estratégias avaliadas. |

### 5. Implicações para as próximas entregas

O cenário indica que as atividades relacionadas à preparação e execução dos experimentos merecem ser aprofundadas na análise de tarefas. Em especial, devem ser analisadas as tarefas T01 — definir ou selecionar a malha viária, T02 — configurar os parâmetros do experimento, T03 — selecionar a estratégia de controle, T04 — iniciar uma simulação e T05 — verificar o estado da execução.

As próximas entregas deverão investigar como essas tarefas são realizadas atualmente, quais decisões o usuário precisa tomar, quais informações precisam estar disponíveis em cada etapa, quais condições precisam ser verificadas antes de uma execução e como o usuário reconhece que um experimento foi concluído corretamente.

Também permanecem questões que ainda precisam de evidência direta, principalmente: quais etapas do processo atual são mais trabalhosas para pesquisadores ou analistas externos à equipe; quais parâmetros eles consideram mais difíceis de compreender ou conferir; como identificam erros durante uma execução; e quais informações consideram indispensáveis para reproduzir ou revisar um experimento.

Essas informações deverão orientar a análise de tarefas e as futuras decisões de interação, mas o cenário atual não define ainda telas, controles, organização visual ou qualquer solução específica para os problemas identificados.

---

## Cenário C02 — Interpretação e comparação de resultados experimentais

**Autor(a):** João Pedro Lopes Santana Villas Bôas — 22.125.065-7  
**Persona(s) relacionada(s):** P02 — Carlos Mendes  
**Necessidade relacionada:** R06 — comparar o comportamento das estratégias sob condições equivalentes; relacionada também a R05 e R07  
**Situação concreta da Entrega 1 relacionada:** Entrega 1 — Seções 4.3, 4.4 e 4.5, referentes à interpretação das métricas, ao risco de conclusões inadequadas e à comparação entre estratégias sob condições equivalentes  
**Hipóteses ainda presentes:** H03

### 1. Cenário inicial

Carlos Mendes é gestor ou coordenador de mobilidade e precisa analisar os resultados de um estudo experimental que compara diferentes estratégias de controle semafórico. Seu objetivo é compreender como o controle de tempo fixo, o Max Pressure convencional e o método híbrido Max Pressure + actuated se comportaram nas condições avaliadas e utilizar essas informações para apoiar uma análise técnica.

Os experimentos produzem diferentes informações sobre o desempenho do tráfego, como tempo médio de espera, tamanho médio das filas, throughput e número de trocas de fase. Carlos também precisa compreender em qual cenário, condição de demanda e estratégia cada resultado foi obtido para que possa interpretar corretamente os valores apresentados.

A análise não depende apenas de observar uma métrica isoladamente. Carlos precisa relacionar os resultados às condições em que foram produzidos e comparar execuções que representem situações equivalentes. Quando existem várias execuções, cenários e métricas, essa atividade pode exigir que ele consulte diferentes informações e mantenha o contexto de cada resultado durante a comparação.

Uma dificuldade surge quando os valores são analisados sem que esteja claro a qual cenário, estratégia ou configuração eles pertencem. Também pode ocorrer de diferentes métricas apontarem aspectos distintos do comportamento do tráfego, exigindo que Carlos interprete o conjunto dos resultados antes de chegar a uma conclusão.

Caso resultados produzidos em condições diferentes sejam comparados como se fossem equivalentes, ou uma métrica seja interpretada sem considerar seu contexto experimental, Carlos pode chegar a uma conclusão inadequada sobre o desempenho das estratégias. Como o estudo atual ocorre em ambiente de simulação, essa consequência não altera diretamente uma interseção real, mas pode comprometer a análise técnica e a comunicação dos resultados do experimento.

### 2. Questões de refinamento

| # | Questão | Por que precisa ser respondida | Fonte/forma de obter resposta |
|---|---|---|---|
| Q1 | **Exploratória — Por que?** Por que Carlos precisa conhecer as condições experimentais associadas aos resultados antes de comparar duas execuções? | Esclarecer a relação entre contexto experimental e validade da comparação, evitando interpretar diferenças causadas por configurações distintas como efeito da estratégia. | TCC1 — estratégia de validação; Entrega 1 — Seções 4.4 e 4.5. |
| Q2 | **Exploratória — O que é?** Quais informações Carlos precisa considerar para compreender o resultado de uma execução? | Identificar quais dados fazem parte da atividade de interpretação e quais informações são necessárias além dos valores das métricas. | TCC1 — metodologia e métricas de avaliação; Entrega 1 — Seção 4.3. |
| Q3 | **Exploratória — Como?** Como Carlos associa atualmente cada conjunto de métricas ao cenário, à estratégia e às condições que produziram aquele resultado? | O cenário inicial estabelece a necessidade de contexto, mas ainda não explica como essa relação é preservada ou recuperada durante a análise. | Observação do processo experimental da equipe, saídas das simulações e registros produzidos pelo controlador. |
| Q4 | **Exploratória — Como?** Como Carlos realiza a comparação quando diferentes métricas apresentam comportamentos distintos entre as estratégias? | Compreender como o usuário constrói uma avaliação a partir de vários indicadores e quais critérios utiliza quando os resultados não apontam todos na mesma direção. | Discussão com a equipe, orientador e futuramente com usuários ou especialistas do perfil representado por P02. |
| Q5 | **Exploratória — O que é?** Quais resultados ou métricas são considerados mais importantes para uma primeira interpretação e quais exigem análise mais detalhada? | Investigar se existe uma hierarquia de informações relevante para o usuário e evitar assumir que todas as métricas possuem a mesma importância em qualquer análise. | TCC1 — métricas de avaliação; consulta a pesquisadores, analistas ou gestores de mobilidade. |
| Q6 | **Exploratória — Como?** Como Carlos identifica se um resultado está incompleto, apresenta alguma condição inesperada ou não deve ser utilizado na comparação? | Aprofundar a etapa de avaliação dos resultados antes que eles sejam utilizados para formar uma conclusão. | Registros das execuções, metodologia experimental e consulta à equipe técnica. |
| Q7 | **Exploratória — Por que?** Quais são as consequências de interpretar incorretamente uma diferença entre duas estratégias? | Tornar explícito o impacto da ruptura sobre a conclusão do estudo e sobre a comunicação dos resultados. | Entrega 1 — Seção 4.4; TCC1 — objetivos e estratégia de validação. |
| Q8 | **Verificação** Carlos consegue produzir uma comparação tecnicamente confiável quando conhece os valores das métricas, mas não consegue confirmar em quais condições cada resultado foi obtido? | Verificar se a associação entre resultado e condição experimental é uma necessidade essencial para a atividade de comparação. | Discussão com a equipe, orientador e posteriormente com usuários ou especialistas do perfil representado por P02. |

### 3. Cenário refinado

Carlos Mendes é gestor ou coordenador de mobilidade e precisa analisar um estudo experimental que compara o controle de tempo fixo, o Max Pressure convencional e o método híbrido Max Pressure + actuated. Seu objetivo é compreender como as estratégias se comportaram nas condições avaliadas e utilizar os resultados para apoiar uma análise técnica.

Os experimentos produzem métricas como tempo médio de espera, tamanho médio das filas, throughput e número de trocas de fase. **[NOVO: Entretanto, os valores dessas métricas somente podem ser interpretados adequadamente quando Carlos também consegue identificar o cenário, a condição de demanda, a estratégia utilizada e as demais condições relevantes associadas à execução.]**

Carlos consulta os resultados de cada experimento e procura identificar diferenças entre as estratégias. **[NOVO: Para que uma comparação seja significativa, ele precisa confirmar se as execuções utilizadas representam condições suficientemente equivalentes e distinguir alterações deliberadas do experimento de diferenças que poderiam comprometer a comparação.]**

A interpretação também exige considerar mais de uma medida de desempenho. **[NOVO: Como as métricas representam aspectos diferentes do comportamento do tráfego, uma estratégia pode apresentar uma diferença relevante em determinada medida sem que isso necessariamente produza a mesma tendência nas demais. Carlos, portanto, precisa interpretar o conjunto das informações antes de formar uma conclusão.]**

Quando existem diversas execuções, cenários e estratégias, aumenta a quantidade de informações que precisa ser relacionada. Carlos precisa reconhecer qual resultado pertence a qual experimento e manter essa relação durante a análise. **[NOVO: Caso essa associação não esteja suficientemente clara, ele pode precisar retornar aos registros das execuções para reconstruir as condições utilizadas antes de continuar a comparação.]**

Outra dificuldade ocorre quando existe dúvida sobre a qualidade de uma execução. **[NOVO: Antes de utilizar determinado resultado, Carlos precisa conseguir avaliar se a execução foi concluída de maneira adequada e se existe alguma condição que impeça sua utilização na comparação.]**

Se resultados obtidos em condições diferentes forem comparados como se fossem equivalentes, Carlos poderá atribuir à estratégia de controle uma diferença causada por outro fator experimental. Da mesma forma, interpretar apenas uma métrica sem considerar as demais pode produzir uma visão incompleta do comportamento observado.

**[NOVO: Uma conclusão incorreta pode comprometer a interpretação técnica do estudo e a forma como seus resultados são comunicados a outras pessoas, mesmo que, no contexto atual do TCC, esses resultados não sejam utilizados para controlar diretamente uma interseção real.]**

Por isso, a atividade de Carlos envolve mais do que consultar valores finais. Ele precisa compreender a origem dos resultados, verificar se eles podem ser comparados, interpretar diferentes indicadores em conjunto e construir uma síntese coerente com as condições em que os experimentos foram realizados.

### 4. Elementos extraídos

| Elemento | Evidência no cenário |
|---|---|
| Ator(es) | P02 — Carlos Mendes, gestor/coordenador de mobilidade interessado principalmente na interpretação, comparação e síntese dos resultados experimentais. Pesquisadores ou equipe técnica podem fornecer informações adicionais quando existe dúvida sobre uma execução. |
| Objetivo(s) | Compreender o desempenho das estratégias de controle, comparar resultados obtidos sob condições equivalentes e construir uma interpretação tecnicamente coerente dos experimentos. |
| Contexto | Análise dos resultados de estudos realizados em ambiente de simulação, envolvendo diferentes cenários, condições de demanda e estratégias de controle semafórico. |
| Recursos/informações | Cenário, demanda, estratégia executada, parâmetros relevantes, identificação da execução, tempo médio de espera, tamanho médio das filas, throughput, número de trocas de fase e demais registros necessários para contextualizar os resultados. |
| Ações | Consultar resultados; identificar o contexto de cada execução; verificar se os experimentos podem ser comparados; interpretar métricas; relacionar diferentes indicadores; investigar resultados duvidosos; comparar estratégias; elaborar uma síntese da análise. |
| Problemas/rupturas | Resultado sem contexto suficiente; dificuldade de relacionar métricas à execução correspondente; comparação de execuções realizadas sob condições distintas; excesso de informações; interpretação isolada de uma métrica; dúvida sobre a validade de uma execução. |
| Consequências | Comparações inadequadas, necessidade de revisar registros e repetir a análise, aumento do esforço para interpretar os experimentos e possibilidade de chegar a conclusões incorretas ou comunicar de forma inadequada o comportamento das estratégias. |

### 5. Implicações para as próximas entregas

O cenário indica que as atividades de consulta, interpretação, comparação e síntese dos resultados devem ser aprofundadas nas próximas análises de tarefas. Em especial, devem ser consideradas T06 — consultar as métricas obtidas, T07 — comparar resultados e T08 — consultar ou gerar uma síntese dos resultados.

A análise de tarefas deverá investigar quais informações Carlos precisa consultar antes de iniciar uma comparação, como verifica se duas execuções são comparáveis, como interpreta várias métricas simultaneamente, como lida com resultados que parecem contraditórios ou incompletos e como transforma a análise realizada em uma conclusão compreensível.

Também permanecem lacunas que ainda precisam ser investigadas diretamente com usuários ou especialistas: quais métricas são priorizadas em diferentes tipos de análise; qual nível de detalhe é necessário para compreender um resultado; quais informações experimentais devem acompanhar obrigatoriamente cada métrica; como usuários experientes lidam com divergências entre indicadores; e quais informações precisam estar presentes para justificar ou comunicar uma conclusão.

Essas questões deverão orientar as próximas etapas de análise e prototipação. Neste momento, o cenário identifica somente as necessidades, decisões e rupturas existentes na atividade, sem definir dashboard, gráficos específicos, organização de telas, filtros, relatórios ou qualquer outra solução de interface.

---

## Checklist

- [x] Há um cenário completo por integrante.
- [x] Cada cenário tem título, ator, objetivo, contexto e problema.
- [x] O cenário possui origem rastreável na Entrega 1 ou justifica claramente a inclusão de uma nova situação.
- [x] O texto descreve a situação atual, sem antecipar a solução.
- [x] Para TCC sem interface original, o cenário descreve uma prática humana plausível relacionada à contribuição técnica, e não “a falta de uma tela”.
- [x] Questões de refinamento acrescentam informação nova.
- [x] O refinamento mostra claramente o que foi adicionado/alterado.
- [x] Cenários são diferentes o suficiente para cobrir objetivos/problemas relevantes.
- [x] Cada cenário está ligado a persona/necessidade na matriz de rastreabilidade.

# Entrega 1 — Conhecendo o projeto, o usuário e o problema

**Data:** 13/08/2026 (versão original)
**Revisão:** 06/10/2026, aplicação do [feedback do professor](../feedbacks_professor/Feedback_Professor_Entrega01_Equipe09.md)
**Status:** 🟦 revisada após feedback
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

| Nome completo                |   Matrícula | GitHub                       |
| ---------------------------- | -----------: | ---------------------------- |
| Kawan Mark Geronimo Da Silva | 22.222.010-5 | https://github.com/KawanMark |
| Gabriel Albertini Pinheiro   | 22.122.094-8 | https://github.com/albertx0  |
| Alexandre Domiciano Pierri   | 22.125.061-6 | https://github.com/Apierri05 |

## 0.2 Título atual do TCC

Detecção de Anomalias em Imagens de Raio-X de Contêineres de Carga

## 0.3 Orientador(a)

Murilo Bouzon

## 0.4 Qual é o resultado principal atualmente previsto no TCC?

Marque e descreva:

- [ ] sistema/aplicação interativa;
- [X] algoritmo;
- [X] modelo de IA/ML/LLM;
- [ ] biblioteca/API/framework;
- [ ] análise de dataset;
- [X] estudo/benchmark/avaliação experimental;
- [ ] infraestrutura/backend;
- [ ] componente embarcado/IoT;
- [ ] outro.

**Descrição:** O TCC desenvolve primariamente um **modelo de IA/ML** baseado em aprendizado (Autoencoder) acompanhado de **algoritmos** de injeção sintética de anomalias e um **estudo experimental/benchmark** avaliando a precisão da detecção em imagens de raio-X de contêineres

## 0.5 O TCC já previa desenvolvimento de interface com usuário?

- [ ] Sim, a interface já faz parte do TCC.
- [ ] Parcialmente; existe alguma interação, mas ainda não está bem definida.
- [X] Não. O TCC é predominantemente técnico e não previa interface.

**Explique o que está formalmente previsto no TCC:** O escopo formal do TCC concentra-se no treinamento e validação de um modelo de aprendizado para detecção de anomalias em imagens radiográficas de contêineres, utilizando datasets públicos e simulação sintética de ameaças, sem prever o desenvolvimento de uma aplicação de interface gráfica.

---

# 1. Entendendo a contribuição do projeto

## 1.1 Explique o TCC em uma frase, sem citar linguagem de programação, framework ou banco de dados.

Um sistema computacional capaz de analisar imagens de raio-x de contêineres de carga para detectar autonomamente mercadorias ilícitas e anomalias ocultas sem depender de exemplos reais prévios de contrabando.

## 1.2 Qual situação, atividade ou problema do mundo real motivou o TCC?

[FT01] A detecção de itens ilícitos por inspeção de raio-X ganhou importância por causa do grande volume de carga que cruza fronteiras, e localizar esses itens é difícil porque as anomalias são imprevisíveis (Fonte: resumo de Gaikwad et al., artigo base do TCC, DOI 10.1016/j.engappai.2024.109675, citado em 4.6).

[H10] As imagens são complexas e têm objetos sobrepostos, o que dificulta a inspeção manual. O resumo do artigo não afirma isso.

[H40] O volume do comércio exterior torna impraticável a inspeção física de todos os contêineres, e por isso os portos recorrem à triagem não intrusiva por raio-X. [F] O artigo base sustenta o grande volume de carga. [?] Não informa que parcela é inspecionada fisicamente.

## 1.3 Qual é a **capacidade/contribuição central** produzida pelo TCC?

> “Nosso TCC produz, melhora, analisa ou permite **detectar e localizar anomalias e riscos em imagens de raio-X de contêineres utilizando aprendizado e geração de imagens residuais**.”

## 1.4 O que se espera que esteja diferente **para pessoas, organizações ou processos** se essa contribuição for bem-sucedida?

[H36] Se bem-sucedida, a tecnologia permitirá que alfândegas e operadores portuários triem um volume muito maior de contêineres com maior precisão, reduzindo o tempo de retenção de cargas lícitas e direcionando a inspeção física apenas para contêineres com alta probabilidade de anomalia.

## 1.5 O que é mérito técnico/científico do TCC e o que seria uma possível aplicação prática?

| Mérito/contribuição técnica                                                                                                                                  | Possível aplicação/valor em uso                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Treinamento de Autoencoder autossupervisionado com cargas normais; injeção sintética de anomalias via Lei de Beer-Lambert; segmentação por imagem residual. | Ferramenta de apoio à decisão para operadores de scanners em portos, destacando discrepâncias e priorizando alvos de vistoria. |

---

# 2. Entendendo as pessoas envolvidas

## 2.1 Quem interage diretamente com o produto, se já existe interface prevista?

NÃO SE APLICA AO ESCOPO ORIGINAL (O TCC não prevê interface).

## 2.2 Quem poderia **usar, configurar, administrar, operar, interpretar ou tomar decisões** a partir da contribuição técnica?

| Perfil                                                     | Relação com a contribuição | O que faria                                                                                                                   | Status/evidência |
| ---------------------------------------------------------- | ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| **Operador da estação de imagem de raio-X** | Usuário direto operacional | Examina a radiografia e o mapa residual de cada contêiner e produz um apontamento sobre o que encontrou. | [H01] Hipótese |
| **Autoridade aduaneira que decide e formaliza (Auditor-Fiscal)** | Usuário direto ou destinatário do apontamento | Decide sobre liberação, vistoria física ou retenção e registra o ato formal. Pode ser a mesma pessoa que opera a estação ou outro cargo. | [H39] Hipótese |
| **Analista de Inteligência Aduaneira**              | Usuário tático               | Consulta relatórios históricos de varreduras, investiga padrões de contrabando e audita decisões anteriores.              | [H02] Hipótese     |
| **Administrador / Engenheiro de IA**                 | Configurador técnico          | Ajusta limiares de sensibilidade (*thresholds*) do modelo e monitora a performance do pipeline de IA.                       | [?01] Lacuna        |

[H39] Operar a estação de imagem e decidir formalmente sobre a carga podem ser atividades de pessoas ou cargos diferentes, com permissões, vocabulário e responsabilidades distintas. [?] Ainda não sabemos quem executa cada parte: quem opera a estação, quem interpreta a imagem, quem recebe o apontamento, quem decide, quem registra a decisão e quem responde formalmente por ela. Nos trechos seguintes, "operador da estação" designa quem examina a imagem e "Auditor-Fiscal" designa quem detém a decisão formal, sem assumir que são a mesma pessoa.

## 2.3 Existem pessoas afetadas que não usariam a interface diretamente?

| Stakeholder                                               | Como é afetado                                                                           | Usa interface?                          | Status/evidência                |
| --------------------------------------------------------- | ----------------------------------------------------------------------------------------- | --------------------------------------- | -------------------------------- |
| **Empresas Importadoras / Exportadoras** | [FT02] O canal de parametrização define se a carga tem desembaraço automático ou passa por exame documental e verificação física, o que altera o tempo de liberação (Fonte: Manual de Despacho de Importação da RFB, análise C02 da Entrega 2). [H] O impacto em custos logísticos ainda não tem fonte. | Não | [FT02] Fato, com a fonte indicada |
| **Autoridades de Segurança Pública / Alfândega** | Beneficiam-se da eficácia na interceptação de ilícitos (drogas, armas, contrabando).  | Não (recebem relatórios consolidados) | [H03] Hipótese                    |

## 2.4 Que características desses perfis podem influenciar a interação?

[H37] Operadores da estação de imagem trabalham sob pressão de tempo severa, em turnos prolongados, sujeitos à fadiga visual. Possuem forte conhecimento prático de leitura radiográfica, mas podem não ter familiaridade com conceitos profundos de aprendizado de máquina (exigem explicações visuais claras e diretas, como heatmaps e scores de risco, em vez de métricas matemáticas complexas).

---

# 3. Entendendo objetivos e atividades

## 3.1 O que o usuário está tentando conseguir no mundo real?

[H38] Ao examinar cada contêiner, quem opera a estação de imagem procura chegar a uma conclusão em que confie: entender se o que aparece na imagem é compatível com a carga declarada, saber onde olhar quando há algo atípico e registrar o que concluiu de forma que possa ser defendida depois. Essa conclusão é tomada sob incerteza. Falsos positivos e falsos negativos são possíveis (H12), e o objetivo é reduzir a incerteza, não eliminá-la.

[?07] Não sabemos se existem metas de liberação por turno para esse perfil, nem como seriam cobradas. A segurança da carga que entra no país e a fluidez do porto são objetivos da organização (H36), não necessariamente o que o usuário busca durante a tarefa.

## 3.2 Quais são as atividades mais importantes?

| ID  | Atividade/objetivo                                                                          | Quem realiza              | Frequência/criticidade inicial | Status/evidência |
| --- | ------------------------------------------------------------------------------------------- | ------------------------- | ------------------------------- | ----------------- |
| A01 | Triar a fila diária de contêineres escaneados por raio-X | Operador da estação de imagem [H01] | Alta / Crítica | [H04] Hipótese |
| A02 | Inspecionar detalhes de uma anomalia detectada (comparar imagem original com mapa residual) | Operador da estação de imagem [H01] | Média / Alta | [H05] Hipótese |
| A03 | Registrar o veredito (liberado, suspeito para vistoria física, retenção) | [?] Operador da estação ou Auditor-Fiscal, conforme H39 | Alta / Crítica | [H06] Hipótese |
| A04 | Consultar histórico de varreduras e laudos anteriores                                      | Analista de Inteligência | Baixa / Média                  | [?02] Lacuna        |

## 3.3 Qual atividade parece mais frequente? Por quê?

[H07] A atividade A01 (triar a fila de contêineres) e A03 (registrar vereditos), pois todo contêiner escaneado precisa passar por verificação e liberação formal no fluxo portuário.

## 3.4 Qual parece mais crítica? Que consequência existe se for mal executada?

[H08] A atividade A03 (tomada de decisão de liberação). Se um contêiner ilícito for liberado por erro de interpretação (falso negativo), há risco de contrabando de armas ou drogas. Se uma carga lícita for retida indevidamente por falso positivo, gera prejuízos financeiros e atrasos logísticos severos.

---

# 4. Entendendo o problema ou processo atual

## 4.1 Como essas atividades são realizadas hoje, antes da interface imaginada na disciplina?

[H09] Hoje, quem opera a estação usa os softwares fornecidos pelos fabricantes dos scanners. [F] Esses softwares já oferecem apoio analítico, como discriminação de materiais por pseudo-cor, realce de bordas e comparação com imagens semelhantes (C01 e C03 da Entrega 2), mas não foi encontrada detecção autossupervisionada de anomalias. [H] A interpretação final da imagem continua sendo visual e humana.

## 4.2 O que é difícil, demorado, confuso, repetitivo, arriscado ou pouco transparente?

[H10] A sobreposição visual de mercadorias complexas (diferentes densidades e materiais), a fadiga visual acumulada após horas de plantão examinando imagens, e a dificuldade de detectar anomalias que não correspondem a assinaturas rígidas pré-cadastradas.

## 4.3 Que informações o profissional precisa interpretar para tomar decisão?

[H11] Tons indicativos de densidade material (orgânico vs. inorgânico vs. metálico), geometria dos objetos no interior do contêiner, contexto da declaração da carga e alertas de sistemas auxiliares.

## 4.4 O que acontece quando a atividade falha ou quando o resultado é interpretado incorretamente?

[H12] Ocorrência de falsos negativos (entrada de ilícitos no país) ou falsos positivos (paralisação de contêineres legítimos, gerando custos de pátio, inspeção física desnecessária e atrito com exportadores).

## 4.5 Conte uma situação concreta.

[H13] Carlos, operador da estação de imagem em um terminal portuário movimentado, inicia seu terceiro turno consecutivo de análise de imagens de raio-X. Às 03:00 da manhã, após centenas de contêineres escaneados, uma densidade levemente atípica camuflada no interior de paletes de madeira passa despercebida na tela devido à exaustão visual, permitindo a passagem de mercadoria não declarada.

Esta situação é um cenário exploratório, criado para discutir o problema. Carlos não é um perfil investigado nem uma persona: turno, horário e volume são suposições [H13].

## 4.6 Que evidência existe hoje?

| Evidência/fonte                                                                                                         | O que sustenta                                                                                       | Limitação                                                                         |
| ------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Artigo base do TCC (*Self-supervised anomaly detection and localization for x-ray cargo images*, Gaikwad et al., 2025) | Grande volume de carga nas fronteiras, dificuldade de localizar anomalias imprevisíveis e proposta de detecção e localização autossupervisionadas (resumo do artigo, DOI 10.1016/j.engappai.2024.109675). | Foco estritamente técnico/algorítmico, sem modelagem de experiência do operador. |

---

# 5. Entendendo o contexto de uso

## 5.1 Onde e em quais situações a interação poderia ocorrer?

[H14] Em salas de controle de raio-X de portos, armazéns alfandegados ou centros de triagem da Receita Federal, sob alta demanda operacional.

## 5.2 Em quais dispositivos/equipamentos?

[H15] Estação de trabalho desktop com monitor dedicado para imagens radiográficas. [F] A especificação da estação de trabalho da Smiths Detection indica monitores de 22" a 24" (C03 da Entrega 2). [?] Não há evidência de configuração com múltiplos monitores.

## 5.3 Existem condições físicas relevantes?

[H16] Iluminação ambiente controlada, ruído de equipamentos e sirenes de pátio portuário, interrupções frequentes e intensa pressão temporal.

## 5.4 Existem fatores sociais ou organizacionais?

[H17] Hierarquia rígida de fiscalização, responsabilidade legal e criminal associada à liberação de cargas, necessidade de auditoria e registro imutável de quem autorizou cada liberação.

## 5.5 Existe necessidade de histórico, rastreabilidade ou auditoria?

[H18] Sim. Toda decisão de liberação ou direcionamento para vistoria deve ser estritamente rastreável para fins legais, investigativos e de conformidade aduaneira.

## 5.6 Um erro pode produzir consequência relevante? Qual?

[H19] Sim. Falhas podem resultar em evasão fiscal, entrada de drogas/armas no território nacional (falso negativo) ou prejuízos logísticos internacionais por retenção injustificada de cargas (falso positivo).

---

# 6. Entendendo mercado e alternativas existentes

> Nesta entrega faça apenas um **levantamento inicial**. A análise aprofundada ocorre na Entrega 2.

## 6.1 Como pessoas resolvem problemas semelhantes hoje?

| Alternativa atual                                                      | Quem usa               | Para quê                                                            | Status/evidência   |
| ---------------------------------------------------------------------- | ---------------------- | -------------------------------------------------------------------- | ------------------- |
| Softwares proprietários dos fabricantes de scanners (ex.: Rapiscan AS&E InSight, Smiths Detection DaiSy) | Operadores de estação de imagem | Visualizar, tratar e comparar imagens de raio-X de contêineres. | [FT03] Fato. Fonte: páginas oficiais da Rapiscan AS&E e da Smiths Detection, analisadas em C01 e C03 da Entrega 2 |

## 6.2 Existem produtos que atuam na mesma área, mesmo sem serem equivalentes ao TCC?

[H20] Sistemas de gerenciamento de carga portuária (TOS - Terminal Operating Systems)

## 6.3 Quais interfaces profissionais esse público já conhece?

[H21] Consoles de operação industrial, softwares GIS/monitoramento, painéis de controle com múltiplos filtros, sistemas ERP alfandegários (ex: Siscomex / Portal Único Siscomex).

## 6.4 O que essas soluções parecem fazer bem?

[H22] Gerenciamento do fluxo logístico global, controle de manifesto de cargas e exibição básica de imagens de raio-X.

## 6.5 O que parecem fazer mal, dificultar ou não atender?

[H23] Falta de inteligência para destacar anomalias invisíveis ao olho humano, interfaces muitas vezes densas, legadas e pouco intuitivas, com alta taxa de falsos alarmes sem explicações claras.

## 6.6 Que padrões de interface ou vocabulário parecem familiares a esse público?

[H24] Terminologia aduaneira e portuária (BL, Manifesto, Recinto, Vistoria, Despacho) e filas de status. [F] O despacho de importação usa quatro canais de parametrização: verde, amarelo, vermelho e cinza (Manual de Despacho de Importação da RFB, C02 da Entrega 2). Os canais são uma classificação normativa do processo de despacho, e não uma escala de risco produzida pelo modelo de IA.

---

# 7. Derivando o escopo de IHC da disciplina

## 7.1 Escolha o caminho do projeto

### Caminho A — TCC já possui interface

Não se aplica: o TCC não previa interface.

### Caminho B — TCC não possui interface prevista

Faça o exercício de transferência de uso:

> **Imagine que o TCC foi concluído com sucesso e uma empresa, laboratório ou organização quer transformar a contribuição em algo utilizável. Quem precisaria interagir com ela e para quê?**

1. quem poderia contratar/adotar a solução? Administrações portuárias, operadores logísticos alfandegados e órgãos aduaneiros (ex: Receita Federal).
2. quem seria o usuário direto? [H01] O operador da estação de imagem de raio-X. [H39] Se a decisão formal couber a outro cargo, o Auditor-Fiscal também seria usuário direto, com outra tarefa.
3. quem administraria/configuraria? Administrador de TI do terminal e Engenheiro de IA.
4. quem interpretaria resultados? [H01] O operador da estação de imagem e, de forma agregada, [H02] analistas de inteligência.
5. quem tomaria decisões? [?] Ainda não sabemos se quem examina a imagem tem autoridade para liberar ou reter, ou se apenas produz um apontamento para o Auditor-Fiscal (H39).
6. quais dados/entradas seriam necessários? Imagens de raio-X de transmissão do contêiner e metadados do manifesto de carga.
7. quais resultados deveriam ser compreendidos? Score de anomalia, mapas residuais de discrepância e regiões de alerta (ROI).
8. que erros/rupturas seriam possíveis? Falsos positivos gerando vistoria desnecessária; falsos negativos deixando passar ameaças; falha de carregamento da imagem radiográfica.

## 7.2 Qual perfil será priorizado no projeto de IHC?

**Operador da estação de imagem de raio-X** [H01].
**Por que esse perfil foi escolhido?** [H01] É quem examina a radiografia de cada contêiner, e é sobre a imagem que a contribuição do TCC atua. [H39] Não está demonstrado que esse perfil também detém a autoridade para liberar ou reter a carga. Essa divisão de papéis é a primeira questão a investigar, porque muda permissões, vocabulário e o próprio fluxo de registro da decisão.

## 7.3 Qual objetivo desse usuário será priorizado?

Analisar os alertas gerados pelo modelo de IA, comparar a imagem original de raio-X com o mapa residual de anomalia e registrar o resultado da análise. [H39] Esse registro pode ser um apontamento técnico encaminhado a quem decide ou a própria decisão de liberação ou vistoria física, conforme a divisão de papéis.

## 7.4 Que interface será explorada na disciplina?

> **Para fins da disciplina de IHC, será projetada uma interface que permita ao `operador da estação de imagem de raio-X` utilizar o `modelo de detecção de anomalias em raio-X` para `triar contêineres suspeitos, inspecionar mapas residuais de discrepância e registrar o resultado da análise`, no contexto de `um terminal portuário alfandegado sob pressão de tempo`.**

## 7.5 Qual é a relação dessa interface com o TCC?

- [ ] Já fazia parte do TCC.
- [ ] É um aprofundamento de algo parcialmente previsto.
- [ ] É uma extensão conceitual criada para a disciplina.
- [X] É um protótipo demonstrativo de aplicação potencial.
- [ ] Outra.

> **Declaração:** a interface desenvolvida nesta disciplina é um artefato de aprendizagem de IHC baseado no tema do TCC. Sua inclusão ou implementação no TCC somente ocorrerá se isso for posteriormente decidido pela equipe e pelo orientador.

---

# 8. Levantando possibilidades de interação — sem desenhar ainda

A equipe pode registrar possibilidades para investigação. **Não significa que todas serão implementadas.**

Marque apenas as que parecem plausíveis e explique o objetivo correspondente.

| Possibilidade | Pode fazer sentido? | Objetivo/tarefa que justificaria | Evidência atual | Classificação no recorte |
| --- | --- | --- | --- | --- |
| **Comparação de resultados** | Sim | Entender onde a imagem se afasta do padrão, vendo a radiografia e o mapa residual | [H30] | 1. Essencial |
| **Explicabilidade/detalhamento** | Sim | Saber qual região foi apontada e por quê | [H31] | 1. Essencial para o destaque da região. O score numérico é hipótese secundária |
| **Auditoria/logs** | Sim | Registrar o resultado da análise e quem o produziu | [H32] | 1. Essencial para o registro do resultado. O formato da trilha é hipótese secundária |
| **Dashboard/visão geral** | Sim | Saber quais contêineres examinar e em que ordem | [H25] | 2. Hipótese secundária, depende de H04 |
| **Alertas/ocorrências** | Sim | Não deixar um caso crítico parado na fila | [H33] | 2. Hipótese secundária, depende de H04 e H25 |
| **Acompanhamento de processamento** | Sim | Saber se a análise da imagem já terminou | [H27] | 2. Hipótese secundária, depende de ?05 |
| **Relatório/resultados** | Sim | Encaminhar o resultado da análise a quem decide ou executa | [H28] | 2. Hipótese secundária, depende de H39 |
| **Histórico com busca/filtros** | Sim | Duas necessidades distintas: recuperar o que já aconteceu com um contêiner ou declaração (AC04) e investigar padrões em varreduras anteriores | [H29], [?02] | 2. Hipótese secundária para a consulta de um caso pelo identificador (AC04). 3. Necessidade de outro perfil para a investigação de padrões (Analista de Inteligência, H02) |
| **Configuração/parametrização** | Talvez | Ajustar sensibilidade de detecção da IA | [?03] | 3. Necessidade de outro perfil (configurador técnico, ?01) |
| **Entrada/upload/seleção de dados** | Talvez | Receber novas imagens de raio-X e metadados do contêiner | [H26] | 4. Pode ser descartada: a imagem tende a chegar do scanner, sem ação do usuário |
| **Ajuda/documentação** | Talvez | Consultar termos radiográficos e instruções de uso | [?04] | 4. Pode ser descartada |
| **Administração/configurações globais** | Não | - | - | Fora do recorte |
| **Usuários/perfis/permissões** | Não | - | - | Fora do recorte |
| **CRUD de entidade do domínio** | Não | - | - | Fora do recorte |

**Classificação no recorte.** O recorte da seção 7.4 é triar, inspecionar o mapa residual e registrar o resultado da análise. Cada possibilidade foi classificada como: 1, essencial para esse fluxo; 2, hipótese secundária que pode apoiá-lo; 3, necessidade de outro perfil; 4, possibilidade que pode ser descartada. Só o nível 1 entra nas próximas entregas sem investigação adicional, e mesmo nele a forma de apresentação continua aberta.

> **Atenção:** “login + dashboard + CRUD” não é uma solução universal. Cada padrão deve surgir de uma tarefa real.

---

# 9. Benefícios e ações iniciais

## 9.1 Qual benefício concreto o projeto de IHC pretende oferecer?

| Benefício esperado                                               | Problema/necessidade                                    | Usuário            | Status/evidência |
| ----------------------------------------------------------------- | ------------------------------------------------------- | ------------------- | ----------------- |
| Redução da fadiga visual e foco direcionado em áreas suspeitas | Exaustão em plantões longos analisando imagens densas | Operador da estação de imagem | [H34] |
| Agilidade para concluir a análise e encaminhar liberação ou vistoria | Gargalos operacionais e filas portuárias | Operador da estação de imagem | [H35] |

## 9.2 Que ações o usuário deverá conseguir realizar?

As linhas descrevem resultados que o usuário precisa alcançar, e não telas ou componentes. A forma de apoiar cada um será definida a partir da modelagem de tarefas.

| ID  | O usuário precisa conseguir...                                                 | Para alcançar...                                     | Prioridade inicial |
| --- | ------------------------------------------------------------------------------- | ----------------------------------------------------- | ------------------ |
| AC01 | Saber quais contêineres examinar e em que ordem (depende de H04) | Dedicar atenção primeiro ao que mais precisa | Alta |
| AC02 | Entender onde e por que a IA apontou discrepância na imagem | Concluir se o apontamento é procedente | Alta |
| AC03 | Registrar o resultado da análise com sua justificativa (apontamento ou decisão, conforme H39) | Deixar a conclusão rastreável para quem decide e para auditoria | Alta |
| AC04 | Recuperar análises anteriores de um contêiner ou declaração | Investigar reincidências ou auditar análises | Média |

## 9.3 Tecnologias/restrições já definidas no TCC

A tecnologia aparece *agora*, depois do entendimento do uso.

| Tecnologia/restrição | Por que existe | Possibilidade ou restrição para a interação (hipótese de design a investigar) |
| ---------------------- | -------------- | -------------------------------- |
| *Modelo de IA Autossupervisionado (Autoencoder)* | Escolha de arquitetura do TCC para aprender o padrão de cargas normais sem necessitar de imagens de contrabando prévio para treino. | [F] O modelo aponta discrepâncias em relação ao padrão de carga normal, e não categorias de objetos. [H] Apresentar o resultado de forma comparativa pode ajudar a entender o que foi apontado. A forma de apresentação está aberta (H30). |
| *Geração de Mapa Residual de Anomalia* | Saída primária do algoritmo que calcula a diferença entre a imagem real de raio-X e a reconstrução do Autoencoder. | [F] Existe uma segunda imagem, o mapa residual, que pode ser mostrada junto da radiografia. [H] Mapa de calor, controle de opacidade, alternância de camadas e lado a lado são alternativas a comparar (H30). Nenhuma decorre da tecnologia. |
| *Tempo de Inferência e Processamento de Imagem* | Restrição computacional do pipeline de visão computacional ao carregar e reconstruir matrizes de alta resolução de raio-X. | [?05] O tempo de inferência ainda não é conhecido. [H27] Se houver espera perceptível, algum retorno sobre o andamento pode ser necessário. A forma desse retorno não está definida. |
| *Injeção Sintética de Anomalias (Lei de Beer-Lambert)* | Método matemático do TCC para simular atenuamentos de radiação de objetos ocultos nas imagens de treino. | [F] O método afeta como o modelo é treinado e avaliado. [H31] Não está demonstrado que um score numérico seja compreensível, confiável ou útil para quem examina a imagem. |

A tecnologia do TCC cria possibilidades e restrições, mas não determina a forma de apresentação. Essa forma depende da atividade, do contexto e das evidências sobre os usuários.

---

# 10. Hipóteses e dúvidas prioritárias

As hipóteses estão ordenadas pelo risco para o projeto: primeiro as que, se estiverem erradas, obrigam a mudar o usuário, o fluxo ou o recorte de IHC. As hipóteses sobre alternativas de solução vêm depois.

| Prioridade | ID | Hipótese/dúvida | O que muda se estiver errada | Como poderá ser investigada |
| --- | --- | --- | --- | --- |
| 1 | H01, H39 | Quem opera a estação de imagem é o usuário direto, e a decisão formal sobre a carga pode caber a outro cargo. | Muda o usuário prioritário, as permissões e o significado do registro feito na interface. | Entrega 7: entrevista com profissional da área ou, na falta, normas e material institucional da RFB sobre conferência com escâner. |
| 1 | H04, H07 | A triagem é uma atividade contínua e frequente, e existe uma fila de contêineres a examinar. | Se as imagens chegam uma a uma, sem fila, a triagem e a priorização saem do recorte. | Entrega 7: entrevista ou observação. A Entrega 5 modela só o que estiver sustentado. |
| 1 | H06, H08 | O resultado da análise é registrado formalmente, e esse registro é a etapa mais crítica. | Muda o fluxo de registro e o risco de duplicar o que já é feito no Siscomex. | Entrega 7: entrevista e documentação do despacho (C02 da Entrega 2). |
| 1 | H11 | Além da imagem, o profissional usa dados da carga declarada para concluir. | Define quais informações precisam estar disponíveis junto da imagem e em que momento. | Entrega 7: entrevista. |
| 1 | H14, H15, H16 | O uso ocorre em sala de controle, em estação dedicada, com ruído, interrupções e pressão de tempo. | Restringe cor, som e densidade de informação. | Entrega 7: entrevista, fotos ou material institucional do ambiente. |
| 2 | H30 | Visualização lado a lado (imagem original e mapa residual) é preferível à sobreposição com ajuste de opacidade. | Define a disposição da tela de análise. Só faz sentido testar depois de confirmados usuário e tarefa. | Entrega 6: comparação de alternativas em baixa fidelidade. |
| 2 | H31 | Exibir a marcação da região apontada e um índice de anomalia aumenta a aceitação da IA por quem examina a imagem. | Define o nível de explicação mostrado. | Entrega 7 para o que o usuário espera de uma explicação; Entrega 6 e Entregas 12 a 14 para as alternativas. |
| 2 | H33 | Avisos em tempo real são necessários para que um contêiner com anomalia alta não fique parado na fila. A reordenação da fila por nível de anomalia é tratada em H35 e H41. | Depende de H04: sem fila, não há o que avisar nem reordenar. | Entrega 7 para a tarefa; Entregas 12 a 14 para a solução. |

Registre em [`../RASTREABILIDADE.md`](../RASTREABILIDADE.md).

---

# 11. Síntese da equipe

| Pergunta                                 | Síntese atual                                                                                                                                                         |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Qual é a contribuição central do TCC? | Detecção autossupervisionada de anomalias em raio-X de contêineres via Autoencoders e imagens residuais.                                                            |
| O TCC já previa interface?              | Não                                                                                                                                                                   |
| Quem é o usuário prioritário de IHC?  | [H01] Operador da estação de imagem de raio-X. A relação com o Auditor-Fiscal que formaliza a decisão está aberta (H39). |
| O que ele precisa alcançar?             | [H38] Chegar a uma conclusão confiável sobre cada contêiner examinado e registrá-la de forma defensável. |
| Qual problema/atividade será estudado?  | Exame de imagens de contêineres e registro do resultado, sob incerteza. Fadiga visual e pressão de tempo são hipóteses (H10, H16).                                                                                    |
| Como isso acontece hoje?                 | [H09] Inspeção visual em softwares dos fabricantes de scanners, que já oferecem apoio analítico (pseudo-cor, realce, comparação), sem detecção autossupervisionada de anomalias. |
| Qual é o contexto de uso?               | [H14, H15, H16] Sala de controle portuária, estação com monitor dedicado de 22" a 24", pressão temporal e gravidade da segurança. |
| Que interface/recorte será explorado?   | Visualizador comparativo (original e mapa residual) e registro do resultado da análise, que pode ser apontamento ou decisão (H39).                                                                                            |
| Como a interface se relaciona ao TCC?    | Protótipo demonstrativo de aplicação potencial da capacidade analítica do modelo.                                                                                  |
| Quais pontos ainda são hipóteses?      | Prioridade 1, porque podem mudar usuário, tarefa ou recorte: H01 e H39 (quem opera e quem decide), H04 e H07 (existência e frequência da triagem em fila), H06 e H08 (registro do resultado), H11 (informações para concluir) e H14 a H16 (contexto). Prioridade 2, alternativas de solução: H30, H31 e H33. Lacunas abertas: ?01 a ?08, com destaque para ?07 e ?08. |

### Delimitação

**Dentro do escopo de IHC:** Visualização comparativa de imagens e registro do resultado da análise. A triagem em fila entra se H04 e H41 se sustentarem.
**Fora do escopo de IHC:** Treinamento do modelo de IA, ajuste de hiperparâmetros do Autoencoder, engenharia de backend e captura física de dados do scanner de raio-X.
**Dentro do escopo formal do TCC:** Pesquisa e desenvolvimento do algoritmo de detecção autossupervisionada e validação experimental por métricas (F1-score).
**Interface da disciplina será implementada no TCC?** não definido

---

# 12. Como esta entrega alimenta as próximas

- **Entrega 2:** verifica mercado, concorrentes e interfaces profissionais representativas.
- **Entrega 3:** detalha perfis e contexto a partir do que for investigado sobre o usuário. O personagem da situação 4.5 não é ponto de partida para persona.
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

1. **Problema/atividade humana:** [FT01] O grande volume de carga que cruza fronteiras torna importante a detecção de itens ilícitos por raio-X, e localizar esses itens é difícil. [H] Quem examina as imagens lida com objetos sobrepostos, fadiga visual e pressão de tempo (H10, H37).
2. **Contribuição técnica do TCC:** Um modelo de inteligência artificial autossupervisionada que aprende o padrão de cargas normais e gera mapas residuais indicando onde a imagem se afasta desse padrão. A precisão desses mapas é o que a avaliação experimental do TCC vai medir.
3. **Como uma pessoa poderia utilizar essa contribuição:** [H] Uma interface em sala de controle portuária que mostre a quem examina a imagem onde a IA encontrou discrepância e apoie o registro da análise. Os benefícios esperados, ainda a validar, são localizar regiões suspeitas com menos esforço (H34) e reter menos cargas lícitas (H36).

Essa síntese ajuda a apresentar o projeto para público não especializado sem reduzir seu mérito técnico.

---

# Checklist de qualidade

- [X] Está clara a diferença entre tema do TCC, escopo formal do TCC e escopo de IHC.
- [X] A equipe declarou se o TCC já previa interface.
- [X] Se não previa, foi derivado um usuário plausível e um objetivo de uso.
- [X] A interface de IHC não foi apresentada como obrigação automática do TCC.
- [X] A contribuição do TCC foi descrita sem começar por tecnologias de implementação.
- [X] Usuários diretos e stakeholders foram diferenciados.
- [X] Foram considerados profissionais que configuram, administram, interpretam ou decidem, quando pertinente.
- [X] Objetivo do usuário não foi confundido com objetivo do projeto.
- [X] Processo/problema atual foi descrito antes da solução.
- [X] Existe situação concreta de uso/problema.
- [X] Contexto físico, social/organizacional, dispositivos e consequências de erro foram considerados.
- [X] Mercado/alternativas existentes foram levantados inicialmente.
- [X] Possibilidades como dashboard, relatório, histórico, filtros e CRUD foram tratadas como hipóteses de solução, não como requisitos automáticos.
- [X] Cada possibilidade de interface tem um objetivo/tarefa que poderia justificá-la.
- [X] Afirmações relevantes estão marcadas `[F]`, `[H]` ou `[?]`.
- [X] Hipóteses prioritárias receberam IDs e foram para a rastreabilidade.
- [X] O recorte de IHC é viável para modelar, prototipar e avaliar no semestre.
- [X] A equipe consegue explicar problema humano → contribuição computacional → forma de uso.

## Histórico de revisões

| Data | O que mudou | Motivo |
|---|---|---|
| 06/10/2026 | Papéis de operador e Auditor-Fiscal (H39), objetivo do usuário (H38), fontes dos fatos, classificação das possibilidades da seção 8, hipóteses de design da seção 9.3, priorização da seção 10 e identificadores. | [Parecer do professor](../feedbacks_professor/Feedback_Professor_Entrega01_Equipe09.md), com o tratamento de cada item anotado no próprio parecer. |
| 12/10/2026 | Enunciados de H31 e H33 iguais aos da matriz. Histórico desdobrado em duas necessidades na seção 8. Síntese e delimitação da seção 11 com o vocabulário das seções 7.3 e 7.4. Ano do artigo base (2025). Campos de template removidos. | Auditoria de coerência de 12/10/2026 (AC-006, AC-007, AC-012, AC-015, AC-016). |

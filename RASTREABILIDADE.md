# Matriz de rastreabilidade de IHC

Esta matriz registra como as decisões do projeto evoluíram desde a contribuição técnica do TCC até os artefatos de IHC. **Não apaga hipóteses antigas ao incorporar uma nova entrega**. Sempre que não houver avaliação ou evidência suficiente, a condição permanece indicada.

A interface já fazia parte do escopo previsto do TCC e existe como **protótipo desktop funcional V0**. A E6 documentou seus estados reais, realizou um walkthrough formativo e registrou propostas V0→V1. A E7 elaborou instrumentos de investigação não aplicados naquela entrega. A E8 definiu capacidades, princípios e metas; as E9/E10 consolidaram o modelo conceitual e a MoLIC; a E11 materializou o protótipo Figma; a E12 planejou a avaliação; a E13 inspecionou os fluxos; e a E14 registrou observações de U01 e U02 e sua consolidação. A documentação acadêmica foi concluída, **sem presumir que as recomendações de usabilidade tenham sido implementadas**.

Uma correção central permanece válida: a V0 oferece **histórico/seleção da execução (PP06)** e **análise individual (PP07)**, mas **não implementa comparação automática entre duas execuções**. T07 é concluída mediante consulta separada de A e B e análise manual externa.

---

## 1. Derivação do escopo de IHC a partir do TCC

| Elemento | Registro da equipe | Evidência/justificativa | Estado |
|---|---|---|---|
| Tema do TCC | Algoritmo híbrido de controle semafórico baseado em Max Pressure e lógica actuated em ambiente de simulação. | TCC1 e entregas anteriores. | Definido. |
| Resultado técnico esperado | Sistema de controle e avaliação experimental em SUMO/TraCI, com interface para configurar, executar, acompanhar e consultar simulações. | TCC e V0 documentada na E6. | Definido; implementação técnica evolui no TCC. |
| Interface prevista no TCC? | Sim, já planejada pela equipe antes da disciplina. | Declaração da equipe e GUI funcional adotada na E6. | Definido. |
| Capacidade central | Selecionar movimentos prioritários e regular trocas/permanência do verde mediante estado observado do tráfego. | Metodologia híbrida do TCC. | Definido. |
| Possíveis interessados | Pesquisadores/analistas/engenheiros de tráfego, gestores e, indiretamente, usuários da malha viária. | E1–E3; ainda sem confirmação empírica do perfil principal. | H. |
| Usuário prioritário de IHC | Pesquisador ou analista de mobilidade urbana. | H01; proto-personas P01/P02. | Hipótese aberta. |
| Objetivo de uso | Preparar, executar, acompanhar, recuperar, interpretar e comparar experimentos em condições adequadas. | E1, E3–E6. | Hipótese de interação materializada parcialmente em V0. |
| Contexto de uso | Computador desktop/notebook em atividade acadêmica/laboratorial e possível uso profissional. | E3, E6, E8. | F/H conforme dimensão. |
| Recorte interativo | Seleção de cenário, configuração, validação, execução e acompanhamento, histórico e análise individual. | PF01–PF03 e PP01–PP07 na E6. | V0 documentada. |
| Limite de comparação | Execuções são consultadas separadamente e comparadas manualmente fora do aplicativo. | Evidências PP06/PP07 e W04/O10. | Fato da V0 documentada. |

---

## 2. Registro de hipóteses e lacunas

| ID | Hipótese | Evidência anterior | Investigação e evidência até E14 | Situação após E14 | Implicação |
|---|---|---|---|---|---|
| **H01** | Pesquisadores/analistas de mobilidade representam o usuário prioritário. | E2 — concorrentes; E3 — P01/P02; E6 — termos técnicos do domínio. | I01/I02 da E7 não foram aplicados. Na E14, U01/U02 foram descritos como participantes *proxy*, sem prática profissional de controle de tráfego. | **Aberta** para o público profissional pretendido. | Manter P01/P02 como proto-personas e não inferir necessidades de especialistas com base nos dois casos. |
| **H02** | A organização cenário → configuração → execução/acompanhamento → análise facilita os experimentos. | E3–E6 — jornada, T01–T08, PF01–PF03, O01–O07. | E9/E10 modelaram objetivos e diálogos; E11 implementou o percurso demonstrativo; E13 encontrou problemas de identidade, diagnóstico e navegação; E14 registrou 8/12 sucessos totais em UT01–UT06, com dificuldades em recuperação, histórico e comparação. | **Parcialmente investigada; não validada de forma geral.** | Preservar a organização essencial e priorizar AU02, AU03 e AU06; avaliar a versão corrigida depois. |
| **H03** | Uma apresentação consolidada/comparativa das métricas facilitaria a interpretação. | E6 — PP06/PP07, O09/O10, comparação manual e externa. | E9/E10 descreveram interpretação e síntese; E11 apresentou resultados demonstrativos individuais; E13 identificou HC04/HC07; E14 relatou dificuldade de U01 na UT05, comentário sobre escala e explicações, e explicação correta de U02 sobre a comparação externa. | **Parcialmente investigada; demanda de comparação automática não comprovada.** | Melhorar contexto, escala e definição das métricas, sem representar uma funcionalidade de comparação lado a lado como implementada. |

Os instrumentos I01/I02 da E7 continuam caracterizados como **projetados, não aplicados naquela entrega**. A observação de usuários na E14 é uma coleta distinta e não altera retrospectivamente o status metodológico da E7. A amostra de **N = 2** da E14, composta por participantes *proxy*, não permite generalização estatística nem validação de H01–H03 para profissionais de tráfego.

---

## 3. Rastreabilidade entre contribuição técnica, necessidades e artefatos

A matriz incorpora os artefatos concluídos até E14. **HC** identifica problemas heurísticos da E13; **AU** indica achados da observação da E14; **UT** indica tarefas padronizadas. Um achado não exercitado durante a observação continua relevante se foi documentado pela inspeção. Não se presume que as propostas de melhoria tenham sido implementadas no Figma ou na V0.

| ID | Capacidade técnica | Necessidade | Persona / cenário | Tarefa | E5 | E6 | E7 | E9 | E10 | E11 | E12 | E13 | E14 | Decisão vigente |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **R01** | Cenários/infraestruturas. | Selecionar a malha para o experimento. | P01 / C01 | T01 | Integrada ao fluxo; sem modelo individual exclusivo. | PF01/PP01; O01. | I01 Q05; I02 E03/E04. | CI01; OBJ02; signo Cenário. | M01 | F01/F01S | UT01 | Sem HC específico sobre catálogo. | UT01: U01 e U02 concluíram a preparação; **2/2 totais**. | Manter separação e contexto do cenário; conferir condições antes da confirmação. |
| **R02** | Parametrização. | Definir e corrigir condições experimentais. | P01 / C01 | T02 | HTA T02 | PF01/PP02/PP03; O02/O03/O05. | I01 Q05–Q07; I02 E03–E05. | CI01; OBJ02/OBJ03; signos Seed e Parâmetros avançados. | M01 | F02/F02A/F02E/F03 | UT01/UT02 | HC05 (explicação da configuração avançada). | **AU02** (2/2); UT02: U01 parcial com ajuda, U02 total. | Vincular mensagem ao campo inválido e preservar recuperação; não confundir UT02 com a falha de processamento de HC03. |
| **R03** | Estratégia de controle e modo. | Reconhecer controlador e modo de execução. | P01 / C01 | T03 | GOMS T03 | PF01/PP02; O02; PG01/PG02. | I01 Q05/Q06; I02 E04/E05. | CI01; OBJ02; signos Controlador e Modo. | M01 | F02/F03 | UT01/UT03 | HC02 (consistência da identidade entre etapas e resultados). | **AU01** (1/2); UT03: 2/2 reconheceram estado/controlador em quadro estável. | Repetir identificação coerente de cenário, controlador, seed e modo no resumo e resultado. |
| **R04** | Execução e acompanhamento. | Validar, iniciar, reconhecer processamento e recuperar falhas. | P01 / C01 | T04/T05 | CTT T04/T05 | PF02/PP03–PP05; O04–O07. | I01 Q08/Q09; I02 E06–E08. | CI01; OBJ03/OBJ04; signos Validação e Estado. | M01 | F03/F04/F04P/F04E/F05 | UT02/UT03 | HC03 (diagnóstico de falha); HC06 (histórico nas conclusões alternativas). | UT03: 2/2 corretos sob apresentação estável; HC03/HC06 não exercitados diretamente. | Melhorar feedback/diagnóstico e acesso ao histórico, sem afirmar adequação da transição automática original. |
| **R05** | Histórico, métricas e gráficos. | Localizar e compreender uma execução. | P01/P02 / C02 | T06 | GOMS T06 | PF03/PP06/PP07; O08/O09. | I01 Q10/Q11; I02 E09/E10/E13. | CI02; OBJ06/OBJ07; signos Registro/Métrica/Gráfico. | M02 | F07/F08/F09/F08E | UT04/UT06 | HC01 (status), HC04 (escala), HC07 (Throughput). | **AU03** (2/2), **AU05** (1/2), **AU06** (1/2). UT04: acerto final 2/2, U02 com ajuda. | Destacar identificadores e status, melhorar escalas/definições e a recuperação de indisponibilidade. |
| **R06** | Comparação de controladores. | Confrontar execuções e verificar equivalência das condições. | P01/P02 / C02 | T07 | HTA T07; CTT T07/T08 | PF03/PP06/PP07 + trabalho externo; O10. | I01 Q12/Q13; I02 E11–E13. | CI02; OBJ08; signos Condições e Métrica. | M02 | F07/F08/F08B/F09/F09B | UT05 | HC02 (identidade) e HC06 (continuidade), sem prova de correção. | **AU04** (2/2 com ocorrências diferentes); UT05: U01 parcial, U02 total. | Manter consulta individual e comparação **externa/manual**; melhorar contexto para prevenir conclusões indevidas. |
| **R07** | Síntese de análise. | Interpretar e comunicar resultados e limitações. | P01/P02 / C02 | T08 | CTT T07/T08 | PF03/PP07 + síntese externa; O09/O10. | I01 Q10–Q17; I02 E14–E20. | CI02; OBJ09; signos Métrica e Gráfico. | M02 | F08/F08B/F09/F09B | UT05 e pós-teste | HC04/HC07 (clareza de representação). | **AU04/AU05**; compreensão final da comparação externa em 2/2, sucesso integral em UT05 de 1/2. | Apoiar explicação dos indicadores e documentação de limites, sem inventar geração automática de síntese. |

O prefixo `C01/C02` também foi utilizado na E2 para **concorrentes** (Aimsun/Vissim), enquanto na E4 designa **cenários de problema**. Nesta matriz, `C01/C02` denotam cenários de E4; concorrentes da E2 são mencionados sempre com o nome do produto ou `E2-C01/E2-C02`, sem alterar retrospectivamente IDs consolidados.

---

## 4. Observação sobre a Entrega 5

A E5 é referência consolidada e não foi modificada. Ela modela HTA T02, GOMS T03, CTT T04/T05, HTA T07, GOMS T06 e CTT T07/T08, cobrindo atividades de Gabriel e João. T01 integra o fluxo do projeto, embora não possua modelagem individual nessa entrega.

---

## 5. Observação sobre a Entrega 6

A E6 adotou a GUI funcional do TCC como **protótipo digital V0**, no contexto da atividade de prototipação formativa. A substituição do papel por um artefato digital pré-existente foi registrada como orientação docente no documento da E6; a matriz conserva essa informação como registro da equipe, sem confundi-la com teste empírico de usuários.

**Fluxos principais:**

- PF01 — Preparar experimento: T01/T02/T03;
- PF02 — Validar, executar e acompanhar: T04/T05;
- PF03 — Localizar e analisar resultados: T06/T07/T08, com comparação externa.

**Estados documentados:**

| Estado | Descrição real da V0 | Evidência |
|---|---|---|
| PP01 | Catálogo/seleção de cenário. | `assets/06_prototipos/pp01_catalogo.png` |
| PP02 | Configuração, modo de execução e parâmetros avançados. | `pp02_configuracao.png`, `pp02_modo_execucao.png`, `pp02_configuracao_avancada.png` |
| PP03 | Validação e confirmação pré-execução. | `pp03_validacao.png`, `pp03_confirmacao.png` |
| PP04 | Inicialização/feedback textual de processamento. | `pp04_execucao.png` |
| PP05 | Execução Visual no SUMO-GUI. | `pp05_sumo_visual.png` |
| PP06 | Histórico e seleção de **uma** execução. | `pp06_historico.png` |
| PP07 | Informações, métricas e gráfico da execução selecionada. | `pp07_resultados.png`, `pp07_grafico.png` |

A captura `visao_geral_v0.png` complementa a documentação. São **12 capturas** no diretório `assets/06_prototipos/`.

### Walkthrough formativo — W01–W04

| ID | Atividade | Resultado documental |
|---|---|---|
| W01 | Preparar experimento. | Fluxo reconhecido; possível necessidade de contexto para termos. |
| W02 | Validar e iniciar. | Prevenção de configuração inválida reconhecida; recuperação pode melhorar. |
| W03 | Acompanhar execução. | Feedback visível, porém próximo de log técnico. |
| W04 | Consultar e comparar resultados. | Consulta individual compreendida; comparação externa/manual. |

### Observações e decisões V0→V1

| ID | Evidência/observação da E6 | Direção de design | Estado da decisão |
|---|---|---|---|
| O01 | Separação cenário/configuração é compreensível. | Preservar organização. | Preservação. |
| O02 | Termos técnicos podem exigir experiência prévia. | Ajuda e descrições contextuais. | Proposta V1. |
| O03 | Parâmetros avançados densos. | Manter área avançada apartada. | Preservar/refinar. |
| O04 | Validação prévia é útil. | Preservar bloqueio de configuração inadequada. | Preservação. |
| O05 | Erros precisam orientar correção. | Mostrar problema, causa possível e ação. | Proposta V1. |
| O06 | Logs competem com status principal. | Tornar estado principal mais evidente. | Proposta V1. |
| O07 | SUMO-GUI evidencia execução Visual. | Preservar modo Visual. | Preservação. |
| O08 | Histórico permite recuperar execuções. | Preservar contexto. | Preservar/refinar. |
| O09 | Resultados possuem informações e gráficos. | Manter vínculo e melhorar hierarquia. | Preservar/refinar. |
| O10 | Comparação demanda alternar execuções e trabalhar externamente. | Investigar apoio lado a lado. | Hipótese futura, não implementada. |

O walkthrough é uma **avaliação formativa registrada na E6**. Não deve ser reapresentado como teste de usabilidade com amostra de usuários finais.

---

## 6. Observação sobre a Entrega 7

A E7 gerou dois instrumentos **planejados**:

- **I01:** questionário de Gabriel — perguntas Q00 (consentimento) e Q01–Q17 (perfil, preparação, execução, métricas, comparação, linguagem e necessidades).
- **I02:** entrevista semiestruturada de João — perguntas E01–E20 (perfil, trabalho, execução, resultados, comparação, histórico, linguagem e necessidades abertas).

Os instrumentos possuem público, método, roteiro/protocolo, consentimento, privacidade, condições de uso de participantes proxy e plano de análise. **Não existem respostas coletadas, entrevistados registrados ou hipóteses validadas nesta etapa.**

### Rastreabilidade das investigações

| Fonte | Questões | Incertidão principal | Decisão eventual |
|---|---|---|---|
| I01 | Q01–Q04; Q15 | H01, H02 | Persona, rótulos e ajuda. |
| I01 | Q05–Q09 | H02 | Configuração, validação, feedback e recuperação. |
| I01 | Q10–Q14; Q16–Q17 | H03 e lacunas abertas | Métricas, histórico, síntese e comparação. |
| I02 | E01/E02/E17 | H01 | Perfil e linguagem. |
| I02 | E03–E08 | H02 | Estrutura de trabalho, parâmetros, estado e erro. |
| I02 | E09–E16/E18–E20 | H02/H03 | Interpretação, critérios de comparabilidade e novas necessidades. |

---

## 7. Rastreabilidade de padrões de interface

| Estado/fluxo | Padrão | Objetivo/tarefa | Situação |
|---|---|---|---|
| PF01/PP01 | Seleção de cenário | T01 | Implementado na V0. |
| PF01/PP02 | Configuração | T02/T03 | Implementado na V0. |
| PF02/PP03 | Validação/confirmação | T02/T04 | Implementado na V0. |
| PF02/PP04/PP05 | Acompanhamento | T04/T05 | Implementado com feedback textual e Visual. |
| PF03/PP06 | Histórico/seleção | T06/T07 | Implementado na V0. |
| PF03/PP07 | Resultado individual/gráfico | T06/T08 | Implementado na V0. |
| Externo à V0 | Comparação entre execuções | T07/T08 | Manual/externa. |
| Não justificado | Login, perfis administrativos e CRUD genérico | Sem tarefa rastreável | Não adotado. |

---

## 8. Decisões de interação acumuladas até a E7

São decisões de preservação ou propostas de evolução, conforme a coluna de estado de O01–O10:

- vincular cenário, método, seed, parâmetros e resultados;
- manter escolha explícita de cenário e estratégia;
- diferenciar configurações principais e avançadas;
- validar e confirmar antes de iniciar;
- reconhecer execução Visual e Headless e informar estado de processamento;
- permitir recuperação de resultados existentes;
- dar contexto e hierarquia às métricas;
- registrar comparação manual como externa à V0;
- não criar funcionalidades administrativas ou analíticas arbitrárias;
- manter H01/H02/H03 abertas até investigação apropriada.

---

## 9. Entrega 8 — Engenharia de usabilidade

A E8 transformou o conteúdo anterior em especificação de plataforma, princípios de design e **metas de uso**. Na E8, os valores de MU eram **alvos planejados**. A E14 registrou posteriormente o confronto desses alvos com os resultados de dois participantes, sem reescrever retrospectivamente as metas.

### Capacidades e restrições de plataforma

| Grupo | Fatores documentados | Relação com o projeto |
|---|---|---|
| Plataforma | Desktop em Python, SUMO/TraCI, teclado/mouse, Visual/SUMO-GUI, Headless. | PF01–PF03 e PP01–PP07. |
| Capacidades | Cenários, parâmetros, estratégias, seed, validação, confirmação, processamento, histórico, métricas/gráfico. | T01–T08, com T07 apenas parcialmente apoiada pela V0. |
| Restrições | Dependências técnicas, terminologia, muitos parâmetros, tempo variável, janela externa, histórico crescente, sem comparação automática. | O02/O03/O05/O06/O10. |
| Contexto | P01/P02 hipotéticas, desktop/laboratório e equipe acadêmica; perfis e ambiente profissional ainda não validados. | E3 e H01. |

### Princípios gerais da E8

| ID | Princípio | Principal rastreabilidade | Estado |
|---|---|---|---|
| PG01 | Identidade e contexto da execução visíveis. | T01–T06, O01/O08/O09. | Preservar/refinar. |
| PG02 | Terminologia técnica com explicação contextual. | H01, O02, I01 Q15, I02 E17. | Proposta V1. |
| PG03 | Separação de parâmetros principais e avançados. | PP02, O03. | Preservar/refinar. |
| PG04 | Prevenção/recuperação de erros. | PP03, O04/O05. | Preservar/refinar. |
| PG05 | Estado principal mais claro que logs. | PP04, O06/O07. | Proposta V1. |
| PG06 | Métricas com síntese e acesso a detalhes. | PP07, O09, H03. | Proposta V1. |
| PG07 | Diferenciar consulta individual e comparação. | PP06/PP07, T07, O10. | Comparação automática não implementada. |
| PG08 | Legibilidade, rótulos e sinais não dependentes somente de cor. | Qualidade de uso/princípios de IHC. | Diretriz futura. |

Referências usadas em E8: ISO 9241-11, ISO 9241-210, Nielsen, Barbosa e Silva e princípios de acessibilidade WCAG 2.2 **adaptados**; não existe alegação de certificação ou conformidade integral.

### Metas qualitativas e quantitativas

| Objetivo/tarefa | Metas qualitativas | Metas quantitativas definidas na E8 | Verificação na E14 (N = 2) |
|---|---|---|---|
| T01–T03: preparar | MQ01/MQ02 | **MU01:** preparar sem ajuda, 100%; **MU03:** mediana ≤ 5 min. | UT01: **2/2** sem ajuda; tempos 02:42 e 02:14; mediana **02:28**. MU01/MU03 atingidas nesta amostra. |
| T02/T04: validar | MQ03 | **MU02:** 100% identificam a recuperação da condição inválida. | UT02: U01 concluiu com ajuda e U02 sem ajuda; **1/2 autônomo**, meta de autonomia não atingida. |
| T05: acompanhar | MQ04 | **MU04:** 100% reconhecem estado e controlador. | UT03: **2/2** corretos sob apresentação estável do estado Executando; duração das transições automáticas originais não avaliada. |
| T06: localizar/consultar | MQ05 | **MU05:** 100% identificam execução e contexto; **MU06:** mediana de localização ≤ 3 min. | UT04: acerto final **2/2**, mas U02 precisou de ajuda. Tempo de localização de U02 **02:58**; U01 tem só duração total **01:34**. Limite compatível; **mediana exata não reconstruível**. |
| T07: comparar | MQ06 | **MU08:** 100% compreendem consulta individual e comparação externa. | UT05: U02 conclusão integral; U01 parcial e entendimento mais completo no pós-teste. **2/2** relataram compreensão final, **1/2** concluiu integralmente a tarefa. |
| PF01–PF03: experiência | MQ07 e clareza geral | **MU07:** mediana de facilidade pós-tarefa ≥ 4/5. | Mediana global **4/5** (12 notas). Por tarefa, UT02, UT04, UT05 e UT06 ficaram abaixo de 4. |

**Evolução da avaliação:** a E12 definiu previamente tarefas e critérios; a E13 inspecionou problemas heurísticos; e a E14 observou dois participantes consentidos segundo os relatos dos moderadores, com registros de desempenho e satisfação. Na amostra, 100% equivale a **2/2**, sem capacidade de generalização estatística. A priorização da E8 (35%/20%/25%/20%) indica **peso de design**, não desempenho observado. A equipe informou dispensa docente de gravação; os comprovantes de consentimento aplicáveis devem permanecer em arquivo privado.

---

## 10. Registro de mudanças e refinamentos

| Data | Registro | Origem | Consequência |
|---|---|---|---|
| 20/10/2026 | A GUI funcional foi formalizada como V0, com PF01–PF03, PP01–PP07 e walkthrough formativo. | E6. | Base para decisões V0→V1. |
| 20–21/10/2026 | Corrigida a representação de PP06/PP07 e da comparação manual. | Capturas e revisão da E6. | T07 deixou de ser indevidamente descrita como comparação automática. |
| 20/10/2026 | E7 documentou I01 e I02 como **instrumentos planejados**, não resultados empíricos. | E7. | H01–H03 permanecem abertas. |
| 21/10/2026 | E8 relacionou plataforma, princípios PG01–PG08 e metas MQ01–MQ07/MU01–MU08 aos artefatos anteriores. | Slides Processos — Partes 1 e 2; E8. | Critérios de projeto/avaliação futura para E9–E14. |
| 21/10/2026 | Reconciliação documental das versões do repositório: final da E7 e matriz recuperados/revisados; E8 concluída. | Histórico de commits, conteúdo do repositório e materiais de aula. | Documentação consolidada, **sem afirmar testes ou alterações da GUI**. |
| 17/11/2026 | E9 registrou CI01/CI02, mapas de objetivos OBJ01–OBJ09 e esquema conceitual de signos. | `docs/09_modelo_conceitual.md`. | Base para os modelos de diálogo e a coerência dos signos. |
| 17/11/2026 | E10 documentou M01 de Gabriel e M02 de João, com alternativas e rupturas. | `docs/10_molic.md`. | Modelos que orientaram a prototipação no Figma; verificação final da notação e legibilidade do M01 registrada no checklist da entrega. |
| 18/11/2026 | E11 documentou o protótipo Figma de M01/M02 com estados demonstrativos. | `docs/11_figma.md`. | Objeto das avaliações E13/E14; não equivale à execução SUMO. |
| 18/11/2026 | E12 concluiu o plano DECIDE, com QA01–QA10, MU01–MU08, UT01–UT06, instrumentos e ética. | `docs/12_planejamento_avaliacao.md`. | Protocolo e metas utilizados nas avaliações. |
| 18/11/2026 | E13 consolidou 12 achados individuais em sete problemas distintos HC01–HC07. | `docs/13_avaliacao_heuristica.md`. | Plano de recomendações heurísticas, com HC02/HC06 em grau 3; sem implementação de correções comprovada. |
| 18–19/11/2026 | E14 documentou duas observações padronizadas no Figma, com U01/Gabriel e U02/João. | `docs/14_observacao_usuario.md`. | 8/12 sucessos totais, 9 erros, 3 ajudas, mediana 4/5, seis achados AU01–AU06 e análise MU01–MU08. |
| 19/11/2026 | Revisão final de consistência: E10 registra a conferência do M01; E11 explicita limites da avaliação de acessibilidade; E12 e o instrumento de consentimento distinguem EX01/EX02 da exploração preliminar e U01/U02 da observação padronizada; E14 tem a conclusão individual harmonizada com a consolidação. | `docs/10_molic.md`, `docs/11_figma.md`, `docs/12_planejamento_avaliacao.md`, `docs/14_observacao_usuario.md` e `instrumentos/termo_consentimento_modelo.md`. | Os três assets provisórios foram excluídos da branch `main`; as verificações administrativas e externas continuam discriminadas no checklist final. |

---

## 11. Situação documental das Entregas 9–14

| Entrega | Artefatos e evidências no repositório | Situação |
|---|---|---|
| **E9** — Modelo conceitual | CI01/CI02, objetivos OBJ01–OBJ09, mapas individuais e consolidado, esquema de signos. | **Concluída.** |
| **E10** — MoLIC | M01/Gabriel e M02/João, com caminhos, alternativas, rupturas e recuperação. | **Concluída.** Modelos documentados e verificações finais de notação e legibilidade registradas. |
| **E11** — Figma | Protótipo navegável dos fluxos M01/M02 e seus estados de erro, sucesso e consulta. | **Concluída.** Resultados são demonstrativos e os achados da E13 não foram declarados como corrigidos. |
| **E12** — DECIDE | Planejamento, participantes, critérios, protocolos e tarefas UT01–UT06. | **Concluída.** |
| **E13** — Heurística | Inspeções A01/A02, dez heurísticas, 12 achados individuais consolidados em HC01–HC07. | **Concluída.** Correções recomendadas permanecem como propostas. |
| **E14** — Observação de usuários | Sessões U01 e U02, pré/pós-testes, 12 tentativas, comparação MU01–MU08, AU01–AU06, relação com HC01–HC07 e conclusão da equipe. | **Relatório concluído.** Resultados e recomendações consolidados; conferência e guarda privada dos registros de consentimento aplicáveis permanecem sob responsabilidade da equipe. |

**Situação geral:** o conjunto de 14 entregas foi produzido. Permanecem diferenças entre **relatório concluído**, **meta de usabilidade atingida** e **melhoria implementada**; nenhuma das últimas duas decorre automaticamente da primeira. Não há decisão de incorporar comparação automática, login, CRUD ou filtros avançados como requisitos obrigatórios. Novas funcionalidades dependerão de objetivo e evidência rastreáveis.

**Fechamento documental:** as Entregas 1–14 foram concluídas e consolidadas no repositório. A E10 registra a conferência da notação e legibilidade dos diagramas MoLIC; a E11 documenta os limites da avaliação de acessibilidade; a E12 e o instrumento de consentimento distinguem EX01/EX02 da exploração preliminar e U01/U02 das sessões padronizadas; e a E14 apresenta os resultados individuais e consolidados das observações.

Os três arquivos gráficos provisórios anteriormente identificados foram excluídos, preservando as evidências reais utilizadas nas entregas. O [Checklist final](CHECKLIST_FINAL.md) registra as verificações de organização, apresentação visual, acesso aos protótipos e requisitos acadêmicos de submissão assinaladas como concluídas pela equipe.

**Situação final:** o conjunto documental da disciplina está concluído. Os problemas HC01–HC07 e AU01–AU06 permanecem como recomendações de melhoria, enquanto H01–H03 mantêm os estados de investigação registrados nesta matriz. A conclusão das entregas não pressupõe implementação de todas as recomendações nem validação estatística das hipóteses.

## 12. Rastreabilidade consolidada dos problemas de usabilidade

### E13 — Inspeção heurística

| ID | Problema consolidado | Severidade E13 | Relação com a E14 | Situação da correção |
|---|---|---:|---|---|
| **HC01** | R2-003 não apresenta rótulo de status explícito antes da abertura. | 1 | UT06: ambos perceberam indisponibilidade **após abrir**; não foi observado o reconhecimento prévio do status. AU06 é dificuldade distinta de retorno. | **Recomendada; não verificada como implementada.** |
| **HC02** | Identificador R2-001 associa controladores diferentes em conclusões alternativas e histórico. | 3 | AU03 reforça importância da identidade, mas os caminhos de conclusão inconsistentes não foram exercitados diretamente. | **Prioritária; não verificada como implementada.** |
| **HC03** | Falha de processamento não oferece diagnóstico suficientemente orientado. | 2 | UT02 tratou de seed ausente, não de falha F04E; problema não exercitado. | **Recomendada; não verificada como implementada.** |
| **HC04** | Gráficos carecem de escala numérica. | 2 | U01 mencionou escala no pós-teste; sem medição isolada de seu efeito. | **Recomendada; não verificada como implementada.** |
| **HC05** | Parâmetro Projeção regional sem ajuda contextual. | 1 | Configuração avançada não exercitada nos relatos de U01/U02. | **Recomendada; não verificada como implementada.** |
| **HC06** | Ação de abrir histórico ausente em conclusões alternativas. | 3 | Conclusões Tempo fixo Visual e Max Pressure Headless não exercitadas na observação. | **Prioritária; não verificada como implementada.** |
| **HC07** | Throughput sem definição contextual suficiente. | 2 | U01 solicitou explicações gerais de métricas, sem mencionar especificamente Throughput. | **Recomendada; não verificada como implementada.** |

### E14 — Observação de usuários

| ID | Problema/oportunidade | Origem | Recorrência na amostra | Decisão de projeto proposta |
|---|---|---|---|---|
| **AU01** | Diferenciar Visual e Headless. | UT01, U01. | 1/2 | Clarificar rótulos e preservar conferência no resumo. |
| **AU02** | Identificar causa de validação inválida (seed). | UT02, U01 e U02; AU07 provisório agrupado aqui. | 2/2 | Vincular a mensagem ao campo e à ação corretiva; U01 exigiu ajuda. |
| **AU03** | Distinguir registros de execução no histórico. | UT04, U01 e U02. | 2/2 | Destacar identificador e condições; U02 exigiu ajuda. |
| **AU04** | Conferir contexto antes de comparar resultados. | UT05, U01 e U02, com dificuldades distintas. | 2/2 | Explicar condições experimentais e comparação externa. |
| **AU05** | Acrescentar escala e ajuda contextual das métricas. | Pós-teste U01. | 1/2 | Incluir escala/definições e testar novamente. |
| **AU06** | Tornar o retorno após indisponibilidade mais evidente. | UT06, U02. | 1/2 | Destacar Voltar ao histórico e manter posição previsível. |

**Prioridade observacional:** AU02 e AU03, depois AU04/AU05 e AU06; AU01 tem menor gravidade no registro por ter sido recuperado espontaneamente. **Prioridade heurística crítica:** HC02 e HC06 (severidade 3). Problemas de inspeção não exercitados na E14 permanecem no plano de melhorias.

## 13. Síntese da avaliação observacional e suas limitações

| Indicador | U01 | U02 | Total/conclusão |
|---|---:|---:|---|
| Sucessos totais em UT01–UT06 | 4/6 | 4/6 | **8/12 (66,7%)** |
| Sucessos parciais | 2/6 | 2/6 | **4/12 (33,3%)** |
| Falhas finais | 0 | 0 | **0/12** |
| Erros | 4 | 5 | **9** |
| Ajudas diretas | 1 | 2 | **3** |
| Mediana de facilidade das seis notas | 4/5 | 4/5 | **4/5** (12 notas) |

As metas foram avaliadas com seus limites: **MU01/MU03** atingidas na amostra; **MU04** atingida somente na apresentação estável; **MU02** não atingida em autonomia; **MU05** com acerto final de 2/2 e ajuda para U02; **MU06** sem mediana exata de localização; **MU07** atingida apenas na agregação global; **MU08** com compreensão final 2/2, embora só U02 tenha concluído integralmente UT05 durante a tentativa.

A coleta refere-se a **dois participantes *proxy*** e a um **Figma demonstrativo**, sem execução real de SUMO. A revisão imutável exata do Figma não foi identificada, a UT03 foi apresentada em estado estável e o tempo exclusivo de localização de U01 não foi registrado. O relatório foi redigido a partir dos registros fornecidos pelos moderadores, sem verificação independente dos originais. A equipe relatou dispensa docente de gravação; os comprovantes privados de consentimento aplicáveis devem ser preservados separadamente dos registros públicos.

O trabalho de IHC documentado **não comprova** que as correções propostas já foram desenvolvidas na GUI V0, que o Figma oferece comparação automática, ou que as hipóteses H01–H03 foram validadas para a população profissional. Os resultados oferecem evidências formativas para uma iteração posterior.

---

## Como usar

- Manter os IDs existentes estáveis; novos artefatos recebem prefixos próprios.
- Usar `PENDENTE` apenas para trabalho realmente ausente; preservar limitações documentais sem convertê-las em resultados inventados.
- Diferenciar **implementado na V0**, **proposto para V1**, **instrumento planejado** e **resultado observado**.
- Registrar correções em vez de apagar silenciosamente decisões anteriores.
- Atualizar a matriz quando novas evidências alterarem H01–H03, as decisões de interação ou o estado das correções.
- Conservar em local privado os registros pessoais e comprovantes de consentimento aplicáveis; não publicar nomes de participantes da E14.

## Convenção de identificadores adotada

| Prefixo | Artefato |
|---|---|
| H | Hipótese ou lacuna de investigação |
| P | Persona/proto-persona |
| C | Cenário de problema (E4); concorrentes da E2 sempre identificados pelo nome ou qualificação E2 |
| T | Tarefa do usuário |
| PF / PP | Fluxo / estado da V0 documentado na E6 |
| W / O | Tarefa / observação do walkthrough formativo da E6 |
| I / Q / E | Instrumento / pergunta do questionário / pergunta da entrevista da E7 |
| UQ / UE | Eventual participante anonimizado do questionário / entrevista; **nenhum existente até E8** |
| PG | Princípio geral do projeto, E8 |
| MQ / MU | Meta qualitativa / meta quantitativa de usabilidade, E8 |
| CI / OBJ | Cenário de interação / objetivo do modelo conceitual, E9 |
| M / F | Diagrama MoLIC, E10 / tela ou estado do Figma, E11 |
| QA | Questão de avaliação definida no DECIDE, E12 |
| UT | Tarefa padronizada de observação, E12/E14 |
| A01 / A02 | Avaliadores Gabriel / João na inspeção heurística, E13 |
| V / A02-V | Achados individuais de Gabriel / João na E13 |
| HC | Problema heurístico consolidado, E13 |
| EX01 / EX02 | Participantes anonimizados da exploração preliminar da aplicação funcional R3, em 15/11/2026 (E12); não compõem a amostra padronizada da E14 |
| U01 / U02 | Participantes anonimizados das sessões padronizadas do Figma na E14, em 18–19/11/2026; identificadores distintos dos da exploração EX01/EX02 |
| AU | Achado da observação de usuários, E14; AU07 provisório agrupado em AU02 |
| L | Condição/limitação de preparação ou observação, quando identificada |
| R | Linha da matriz de rastreabilidade |

# Matriz de rastreabilidade de IHC

Esta matriz registra como as decisões do projeto evoluíram desde a contribuição técnica do TCC até os artefatos de IHC. **Não apaga hipóteses antigas ao incorporar uma nova entrega**. Sempre que não houver avaliação ou evidência suficiente, a condição permanece indicada.

A interface já fazia parte do escopo previsto do TCC e existe como **protótipo desktop funcional V0**. A E6 documentou seus estados reais, realizou um walkthrough formativo e registrou propostas V0→V1. A E7 elaborou instrumentos de coleta ainda **não aplicados**. A E8 especificou capacidades/restrições, princípios e **metas futuras de usabilidade**, ainda não medidas.

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

| ID | Hipótese | Evidências acumuladas sem validação empírica | Investigação prevista | Estado após E8 | Implicação |
|---|---|---|---|---|---|
| H01 | Pesquisadores/analistas de mobilidade representam o usuário prioritário. | E2 — ferramentas profissionais; E3 — P01/P02; E6 — identificação de termos técnicos. | I01 Q01–Q04/Q15; I02 E01/E02/E17; avaliações posteriores. | **Aberta.** | Revisar personas, vocabulário e ajuda se dados indicarem. |
| H02 | Organização cenário → configuração → execução/acompanhamento → análise facilita os experimentos. | E3–E5 — jornada/tarefas; E6 — PF01–PF03, O01–O07. | I01 Q05–Q09; I02 E03–E08; MU01–MU04 na avaliação. | **Aberta.** | Manter organização como hipótese de design e verificar eficácia/eficiência. |
| H03 | Apresentação consolidada/comparativa de métricas facilita interpretação. | E6 — histórico, análise individual e gráfico; O09/O10 expõem custo da comparação externa. | I01 Q10–Q14; I02 E09–E16; MU05–MU08 quando pertinentes. | **Aberta.** | Apoio comparativo automático segue possibilidade de V1, não requisito validado. |

Nenhuma das hipóteses foi sustentada, refutada ou validada por participantes na E7: I01/I02 **não foram aplicados**. Na E8 foram definidas metas para testes futuros, não resultados.

---

## 3. Rastreabilidade entre contribuição técnica, necessidades e artefatos

`PENDENTE` nas colunas E9–E14 significa que a entrega ainda não foi produzida; não corresponde a uma falha da V0.

| ID | Capacidade técnica | Necessidade | Persona | Cenário | Tarefa | E5: modelo | E6: fluxo/estado | E7: investigação | E9: cenário/signos | E10 | E11 | E13 | E14 | Decisão vigente |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R01 | Cenários/infraestruturas. | Definir local da simulação. | P01 | C01 | T01 | Sem modelo individual dedicado. | PF01/PP01 | I01 Q05; I02 E03/E04 | PENDENTE | PENDENTE | PENDENTE | PENDENTE | PENDENTE | O01; PG01 — manter separação e contexto. |
| R02 | Parametrização. | Definir condições corretas. | P01 | C01 | T02 | HTA T02 | PF01/PP02/PP03 | I01 Q05–Q07; I02 E03–E05 | PENDENTE | PENDENTE | PENDENTE | PENDENTE | PENDENTE | O02/O03/O05; PG02–PG04. |
| R03 | Escolha de estratégia. | Identificar controlador ativo. | P01 | C01 | T03 | GOMS T03 | PF01/PP02 | I01 Q05/Q06; I02 E04/E05 | PENDENTE | PENDENTE | PENDENTE | PENDENTE | PENDENTE | O02; PG01/PG02. |
| R04 | Execução de experimentos. | Iniciar e reconhecer processamento. | P01 | C01 | T04/T05 | CTT T04/T05 | PF02/PP03–PP05 | I01 Q08/Q09; I02 E06–E08 | PENDENTE | PENDENTE | PENDENTE | PENDENTE | PENDENTE | O04–O07; PG04/PG05. |
| R05 | Métricas e gráficos. | Consultar uma execução. | P01/P02 | C02 | T06 | GOMS T06 | PF03/PP06/PP07 | I01 Q10/Q11; I02 E09/E10/E13 | PENDENTE | PENDENTE | PENDENTE | PENDENTE | PENDENTE | O08/O09; PG01/PG06. |
| R06 | Comparação científica de controladores. | Comparar condições equivalentes. | P01/P02 | C02 | T07 | HTA T07; CTT T07/T08 | PF03/PP06/PP07 + trabalho externo | I01 Q12/Q13; I02 E11–E13 | PENDENTE | PENDENTE | PENDENTE | PENDENTE | PENDENTE | O10; PG07 — comparação automática ainda não existe. |
| R07 | Síntese de análise. | Interpretar/comunicar resultados. | P01/P02 | C02 | T08 | CTT T07/T08 | PF03/PP07 + síntese externa | I01 Q10–Q17; I02 E14–E20 | PENDENTE | PENDENTE | PENDENTE | PENDENTE | PENDENTE | O09/O10; PG06/PG07. |

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

A E8 transformou o conteúdo anterior em especificação de plataforma, princípios de design e **metas de uso**. Valores de MU são **alvos planejados**, não resultados de participantes.

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

| Objetivo/tarefa | Metas qualitativas | Metas quantitativas planejadas | Evidência futura |
|---|---|---|---|
| T01–T03: preparar | MQ01/MQ02 | MU01: conclusão correta por todos os participantes observados; MU03: mediana ≤ 5 min. | E12/E14, registro de sucesso, ajuda e tempo. |
| T02/T04: validar | MQ03 | MU02: identificar e corrigir condição inválida por todos os participantes avaliados. | E12/E14, cenário controlado de erro. |
| T05: acompanhar | MQ04 | MU04: reconhecer estado e estratégia por todos os participantes. | E12/E14, pergunta objetiva em etapa definida. |
| T06: localizar/consultar | MQ05 | MU05: identificar contexto corretamente por todos; MU06: mediana de localização ≤ 3 min. | E12/E14, histórico padronizado. |
| T07: comparar | MQ06 | MU08: entender o limite de comparação da versão avaliada por todos. | E12/E14; comparação manual enquanto não houver V1 implementada. |
| PF01–PF03: experiência | MQ07 e clareza geral | MU07: mediana de facilidade pós-tarefa ≥ 4/5. | E12/E14, escala de satisfação. |

**Medição futura:** E12 definirá tarefas e critérios antes da coleta, E13 inspecionará problemas heurísticos e E14 observará participantes com consentimento. Para amostra de dois participantes, 100% equivale a 2/2 e não autoriza generalização estatística. A priorização de grupos de metas na E8 (35%/20%/25%/20%) indica **peso de design**, não desempenho observado.

---

## 10. Registro de mudanças e refinamentos

| Data | Registro | Origem | Consequência |
|---|---|---|---|
| 20/10/2026 | A GUI funcional foi formalizada como V0, com PF01–PF03, PP01–PP07 e walkthrough formativo. | E6. | Base para decisões V0→V1. |
| 20–21/10/2026 | Corrigida a representação de PP06/PP07 e da comparação manual. | Capturas e revisão da E6. | T07 deixou de ser indevidamente descrita como comparação automática. |
| 20/10/2026 | E7 documentou I01 e I02 como **instrumentos planejados**, não resultados empíricos. | E7. | H01–H03 permanecem abertas. |
| 21/10/2026 | E8 relacionou plataforma, princípios PG01–PG08 e metas MQ01–MQ07/MU01–MU08 aos artefatos anteriores. | Slides Processos — Partes 1 e 2; E8. | Critérios de projeto/avaliação futura para E9–E14. |
| 21/10/2026 | Reconciliação documental das versões do repositório: final da E7 e matriz recuperados/revisados; E8 concluída. | Histórico de commits, conteúdo do repositório e materiais de aula. | Documentação consolidada, **sem afirmar testes ou alterações da GUI**. |

---

## 11. Continuidade para E9–E14

| Entrega | O que deverá utilizar desta matriz | Estado |
|---|---|---|
| E9 — Modelo conceitual | H01–H03, P01/P02, C01/C02, T01–T08, PG01–PG08, MQ. | PENDENTE. |
| E10 — MoLIC | Cenários de interação/signos resultantes da E9, rupturas de PP03/PP04 e caminhos PP06/PP07. | PENDENTE. |
| E11 — Figma | Conversas MoLIC e diretrizes E8; distinguir V1 proposta de V0 existente. | PENDENTE. |
| E12 — DECIDE | MQ/MU, critérios de sucesso, perfis, protocolo, ética e piloto. | PENDENTE. |
| E13 — Heurística | Versão avaliada, 10 heurísticas, prints e severidade. | PENDENTE. |
| E14 — Observação de usuários | Participantes consentidos, tarefas, sucesso, tempo, erros, ajuda e satisfação. | PENDENTE. |

Não há decisão de incorporar comparação automática, login, CRUD ou filtros avançados como requisito obrigatório. Qualquer nova funcionalidade deverá ser justificada por evidência, objetivos e avaliação.

---

## Como usar

- Manter os IDs existentes estáveis; novos artefatos recebem prefixos próprios.
- Usar `PENDENTE` quando o trabalho ainda não existe, e não preencher lacunas inventando achados.
- Diferenciar **implementado na V0**, **proposto para V1**, **instrumento planejado** e **resultado observado**.
- Registrar correções em vez de apagar silenciosamente decisões anteriores.
- Atualizar a matriz quando novas evidências reais alterarem H01–H03 ou decisões de interação.

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
| M / F | Diagrama MoLIC / tela ou fluxo do Figma (futuro) |
| UT | Tarefa de avaliação por observação (futuro) |
| R | Linha da matriz de rastreabilidade |

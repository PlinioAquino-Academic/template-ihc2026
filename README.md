# Projeto de Interação Humano-Computador (IHC) - Equipe 24

## Princípio do projeto da disciplina

A disciplina utiliza **preferencialmente o tema do TCC em andamento** como domínio para exercitar os métodos de Interação Humano-Computador.

- Se o TCC **já prevê interface**, ela pode ser objeto principal das atividades de IHC.
- Se o TCC **não prevê interface**, a equipe precisa delimitar um uso humano plausível e investigar quem se beneficiaria, o que precisaria fazer e em qual contexto.
- Uma interface concebida na disciplina não se torna automaticamente obrigação de outro TCC; sua incorporação depende do escopo e das decisões da equipe/orientador.

Leia também o [Guia para definir o escopo de IHC a partir do tema do TCC](GUIA_ESCOPO_IHC.md).

**Neste projeto, aplica-se o primeiro caso:** a interface desktop **já fazia parte do escopo previsto do TCC**, existe funcionalmente e foi utilizada como protótipo digital V0 na Entrega 6. A disciplina serve para compreender, modelar e aperfeiçoar sua interação; não se trata de uma extensão fictícia sem relação com a plataforma experimental.

## Identificação

**Título do projeto de IHC:** Interface para Configuração, Execução e Análise de Simulações de Controle Semafórico Inteligente  
**TCC/projeto de origem:** Algoritmo Híbrido de Controle Semafórico Baseado em Max Pressure e Lógica Actuated em Ambiente de Simulação  
**Orientador(a):** Ricardo de Carvalho Destro  
**Disciplina:** Interação Humano-Computador — CC8122  
**Instituição:** Centro Universitário FEI  
**Semestre:** 2026/2

### Equipe

| Nome completo | Matrícula | GitHub | Responsabilidade principal |
|---|---:|---|---|
| Gabriel Koiama de Rocha Lira | 22.125.067-3 | @koiamagabriel | Desenvolvimento do projeto de IHC; I01 na E7 e contribuições à E8. |
| João Pedro Lopes Santana Villas Bôas | 22.125.065-7 | @JPLopes05 | Desenvolvimento do projeto de IHC; I02 na E7 e contribuições à E8. |

A E8 constitui uma **entrega consolidada por equipe**. A divisão de commits entre integrantes não corresponde a documentos acadêmicos separados.

## Relação entre TCC e projeto de IHC

| Item | Descrição |
|---|---|
| Tema central do TCC | Algoritmo híbrido de controle semafórico inteligente baseado em Max Pressure e lógica actuated. |
| Resultado técnico esperado | Controlador implementado em Python e integrado ao SUMO via TraCI, com avaliação experimental e interface para configuração, execução, acompanhamento e análise de simulações. |
| O TCC já previa interface? | **Sim.** A interface já era considerada antes da disciplina e existe como GUI desktop funcional. Nas etapas iniciais do TCC1 ela ainda não estava formalmente detalhada. |
| Contribuição técnica | Seleção dinâmica de prioridades semafóricas e controle do tempo de verde a partir do estado da rede, comparado a estratégias de referência. |
| Capacidade útil a pessoas | Definir cenários e condições, executar experimentos, acompanhar a simulação, recuperar registros e interpretar resultados experimentais. |
| Usuário prioritário adotado em IHC | Pesquisador ou analista de mobilidade urbana — **hipótese H01, ainda não validada**. |
| Objetivo principal do usuário | Preparar, executar e analisar experimentos com diferentes estratégias de controle sob condições adequadas. |
| Interface/recorte da disciplina | Seleção, configuração, validação, execução/acompanhamento, histórico e análise individual dos resultados. |
| Relação com TCC | A interface integra o escopo previsto do TCC. E6 a formalizou como V0, observou seu uso em walkthrough e registrou propostas de V1. |

> O funcionamento técnico documentado não equivale a validação definitiva de usabilidade. O mérito técnico do algoritmo e a qualidade de uso da interface são avaliados por critérios diferentes.

## Resumo do projeto pela perspectiva do usuário

Um **pesquisador ou analista de mobilidade urbana** precisa investigar estratégias de controle semafórico por meio de experimentos comparáveis. Para isso, deve selecionar a malha, preparar parâmetros, escolher estratégia e seed, validar condições, executar e acompanhar o processamento, localizar resultados e interpretá-los.

O TCC emprega **Python, SUMO, TraCI, detectores E1, Max Pressure, lógica actuated e controlador híbrido Max Pressure + actuated**, além de estratégias de referência como Fixed-Time e Max Pressure. Diferentes cenários e seeds sustentam sua metodologia experimental.

Na interface V0, o fluxo principal efetivamente documentado é:

**selecionar cenário → configurar parâmetros/controlador/seed/modo → validar/confirmar → executar e acompanhar → localizar execução no histórico → consultar resultados individuais → comparar manualmente, fora da aplicação, quando necessário**.

### Entrega 6 — Protótipo digital V0

A E6 adotou a GUI funcional pré-existente no contexto da atividade de prototipação formativa e a organizou em três fluxos:

- **PF01 — Preparar experimento**;
- **PF02 — Validar, executar e acompanhar**;
- **PF03 — Localizar e analisar resultados**.

Os estados documentados são:

- **PP01 — Catálogo e seleção do cenário**;
- **PP02 — Configuração da simulação**, incluindo modo e parâmetros avançados;
- **PP03 — Validação e confirmação pré-execução**;
- **PP04 — Inicialização e feedback**;
- **PP05 — Execução no modo Visual/SUMO-GUI**;
- **PP06 — Histórico e seleção de uma execução**;
- **PP07 — Análise individual dos resultados e gráficos**.

São **12 capturas reais** em [`assets/06_prototipos/`](assets/06_prototipos/). O walkthrough formativo W01–W04 gerou O01–O10 e propostas V0→V1, entre elas:

- preservar separação cenário/configuração e área avançada;
- oferecer ajuda contextual para termos especializados;
- manter validação e melhorar mensagens de recuperação de erros;
- destacar estado principal, mantendo logs como detalhe;
- preservar vínculo cenário–controlador–seed–execução–resultado;
- melhorar hierarquia da apresentação das métricas;
- investigar, futuramente, apoio direto à comparação de execuções.

**A V0 não possui comparação automática entre duas execuções.** PP06 lista/seleciona execuções; PP07 exibe a execução selecionada. T07 é apoiada parcialmente e a comparação entre A/B é manual/externa. Uma futura visualização lado a lado não deve ser descrita como implementada.

### Entrega 7 — Identificação de necessidades, instrumentos e ética

Foram definidos dois instrumentos completos e complementares:

- **I01 — Questionário exploratório** sobre atividades de simulação e análise, desenvolvido por Gabriel. Inclui consentimento Q00, perguntas Q01–Q17, protocolo e plano de tabulação/análise.
- **I02 — Entrevista semiestruturada** sobre processos técnicos e interpretação de resultados, desenvolvida por João. Inclui E01–E20, aprofundamentos, protocolo e análise temática planejada.

Ambos consideram recrutamento de público especializado, eventual uso de participantes *proxy*, voluntariedade, consentimento, privacidade, armazenamento e anonimização.

**Os instrumentos foram elaborados, mas não aplicados na Entrega 7.** Não existem respostas empíricas, entrevistas conduzidas, métricas de participantes ou validação de H01–H03 decorrentes deles.

### Entrega 8 — Ciclo de vida e engenharia de usabilidade

A E8 foi concluída documentalmente como **solução consolidada pela equipe**, retomando o contexto, as tarefas e os problemas observados:

- descreveu software, hardware, capacidades e restrições da plataforma e suas consequências para a interação;
- relacionou princípios gerais do projeto ao contexto de uso e a referências como ISO 9241-11, ISO 9241-210, Nielsen e materiais da disciplina;
- definiu diretrizes **PG01–PG08**, relacionadas a contexto experimental, linguagem, parâmetros avançados, erros, estado, resultados, comparação e legibilidade;
- definiu metas qualitativas **MQ01–MQ07** e quantitativas **MU01–MU08** para avaliações futuras;
- registrou o ciclo de aperfeiçoamento de E9 a E14, incluindo planejamento, inspeção e observação.

As metas de E8 são **alvos planejados, não resultados medidos**. Em particular, não se confundem tempo de tarefa humana e tempo de processamento do simulador; não significam que recursos de V1 já tenham sido implementados e não validam H01–H03.

## Por que pensar em interface mesmo em TCCs técnicos?

Algoritmos, simulações, APIs e análises podem possuir valor técnico independentemente da interface. Porém, sua utilização e interpretação envolvem pessoas que selecionam dados, configuram parâmetros, acompanham processamento, examinam falhas e interpretam resultados. IHC investiga essas tarefas e a relação das pessoas com uma solução interativa.

Entre padrões possíveis estão configuração, visualização, histórico, relatórios, comparação, filtros, alertas e ajuda contextual. **Nenhum desses recursos é obrigatório por si só.** Cada um deve ser sustentado por um objetivo de usuário e por evidência apropriada.

Neste TCC a GUI já era planejada e foi construída. A E6 documentou o que realmente existe; a E7 preparou a investigação das necessidades e a E8 registrou princípios/metas para orientar sua evolução. Isso **não autoriza inventar** login, CRUD, comparador automático ou outros recursos não justificados.

## Relação com apresentação e potencial de aplicação

A disciplina ajuda a comunicar o projeto em termos de **problema humano → contribuição computacional → forma de uso → benefício potencial** — inclusive em apresentações como a INOVA.

No caso concreto:

**problema de controle semafórico → algoritmo híbrido no SUMO → GUI de simulação e análise → apoio à experimentação e interpretação de resultados**.

É importante distinguir resultados reais do algoritmo, funcionalidades existentes na V0, hipóteses de usuário e propostas de V1. O protótipo funcionar tecnicamente não prova que todos os fluxos sejam fáceis ou satisfatórios, assim como questionários planejados não constituem dados coletados.

## Situação das principais hipóteses

| ID | Hipótese | Situação após E8 |
|---|---|---|
| H01 | Pesquisadores/analistas de mobilidade representam o usuário prioritário. | **Aberta.** P01/P02 são proto-personas, E6 apontou questões de linguagem e E7 produziu instrumentos não aplicados. |
| H02 | O fluxo cenário → configuração → execução/acompanhamento → análise facilita os experimentos. | **Aberta.** A V0 e o walkthrough deram base a melhorias; E8 definiu PG/MQ/MU para avaliações futuras. |
| H03 | Uma apresentação consolidada/comparativa das métricas facilita interpretação. | **Aberta.** A V0 exibe resultados individuais; a comparação permanece manual. Necessidades e alternativas deverão ser investigadas/avaliadas. |

## Como usar este repositório

1. Leia o [Guia de uso e apresentação](GUIA_DE_USO.md).
2. Leia o [Guia de definição de escopo](GUIA_ESCOPO_IHC.md), especialmente se o TCC não previa interface; **não é o caso desta equipe**.
3. Desenvolva as entregas em sequência, reaproveitando decisões anteriores, sem reiniciar o projeto.
4. Identifique autoria individual nas entregas que exigem soluções por integrante.
5. Registre imagens, diagramas e evidências nos diretórios de [`assets/`](assets/README.md).
6. Mantenha a [Matriz de rastreabilidade](RASTREABILIDADE.md) atualizada.
7. Diferencie **[F] fato, [H] hipótese e [?] lacuna** sempre que necessário.
8. Antes de concluir, confira o [Checklist final](CHECKLIST_FINAL.md) e o checklist próprio da entrega.
9. Registre refinamentos, sem apagar o histórico de decisões.
10. Não confunda funcionalidades existentes, propostas de design, metas futuras e resultados empíricos.

## Entregas

| # | Entrega | Quantidade mínima / responsabilidade | Status |
|---:|---|---|---|
| 1 | [Conhecendo o projeto, o usuário e o problema](docs/01_conhecendo_o_problema.md) | 1 solução consolidada por equipe | 🟩 |
| 2 | [Público-alvo e análise de concorrência](docs/02_analise_concorrencia.md) | 1 concorrente/interface por integrante + síntese | 🟩 |
| 3 | [Personas, empatia, contexto e jornada](docs/03_personas_contexto_jornada.md) | 1 persona por integrante + consolidação | 🟩 |
| 4 | [Cenários de análise/problema](docs/04_cenarios_problema.md) | 1 cenário completo por integrante | 🟩 |
| 5 | [Análise de tarefas: HTA, GOMS e CTT](docs/05_analise_tarefas.md) | 1 HTA + 1 GOMS + 1 CTT por integrante | 🟩 |
| 6 | [Prototipação em papel / protótipo digital V0](docs/06_prototipacao_papel.md) | 1 protótipo integrado por equipe e walkthrough formativo | 🟩 |
| 7 | [Coleta de dados e aspectos éticos](docs/07_coleta_dados.md) | Instrumentos individuais distintos; questionário incluído | 🟩 |
| 8 | [Ciclo de vida e engenharia de usabilidade](docs/08_engenharia_usabilidade.md) | 1 solução consolidada por equipe | 🟩 |
| 9 | [Modelo conceitual e design centrado na comunicação](docs/09_modelo_conceitual.md) | Soluções individuais + consolidação de objetivos/signos | ⬜ |
| 10 | [MoLIC](docs/10_molic.md) | 1 diagrama completo por integrante | ⬜ |
| 11 | [Protótipo no Figma](docs/11_figma.md) | 1 protótipo integrado cobrindo fluxos modelados | ⬜ |
| 12 | [Planejamento da avaliação — DECIDE](docs/12_planejamento_avaliacao.md) | 1 plano consolidado por equipe | ⬜ |
| 13 | [Avaliação heurística](docs/13_avaliacao_heuristica.md) | 1 avaliação completa por integrante, 10 heurísticas | ⬜ |
| 14 | [Avaliação por observação de usuários](docs/14_observacao_usuario.md) | Avaliação consolidada; nº de participantes conforme enunciado | ⬜ |

> As orientações específicas e eventuais alterações posteriores do docente para a turma prevalecem sobre a descrição resumida do repositório.

## Visão de continuidade

A cadeia de evidências do projeto é:

**TCC → usuários/stakeholders → hipóteses H01–H03 → personas P01/P02 → cenários C01/C02 → tarefas T01–T08 → V0/PF01–PF03/PP01–PP07 → walkthrough W01–W04 → observações O01–O10 → decisões V0→V1 → investigação I01/I02 → engenharia de usabilidade PG/MQ/MU → modelo conceitual → MoLIC → Figma → DECIDE → inspeção → observação de usuários → revisões**.

A E6 documentou a sequência real da V0 e corrigiu a interpretação da comparação como **manual e externa**. A E7 transformou lacunas em instrumentos reproduzíveis; sem aplicação, não alterou H01–H03. A E8 definiu capacidades e restrições, princípios e metas de usabilidade a verificar.

A **próxima etapa é E9**, com cenários de interação, design centrado na comunicação, mapa de objetivos e esquema conceitual de signos fundamentados em E1–E8. A E9 não deve inventar funções, nem copiar integralmente decisões futuras para dentro da V0 existente. As escolhas devem permanecer documentadas na rastreabilidade.

## Documentos de apoio

- [Guia de uso e apresentação](GUIA_DE_USO.md)
- [Guia para definir o escopo de IHC a partir do TCC](GUIA_ESCOPO_IHC.md)
- [Matriz de rastreabilidade](RASTREABILIDADE.md)
- [Checklist final](CHECKLIST_FINAL.md)
- [Bibliografia de IHC](BIBLIOGRAFIA.md)
- [Orientações de contribuição no GitHub](CONTRIBUTING.md)
- [Instrumentos reutilizáveis](instrumentos/README.md)

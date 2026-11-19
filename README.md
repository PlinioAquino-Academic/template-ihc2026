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
| Gabriel Koiama de Rocha Lira | 22.125.067-3 | [@koiamagabriel](https://github.com/koiamagabriel) | I01 na E7; CI01 e mapa individual na E9; MoLIC M01 na E10; inspeção A01 na E13; moderação e análise de U01 na E14; participação nas soluções de equipe. |
| João Pedro Lopes Santana Villas Bôas | 22.125.065-7 | [@JPLopes05](https://github.com/JPLopes05) | I02 na E7; CI02 e mapa individual na E9; MoLIC M02 na E10; inspeção A02 na E13; moderação e análise de U02 na E14; participação nas soluções de equipe. |

As entregas consolidadas foram produzidas em equipe, com autoria individual registrada onde o enunciado exigiu. A divisão de commits entre integrantes não representa documentos acadêmicos independentes nem altera a responsabilidade conjunta pelo relatório final.

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

Na E8, essas metas foram **definidas como alvos**, não como medições. A E14 posteriormente as confrontou com resultados de dois participantes. Tempo de interação não é tempo de processamento do SUMO, e uma meta observacional atingida na pequena amostra não valida automaticamente H01–H03 ou implementa recursos de V1.

### Entrega 9 — Cenários de interação e modelo conceitual

A E9 transformou os cenários de problema C01/C02 nos cenários de interação **CI01** (preparar e executar experimentos) e **CI02** (interpretar e comparar resultados). Foram documentados mapas individuais de objetivos — Gabriel/CI01 e João/CI02 —, mapa consolidado **OBJ01–OBJ09** e esquema conceitual de signos: cenário, controlador, seed, modo, validação, estado, registro, métricas e gráficos. O vínculo entre configuração e consulta é o **registro da execução**.

### Entrega 10 — Diagramas MoLIC

Foram documentados dois modelos completos: **M01**, de Gabriel, representa preparação, validação, processamento, conclusão, alternativas e recuperação; **M02**, de João, representa histórico, resultado individual, gráfico e recuperação diante de indisponibilidade. Os diagramas derivam de CI01/CI02 e preservam a comparação de execuções como tarefa **manual e externa**, sem apresentar um comparador inexistente como funcionalidade implementada.

### Entrega 11 — Protótipo navegável no Figma

A E11 integrou os fluxos M01 e M02 em um protótipo navegável com seleção de cenário, configuração, validação da seed, processamento, conclusão, falha, histórico, resultados individuais e gráficos. O Figma representa estados e números **demonstrativos**; não executa SUMO nem produz evidências do desempenho do algoritmo.

- [Figma — fluxo M01, preparação e execução](https://www.figma.com/proto/YJJhBTujdrsjDY113Iefj4/Sem-t%C3%ADtulo?node-id=4-12&scaling=scale-down-width&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=4%3A12).
- [Figma — fluxo M02, histórico e resultados](https://www.figma.com/proto/YJJhBTujdrsjDY113Iefj4/Sem-t%C3%ADtulo?node-id=16-206&scaling=scale-down-width&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=16%3A206).
- [Arquivo editável da equipe](https://www.figma.com/design/YJJhBTujdrsjDY113Iefj4/Sem-t%C3%ADtulo?node-id=4-12).

### Entrega 12 — Planejamento DECIDE

O planejamento de avaliação estabeleceu objetivos, questões QA01–QA10, critérios e metas **MU01–MU08**, tarefas padronizadas **UT01–UT06**, instrumentos de consentimento, pré e pós-teste, planilha de observação e procedimento piloto. A exploração da GUI funcional em **15/11/2026**, no cenário R3, foi registrada separadamente e não substituiu as sessões padronizadas do Figma da E14.

### Entrega 13 — Avaliação heurística

Gabriel (**A01**) e João (**A02**) inspecionaram os fluxos definidos com as **dez heurísticas de Nielsen**. Seus 12 achados individuais foram consolidados, agrupando cinco coincidências, em **sete problemas distintos (HC01–HC07)**. Os de maior severidade (grau 3) são **HC02**, inconsistência de identificação do registro entre conclusões e histórico, e **HC06**, falta de acesso uniforme ao histórico em conclusões alternativas. As recomendações são propostas, não correções já comprovadamente implementadas.

### Entrega 14 — Teste de usabilidade por observação de usuários

A E14 registrou duas sessões de observação no Figma: **U01**, moderada por Gabriel em **18/11/2026**, e **U02**, moderada por João em **19/11/2026**. Ambos os participantes são externos à equipe e foram descritos como perfis aproximados (*proxy*), sem experiência profissional em controle de tráfego. Foram observadas seis tarefas por participante, com sucesso, erros, ajudas, tempos, facilidade percebida e entrevistas pós-teste.

| Indicador | Resultado consolidado da E14 |
|---|---|
| Tentativas de tarefa | 12 (6 por participante) |
| Sucessos totais | **8/12 (66,7%)** |
| Sucessos parciais | **4/12 (33,3%)** |
| Falhas finais | **0/12** |
| Erros e ajudas diretas | **9 erros** e **3 ajudas** |
| Mediana global das notas de facilidade | **4/5** |
| Achados observacionais | **AU01–AU06**, após agrupamento das duplicidades |

As metas **MU01 e MU03** foram atingidas na amostra; **MU04** foi atingida apenas na condição de apresentação estável do estado Executando. **MU02 não atingiu a autonomia prevista para 100% dos participantes**. **MU05** teve acerto final de 2/2, com ajuda em um caso. **MU06** teve limite de 3 minutos compatível com os dados, mas não possui mediana exata de localização porque U01 não separou o instante de abertura do registro. **MU07** atingiu a mediana global, embora quatro tarefas tenham medianas inferiores a 4. **MU08** teve compreensão final relatada por 2/2, mas somente U02 concluiu integralmente a comparação durante a tarefa.

Os achados reforçam a necessidade de melhorar identificação de registros, recuperação de erros, contexto da comparação e clareza das métricas. **A E14 documenta uma avaliação formativa, não validação estatística do público profissional nem certificação de usabilidade.** A equipe informou que o professor dispensou gravação; os registros foram feitos por anotações. Os comprovantes de consentimento aplicáveis são responsabilidade da equipe e não devem ser publicados com dados pessoais.

## Por que pensar em interface mesmo em TCCs técnicos?

Algoritmos, simulações, APIs e análises podem possuir valor técnico independentemente da interface. Porém, sua utilização e interpretação envolvem pessoas que selecionam dados, configuram parâmetros, acompanham processamento, examinam falhas e interpretam resultados. IHC investiga essas tarefas e a relação das pessoas com uma solução interativa.

Entre padrões possíveis estão configuração, visualização, histórico, relatórios, comparação, filtros, alertas e ajuda contextual. **Nenhum desses recursos é obrigatório por si só.** Cada um deve ser sustentado por um objetivo de usuário e por evidência apropriada.

Neste TCC a GUI já era planejada e foi construída. As E6–E14 documentaram a V0, seus objetivos, a proposta navegável e as avaliações. Essa continuidade **não autoriza inventar** login, CRUD, comparador automático ou outros recursos não justificados. Achados da E13/E14 indicam melhorias futuras, sem pressupor sua implementação na GUI funcional.

## Relação com apresentação e potencial de aplicação

A disciplina ajuda a comunicar o projeto em termos de **problema humano → contribuição computacional → forma de uso → benefício potencial** — inclusive em apresentações como a INOVA.

No caso concreto:

**problema de controle semafórico → algoritmo híbrido no SUMO → GUI de simulação e análise → apoio à experimentação e interpretação de resultados**.

É importante distinguir resultados reais do algoritmo, funcionalidades existentes na V0, hipóteses de usuário, propostas para versões futuras e resultados observacionais da E14. O Figma utiliza métricas demonstrativas; os tempos, erros e notas da E14 são medidas de interação relatadas pelos moderadores. A inspeção e as duas observações identificam dificuldades concretas, mas não comprovam conformidade de acessibilidade, implementação das recomendações ou representatividade estatística.

## Situação das principais hipóteses

| ID | Hipótese | Situação após E14 |
|---|---|---|
| **H01** | Pesquisadores/analistas de mobilidade representam o usuário prioritário. | **Aberta.** P01/P02 continuam proto-personas; U01/U02 são participantes *proxy*, não profissionais de tráfego. A E14 não valida o perfil profissional pretendido. |
| **H02** | O fluxo cenário → configuração → execução/acompanhamento → análise facilita os experimentos. | **Parcialmente investigada.** UT01 e UT03 foram concluídas integralmente por 2/2 (estado estável em UT03); recuperação inválida, localização e indisponibilidade apresentaram dificuldades e ajudas. A amostra não permite generalizar a facilidade do fluxo. |
| **H03** | Uma apresentação consolidada/comparativa das métricas facilita a interpretação. | **Parcialmente investigada.** U01 apresentou dificuldade em UT05 e pediu ajuda contextual/escala; U02 explicou a comparação externa. HC04/HC07 apontam necessidades de apresentação. Um comparador automático continua ausente da V0 e do Figma avaliado. |

A conclusão de cada entrega é **documental e acadêmica**. A permanência de hipóteses abertas e de problemas de usabilidade a corrigir não significa que os respectivos relatórios estejam inacabados.

## Como usar este repositório

1. Leia o [Guia de uso e apresentação](GUIA_DE_USO.md).
2. Leia o [Guia de definição de escopo](GUIA_ESCOPO_IHC.md), especialmente se o TCC não previa interface; **não é o caso desta equipe**.
3. Consulte as 14 entregas concluídas em sequência, observando como cada artefato deriva das decisões anteriores.
4. Identifique autoria individual nas entregas que exigem soluções por integrante.
5. Registre imagens, diagramas e evidências nos diretórios de [`assets/`](assets/README.md).
6. Mantenha a [Matriz de rastreabilidade](RASTREABILIDADE.md) atualizada.
7. Diferencie **[F] fato, [H] hipótese e [?] lacuna** sempre que necessário.
8. Para a conferência de submissão, consulte o [Checklist final](CHECKLIST_FINAL.md) e os checklists de cada entrega; itens administrativos ainda não comprovados não devem ser marcados automaticamente.
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
| 9 | [Modelo conceitual e design centrado na comunicação](docs/09_modelo_conceitual.md) | Soluções individuais + CI01/CI02 e OBJ01–OBJ09 | 🟩 |
| 10 | [MoLIC](docs/10_molic.md) | M01/Gabriel e M02/João; modelagem e rupturas | 🟩 |
| 11 | [Protótipo no Figma](docs/11_figma.md) | Protótipo navegável integrado com M01/M02 | 🟩 |
| 12 | [Planejamento da avaliação — DECIDE](docs/12_planejamento_avaliacao.md) | Plano de equipe, instrumentos e UT01–UT06 | 🟩 |
| 13 | [Avaliação heurística](docs/13_avaliacao_heuristica.md) | A01/A02; dez heurísticas; HC01–HC07 | 🟩 |
| 14 | [Avaliação por observação de usuários](docs/14_observacao_usuario.md) | U01/U02, análise por tarefa, MU01–MU08, AU01–AU06 e conclusão | 🟩 |

> As orientações específicas e eventuais alterações posteriores do docente para a turma prevalecem sobre a descrição resumida do repositório.

## Visão de continuidade

A cadeia de evidências do projeto é:

**TCC → usuários/stakeholders → hipóteses H01–H03 → personas P01/P02 → cenários C01/C02 → tarefas T01–T08 → V0/PF01–PF03/PP01–PP07 → walkthrough W01–W04 → observações O01–O10 → decisões V0→V1 → investigação I01/I02 → engenharia de usabilidade PG/MQ/MU → modelo conceitual → MoLIC → Figma → DECIDE → inspeção → observação de usuários → revisões**.

A E6 documentou a sequência real da V0 e corrigiu a interpretação da comparação como **manual e externa**. A E7 produziu instrumentos exploratórios que não foram aplicados naquela entrega. A E8 definiu princípios, metas e um ciclo iterativo; as E9–E14 realizaram a modelagem, prototipação e avaliação, mantendo rastreabilidade e registrando limitações.

**As 14 entregas possuem conteúdo acadêmico concluído no repositório.** A E9 elaborou CI01/CI02 e OBJ01–OBJ09; a E10 construiu M01/M02; a E11 materializou os fluxos no Figma; a E12 planejou a avaliação; a E13 consolidou HC01–HC07; e a E14 documentou U01/U02, avaliou as metas e produziu AU01–AU06 e recomendações. A conclusão documental **não equivale** à implementação de todas as melhorias nem à validação de H01–H03.

As 14 entregas possuem seus conteúdos acadêmicos documentados, incluindo a avaliação heurística e a consolidação da observação de usuários. O [Checklist final](CHECKLIST_FINAL.md) foi revisado para distinguir os requisitos já documentados, os elementos não aplicáveis e as verificações operacionais ou administrativas que ainda dependem de confirmação da equipe.

O encerramento definitivo exige conferir a notação e a legibilidade do MoLIC M01, o acesso aos fluxos do Figma sem autenticação privilegiada e a preservação privada dos registros de consentimento aplicáveis. A equipe informou que o professor dispensou a gravação das sessões da Entrega 14. Essa autorização não elimina a necessidade de consentimento voluntário dos participantes.

As oportunidades de melhoria identificadas nas avaliações permanecem documentadas como recomendações, sem serem apresentadas como funcionalidades já implementadas.

## Documentos de apoio

- [Guia de uso e apresentação](GUIA_DE_USO.md)
- [Guia para definir o escopo de IHC a partir do TCC](GUIA_ESCOPO_IHC.md)
- [Matriz de rastreabilidade](RASTREABILIDADE.md)
- [Checklist final](CHECKLIST_FINAL.md)
- [Bibliografia de IHC](BIBLIOGRAFIA.md)
- [Orientações de contribuição no GitHub](CONTRIBUTING.md)
- [Instrumentos reutilizáveis](instrumentos/README.md)

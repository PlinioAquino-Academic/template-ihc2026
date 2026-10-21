# Entrega 8 — Ciclo de vida e engenharia de usabilidade

**Data:** 21/10/2026  
**Status:** 🟩 concluída  
**Responsabilidade:** 1 solução consolidada por equipe

## Objetivo da atividade

Transformar o conhecimento acumulado nas Entregas 1–7 sobre usuários, tarefas, contexto de uso, plataforma e protótipo em **princípios de projeto e metas de usabilidade verificáveis**, conforme o ciclo de Engenharia de Usabilidade de Mayhew apresentado na disciplina.

A análise considera:

- H01–H03 — hipóteses prioritárias, ainda abertas;
- P01/P02 — proto-personas;
- C01/C02 — cenários de problema;
- T01–T08 — tarefas;
- PF01–PF03 e PP01–PP07 — fluxos e estados do protótipo V0;
- W01–W04 e O01–O10 — percurso e observações do walkthrough formativo da E6;
- I01/I02 — instrumentos planejados na E7, ainda não aplicados.

A V0 é uma **interface desktop funcional já prevista no TCC**. As propostas de melhoria documentadas para V1 ainda não devem ser confundidas com recursos implementados ou validados por usuários. Esta entrega registra requisitos e **metas futuras**: nenhuma taxa de sucesso, tempo, satisfação ou outro indicador de usabilidade foi medido aqui.

---

# Delimitação do sistema interativo

| Camada | O que pertence ao projeto | O que será analisado em IHC |
|---|---|---|
| Contribuição técnica do TCC | Algoritmo híbrido de controle semafórico baseado em Max Pressure e lógica actuated, implementado em Python, com SUMO e TraCI, além das estratégias de referência Fixed-Time e Max Pressure. | O desempenho dos controladores — filas, tempo de espera/viagem, throughput etc. — não é uma medida de usabilidade. |
| Camada de interação | Interface para selecionar cenários, configurar parâmetros, validar, executar/acompanhar simulações, recuperar execuções e consultar resultados individuais. | Compreensão, prevenção/recuperação de erros, feedback, eficácia, eficiência e satisfação na execução das tarefas humanas. |
| Integrações e registros | SUMO/SUMO-GUI, configurações, execução experimental, logs, histórico, métricas e gráficos. | Clareza dos estados e da relação cenário–controlador–seed–execução–resultados. |

A comparação entre duas execuções **não é automática na V0**: PP06 oferece histórico e seleção de uma execução, PP07 oferece análise individual e T07 exige alternância entre resultados e comparação manual externa. Uma futura comparação lado a lado é hipótese de melhoria, não capacidade existente.

---

# 1. Características da plataforma

Conforme a atividade de *Processos de Projeto de IHC — Parte 1*, esta seção explicita o software/hardware previstos e as **capacidades e restrições da plataforma com suas justificativas**. O conteúdo aproveita a caracterização já documentada na primeira parte da E8.

## 1.1 Características gerais

| Característica | Descrição | Consequência para IHC |
|---|---|---|
| Software | Aplicação desktop em Python integrada à simulação SUMO/TraCI. | Respeitar convenções de aplicações em janelas e separar decisões de interface dos detalhes do algoritmo. |
| Ambiente de simulação | O SUMO processa o experimento; no modo Visual, o SUMO-GUI mostra a rede. | A abertura de janela externa não deve comprometer a identificação do experimento ativo. |
| Hardware/dispositivos | Computador desktop ou notebook com capacidade de executar o ambiente; uso predominante de monitor, teclado e mouse. | Interface prioritariamente para desktop, com legibilidade de controles, mapas e tabelas. Não foi definida versão móvel. |
| Processamento | Duração variável conforme cenário, parâmetros, controlador, seed e modo. | Exibir estado da execução e evitar que a espera seja confundida com travamento. |
| Arquivos e histórico | Execuções produzem dados recuperáveis posteriormente. | Preservar contexto para reconhecer o que foi executado e interpretar resultados. |
| Execução Visual | Acompanha o comportamento do tráfego no SUMO-GUI. | Explicitar vínculo entre janela de simulação e configuração iniciada. |
| Execução Headless | Executa sem visualização gráfica do SUMO-GUI. | Feedback textual/estado torna-se ainda mais importante. |
| Parâmetros avançados | Algumas opções técnicas são disponibilizadas em área própria e podem depender do cenário/controlador. | Exibir quando pertinentes, sem sobrecarregar a preparação normal. |

As evidências gráficas da E6 mostram a aplicação em ambiente de janelas desktop. **Não está demonstrada aqui compatibilidade universal com diferentes sistemas operacionais**; essa questão precisaria de teste técnico específico, fora do escopo da presente avaliação de IHC.

## 1.2 Capacidades da plataforma

| Capacidade documentada da V0 | Justificativa | Implicação para a interface |
|---|---|---|
| Selecionar diferentes cenários e infraestruturas. | Permite experimentos em condições viárias distintas. | Identificação persistente do cenário ativo; PP01. |
| Exibir informações e representação do cenário. | Ajuda a verificar o local da simulação. | Texto e visualização devem ser relacionados e legíveis. |
| Configurar parâmetros e condições experimentais. | Define a execução e sua reprodutibilidade. | Agrupar valores, indicar unidades e distinguir principais/avançados; PP02. |
| Selecionar Fixed-Time, Max Pressure ou Hybrid. | Estratégias são objeto da avaliação técnica do TCC. | Mostrar o controlador escolhido com rótulo consistente. |
| Configurar seed. | Identifica condição de reprodutibilidade. | Preservar o valor da seed junto ao registro da execução. |
| Selecionar Visual ou Headless. | Existem modos de execução com feedback diferente. | Esclarecer a consequência de cada escolha. |
| Validar e confirmar antes de executar. | Previne processamento com condições inadequadas. | Mostrar problema e, idealmente, orientação para corrigir; PP03. |
| Iniciar/acompanhar execução e apresentar mensagens. | O processamento pode ser demorado. | Realçar status inteligível sem depender de leitura do log; PP04. |
| Abrir SUMO-GUI no modo Visual. | Permite inspecionar o comportamento do tráfego. | Preservar continuidade de contexto entre janelas; PP05. |
| Recuperar execuções no histórico. | Métodos, cenários e seeds são combinados em vários experimentos. | Manter identidade/contexto dos registros; PP06. |
| Consultar resultado e gráfico de uma execução. | Sustenta análise experimental individual. | Priorizar leitura e vínculo das métricas com sua origem; PP07. |

## 1.3 Restrições da plataforma

| Restrição | Justificativa | Consequência para IHC |
|---|---|---|
| Dependência da instalação/configuração do SUMO e do ambiente Python. | A simulação depende da infraestrutura técnica. | Falhas de inicialização devem ser explicadas e permitir recuperação. |
| Terminologia especializada. | Termos como seed, Hybrid, Headless, Max Pressure e regiões de detecção são do domínio técnico. | Preservar precisão e disponibilizar contexto/ajuda conforme O02. |
| Número variável de parâmetros. | Cenários/controladores admitem opções adicionais. | Manter o caminho principal enxuto e opções avançadas separadas (O03). |
| Processamento demorado ou variável. | A duração não é constante. | Sinalizar que está ativo, concluído ou em erro; não prometer tempos que não podem ser estimados. |
| SUMO-GUI em janela externa. | A execução Visual ocorre fora da janela principal. | Manter identificação do estudo e orientar o retorno à interface. |
| Histórico potencialmente grande. | O TCC envolve múltiplos cenários, controladores e seeds. | Considerar organização e posterior investigação de busca/filtros; não presumir sua necessidade validada. |
| Ausência de comparador automático na V0. | PP06 e PP07 operam com consultas individuais. | T07 permanece parcialmente apoiada; comparação externa manual. |
| Exigência de conhecimento do domínio. | Resultados científicos requerem contexto e interpretação técnica. | Não esconder dados essenciais nem impor conhecimento de implementação interna. |
| Ausência de cadastro e administração no recorte atual. | Nenhuma tarefa de E1–E7 justifica gestão de perfis/permissões. | Não criar login ou CRUD administrativo artificialmente. |

## 1.4 Conectividade e execução local

O fluxo principal da V0 utiliza o ambiente experimental instalado no computador empregado para executar Python/SUMO/TraCI. A conexão permanente com serviços externos **não integra as tarefas principais PF01–PF03 documentadas**; por isso, problemas de latência de rede não aparecem como restrição central.

O tempo percebido está mais relacionado à inicialização, à complexidade da infraestrutura, à configuração, ao controlador e ao processamento disponível. Eventual distribuição remota do sistema seria uma decisão futura de arquitetura, não um fato da V0.

## 1.5 Segurança e privacidade

A operação documentada da V0 lida predominantemente com cenário, parâmetros, seed, estratégias, logs e resultados, sem fluxo de cadastro de usuários ou coleta operacional de informações pessoais.

Os cuidados relevantes são prevenir perda de contexto, evitar alterações acidentais de parâmetros e não divulgar caminhos locais ou dados identificáveis em material público. **Os aspectos éticos de futuros participantes da pesquisa são tratados separadamente na E7**, pois não se confundem com os dados das simulações.

## 1.6 Volume de dados e histórico

A necessidade de **recuperar execuções anteriores** está sustentada pela metodologia do TCC e pela V0. A necessidade de filtros complexos, busca avançada, agrupamentos e paginação **não foi validada com usuários**. A decisão atual é manter o histórico e o contexto experimental existente, identificar dificuldades futuras por investigação e evitar adicionar funcionalidades apenas porque aparecem em ferramentas concorrentes.

## 1.7 Tempo de processamento e feedback

O usuário precisa distinguir estados e transições relevantes, como:

```text
Configuração preparada
        ↓
Validação
        ├── inadequada → informar problema → corrigir e validar novamente
        ↓ adequada
Confirmação
        ├── cancelar → voltar à preparação
        ↓ confirmar
Inicialização
        ↓
Execução (Headless ou Visual/SUMO-GUI)
        ├── falha → comunicar erro/possível ação
        ↓
Conclusão
        ↓
Histórico/seleção (PP06) → análise individual (PP07)
```

Esse diagrama representa uma **organização de estados e feedback desejada**, tomando como base a V0 e as observações O04–O07; não afirma que todos esses rótulos e possibilidades de recuperação já existam exatamente assim. A captura `pp04_execucao.png`, por exemplo, evidencia mensagens técnicas de processamento, mas não comprova uma estimativa confiável de tempo restante.

A V1 deverá destacar estado principal e contexto antes dos logs, mantendo detalhes técnicos acessíveis aos usuários que deles necessitarem. Quando não houver percentual verdadeiro ou tempo restante confiável, é preferível informar apenas estado/etapa a inventar uma estimativa.

---

# 2. Princípios gerais do projeto

Conforme a atividade de *Processos de Projeto de IHC — Parte 1*, a tabela deve conectar **contexto de uso, nome da referência, descrição/importância para o projeto e link**. Normas e diretrizes são orientações de design; sua inclusão não significa certificação de conformidade.

## 2.1 Contexto de uso considerado

A descrição abaixo retoma o contexto consolidado na Entrega 3, preservando a classificação como fato, hipótese ou lacuna.

| Dimensão | Contexto de uso herdado de E3 | Implicação de design |
|---|---|---|
| Usuários | **[H]** P01 — Marina Ribeiro, responsável pelo fluxo completo, e P02 — Carlos Mendes, mais interessado em interpretar e sintetizar. São proto-personas. | Priorizar fluxo de P01 e permitir interpretação clara para P02. |
| Tarefas | **[F/H]** T01–T08, da seleção do cenário à comparação e síntese, derivadas da metodologia experimental e da modelagem de tarefas. | Relacionar configuração, execução e resultados sem sobrecarregar uma única tela. |
| Equipamentos | **[H]** Desktop/notebook com teclado, mouse e monitor, adequado a mapas, parâmetros, tabelas e gráficos. | Priorizar convenções e legibilidade de desktop. |
| Ambiente físico | **[H]** Laboratório, ambiente acadêmico ou profissional; condições específicas de iluminação/ruído **[?]** não foram investigadas. | Evitar alegar condições ambientais não observadas. |
| Organização | **[F]** O TCC é desenvolvido por equipe com orientador; **[H]** profissionais distintos poderiam configurar ou interpretar estudos. | Resultados precisam conservar contexto compreensível para quem não executou o experimento. |
| Permissões | **[?]** Não existe evidência de necessidade de papéis administrativos. | Não criar autenticação/permissões artificiais. |
| Dados/histórico | **[F/H]** Há diversos experimentos e necessidade de identificar condições; **[?]** filtros avançados ainda não foram validados. | Preservar vínculo execução–configuração e investigar ampliação de histórico. |

## 2.2 Referências e princípios aplicáveis

| Contexto de uso | Nome da referência | Descrição da referência e importância para o projeto | Link de referência |
|---|---|---|---|
| Pesquisador/analista realiza tarefas em computador com objetivos específicos. | **ISO 9241-11:2018 — Usabilidade: definições e conceitos** | Apresenta a usabilidade em termos de eficácia, eficiência e satisfação em contexto de uso. Fundamenta as metas verificáveis da seção 3; não se confunde com métricas de tráfego. | https://www.iso.org/standard/63500.html |
| Usuários e tarefas ainda têm hipóteses abertas. | **ISO 9241-210:2019 — Design centrado no ser humano** | Recomenda compreender contexto, envolver usuários e avaliar iterativamente as soluções. Justifica o uso de I01/I02, avaliações futuras e revisão de P01/P02. | https://www.iso.org/standard/77520.html |
| Longa execução técnica e possíveis erros de configuração. | **Heurísticas de usabilidade de Nielsen — visibilidade, prevenção e recuperação de erros** | Orientam feedback de estado, revisão antes de iniciar e mensagens que indiquem problemas e formas de recuperação; relacionam-se a O04–O06. | https://www.nngroup.com/articles/ten-usability-heuristics/ |
| Interface desktop com muitos controles e terminologia especializada. | **Princípios e diretrizes de design de IHC — Barbosa e Silva (material da disciplina)** | Correspondência com expectativas, consistência, organização de opções e ajuda contextual para diminuir memorização e sobrecarga. Relacionam-se a O02/O03 e às futuras decisões de V1. | [Material da disciplina](../BIBLIOGRAFIA.md) |
| Apresentação de resultados, gráficos e mensagens. | **WCAG 2.2 — princípios de acessibilidade (referência adaptada)** | Princípios como perceptibilidade, operação por teclado, compreensão de rótulos e distinção não exclusivamente por cor podem orientar a interface desktop. **Não se declara conformidade WCAG**, que é destinada a conteúdo Web e exigiria avaliação própria. | https://www.w3.org/TR/WCAG22/ |

Não há base para declarar que a V0 satisfaz todas as normas anteriores; elas orientam **decisões e avaliações futuras**. A LGPD não foi usada como justificativa para criar login, papéis administrativos ou coletar dados pessoais inexistentes. Se houver participantes em avaliações, devem ser aplicados os cuidados de ética e privacidade da E7.

## 2.3 Decisões gerais de interface decorrentes

| ID | Princípio de projeto para V1 | Origem e justificativa | Situação |
|---|---|---|---|
| PG01 | Identificar cenário, estratégia, seed e condições antes de iniciar e ao consultar resultados. | T01–T06; O01/O08/O09; reprodutibilidade. | Diretriz de preservação/refinamento. |
| PG02 | Usar termos técnicos corretos com explicações breves quando necessárias. | H01, O02, I01-Q15, I02-E17. | Proposta a avaliar. |
| PG03 | Manter parâmetros principais separados dos avançados. | PP02 e O03. | Manter e refinar. |
| PG04 | Validar entradas e mostrar mensagens com problema e ação de recuperação. | PP03; O04/O05. | Preservar validação; melhorar comunicação. |
| PG05 | Mostrar estado principal do processamento mais claramente que os logs. | PP04/PP05, O06/O07. | Proposta a avaliar. |
| PG06 | Priorizar métricas e permitir acesso a detalhes/contexto da execução. | PP07, O09, H03. | Proposta a avaliar. |
| PG07 | Diferenciar consulta individual de comparação entre execuções. | PP06/PP07, T07, O10. | Comparação automática apenas hipótese futura. |
| PG08 | Usar rótulos e sinais que não dependam exclusivamente de cor. | Qualidade de uso, acessibilidade e legibilidade. | Diretriz a verificar no protótipo. |

Esses princípios funcionarão como guia inicial de estilo e interação e deverão ser retomados em E9–E11, sem converter sugestões em capacidades já disponíveis.

## 2.4 Registro inicial de guia de estilo e interação

O material *Processos — Parte 2* orienta manter um guia de estilo que registre decisões adotadas ao longo do ciclo. Nesta etapa, o registro é **conceitual e provisório**: não se inventam cores, tipografias ou componentes que ainda serão definidos no Figma.

| Elemento | Decisão registrada até E8 | Próxima verificação |
|---|---|---|
| Nomenclatura | Usar os mesmos nomes para cenário, estratégia, seed, modo, execução e resultados; explicar termos pouco familiares. | Esquema de signos da E9 e protótipo E11. |
| Organização | Distinguir seleção de cenário, configuração principal/avançada, validação, execução e resultados. | E9–E11 e testes. |
| Mensagens | Tornar feedback de processamento e de recuperação de erros orientado à tarefa; não depender só de logs. | MoLIC de rupturas, E10, e heurística E13. |
| Visualização de resultados | Vincular dados ao contexto de execução e diferenciar síntese de detalhe. | E9–E11; H03 aberta. |
| Acessibilidade | Considerar legibilidade, indicadores não exclusivos por cor e foco/navegação por teclado quando aplicáveis. | Inspeção da versão concretamente avaliada. |
| Componentes visuais específicos | Ainda não definidos nesta etapa. | Registrar escolhas no Figma/E11 e refletir mudanças na rastreabilidade. |

---

# 3. Metas de usabilidade

As metas a seguir são **critérios planejados pela equipe**, não índices já obtidos. Derivam da distinção entre eficácia, eficiência e satisfação apresentada nos slides *Qualidade de Uso* e *Processos de Projeto de IHC — Parte 2*. Devem ser verificados em tarefas e perfis definidos previamente, com instrumentos planejados na E12 e avaliações E13/E14.

## 3.1 Metas qualitativas

| ID | Meta qualitativa | Público/tarefa | Evidência desejada em avaliação futura | Justificativa |
|---|---|---|---|---|
| MQ01 | Usuário reconhece a sequência cenário → configuração → validação → execução → resultado. | P01, T01–T06 | Caminho encontrado sem orientação direta; comentários espontâneos sobre clareza. | H02 e O01. |
| MQ02 | Termos de controlador, seed e modo de execução são compreensíveis com ajuda contextual disponível. | P01, T02/T03 | Participante explica corretamente as escolhas e encontra ajuda, quando necessária. | O02; H01 ainda aberta. |
| MQ03 | Erros permitem entender o problema e a ação necessária para prosseguir. | P01, T02/T04 | Participante reconhece causa e tentativa de correção. | O04/O05. |
| MQ04 | O estado da simulação é perceptível sem depender exclusivamente de logs. | P01, T05 | Participante identifica inicialização, processamento, conclusão ou falha. | O06/O07. |
| MQ05 | Resultados conservam vínculo com cenário, controlador e seed. | P01/P02, T06/T08 | Participante localiza e descreve contexto do resultado. | O08/O09. |
| MQ06 | O usuário entende os limites do apoio da interface à comparação. | P01/P02, T07 | Distingue consulta individual da comparação externa, sem esperar função inexistente na V0. | O10; H03 aberta. |
| MQ07 | A interface possibilita uso com rótulos legíveis e navegação convencional de desktop, considerando necessidades diversas. | P01/P02, fluxos principais | Inspeção de legibilidade, contraste, foco e informação não baseada só em cor. | Princípios de qualidade de uso. |

## 3.2 Metas quantitativas previstas

Valores abaixo são **alvos iniciais propostos**, escolhidos antes de qualquer teste, para orientar a avaliação da solução evoluída. Não representam percentuais observados nem estimativas estatísticas de população. Como a E14 prevê número final reduzido de participantes, contagens absolutas sempre acompanharão os percentuais, e resultados não serão generalizados.

| ID | Dimensão | Métrica e critério de conclusão | Tarefa/escopo | Meta preliminar | Como medir | Justificativa |
|---|---|---|---|---|---|---|
| MU01 | Eficácia | Concluir seleção de cenário, controlador, seed e modo e revisar resumo sem ajuda do moderador. | T01–T03, PP01–PP03 | **100%** dos participantes observados na tarefa. | Registro de sucesso/falha e intervenções. | Configuração incorreta compromete experimento; H02. |
| MU02 | Eficácia/segurança de interação | Perceber configuração inválida e identificar ação correta de recuperação. | T02/T04, PP03 | **100%** dos participantes expostos ao cenário de erro. | Tarefa de erro planejada com critério observável. | O04/O05: prevenção e recuperação. |
| MU03 | Eficiência | Tempo para concluir preparação e revisão em cenário padronizado, sem erros impostos. | T01–T03 | **Mediana ≤ 5 min**. | Cronômetro da instrução ao cumprimento do critério. | Limitar retrabalho sem comparar máquinas/processamento. |
| MU04 | Eficácia | Identificar corretamente estado e estratégia da execução sem interpretar exclusivamente o log técnico. | T05, PP04/PP05 | **100%** dos participantes. | Pergunta objetiva em etapa definida da tarefa. | O06: estado principal pouco destacado. |
| MU05 | Eficácia | Localizar uma execução previamente identificada e apontar cenário, controlador e seed. | T06, PP06/PP07 | **100%** dos participantes. | Checklist de campos corretamente identificados. | H03, O08/O09 e rastreabilidade. |
| MU06 | Eficiência | Tempo de localização de execução predefinida no histórico. | T06, PP06 | **Mediana ≤ 3 min**. | Cronômetro em base experimental previamente padronizada. | Avalia interação, não tempo de simulação. |
| MU07 | Satisfação | Nota pós-tarefa para clareza do fluxo, de 1 (muito difícil) a 5 (muito fácil). | PF01–PF03 | **Mediana ≥ 4/5**. | Pergunta pós-tarefa padronizada, resposta anônima. | Capta percepção, além de sucesso e tempo. |
| MU08 | Eficácia/compreensão | Reconhecer que, na versão avaliada, a comparação A/B exige consultas individuais e trabalho externo, quando essa limitação permanecer. | T07, PP06/PP07 | **100%** dos participantes informados sobre o fluxo avaliado. | Verificação do entendimento após consulta às duas execuções. | Evita confundir função proposta com implementada. |

**Definição de sucesso:** cumprir o objetivo solicitado e os campos/contextos exigidos **sem o avaliador ensinar o caminho**. Ajuda fornecida deve ser registrada; os critérios exatos por tarefa serão detalhados em E12. Em MU02 a condição de erro será controlada e segura para não comprometer experimentos reais.

**Limites metodológicos:** os tempos MU03 e MU06 dizem respeito apenas à interação padronizada. O piloto da E12 poderá revelar que um limiar é inadequado; qualquer ajuste precisa ser **justificado e registrado antes da coleta final**, jamais depois de conhecer resultados para fazer a meta parecer atingida. Com dois participantes, sucesso de 100% corresponde a 2/2 e não constitui evidência de desempenho populacional.

## 3.3 Priorização das metas

A priorização abaixo registra o esforço de design, **não** é resultado de medição. A soma de 100% indica importância relativa dos objetivos na próxima iteração e não substitui os limiares de eficácia, eficiência ou satisfação.

| Grupo de metas | Peso de prioridade | Justificativa |
|---|---:|---|
| Preparação correta e prevenção/recuperação de erros (MU01–MU03). | 35% | Evitar execuções em condições incorretas e retrabalho. |
| Estado/feedback da execução (MU04). | 20% | Reduzir incerteza durante processamento. |
| Recuperação e interpretação contextual de resultados (MU05–MU06). | 25% | Preservar origem da execução e permitir análise correta. |
| Satisfação e entendimento dos limites da comparação (MU07–MU08). | 20% | Clareza da interação e expectativas realistas. |
| **Total** | **100%** | Prioridades propostas para discussão e avaliação. |

---

# 4. Iteração do ciclo de engenharia de usabilidade

A engenharia de usabilidade não termina na formulação de metas. O processo aplicado ao projeto será iterativo e rastreável:

1. **Analisar:** retomar P01/P02, C01/C02, T01–T08 e hipóteses H01–H03; quando disponíveis, confrontar com dados de I01/I02.
2. **Especificar:** adotar PG01–PG08, MQ01–MQ07 e MU01–MU08 como critérios iniciais de design e de avaliação.
3. **Projetar:** construir cenários de interação, mapa de objetivos e signos (E9), conversas MoLIC (E10) e protótipo integrado no Figma (E11), preservando a distinção V0/V1.
4. **Planejar a avaliação:** associar tarefas e metas ao método DECIDE, aos critérios de sucesso, ao piloto e à ética da coleta (E12).
5. **Inspecionar:** avaliar o protótipo pelas heurísticas aplicáveis, identificando violações reais e sua severidade (E13).
6. **Observar:** conduzir tarefas com participantes consentidos, registrar sucesso, tempo, erro, ajuda, satisfação e observações qualitativas (E14).
7. **Revisar:** comparar resultados às metas, priorizar problemas, atualizar signos/fluxos/telas e registrar mudanças na rastreabilidade. Se necessário, repetir projeto e avaliação.

O fato de uma avaliação ainda não ter acontecido não impede o planejamento de metas; apenas impede declarar resultados. Os instrumentos I01/I02 da E7 continuam disponíveis para investigação futura, **sem aplicação presumida**.

---

# 5. Síntese da equipe

A Entrega 8 conclui a etapa de **especificação da engenharia de usabilidade**, não a validação final da interface. A contribuição inicial desenvolvida a partir da V0 foi preservada e complementada com a tabela de princípios gerais e com requisitos qualitativos, metas quantitativas e plano de iteração solicitados nos materiais da disciplina.

O desenho futuro deve preservar os pontos positivos observados na V0, melhorar comunicação de termos e erros, realçar o status, organizar resultados e **investigar** se há necessidade de apoio comparativo. H01–H03 continuam abertas e a comparação automática permanece ausente na V0. As métricas experimentais de tráfego continuarão sendo avaliadas no TCC, independentemente das medidas de usabilidade planejadas aqui.

## Checklist

- [x] Características de software/hardware e contexto de uso descritos.
- [x] Capacidades e restrições da plataforma justificadas e relacionadas à interação.
- [x] Distinção entre resultado técnico do TCC e qualidade de uso da interface preservada.
- [x] Princípios gerais associados a contexto de uso, referência, importância e link.
- [x] Diretrizes de projeto derivadas de artefatos anteriores.
- [x] Metas qualitativas associadas a usuários/tarefas e evidências futuras.
- [x] Metas quantitativas definem dimensão, tarefa, critério, alvo e modo de coleta.
- [x] Eficácia, eficiência e satisfação consideradas.
- [x] Prioridades distinguem peso de projeto de indicadores observados.
- [x] Ciclo de iteração relacionado às Entregas 9–14.
- [x] Nenhuma aplicação de I01/I02, avaliação com usuários ou comparação automática foi inventada.

## Referências

- BARBOSA, Simone D. J.; SILVA, Bruno S. *Interação Humano-Computador*. Elsevier/Campus, 2010.
- CENTRO UNIVERSITÁRIO FEI. *CC8122 — Processos de Projeto de IHC — Parte 1*; *Parte 2*; *Qualidade de Uso*; *Princípios e Diretrizes para o Design de IHC*. Materiais de aula, 2026/2.
- ISO. *ISO 9241-11:2018 — Usability: Definitions and concepts*. https://www.iso.org/standard/63500.html
- ISO. *ISO 9241-210:2019 — Human-centred design for interactive systems*. https://www.iso.org/standard/77520.html
- NIELSEN NORMAN GROUP. *10 Usability Heuristics for User Interface Design*. https://www.nngroup.com/articles/ten-usability-heuristics/
- W3C. *Web Content Accessibility Guidelines (WCAG) 2.2*. https://www.w3.org/TR/WCAG22/
- Entregas 1–7 e [`../RASTREABILIDADE.md`](../RASTREABILIDADE.md) deste projeto.

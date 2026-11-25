# Projeto de Interação Humano-Computador (IHC)

## Princípio do projeto da disciplina

A disciplina utiliza **preferencialmente o tema do TCC em andamento** como domínio para exercitar os métodos de Interação Humano-Computador.

Isso vale também quando o TCC é predominantemente técnico e **não previa o desenvolvimento de uma interface**.

- Se o TCC **já prevê interface**, ela pode ser o objeto principal das atividades de IHC.
- Se o TCC **não prevê interface**, a equipe deverá derivar um **escopo de IHC** a partir da contribuição técnica: quem poderia utilizar ou se beneficiar do resultado, o que essa pessoa precisaria fazer, em qual contexto e que interação seria necessária.
- A interface criada na disciplina **não se torna automaticamente uma obrigação do TCC**. Ela pode ser um protótipo de aprendizagem, uma extensão conceitual ou uma demonstração de aplicação potencial. Sua incorporação ao TCC depende de decisão da equipe e do orientador.

Leia obrigatoriamente o [Guia para definir o escopo de IHC a partir do tema do TCC](GUIA_ESCOPO_IHC.md).

## Identificação

**Título do projeto de IHC:** Estação de triagem aduaneira assistida por IA — interface para análise de imagens de raio-X de contêineres  
**TCC/projeto de origem:** Detecção de Anomalias em Imagens de Raio-X de Contêineres de Carga  
**Orientador(a):** Murilo Bouzon  
**Disciplina:** Interação Humano-Computador  
**Instituição:** Centro Universitário FEI  
**Semestre:** 2026/2

### Equipe

| Nome completo | Matrícula | GitHub | Responsabilidade principal |
|---|---:|---|---|
| Kawan Mark Geronimo Da Silva | 22.222.010-5 | [@KawanMark](https://github.com/KawanMark) | C01 (Rapiscan InSight) na Entrega 2, persona P01 na Entrega 3, cenário CP01 na Entrega 4, tarefas T01 a T03 na Entrega 5 e protótipo integrado PF01/PF02 na Entrega 6 |
| Gabriel Albertini Pinheiro | 22.122.094-8 | [@albertx0](https://github.com/albertx0) | C02 (Portal Único Siscomex) na Entrega 2, persona P02 na Entrega 3, cenário CP02 na Entrega 4, tarefas T04 a T06 na Entrega 5 e protótipo integrado PF01/PF02 na Entrega 6 |
| Alexandre Domiciano Pierri | 22.125.061-6 | [@Apierri05](https://github.com/Apierri05) | C03 (Smiths Detection DaiSy/viZual) na Entrega 2, proto-persona P03 na Entrega 3, cenário CP03 na Entrega 4, tarefas T07 a T09 na Entrega 5 e protótipo integrado PF01/PF02 na Entrega 6 |

## Relação entre TCC e projeto de IHC

| Item | Descrição |
|---|---|
| Tema central do TCC | Análise automática de imagens radiográficas de contêineres de carga para detectar mercadorias ilícitas e anomalias ocultas sem depender de exemplos reais prévios de contrabando. |
| Resultado técnico esperado do TCC | Modelo de classificação (EfficientNet-B1), anomalias sintéticas e estudo experimental; a versão técnica consultada produz mapas de atenção por Grad-CAM. Autoencoder/mapa residual corresponde à formulação inicial da Entrega 1. |
| O TCC já previa interface? | não |
| Capacidade técnica que pode gerar valor para pessoas | Classificar imagens e indicar aproximadamente regiões relevantes para a predição por mapa de atenção; não equivale ao mapa residual da formulação inicial. |
| Usuário principal adotado em IHC | Operador da estação de imagem de raio-X (H01). A autoridade para decidir sobre a carga pode caber a outro cargo, o Auditor-Fiscal (H39). |
| Objetivo principal desse usuário | Chegar a uma conclusão confiável sobre cada contêiner examinado e registrá-la de forma defensável, sob incerteza (H38). |
| Interface/recorte explorado na disciplina | Visualizador comparativo (imagem original × mapa de atenção) e registro do resultado da análise com justificativa. Ordem de exame por nível de anomalia, score numérico e formato da trilha de registro são hipóteses a investigar (H25, H31, H32). |
| Relação com o escopo formal do TCC | protótipo demonstrativo |

> **Importante:** a tabela acima explica a relação entre os dois trabalhos. Ela não altera o compromisso formal do TCC.

## Resumo do projeto pela perspectiva do usuário

Quem opera a estação de imagem de raio-X precisa chegar, contêiner a contêiner, a uma conclusão em que confie sobre o que a imagem mostra e registrá-la de forma defensável, em uma sala de controle de recinto alfandegado. A decisão formal de liberar, exigir ou reter a carga pode caber a outro cargo, o Auditor-Fiscal, e essa divisão de papéis ainda está em investigação. Hoje a imagem é examinada em softwares dos fabricantes dos scanners, que já oferecem apoio analítico como pseudo-cor por material, realce de bordas e comparação com imagens semelhantes, mas a interpretação final continua visual e humana. A equipe supõe que a sobreposição de mercadorias e a fadiga visual dificultam essa leitura, com risco de deixar passar uma anomalia ou de reter uma carga regular. A versão técnica do TCC consultada investiga classificação de imagens de carga com anomalias sintéticas e usa mapas de atenção para indicar regiões relevantes para a predição. A formulação inicial de autoencoder/mapa residual está preservada na Entrega 1 como histórico; os dois métodos não são equivalentes. Para fins da disciplina de IHC, será explorada uma interface que permita a esse operador comparar a imagem original com o mapa de atenção, examinar as regiões relevantes para a predição e registrar o resultado da análise com justificativa.

As afirmações deste resumo que ainda são hipóteses (papéis, dificuldades e contexto) estão registradas com seus IDs na [Entrega 1](docs/01_conhecendo_o_problema.md) e na [Matriz de rastreabilidade](RASTREABILIDADE.md).

## Por que pensar em interface mesmo em TCCs técnicos?

Algoritmos, modelos, APIs, análises de datasets e componentes de infraestrutura podem não exigir interface como resultado acadêmico do TCC. Porém, quando essas contribuições são transferidas para uma situação real, normalmente existem pessoas que:

- configuram parâmetros;
- fornecem ou selecionam dados;
- iniciam ou acompanham processamento;
- interpretam resultados;
- comparam alternativas;
- tomam decisões;
- administram usuários e permissões;
- consultam histórico;
- geram relatórios;
- investigam erros;
- auditam mudanças.

Essas atividades fornecem um campo legítimo para exercitar IHC.

Possibilidades de interface incluem **dashboards, telas administrativas, configuração, relatórios, histórico com filtros, comparação de resultados, visualização de dados, acompanhamento de processamento, gestão de perfis e permissões, CRUDs justificados pelo domínio, alertas, auditoria e ajuda contextual**. Nenhuma dessas telas é obrigatória por si só: deve existir uma tarefa e um objetivo de usuário que a justifique.

## Relação com apresentação e potencial de aplicação

A reflexão sobre usuários ajuda a equipe a explicar o projeto para públicos externos, inclusive em eventos como a **INOVA**. Em vez de comunicar apenas a técnica implementada, a equipe pode apresentar:

**problema humano → contribuição computacional → forma de uso → impacto potencial**.

O protótipo de IHC pode, portanto, funcionar como uma demonstração do potencial de mercado, transferência tecnológica ou impacto extensionista do tema do TCC, sem necessariamente integrar a implementação final do trabalho de conclusão.

## Como usar este repositório

1. Leia o [Guia de uso e apresentação](GUIA_DE_USO.md).
2. Leia o [Guia de definição de escopo de IHC](GUIA_ESCOPO_IHC.md), especialmente se o TCC não previa interface.
3. Preencha as entregas na ordem em que forem trabalhadas na disciplina.
4. Em toda entrega individual, **identifique o autor**.
5. Salve imagens, diagramas e evidências em [`assets/`](assets/README.md).
6. Mantenha a [Matriz de rastreabilidade](RASTREABILIDADE.md) atualizada.
7. Na Entrega 1, diferencie **[F] fatos**, **[H] hipóteses** e **[?] lacunas de conhecimento**.
8. Antes de cada entrega, revise o checklist do arquivo e o [Checklist final](CHECKLIST_FINAL.md).
9. Sempre que uma evidência posterior contrariar uma hipótese inicial, **revise o projeto**. IHC é um processo iterativo.

## Entregas

| # | Entrega | Quantidade mínima / responsabilidade | Status |
|---:|---|---|---|
| 1 | [Conhecendo o projeto, o usuário e o problema](docs/01_conhecendo_o_problema.md) | 1 solução consolidada por equipe | 🟦 |
| 2 | [Público-alvo e análise de concorrência](docs/02_analise_concorrencia.md) | no mínimo 1 concorrente/interface representativa por integrante + síntese | 🟦 |
| 3 | [Personas, empatia, contexto e jornada](docs/03_personas_contexto_jornada.md) | 1 persona por integrante; demais artefatos consolidados | 🟦 |
| 4 | [Cenários de análise/problema](docs/04_cenarios_problema.md) | 1 solução completa por integrante | 🟦 |
| 5 | [Análise de tarefas: HTA, GOMS e CTT](docs/05_analise_tarefas.md) | cada integrante: pelo menos 1 HTA + 1 GOMS + 1 CTT | 🟦 |
| 6 | [Prototipação em papel](docs/06_prototipacao_papel.md) | 1 protótipo integrado por equipe | 🟦 |
| 7 | [Coleta de dados e aspectos éticos](docs/07_coleta_dados.md) | pesquisa documental + três instrumentos individuais | 🟦 |
| 8 | [Ciclo de vida e engenharia de usabilidade](docs/08_engenharia_usabilidade.md) | 1 solução consolidada por equipe | 🟦 |
| 9 | [Modelo conceitual e design centrado na comunicação](docs/09_modelo_conceitual.md) | soluções individuais + consolidação de objetivos/signos | 🟦 |
| 10 | [MoLIC](docs/10_molic.md) | 1 diagrama completo por integrante | 🟩 |
| 11 | [Protótipo no Figma](docs/11_figma.md) | 1 protótipo integrado por equipe, cobrindo fluxos modelados | 🟩 |
| 12 | [Planejamento da avaliação — DECIDE](docs/12_planejamento_avaliacao.md) | 1 plano consolidado por equipe | 🟩 |
| 13 | [Avaliação heurística](docs/13_avaliacao_heuristica.md) | 1 avaliação completa por integrante, todas as telas/estados e 10 heurísticas | 🟩 |
| 14 | [Avaliação por observação de usuários](docs/14_observacao_usuario.md) | avaliação consolidada; nº de participantes finais = nº de integrantes | 🟩 |

Estados: ⬜ não iniciada, 🟨 em andamento, 🟩 concluída, 🟦 revisada após feedback.

A revisão da Entrega 7 possui [pendências de configuração e verificação dos formulários online](instrumentos/07_coleta/README.md#pendências-online-após-o-feedback-de-15112026). 🟦 registra a revisão; não declara que essas alterações externas foram executadas nem que houve coleta com pessoas.

> Se o docente definir quantidade diferente para a turma/semestre, a orientação da disciplina prevalece.

## Visão de continuidade

O projeto deve formar uma cadeia de evidências:

**tema/contribuição do TCC → possível aplicação → usuários/stakeholders → objetivos → problema/contexto → alternativas → necessidades → personas → cenários → tarefas → modelo conceitual → MoLIC → protótipo → planejamento → inspeção → teste com usuários → melhorias**.

Uma entrega não deve “reiniciar” o projeto. Se o escopo de IHC foi criado para um DBA, por exemplo, as personas, tarefas, MoLIC, protótipo e avaliação devem permanecer coerentes com esse perfil, salvo quando novas evidências justificarem a revisão.

## Documentos de apoio

- [Guia de uso e apresentação](GUIA_DE_USO.md)
- [Guia para definir o escopo de IHC a partir do TCC](GUIA_ESCOPO_IHC.md)
- [Matriz de rastreabilidade](RASTREABILIDADE.md)
- [Checklist final](CHECKLIST_FINAL.md)
- [Bibliografia de IHC](BIBLIOGRAFIA.md)
- [Orientações de contribuição no GitHub](CONTRIBUTING.md)
- [Instrumentos reutilizáveis](instrumentos/README.md)

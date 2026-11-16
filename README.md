# Projeto de Interação Humano-Computador (IHC)

> **Template acadêmico para documentação do projeto no GitHub.**  
> Substitua todo texto entre `{{...}}`, remova exemplos que não se aplicam e mantenha evidências no próprio repositório sempre que possível.

## Princípio do projeto da disciplina

A disciplina utiliza **preferencialmente o tema do TCC em andamento** como domínio para exercitar os métodos de Interação Humano-Computador.

Isso vale também quando o TCC é predominantemente técnico e **não previa o desenvolvimento de uma interface**.

- Se o TCC **já prevê interface**, ela pode ser o objeto principal das atividades de IHC.
- Se o TCC **não prevê interface**, a equipe deverá derivar um **escopo de IHC** a partir da contribuição técnica: quem poderia utilizar ou se beneficiar do resultado, o que essa pessoa precisaria fazer, em qual contexto e que interação seria necessária.
- A interface criada na disciplina **não se torna automaticamente uma obrigação do TCC**. Ela pode ser um protótipo de aprendizagem, uma extensão conceitual ou uma demonstração de aplicação potencial. Sua incorporação ao TCC depende de decisão da equipe e do orientador.

Leia obrigatoriamente o [Guia para definir o escopo de IHC a partir do tema do TCC](GUIA_ESCOPO_IHC.md).

## Identificação

**Equipe:** 14   
**Título do projeto de IHC:** Estoque com ML   
**TCC/projeto de origem:** Previsão de estoque usando machine learning  
**Orientador(a):** Fagner de Assis Moura Pimentel  
**Disciplina:** Interação Humano-Computador    
**Instituição:** FEI  
**Semestre:** oitavo semestre  

### Equipe

| Nome completo | Matrícula | GitHub | Responsabilidade principal |
|---|---:|---|---|
| Paulo Andre de Oliveira Hirata | 22125072-3 | @poulison | {{...}} |
| Victor Merker Binda | 22.125.075-6 | {{@usuario}} | {{...}} |

## Relação entre TCC e projeto de IHC

| Item | Descrição |
|---|---|
| Tema central do TCC | O uso de ML para fazer previsões que envolvem o comportamento e movimentação de um estoque |
| Resultado técnico esperado do TCC | Sistema |
| O TCC já previa interface? | sim |
| Capacidade técnica que pode gerar valor para pessoas | Analisar o histórico do estoque, prever demanda e comparar modelos para apoiar reposições |
| Usuário principal adotado em IHC | Responsável pelo controle e reposição do estoque de um pequeno comércio |
| Objetivo principal desse usuário | Antecipar reposições, evitando falta e excesso de produtos |
| Interface/recorte explorado na disciplina | Consulta de riscos, interpretação da previsão e planejamento de reposição |
| Relação com o escopo formal do TCC | Parte prevista e aprofundamento da interface sob a perspectiva de IHC |

> **Importante:** a tabela acima explica a relação entre os dois trabalhos. Ela não altera o compromisso formal do TCC.

## Resumo do projeto pela perspectiva do usuário

Escreva **um parágrafo curto e concreto** explicando: quem é o usuário escolhido, o que precisa alcançar, qual problema enfrenta ou qual atividade precisa executar, em qual contexto e como a contribuição do TCC se relaciona com essa situação.

Evite começar pela tecnologia.

> **Estrutura sugerida:** “`{{tipo de usuário}}` precisa `{{objetivo}}` em `{{contexto}}`. Atualmente enfrenta `{{problema/limitação}}` e utiliza `{{processo/alternativa atual}}`. O tema do TCC investiga `{{contribuição técnica}}`. Para fins da disciplina de IHC, será explorada uma interface que permita `{{forma de uso da contribuição}}`.”

Se alguma afirmação ainda não estiver sustentada por evidência, registre-a como hipótese na [Entrega 1](docs/01_conhecendo_o_problema.md).

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
| 2 | [Público-alvo e análise de concorrência](docs/02_analise_concorrencia.md) | no mínimo 1 concorrente/interface representativa por integrante + síntese |  🟦  |
| 3 | [Personas, empatia, contexto e jornada](docs/03_personas_contexto_jornada.md) | 1 persona por integrante; demais artefatos consolidados | 🟩  |
| 4 | [Cenários de análise/problema](docs/04_cenarios_problema.md) | 1 solução completa por integrante | 🟩  |
| 5 | [Análise de tarefas: HTA, GOMS e CTT](docs/05_analise_tarefas.md) | cada integrante: pelo menos 1 HTA + 1 GOMS + 1 CTT | 🟩 |
| 6 | [Prototipação em papel](docs/06_prototipacao_papel.md) | 1 protótipo integrado por equipe | 🟩 |
| 7 | [Coleta de dados e aspectos éticos](docs/07_coleta_dados.md) | soluções individuais + técnicas distintas; questionário entre as técnicas | 🟩 |
| 8 | [Ciclo de vida e engenharia de usabilidade](docs/08_engenharia_usabilidade.md) | 1 solução consolidada por equipe | 🟩 |
| 9 | [Modelo conceitual e design centrado na comunicação](docs/09_modelo_conceitual.md) | soluções individuais + consolidação de objetivos/signos | 🟩 |
| 10 | [MoLIC](docs/10_molic.md) | 1 diagrama completo por integrante | 🟩 |
| 11 | [Protótipo no Figma](docs/11_figma.md) | 1 protótipo integrado por equipe, cobrindo fluxos modelados | 🟩 |
| 12 | [Planejamento da avaliação — DECIDE](docs/12_planejamento_avaliacao.md) | 1 plano consolidado por equipe | 🟨 |
| 13 | [Avaliação heurística](docs/13_avaliacao_heuristica.md) | 1 avaliação completa por integrante, todas as telas/estados e 10 heurísticas | 🟨 |
| 14 | [Avaliação por observação de usuários](docs/14_observacao_usuario.md) | avaliação consolidada; nº de participantes finais = nº de integrantes | 🟨 |

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

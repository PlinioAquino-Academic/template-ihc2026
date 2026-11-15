# Entrega 8 — Ciclo de vida e engenharia de usabilidade

**Data:** 04/11/2026<br>
**Status:** 🟩 concluída<br>
**Autores:** Kawan Mark Geronimo Da Silva (22.222.010-5), Gabriel Albertini Pinheiro (22.122.094-8) e Alexandre Domiciano Pierri (22.125.061-6)

## Objetivo e recorte

Definir requisitos e metas para a **Mesa de inspeção**, que permite comparar uma radiografia de contêiner com o destaque do modelo, marcar regiões e registrar um parecer. A base são as [tarefas da Entrega 5](05_analise_tarefas.md), os fluxos PF01/PF02 da [Entrega 6](06_prototipacao_papel.md) e a [pesquisa documental da Entrega 7](07_coleta_dados.md).

| Camada | O que pertence ao projeto | O que será avaliado |
|---|---|---|
| Contribuição técnica do TCC | Classificação de imagens de raio-X com anomalias sintéticas e localização aproximada por mapa de atenção. O código local consultado utiliza EfficientNet-B1 e Grad-CAM. | Métricas do modelo pertencem ao estudo experimental do TCC. |
| Interação de IHC | Comparação visual, ajustes da imagem, marcação, comentário e emissão de parecer. | Compreensão, conclusão da tarefa, esforço, prevenção de erro e satisfação. |
| Dados e integrações do protótipo | Casos fictícios, resultados previamente preparados e espera simulada quando não houver integração. Sem envio real à RFB/Siscomex. | Entendimento dos estados e do fluxo; não desempenho de uma operação portuária. |

O mapa indica regiões relevantes para a predição, sem provar a presença de ilícito. O indicador e o limiar devem corresponder à versão técnica demonstrada: os valores da Entrega 6 são exemplos de interface, não uma probabilidade comprovada de contrabando. A interface da disciplina permanece um protótipo demonstrativo.

## 1. Características da plataforma

| Característica | Definição para o protótipo | Consequência para IHC |
|---|---|---|
| Software | Interface para uso em computador, com protótipo navegável no Figma; demonstração técnica local em navegador, quando integrada. Windows/Linux como ambientes previstos, sem dependência de celular. | Manter os mesmos termos e estados entre os protótipos. |
| Hardware | Mouse, teclado e um monitor; referência de avaliação: 1920 × 1080, em tela de 22–24 polegadas. | Dar prioridade à radiografia e verificar a legibilidade dos painéis. É uma condição de teste, não um levantamento do posto real. |
| Capacidades | Abrir um caso, ajustar visualização, comparar camadas, marcar regiões e gerar parecer. | Ajustes e marcações devem ser reversíveis, preservando a imagem original. |
| Restrições | Mapa de atenção aproximado e sem classificação do tipo de ilícito. | Explicar limites do resultado e separar indicação automática de conclusão humana. |
| Conectividade | Demonstração local ou navegável, sem integração institucional. | Falhas de processamento/exportação devem permitir tentar novamente sem perder anotações. |
| Tempo de processamento | Latência real ainda não medida; no teste, usar espera simulada fixa de 3 segundos. | Exibir “Analisando imagem”; em erro, explicar a falha. Não mostrar percentual sem progresso conhecido. |
| Dados/histórico | Um caso aberto por vez, com imagem, identificação fictícia e parecer. Histórico agregado fora do recorte. | Evitar troca de caso sem aviso sobre registros não exportados. |
| Privacidade | Casos fictícios ou imagens públicas com origem identificada; participantes futuros identificados por códigos. | Não expor nomes, placas, empresas ou operações reais na demonstração. |
| Papéis | P01 examina e registra; P02 consulta o parecer como apoio à decisão. P03 continua stakeholder (H42). | A Mesa não autoriza desembaraço nem cria uma interface móvel para P03. |

**Limitação da evidência atual:** [F] não houve validação profissional da interface nem aplicação dos instrumentos com pessoas. A pesquisa documental da Entrega 7 é complementar. [H] Plataforma, vocabulário, equipamentos e critérios iniciais devem ser revistos após investigação profissional; isso não é uma restrição do software.

## 2. Princípios do projeto

**Contexto de uso adotado:** P01 examina a radiografia em estação com teclado, mouse e monitor dedicado; P02 recebe o parecer para apoiar o despacho. A sala de operação é documentada, mas iluminação, interrupções, volume por turno e pressão temporal continuam hipóteses (H14–H16, ?07). O protótipo trabalha um caso por vez. Essas condições orientam os princípios abaixo.

### 2.1 Princípios de negócio/domínio

| Regra do domínio e base | Consequência para o projeto | Limite da evidência |
|---|---|---|
| [F] O despacho possui responsável e atos formais, conforme C02; ED01/ED03 distinguem operação e fiscalização. | [H39] P01 registra a conclusão técnica; P02 é destinatário do parecer e formaliza o ato fora da Mesa. A Mesa não autoriza desembaraço. | A divisão concreta de cargos e o encaminhamento completo dependem de H01/H39/?08; não pressupor P02 como usuário da Mesa. |
| [F] ED01/ED02 documentam imagem vinculada a metadados e transmissão à RFB. | [H11/H26] Manter o caso identificável e conferir correspondência entre imagem, região e parecer; upload local é demonstrativo. | Não simular transmissão automática como se fosse integração real. Campos usados pelo analista ainda a investigar. |
| [F] C02 documenta o registro motivado do ato e a responsabilidade do auditor. | [H28/H32] O parecer identifica caso, autoria e fundamento como apoio; seu formato e guarda não substituem os registros institucionais. | Não implementar histórico agregado ou prometer conformidade legal da trilha sem evidência. |
| [F] Os quatro canais do despacho possuem semântica própria (C02/RC05). | Separar canal aduaneiro, resultado do modelo e conclusão da imagem; nenhum score determina o canal. | A ligação entre imagem e parametrização permanece ?08. |
| [F] A pesquisa usa fontes públicas e casos fictícios (Entrega 7). | Não expor declarações, cargas ou pessoas identificáveis; consentimento e acesso restrito para dados de pesquisa. | A demonstração não pressupõe acesso a sistemas fiscais restritos. |

Fontes já investigadas: [C02](02_analise_concorrencia.md) e [ED01–ED03 e aspectos éticos](07_coleta_dados.md). As regras locais de retenção e guarda citadas nas entregas anteriores conservam seu alcance local; não são generalizadas para todos os portos.

### 2.2 Princípios de interface

| Contexto de uso | Referência | O que orienta e por que importa | Link |
|---|---|---|---|
| P01 compara a imagem com o destaque do modelo. | Mayhew — engenharia de usabilidade, conforme aula 8 | Relacionar usuário, tarefa e plataforma antes de fixar a solução; avaliar e revisar as decisões com base nas metas. | [Material da aula 8 no Moodle](https://moodle.fei.edu.br/mod/resource/view.php?id=2524), págs. 8–15; [perfil](03_personas_contexto_jornada.md) e [tarefas](05_analise_tarefas.md). |
| Radiografia e camada do modelo usam informação visual. | WCAG 2.2 — 1.4.1 e 1.4.3 | Usar texto além da cor e contraste de 4,5:1 para texto comum e 3:1 para texto grande, para favorecer a leitura dos rótulos e avisos. | [Uso de cor](https://www.w3.org/TR/WCAG22/#use-of-color) e [contraste](https://www.w3.org/TR/WCAG22/#contrast-minimum). |
| Controles usados com teclado e mouse na estação. | WCAG 2.2 — 2.1.1, 2.4.7 e 4.1.2 | Oferecer teclado, foco visível e nomes acessíveis. Comparar não deve depender apenas de manter a tecla C pressionada. | [Teclado](https://www.w3.org/TR/WCAG22/#keyboard), [foco](https://www.w3.org/TR/WCAG22/#focus-visible) e [nome/papel/valor](https://www.w3.org/TR/WCAG22/#name-role-value). |
| P01 preenche e revisa o parecer. | WCAG 2.2 — 3.3.1 e 3.3.3 | Identificar o campo incompleto e explicar a correção, preservando as demais informações para evitar retrabalho. | [Identificação de erro](https://www.w3.org/TR/WCAG22/#error-identification) e [sugestão de correção](https://www.w3.org/TR/WCAG22/#error-suggestion). |
| A análise pode exigir voltar à imagem e corrigir um achado. | Controle do usuário e reversibilidade | Permitir ocultar mapa, restaurar ajustes e editar/excluir marcações antes da exportação. Confirmar descarte ao trocar o caso. | [Protótipo e estados de recuperação](06_prototipacao_papel.md), RC01/RC09. |
| Resultado automático e decisão humana têm alcances diferentes. | Clareza da comunicação e divisão de responsabilidades | Distinguir resultado do modelo e parecer. A interface não usa liberação de carga como sinônimo de conclusão da imagem. | [Evidências ED01–ED05 e limites](07_coleta_dados.md), H31/H39. |
| Demonstração e futura avaliação usam casos e anotações. | Minimização de dados e consentimento | Usar identificação fictícia; não expor operações reais nem dados pessoais nos resultados publicados. | [Aspectos éticos e armazenamento](07_coleta_dados.md). |

O link do material de aula exige acesso ao Moodle da FEI; a referência foi conferida na cópia local. Esses critérios orientam o projeto; sua inclusão não declara conformidade integral do protótipo com a WCAG.

## 3. Metas de usabilidade

### 3.1 Metas qualitativas

| Meta | Público/tarefa | Evidência desejada | Motivo |
|---|---|---|---|
| Entender o papel da IA | P01/P02, leitura da triagem | Explicar que mapa e indicador apoiam a análise, sem provar ilícito. | Evitar confiança excessiva no resultado (H31/H37). |
| Comparar sem perder o contexto | P01, T01/T02 | Alternar a camada e localizar a mesma região na imagem original. | Preservar a leitura da radiografia (H30, RC09). |
| Produzir um parecer compreensível | P01, T03/PF02 | Parecer com caso, região comentada e conclusão técnica, produzido sem ajuda. | Preservar o achado na emissão (R03). |
| Compreender o parecer recebido | P02, consulta externa associada a T05 | Localizar caso, região, comentário e conclusão no PDF, identificar informação insuficiente e explicar seus limites. | Avaliar a comunicação do artefato recebido; não avaliar T06 nem uso de uma interface de P02 na Mesa. |

### 3.2 Metas quantitativas

São **critérios propostos**, ainda sem resultados. Nas Entregas 12–14, prever três participantes externos à equipe, como exige a Entrega 14. Priorizar o perfil profissional; se forem utilizados proxies, registrar a relação de cada um com a tarefa e limitar a conclusão à interação. A sessão começa com a mesma apresentação dos controles, sem treino das tarefas avaliadas.

| ID | Dimensão e tarefa | Métrica e meta | Como medir | Justificativa |
|---|---|---|---|---|
| MU01 | Eficácia — comparar original/mapa (T01/T02, PF01) | 3/3 concluem sem ajuda: localizar região indicada, ocultar o mapa e voltar à comparação. | Registrar sucesso e intervenções por participante. | A comparação é a tarefa central de AC02. |
| MU02 | Compreensão — interpretar triagem (PF01) | 3/3 distinguem indicação do modelo de prova de ilícito e de autorização de liberação. | Pergunta aberta após a tarefa, avaliada pelos dois critérios. | A interpretação errada afeta toda a análise. |
| MU03 | Eficácia — registrar parecer (P01, T03/PF02) | 3/3 geram parecer com caso correto, região comentada, responsável fictício e conclusão. | Conferir os quatro itens no documento produzido. | O registro precisa preservar a relação entre achado e caso. |
| MU04 | Eficiência — registrar um achado (PF02) | Mediana de até 3 minutos, sem ajuda. | Cronometrar da instrução, com caso já aberto, até a exportação; anotar falhas separadamente. | [H] Baseline inicial proposta pela equipe para uma região e comentário curto, sem medição anterior. Rever após a primeira rodada, preservando os tempos observados; não representa produtividade portuária. |
| MU05 | Prevenção/recuperação — parecer incompleto e falha de exportação | Nenhuma exportação sem campos exigidos; 3/3 corrigem a omissão e repetem exportação sem perder dados. | Tentar exportar sem responsável e simular uma falha após o preenchimento. | Evitar documento incompleto e retrabalho. |
| MU06 | Satisfação — comparação e registro | Mediana ≥ 4 em escala de satisfação de 1 a 5. | Perguntar após cada tarefa: “Quão satisfeito(a) você ficou com a interação nesta tarefa?”, de 1 (muito insatisfeito) a 5 (muito satisfeito), com comentário opcional sobre o motivo. | Complementar tempo e sucesso com satisfação declarada; a medida não demonstra confiança no modelo nem facilidade de uso por si só. |

“Sem ajuda” significa sem orientação do facilitador após a instrução; consultar a ajuda da própria interface é permitido e será registrado. Em amostra de três pessoas, apresentar contagens individuais, mediana e falhas, sem generalização estatística. Tempos acima do limite ou tarefas não concluídas permanecem no relatório, sem descarte para melhorar a meta.

### 3.3 Prioridades das cinco dimensões de Nielsen

[H] Pesos de projeto propostos pela equipe para o contexto atual, não resultados de avaliação ou percentuais de desempenho.

| Dimensão de Nielsen | Peso | Justificativa no contexto | Metas específicas relacionadas |
|---|---:|---|---|
| Facilidade de aprendizado | 25% | Compreender resultado automático, marcações e parecer na primeira utilização, sem treinamento da tarefa avaliada. | MU01/MU02/MU03 |
| Facilidade de memorização | 10% | Retomar comparação e registro após intervalo; a frequência profissional permanece hipótese. | MU01/MU03 como tarefas de referência; medir retenção exige sessão de retorno. |
| Eficiência | 15% | Concluir o registro sem retrabalho, preservando a qualidade da análise. | MU04; recuperação em MU05 |
| Baixa taxa de erros | 35% | Evitar confusão entre indício, parecer e ato formal; impedir documentos incompletos e perda de dados. | MU02/MU03/MU05 |
| Satisfação positiva do usuário | 15% | Avaliar a experiência declarada na comparação e no registro. | MU06 |
| **Total** | **100%** | Prioridade relativa das dimensões. | MU01–MU06 continuam critérios específicos. |

As MU dizem o que será observado no protótipo; os pesos expressam a importância das cinco dimensões. MU01/MU03 na primeira utilização podem informar aprendizado; não demonstram memorização. Para esta última, planejar nas Entregas 12–14 retorno após sete dias, repetindo comparação e registro sem reapresentar os controles, registrando sucesso, ajuda e tempo por participante. [H] Sete dias é uma condição inicial de teste, não uma frequência de trabalho observada. Se não houver retorno, relatar memorização como não avaliada.

## 4. Ciclo de revisão

A organização segue a **engenharia de usabilidade de Mayhew**, trabalhada na aula: perfil e tarefas alimentam plataforma, princípios e metas; seguem-se modelo conceitual, protótipos e avaliações iterativas. No recorte da disciplina, o ciclo é **compreender o contexto → definir requisitos → projetar → avaliar → revisar**. A pesquisa documental sustenta a primeira definição; a ausência de acesso profissional continua como limite da base de conhecimento.

No ciclo de Mayhew, a análise de requisitos reúne perfil, tarefas, plataforma, princípios e metas (Entregas 1–8). O projeto essencial/reengenharia do trabalho revê como a comparação e o registro podem apoiar P01 sem assumir o ato de P02; o modelo conceitual organiza objetivos e signos (Entrega 9). Protótipos e avaliação verificam esse modelo; padrões de tela e diálogo orientam a consistência (Entregas 10/11), e o projeto detalhado é avaliado e revisto quando as metas não forem alcançadas (Entregas 12–14). São níveis de projeto, com retornos aos requisitos quando necessário.

A Entrega 9 transforma PF01/PF02 em objetivos e signos; as Entregas 10/11 modelam e prototipam a interação. A avaliação heurística verifica estados, linguagem e recuperação; o teste observado verifica MU01–MU06. Quando uma meta falhar, registrar o problema e sua origem na rastreabilidade, revisar o fluxo e repetir a tarefa afetada. Evidência nova sobre H39 ou H42 também pode exigir revisão das personas e das tarefas.

## Checklist

- [x] Capacidades e restrições têm consequências de IHC.
- [x] Contribuição técnica e camada de interação estão separadas.
- [x] Dados, resultados e espera simulados foram explicitados.
- [x] As metas avaliam a interação e não substituem métricas do TCC.
- [x] Tabela de princípios contém contexto, referência, justificativa e link.
- [x] Metas indicam público, tarefa, medida e limite aceitável.
- [x] Eficácia, eficiência e satisfação foram consideradas.
- [x] Critérios podem ser verificados nas Entregas 12–14.

## Referências

- AQUINO JR., Plinio T. *Processos de Projeto de IHC*, Parte A+B, págs. 13–15, e Parte C, págs. 3–6. Material da aula 8, baseado em Barbosa e Silva (2010). Cópia local: `Estudos/FEI_CC8122_IHC/08 - Tópico 8/`.

- Entregas [5](05_analise_tarefas.md), [6](06_prototipacao_papel.md) e [7](07_coleta_dados.md); [rastreabilidade](../RASTREABILIDADE.md).
- W3C. *Web Content Accessibility Guidelines (WCAG) 2.2*. Recomendação de 2024. [Critérios de acessibilidade](https://www.w3.org/TR/WCAG22/). Acesso em 04/11/2026.
- BARBOSA, S. D. J.; SILVA, B. S. *Interação Humano-Computador*. Elsevier/Campus. Referência conceitual da [bibliografia da disciplina](../BIBLIOGRAFIA.md).
- TCC da equipe: `IHC/TCC/TCC-VisaoRaioxContainer/codigo/main.py`, consultado para caracterizar a contribuição técnica. A avaliação de IHC não depende da execução desse código.

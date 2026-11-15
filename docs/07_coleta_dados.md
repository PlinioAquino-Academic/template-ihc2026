# Entrega 7 — Coleta de dados, necessidades e aspectos éticos

**Data:** 04/11/2026<br>
**Status:** 🟩 concluída<br>
**Responsabilidade:** contribuições individuais e síntese da equipe

## Objetivo e método

Levantar informações para a Mesa de inspeção de raio-X de contêineres: quem analisa a imagem, quais dados consulta e como registra e encaminha uma suspeita.

[F] Não houve acesso ao profissional nem aplicação dos instrumentos com pessoas. [H] O plano obrigatório utiliza investigação contextual (I01), questionário (I02) e entrevista semiestruturada (I03), métodos permitidos e distintos. A falta de acesso é limitação de recrutamento, não autorização para substituir o método. [F] Cinco fontes públicas foram consultadas como **pesquisa documental complementar** (ED01–ED05).

O levantamento retoma as hipóteses da [Entrega 1](01_conhecendo_o_problema.md), a análise de concorrentes, as personas, os cenários, as tarefas e o [protótipo da Entrega 6](06_prototipacao_papel.md). Os documentos ajudam a fundamentar o projeto, mas não revelam todas as práticas de uma unidade portuária.

## Hipóteses prioritárias

| Hipóteses/lacunas | O que precisamos saber | Decisão afetada | Prioridade |
|---|---|---|---|
| H01, H39 | Quem opera o escâner, interpreta a imagem e decide sobre a carga? | Papéis de P01/P02 e significado do parecer. | alta |
| H11, H26 | Quais dados acompanham a imagem e como chegam ao sistema? | Contexto da carga e entrada de imagens. | alta |
| H06, H28, H32, ?08 | Como a suspeita é registrada e ligada ao despacho? | Conteúdo e encaminhamento do parecer. | alta |
| H03, H42 | Quem realiza a conferência física e que informação recebe? | Papel de P03 como usuário ou stakeholder. | alta |
| H04, H41 | Existe fila de imagens e autonomia para mudar a ordem? | Necessidade de priorização. | alta |
| H30, H31, H37 | Como apresentar a comparação, o mapa e o indicador do modelo? | Organização visual e linguagem. | média |
| H10, H16, H34, ?07 | Quais dificuldades, condições de trabalho e metas existem? | Requisitos de uso e benefícios a avaliar. | média |

## Parte A — necessidades e aspectos éticos

### Dados a investigar — cinco grupos da aula

| Grupo | Informação relevante para nosso projeto | Uso no design e forma de obter |
|---|---|---|
| O próprio usuário | Papel, formação necessária, vocabulário profissional e necessidades de leitura/acessibilidade. | Identificar quem interpreta a imagem e adequar termos e legibilidade. Documentos ajudam a definir o papel; características pessoais continuam desconhecidas. Não coletar sexo ou renda sem necessidade para o projeto. |
| Relação com tecnologia | Softwares de inspeção conhecidos, uso de mouse/teclado, monitor e ferramentas de realce disponíveis. | Reaproveitar convenções e dimensionar a comparação. Manuais mostram capacidades; experiência e preferências pessoais exigiriam contato direto. |
| Conhecimento do domínio | Prática com radiografias de carga, leitura da declaração e entendimento dos limites da IA. | Definir explicações do mapa e do indicador. Distinguir experiência em logística de experiência em interpretação radiográfica. |
| Conhecimento das tarefas | Responsabilidades, sequência, frequência, consulta de dados e consequência dos erros. | Priorizar comparação e parecer. Investigar H01/H11/H39; fila e frequência continuam abertas quando não documentadas. |
| Motivações e valores | O que caracteriza uma análise bem feita, confiança no registro, autonomia e preferência de treinamento. | Orientar ajuda e comunicação da incerteza. Documentos não revelam sentimentos ou preferências individuais: H37/H38 continuam hipóteses. |

**De quem obter:** o perfil principal é quem interpreta a imagem (P01); a autoridade que recebe o parecer e decide (P02) também interessa. A RFB e a administração do recinto definem os processos documentados. Depositário, representantes da carga e equipe de conferência são afetados, mas isso não demonstra uso direto da Mesa por P03. Não houve coleta com essas pessoas; o levantamento atual é documental.


### A01 — análise da imagem

**Autor(a):** Kawan Mark Geronimo Da Silva — 22.222.010-5

| Dados a coletar | Por que coletar / decisão de design | Hipóteses |
|---|---|---|
| Recursos de comparação, realce e marcação disponíveis nas estações | Conhecer as ferramentas existentes e orientar a comparação no protótipo. | H05, H09, H30 |
| Significado do mapa e do indicador do modelo | Explicar o resultado sem sugerir certeza de ilícito. | H31, H37 |
| Equipamento e contexto de uso documentados | Definir premissas de tela e identificar o que ainda depende de pesquisa com usuários. | H14, H15, H16 |

**De quem/fontes:** documentos sobre o trabalho de P01, publicados por fabricantes de scanners de carga e pesquisadores dos métodos utilizados. Incluir fontes com autoria e descrição do recurso; excluir radiologia médica e materiais sem origem identificável.

**Ética:** citar as fontes e respeitar a licença das imagens. Não publicar nomes de operadores, placas ou cargas identificáveis. O destaque do modelo deve ser apresentado como apoio à análise, sem atribuir a ele uma capacidade de identificar ilícitos que o TCC não demonstrou.

### A02 — registro e responsabilidades

**Autor(a):** Gabriel Albertini Pinheiro — 22.122.094-8

| Dados a coletar | Por que coletar / decisão de design | Hipóteses/lacunas |
|---|---|---|
| Responsabilidades do recinto, de quem analisa e da fiscalização | Separar o parecer técnico da decisão sobre a carga. | H01, H39 |
| Dados vinculados à imagem e forma de transmissão | Identificar o caso corretamente e evitar entrada manual desnecessária. | H11, H26 |
| Registro e encaminhamento da suspeita | Definir o conteúdo do parecer e sua relação com o processo. | H06, H28, H32, ?08 |

**De quem/fontes:** manuais públicos da Receita Federal e do Siscomex que descrevam os papéis de P01/P02, dados e procedimentos. Registrar a data e o alcance da fonte; uma orientação local não será tratada como regra de todos os portos.

**Ética:** não acessar declarações fiscais, processos identificáveis ou telas restritas. Usar apenas campos e procedimentos públicos. O PDF do protótipo é um registro de apoio, sem valor de autorização para desembaraço.

### A03 — conferência física

**Autor(a):** Alexandre Domiciano Pierri — 22.125.061-6

| Dados a coletar | Por que coletar / decisão de design | Hipóteses/lacunas |
|---|---|---|
| Atores e finalidade da verificação física | Delimitar o papel de P03. | H03, H39, H42 |
| Informações usadas para localizar e verificar a suspeita | Investigar o que precisa acompanhar o parecer. | H28, ?08 |
| Registro do achado e retorno a quem analisou a imagem | Investigar a comunicação entre análise e conferência. | H17, H38, ?08 |

**De quem/fontes:** documentação institucional sobre fiscalização, depositário e representante do importador. Incluir textos que diferenciem suas responsabilidades. A existência de conferência física, sozinha, não demonstra que P03 usa nossa interface.

**Ética:** não usar fotos de apreensões ou operações identificáveis. Os episódios dos cenários anteriores continuam ficcionais. A pesquisa não envolve gravações nem contato com equipes de fiscalização.

**Armazenamento e privacidade:** referências e sínteses sem dados pessoais permanecem no repositório. Cópias de trabalho serão mantidas apenas quando a licença permitir e descartadas até 90 dias após o encerramento da disciplina. Se houver aplicação dos instrumentos abaixo, respostas e consentimentos ficarão restritos à equipe, identificados por códigos, com descarte no mesmo prazo. Não serão solicitados nome, empregador, unidade exata ou informações sigilosas.

## Parte B — instrumentos de coleta

### I01 — investigação contextual

**Autor(a):** Kawan Mark Geronimo Da Silva — 22.222.010-5.<br>
**Técnica:** investigação contextual, distinta do questionário I02 e da entrevista I03.<br>
**Situação:** [H] instrumento planejado, não aplicado. A pesquisa documental ED01–ED05 é complementar, não cumpre esta responsabilidade individual.

**Objetivo:** compreender a atividade situada de exame e registro: sequência real, informações consultadas, alternância entre ferramentas, interrupções, dúvidas e comunicação com quem decide (H01/H05/H11/H16/H28/H30/H31/H39/H41/?08). Observar o trabalho e esclarecer brevemente a ação no seu contexto, sem conduzir uma entrevista isolada da atividade.

**Público/recrutamento:** planejar três sessões individuais: duas com adultos que interpretam radiografias de carga (P01) e uma com quem recebe a análise para decidir (P02). Incluir experiência direta na respectiva atividade e autorização institucional para observação; excluir menores, quem não consentir e situações em que não seja possível evitar dados sigilosos. Convidar por contato institucional autorizado, informando finalidade acadêmica, duração de 45–60 minutos, ausência de avaliação individual e proibição de fornecer dados de operações. Não abordar profissionais durante fiscalização nem coletar contato no instrumento.

**Alternativa de acesso:** [?] recrutamento profissional ainda não disponível. Se for utilizado adulto de logística/área próxima, realizar somente simulação com caso fictício e registrar `proxy/simulação`. A simulação permite verificar entendimento e coordenação proposta; não demonstra rotina, frequência, pressão ou prática de P01/P02. Não misturar seus registros com os profissionais. Não realizar observação real sem as autorizações necessárias.

**Abertura/consentimento a ler:** “Sou integrante da equipe 09 de IHC da FEI. Queremos entender como informações e ferramentas apoiam o exame de imagens de cargas e o registro da conclusão. A sessão dura de 45 a 60 minutos e não avalia seu desempenho pessoal. Participar é voluntário; pode pular explicações, pedir pausa ou encerrar sem prejuízo. Usaremos somente notas anonimizadas, sem gravação, fotografias, nomes, placas, empresas, números de processo ou cópias de telas operacionais. Não mostre informações sigilosas; interromperemos o registro se elas surgirem. As notas ficarão restritas à equipe e serão descartadas até 90 dias após o encerramento da disciplina. Antes de começar, você receberá código, prazo e canal privado para pedir exclusão, conforme o procedimento ético desta entrega. Você autoriza a observação e as notas escritas?” Registrar sim/não; se não, encerrar sem notas de trabalho.

**Procedimento padronizado:**

1. Confirmar critério de inclusão e permissão; preparar ficha sem identificação pessoal. Distinguir profissional em contexto real de proxy em simulação. Entregar código e informar prazo/canal de exclusão antes do consentimento. Não aplicar enquanto a pendência de contato não estiver resolvida.
2. Apresentar objetivo e ler a abertura; registrar consentimento e autorização para notas. O participante controla o que pode ser observado. Preferir exemplo sanitizado pela instituição; em proxy, usar caso fictício e os estados da Entrega 6.
3. Pedir que mostre uma atividade de análise/recebimento do resultado que conhece diretamente. Observar primeiro, sem demonstrar a solução da equipe nem direcionar a sequência.
4. Registrar eventos e esclarecer no momento adequado com o roteiro abaixo; evitar interromper decisões críticas. Não cronometar produtividade profissional nem transcrever dados da carga.
5. Recapitular a sequência anotada e pedir correção da interpretação, distinguindo observação, explicação do participante e inferência da equipe. Não apresentar preferências como regra geral.
6. Encerrar, agradecer, reafirmar o código/prazo/canal e guardar as notas em área restrita. Publicar somente síntese anonimizada, com limites do contexto e da amostra.

**Instrumento integral de observação e esclarecimento:**

| Bloco | O que observar | Pedido neutro de esclarecimento | Hipóteses |
|---|---|---|---|
| Início e papel | Evento que leva à análise e quem assume cada etapa. | “O que iniciou esta atividade e qual parte cabe a você?” | H01/H39 |
| Contexto do caso | Tipos de informação consultados e onde são encontrados, sem registrar valores reais. | “Que informação você procura neste momento e para quê?” | H11/H26 |
| Sequência e ferramentas | Mudanças de ferramenta, comparação, realce e exame da imagem. | “O que você procura esclarecer com esta ação? Como sabe quando seguir?” | H05/H09/H30/H43 |
| Dúvida e resultado automático | Estratégia perante indicação insuficiente ou discordância, se existir no trabalho observado. | “O que faz quando a informação não é suficiente? Usa alguma indicação automática? Como a interpreta?” | H12/H31/H37 |
| Interrupção e prioridade | Interrupções efetivamente ocorridas e retomada, sem supor fila. | “Como retoma o que estava fazendo? Quem define o próximo caso, quando isso se aplica?” | H16/H41 |
| Registro e passagem entre papéis | Tipo de registro, destinatário e confirmação de recebimento. | “O que precisa acompanhar essa conclusão e quem recebe depois?” | H28/H32/H39/?08 |
| Retorno e avaliação | Como verifica se terminou e se recebe algum desfecho. | “Como percebe que sua parte terminou? Que retorno recebe sobre o resultado?” | H38/?08 |

**Ficha por evento:** código da sessão; perfil amplo; real/proxy; contexto sanitizado; minuto relativo; ação observada; tipo de ferramenta/informação; dificuldade ou interrupção; esclarecimento parafraseado; interpretação da equipe; hipótese associada; correção solicitada pelo participante. Não registrar imagem, identificadores ou descrições de ameaças específicas. Assinalar `não observado` em vez de inferir ausência.

**Análise:** reconstruir sequências de trabalho por perfil; agrupar alternância, comunicação, dúvidas e retomada. Comparar observação e explicação com ED01–ED05, marcando sustentação parcial, divergência ou lacuna em cada hipótese. Separar proxies e contextos; contagem de eventos em três sessões não representa frequência profissional. Só propor mudança em comparação, filtros, contexto da carga ou parecer quando houver evidência compatível, registrada na matriz.

### I02 — questionário

**Autor(a):** Gabriel Albertini Pinheiro — 22.122.094-8<br>
**Objetivo:** investigar a compreensão do resultado apresentado pela interface (H31, H37).<br>
**Público:** adultos externos à equipe, com experiência em inspeção de cargas ou área próxima. Respostas de pessoas sem essa experiência serão analisadas separadamente, apenas quanto à compreensão da informação.<br>
**Situação:** instrumento preparado, não aplicado.

**Procedimento:** apresentar o objetivo e o consentimento, mostrar o mesmo exemplo a todos e aplicar as perguntas sem explicar previamente as respostas. Duração prevista: 5 a 10 minutos. Não coletar nome ou contato; permitir pular questões e encerrar a participação.

**Consentimento:** “Este questionário acadêmico investiga a compreensão de uma interface. Participar é voluntário e você pode interromper sem prejuízo. Não informe pessoas, empresas ou operações identificáveis. As respostas serão usadas sem identificação e descartadas até 90 dias após o encerramento da disciplina. Você aceita participar?” **Sim / Não (encerrar).**

**Exemplo apresentado:** “A tela mostra uma radiografia, um mapa colorido e o cartão ‘Indício de anomalia — 94%; limiar 70%’. Uma pessoa registra o parecer.” Os valores são ilustrativos do protótipo.

1. Qual sua relação com inspeção de cargas? **Interpreto radiografias / atuo em logística ou atividade aduaneira / estudo ou pesquiso IA / não tenho experiência / prefiro não responder.**
2. O que você entende por “indício de anomalia”? **Resposta aberta.**
3. O que o valor “94%” significa para você? **Resposta aberta.**
4. O que o mapa colorido permite concluir? **Resposta aberta.**
5. Que informação falta para compreender o resultado? **Resposta aberta.**
6. A diferença entre resultado do modelo e parecer humano está clara? **1 — nada clara a 5 — muito clara / não sei avaliar.** Explique, se desejar.
7. Que expressão você mudaria na tela e por quê? **Resposta aberta, opcional.**

**Encerramento e análise:** esclarecer que o resultado não comprova ilícito nem autoriza liberação da carga. Fornecer um código para solicitar exclusão antes da consolidação. Contar respostas por perfil e agrupar dúvidas sobre indicador, mapa e decisão humana. A análise serve para revisar a linguagem; não mede aceitação profissional ou desempenho do algoritmo.

### I03 — entrevista semiestruturada

**Autor(a):** Alexandre Domiciano Pierri — 22.125.061-6<br>
**Objetivo:** aprofundar a comunicação entre análise da imagem, decisão e conferência física.<br>
**Público:** profissional de inspeção de cargas ou área aduaneira/logística, respondendo sobre atividades que conhece diretamente.<br>
**Situação:** roteiro preparado, não aplicado.

**Procedimento:** explicar o objetivo, apresentar o consentimento do I02 adaptado à entrevista e pedir autorização para notas escritas. Conversa de aproximadamente 20 minutos, sem gravação. Permitir interrupção, não solicitar exemplos identificáveis e aceitar perguntas sem resposta. Ao final, recapitular as notas para correção e fornecer código para exclusão antes da consolidação.

**Roteiro:**

1. Com quais atividades de inspeção ou despacho você tem experiência direta?
2. Quem opera o escâner, interpreta a imagem e formaliza a decisão? Esses papéis coincidem?
3. Que informações são consultadas junto da imagem e onde ficam disponíveis?
4. Como uma suspeita é registrada e encaminhada? O que acompanha esse registro?
5. Como é definida a ordem de análise e quem pode alterá-la?
6. O que acontece quando a imagem deixa uma dúvida?
7. Que informação chega a quem realiza a conferência física? Essa pessoa consulta imagens?
8. Onde o desfecho é registrado e quem recebe retorno?
9. Que dificuldade de comunicação você já observou, sem identificar pessoas ou operações?

**Análise:** organizar as notas por papéis, informações, registros e dificuldades. Separar experiência direta de suposição e comparar com os documentos. Um relato descreve seu contexto; não representa todos os recintos. Guardar as notas conforme as regras de privacidade da Parte A.

### Preparação dos instrumentos online

Os dois instrumentos foram criados no Google Forms em **05/11/2026**, com acesso verificado sem login e coleta de e-mail desativada:

- **I02 — [Questionário de compreensão da triagem](https://docs.google.com/forms/d/e/1FAIpQLSdSndNp5FioH8sv7jDSutkHYdAmeOqOeKNn247wJcviVF-Pkg/viewform)** — Gabriel. [Captura do formulário vazio](../assets/07_coleta/i02_questionario.png).
- **I03 — [Roteiro de entrevista](https://docs.google.com/forms/d/e/1FAIpQLSfsc7UUP9KlAzQQzuqxQjVzSOzdyPg5rU0ag7LPhFXdi7pfGg/viewform)** — Alexandre. Formulário para notas do entrevistador, não para resposta autônoma do participante. [Captura do roteiro vazio](../assets/07_coleta/i03_roteiro_entrevista.png).

Os instrumentos estão publicados, mas **não foram aplicados**. A verificação percorreu as seções sem enviar respostas. O conteúdo textual permanece acima; o [código de criação e os links de edição](../instrumentos/07_coleta/README.md) também foram preservados.

## Resultados da pesquisa documental

Foram consultados cinco documentos em **04/11/2026**. As referências completas estão ao final.

| Evidência | Fonte e localização | Informação encontrada | Consequência para o projeto |
|---|---|---|---|
| ED01 | D01 — primeiro parágrafo e “Transmissão de Imagens” | O recinto disponibiliza equipamento e operação; as imagens são transmitidas à RFB, com integração ao SICA/API Recintos. | Refina H01, H26 e H39. O upload local é adequado à demonstração, mas não representa toda a entrada institucional. |
| ED02 | D02 — “Evento Inspeção não Invasiva” | O envio reúne imagem e metadados do escâner, com atributos da unidade inspecionada. | Sustenta parte de H11: existem dados vinculados à imagem. Não mostra quais deles o analista consulta em tela nem resolve ?08. |
| ED03 | D03 — parágrafos sobre meios e responsáveis pela verificação | O manual prevê uso de imagens e diferencia fiscalização, atuação sob supervisão e participação do depositário. | Refina os atores de H39/H42. P03 permanece stakeholder, pois não há evidência de uso direto da solução. |
| ED04 | D04 — itens “High Density” e “Similar Cargo” | O fabricante oferece destaque de alta densidade e comparação lado a lado entre radiografias. | Refina H30: há referência de mercado para comparação, sem demonstrar preferência entre original/mapa lado a lado e sobreposição. |
| ED05 | D05 — resumo do artigo | Grad-CAM destaca aproximadamente as regiões relevantes para uma predição. | Orienta a linguagem de H31/H37: o mapa indica relevância para o modelo, não delimitação exata ou prova de ilícito. |

As entregas iniciais usavam o termo **mapa residual**, associado a autoencoder. A Entrega 6 passou a descrever classificação e mapas de atenção. Nesta entrega, a indicação visual é tratada conforme o método utilizado: mapa de atenção e mapa residual não são equivalentes. O limiar e o indicador do protótipo também não representam uma medida comprovada de probabilidade de ilícito.

## Síntese

A pesquisa fundamenta a separação entre operação, análise e decisão, a vinculação de dados à imagem e a comparação visual como recurso de apoio. Para PF01/PF02, isso orienta a identificação do caso, a preservação da radiografia original e o registro do parecer com justificativa.

H01/H39, H11/H26 e H30 foram **refinadas ou parcialmente sustentadas**, no alcance descrito acima. H28, H32 e ?08 continuam sem resposta sobre o caminho completo do parecer até a decisão. H04/H41 (fila e autonomia), H10/H16 (fadiga e ambiente), H31/H37 (compreensão e aceitação) e H34 (redução de esforço) permanecem abertas. Nenhuma hipótese de comportamento profissional foi integralmente refutada ou confirmada.

Esses resultados estão registrados na [rastreabilidade](../RASTREABILIDADE.md#21a-atualização-documental-da-entrega-7). Eles orientam as próximas etapas de modelagem e avaliação, sem atribuir à pesquisa documental a observação de uma rotina profissional.

## Relação com a aula

A Parte A segue os cinco grupos da aula 7 (Parte A, páginas 2–8 e exercício da página 13). A Parte B apresenta instrumentos e protocolos, como solicitado na Parte B, páginas 20–21. Investigação contextual, questionário e entrevista compõem o planejamento. A pesquisa documental permanece evidência secundária complementar, sem ser contabilizada como método individual obrigatório.

## Checklist

- [x] Cinco grupos de dados da aula relacionados ao projeto.
- [x] Hipóteses e lacunas da Entrega 1 retomadas.
- [x] Dados, fontes e decisões de design relacionados ao projeto.
- [x] Uma Parte A por integrante, com autoria e aspectos éticos.
- [x] Três instrumentos completos, com técnicas distintas e questionário incluído.
- [x] Procedimentos de aplicação e análise definidos.
- [x] Perguntas sem pressupor necessidade de funcionalidades.
- [x] Pesquisa documental realizada, com fontes e localização dos achados.
- [x] Instrumentos preparados diferenciados de coleta realizada.
- [x] Limitações e hipóteses ainda abertas registradas.
- [x] Rastreabilidade atualizada.
- [x] Instrumentos criados no Google Forms e links verificados sem login.

## Referências

- AQUINO JR., Plinio T. *Identificação de Necessidades dos Usuários e Requisitos de IHC*, Partes A e B. Material da aula 7, baseado em Barbosa e Silva (2010). Cópia local: `Estudos/FEI_CC8122_IHC/07 - Tópico 7/`.

Acesso às fontes em 04/11/2026.

- **D01 — Receita Federal.** *Disponibilização, Manutenção e Operação de Instrumentos de Inspeção não Invasiva*. 2024. [Manual de Alfandegamento](https://www.gov.br/receitafederal/pt-br/assuntos/aduana-e-comercio-exterior/manuais/alfandegamento/requisitos-para-o-alfandegamento/requisitos-tecnicos-e-operacionais/disponibilizacao-manutencao-e-operacao-de-instrumentos-e-aparelhos-de-inspecao-nao-invasiva).
- **D02 — Siscomex.** *Recintos — perguntas frequentes*. Seção “Evento Inspeção não Invasiva”, respostas atualizadas em 2022 e 2024. [Documento](https://www.gov.br/siscomex/pt-br/informacoes/perguntas-frequentes/perguntas-frequentes-recintos).
- **D03 — Receita Federal.** *Verificação Física da Mercadoria — Introdução*. Atualizado em 2020. [Manual de Importação](https://www.gov.br/receitafederal/pt-br/assuntos/aduana-e-comercio-exterior/manuais/despacho-de-importacao/topicos-1/despacho-de-importacao/etapas-do-despacho-aduaneiro-de-importacao/conferencia-aduaneira/verificacao-da-mercadoria-1/introducao).
- **D04 — Rapiscan AS&E.** *InSight Intelligent Image Analytics*. Sem data. [Página do produto](https://www.rapiscan-ase.com/products/software/insight-operator-assist-tools).
- **D05 — Selvaraju et al.** *Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization*. ICCV, 2017; versão ampliada, 2019. [Artigo, versão 4](https://arxiv.org/abs/1610.02391v4).

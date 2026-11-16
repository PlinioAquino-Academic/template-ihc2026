# Entrega 4 — Cenários de análise/problema

**Data:** 05/10/2026  
**Status:** 🟦 revisada após feedback  
**Revisão:** 12/11/2026  
**Responsabilidade:** 1 solução completa da atividade por integrante: Paulo Andre de Oliveira Hirata — C01; Victor Merker Binda — C02.

## Objetivo da atividade

Descrever situações atuais em que o responsável por um pequeno comércio digital e seu auxiliar tentam realizar atividades de reposição e controle de estoque, mas encontram dificuldades. Os cenários tornam explícitos os atores, os objetivos, o contexto, o planejamento, as ações, os eventos, a avaliação e as consequências dos problemas, sem antecipar a interface do TCC.

O trabalho se relaciona à **previsão de demanda com aprendizado de máquina para apoiar o planejamento de reposição em pequenos comércios**. A formulação anterior incluía recomendação de quantidade e momento; essa capacidade permanece pendente de confirmação no escopo formal do TCC. A participação de vendas online é um refinamento hipotético da Entrega 3. Nesta entrega, porém, o foco está na atividade humana que motiva o projeto, e não na execução do algoritmo ou nas funcionalidades da futura aplicação.

> **Regra central:** os cenários contam a história do problema antes da adoção da solução do TCC. Caderno, calculadora, planilha e mensagens aparecem como recursos da rotina atual hipotética; não como componentes de uma nova interface.

### Base e continuidade com as entregas anteriores

- **P01 — Mariana Alves:** 65 anos, proprietária de pequeno comércio que também vende pela internet, experiente nas decisões comerciais e com pouca familiaridade com sistemas digitais. A baixa experiência tecnológica pertence ao perfil construído, não é uma consequência presumida da idade.
- **P02 — Rafael Costa:** 22 anos, auxiliar operacional e de estoque, familiarizado com formulários, buscas, marketplaces e planilhas. Apoia os registros e as conferências, sem assumir sozinho decisões financeiras de compra.
- **C01** aprofunda a rotina anterior ao uso e o gatilho da jornada de Mariana, descritos nas etapas 1 e 2 da Entrega 3.
- **C02** aprofunda os objetivos, as dores e os comportamentos operacionais de Rafael descritos na Entrega 3. Trata da confiabilidade dos registros que podem apoiar a decisão de reposição, e não da decisão de compra em si.

**Nota metodológica:** não foram fornecidos resultados de entrevistas ou observações de usuários para esta entrega. As narrativas, os sentimentos, os produtos, os horários, as quantidades e as respostas incorporadas no refinamento são construções hipotéticas para análise. A expressão **evidência no cenário** identifica um trecho da narrativa, não uma comprovação empírica. As fontes indicadas nas questões são formas propostas de obter respostas reais, ainda não executadas.

**Rastreabilidade:** a Entrega 1 original foi conferida nesta revisão. C01 se relaciona ao relato de ruptura e contagem manual (seção 4), ao planejamento de reposições (seção 3) e às lacunas sobre processo e dados (seção 10). C02 aprofunda as lacunas sobre movimentações e divergências, sem atribuir duplicidade a um caso realmente observado. Acúmulo de tarefas, apoio operacional e pouca familiaridade digital são refinamentos hipotéticos da Entrega 3. As necessidades **R04-01** e **R04-02** foram integradas à [matriz central](../RASTREABILIDADE.md). Os detalhes **[NOVO — Cxx-Qn: ...]** indicam refinamento narrativo e permanecem hipotéticos.

## Cenário C01 — Decidir a reposição antes do prazo do fornecedor com informações dispersas

**Autor(a):** Paulo Andre de Oliveira Hirata — 22.125.072-3
**Persona(s) relacionada(s):** P01 — Mariana Alves; P02 — Rafael Costa, como apoio eventual
**Necessidade relacionada:** R04-01 — decidir quais produtos repor, em que momento e em qual quantidade, considerando disponibilidade, procura, prazo de entrega e dinheiro disponível, mantendo o controle da decisão.
**Situação da Entrega 1 relacionada:** relato de ruptura e contagem manual, seção 4; objetivo de planejar reposições, seção 3; lacunas de processo/dados, seção 10. O prazo do fornecedor e a dispersão dos registros são refinamentos hipotéticos associados às etapas 1 e 2 da jornada da Entrega 3.
**Hipóteses ainda presentes:** perfil responsável pela reposição; acúmulo de tarefas e pouco tempo; uso de registros manuais e ferramentas dispersas; controle humano da compra; apoio operacional eventual; pouca familiaridade digital de Mariana. As condições específicas deste episódio também são hipotéticas.

### 1. Cenário inicial

Em uma manhã de trabalho, Mariana Alves, 65 anos, atende clientes no balcão de seu pequeno comércio, que também recebe pedidos pela internet. Entre um atendimento e outro, percebe que um produto procurado pelos clientes está com poucas unidades na prateleira. Uma mensagem do fornecedor informa que ela precisa enviar o pedido para participar da próxima entrega. Mariana quer repor o produto sem comprar além do necessário nem comprometer o dinheiro reservado para outras despesas.

Ela decide conferir as unidades disponíveis e consultar as vendas recentes antes de escolher a quantidade. Conta os produtos na prateleira, abre o caderno de anotações e procura os pedidos recebidos por mensagens. Os registros estão separados e nem sempre deixam claro se uma mercadoria foi apenas solicitada, vendida ou já retirada. Mariana conhece o movimento da loja, mas não consegue reunir com segurança as informações necessárias dentro do tempo disponível.

Sem concluir a conferência, envia uma quantidade parecida com a da última compra. Retoma o atendimento preocupada: conseguiu encaminhar o pedido, mas ainda não sabe se a quantidade atenderá à procura até a próxima entrega ou se deixará dinheiro parado no estoque.

### 2. Questões de refinamento

As perguntas abaixo investigam lacunas do cenário inicial. A classificação segue a aula: questões **exploratórias** investigam motivos, procedimentos e objetos; questões **de verificação** examinam se uma relação ou forma de realizar a atividade é válida. As respostas utilizadas na seção seguinte são hipóteses de trabalho, não entrevistas realizadas.

| # | Questão | Por que precisa ser respondida | Fonte/forma de obter resposta |
|---|---|---|---|
| C01-Q1 | **Exploratória — por quê? / objetivo e evento:** por que o pedido precisa ser decidido naquela manhã, qual é o limite para enviá-lo e quando a mercadoria poderia chegar? | O cenário inicial menciona uma próxima entrega, mas não explicita a janela de decisão nem o período em que Mariana ficará exposta à falta. | Entrevistar a proprietária sobre uma compra recente e conferir, com autorização, as condições comunicadas pelo fornecedor. |
| C01-Q2 | **Exploratória — como? / ambiente:** quanto tempo ela consegue dedicar à conferência e que acontecimentos disputam sua atenção durante esse intervalo? | Caracteriza os recursos de tempo e as interrupções concretas, em vez de apenas afirmar que a rotina é corrida. | Observar um ciclo de reposição, registrando início, pausas, motivos das interrupções e retomadas. |
| C01-Q3 | **Exploratória — o que é? / recursos e informações:** o que compõe o saldo contado e o que significam as anotações usadas para estimar a procura? | Distingue unidades fisicamente presentes, já comprometidas e ainda disponíveis, além de esclarecer unidade, produto e período dos registros. | Comparar contagem física, pedidos e caderno, usando exemplos anonimizados e confirmando o significado dos termos com a proprietária. |
| C01-Q4 | **Exploratória — como? / atores e dependências:** de quem Mariana depende para acessar os registros de vendas online, que informação essa pessoa fornece e ela está disponível nesse momento? | O cenário não informa a divisão de trabalho nem se os dados necessários dependem de ajuda, aspecto diferente da autonomia para decidir a compra. | Entrevistar proprietária e auxiliar separadamente e observar uma situação real de consulta aos registros. |
| C01-Q5 | **Exploratória — como? / planejamento:** como Mariana compara comprar agora, esperar uma conferência e comprar uma quantidade menor quando não pode repor todos os itens? | Revela alternativas, critérios, conflitos e o motivo da escolha; repetir uma compra anterior não explica, por si só, o planejamento. | Pedir que a proprietária reconstrua uma decisão recente, indicando informações consideradas e razões para descartar alternativas. |
| C01-Q6 | **Exploratória — como? / ações e eventos:** como ela retoma a comparação depois de uma interrupção e identifica quais registros já conferiu? | Investiga o ponto de perda de continuidade e a necessidade de repetir ações; esse mecanismo não aparece no cenário inicial. | Acompanhar a sequência de consulta e anotar como a pessoa marca ou recupera o ponto em que parou. |
| C01-Q7 | **Verificação / ação e precondição:** a quantidade fisicamente presente pode ser usada diretamente como quantidade disponível para novos pedidos? | Verifica uma relação específica que pode tornar a compra insuficiente ou a promessa ao cliente incorreta. | Conferir um mesmo produto na prateleira e nos pedidos pendentes de retirada ou envio, com autorização. |
| C01-Q8 | **Exploratória — como? / avaliação e consequências:** como Mariana distingue pedido enviado, entrega combinada e reposição que realmente atendeu à necessidade? | Separa a conclusão de uma ação do alcance do objetivo, identificando evidências posteriores de falta ou excesso. | Acompanhar a confirmação do fornecedor, o recebimento e os registros de vendas/faltas até o próximo ciclo de compra. |

**Cobertura explícita dos sete elementos:**

| Elemento | Questões que o investigam | O que precisa ficar claro |
|---|---|---|
| Contexto/ambiente | C01-Q2 e Q3 | Tempo, espaço, equipamentos, registros e restrições |
| Atores | C01-Q4 | Quem age, de quem depende e quem recebe o resultado |
| Objetivos | C01-Q1 e Q8 | Por que agir e qual resultado realmente atende à necessidade |
| Planejamento | C01-Q5 | Alternativas, ordem e critério para escolher o próximo passo |
| Ações | C01-Q3, Q6 e Q7 | O que a pessoa consulta, compara, registra e retoma |
| Eventos | C01-Q1 e Q6 | Gatilho da atividade e interrupções que mudam sua execução |
| Avaliação | C01-Q7 e Q8 | Precondições, verificação do desfecho e limites da conclusão |

### 3. Cenário refinado

Em uma manhã de trabalho, Mariana Alves, 65 anos, atende clientes no balcão de seu pequeno comércio, que também recebe pedidos pela internet. Entre um atendimento e outro, percebe que um produto procurado pelos clientes está com poucas unidades na prateleira. **[NOVO — C01-Q1: é segunda-feira, e o fornecedor informa por mensagem que recebe pedidos até as 12h para entrega na quinta-feira; pedidos posteriores ficam para a rota seguinte, cuja data ainda precisaria ser confirmada.]** Mariana quer repor o produto sem comprar além do necessário nem comprometer o dinheiro reservado para outras despesas.

Ela decide conferir as unidades disponíveis e consultar as vendas recentes antes de escolher a quantidade. **[NOVO — C01-Q2: a conferência começa por volta das 11h, no próprio balcão, com caderno, calculadora e celular. Mariana espera usar cerca de vinte minutos, mas continua responsável por atender quem chega e responder às ligações.]** Sua experiência com produtos e fornecedores a ajuda a perceber a urgência, embora reunir os registros digitais seja menos familiar para ela.

Mariana conta os produtos na prateleira, abre o caderno de anotações e procura os pedidos recebidos por mensagens. **[NOVO — C01-Q3: o item é uma garrafa térmica azul de 500 ml. Ela conta seis unidades na prateleira, mas duas já foram separadas para um pedido pago que ainda será retirado. No caderno, algumas linhas registram apenas “garrafa”, sem indicar cor ou capacidade; as mensagens misturam perguntas sobre disponibilidade e pedidos confirmados.]** A quantidade presente, portanto, não esclarece sozinha quanto ainda pode ser vendido nem qual foi a procura recente daquela variação.

**[NOVO — C01-Q4: Rafael, 22 anos, costuma consultar os pedidos do marketplace e manter uma planilha. Naquele momento, está ocupado com a separação de encomendas. Ele informa de memória um total de vendas recentes, mas não consegue confirmar imediatamente o período nem se todas são da garrafa azul de 500 ml. Mariana depende dele para essa consulta específica, não para autorizar a compra. Ela evita alterar a planilha sozinha porque não domina a organização do arquivo e receia prejudicar os registros.]**

**[NOVO — C01-Q5: Mariana considera esperar a conferência de Rafael, repetir a compra anterior ou fazer uma compra menor. O dinheiro disponível não permite repor integralmente todos os produtos desejados. Decide priorizar a garrafa, por lembrar de clientes procurando esse item, e adiar outro produto de saída mais lenta. Descarta esperar porque não sabe se conseguirá concluir a conferência antes das 12h.]** A experiência comercial orienta a escolha, mas não elimina a incerteza sobre a quantidade necessária até a entrega.

**[NOVO — C01-Q6: durante a comparação, um cliente chega para retirar uma encomenda de outro produto. Mariana interrompe a soma, atende e volta ao caderno sem ter marcado a última linha conferida. Repete parte da leitura e da soma para evitar contar a mesma venda duas vezes, consumindo mais tempo do intervalo disponível.]** Os registros dispersos e pouco específicos continuam impedindo uma conferência segura.

**[NOVO — C01-Q7: ao recontar o item, ela reconhece que as duas unidades comprometidas não estão livres para novos pedidos. Restam quatro unidades disponíveis, e não seis. Essa distinção muda sua percepção do risco de faltar mercadoria antes de quinta-feira, mas ainda não resolve a ausência de um histórico confiável da procura. Sem concluir a comparação, Mariana envia um pedido de seis unidades, repetindo a quantidade da última compra.]** Esse valor representa a decisão da personagem no episódio, não uma recomendação calculada ou validada.

**[NOVO — C01-Q8: o fornecedor confirma o recebimento do pedido e a entrega prevista para quinta-feira. Mariana anota o combinado e considera concluído o envio, mas não considera resolvido o problema da reposição. Para avaliar o resultado, precisará conferir a quantidade recebida e observar, até a compra seguinte, pedidos não atendidos e unidades que permaneceram sem saída.]** Ela retoma o atendimento preocupada com a possibilidade de faltar produto antes da chegada ou de ter comprado mais do que conseguirá vender. A ação imediata foi concluída, mas a adequação da decisão permanece incerta.

### 4. Elementos extraídos

| Elemento | Evidência no cenário |
|---|---|
| Ator(es) | Mariana, proprietária que decide a compra; Rafael, apoio na consulta aos pedidos online; fornecedor, que define o prazo e confirma a entrega; clientes, que demandam produtos e interrompem a conferência. C01-Q1, Q2 e Q4. |
| Objetivo(s) | Escolher a reposição necessária sem faltar mercadoria nem comprometer recursos de outras despesas. Enviar um pedido é uma ação intermediária, não garantia de alcance do objetivo. C01-Q5 e Q8. |
| Contexto | Balcão de pequeno comércio com vendas online, segunda-feira perto do limite das 12h, entrega prevista para quinta-feira e atendimento em paralelo à conferência. C01-Q1 e Q2. |
| Recursos/informações | Caderno, calculadora, celular, prateleira, planilha mantida pelo auxiliar, mensagens, condições do fornecedor e conhecimento comercial. Há seis unidades presentes, duas comprometidas e quatro disponíveis. C01-Q2, Q3, Q4 e Q7. |
| Planejamento | Comparar saldo e vendas; considerar esperar, repetir a compra ou reduzir a quantidade; priorizar a garrafa em vez de outro item, diante do prazo e da limitação de recursos. C01-Q5. |
| Ações | Contar unidades, ler anotações, consultar mensagens, pedir informação a Rafael, somar registros, atender um cliente, repetir a conferência e enviar o pedido. C01-Q3, Q4 e Q6. |
| Eventos | Aviso do fornecedor com limite de horário, chegada do cliente para retirada e confirmação posterior do pedido. C01-Q1, Q6 e Q8. |
| Avaliação | Mariana percebe que presença física não significa disponibilidade; reconhece que o envio foi concluído, mas que o resultado da compra depende da entrega e do movimento posterior. C01-Q7 e Q8. |
| Problemas/rupturas | Dados dispersos e ambíguos; dependência de uma consulta que não está imediatamente disponível; retomada sem referência do ponto anterior; pouco tempo para confrontar saldo, procura e prazo. C01-Q3 a Q7. |
| Consequências | Repetição de trabalho, compra apoiada parcialmente na memória e manutenção da incerteza. Falta antes da entrega, excesso posterior e perda de vendas são riscos, não resultados medidos deste cenário. C01-Q6 e Q8. |

### 5. Implicações para as próximas entregas

| Tarefa que merece análise | Informação que precisa ser coletada | Relação com a necessidade |
|---|---|---|
| Apurar a quantidade efetivamente disponível de um produto e de suas variações. | Como são identificadas reservas, retiradas, pedidos pagos e unidades separadas; quem atualiza cada informação e quando. | R04-01: evita confundir mercadoria presente com quantidade livre para venda. |
| Reconstruir a procura recente a partir dos registros atuais. | Quais canais são usados, como se identifica uma venda confirmada, como se reconhece a mesma variação e se há duplicidade entre canais. | R04-01: esclarece em que informação Mariana baseia sua estimativa de reposição. |
| Comparar alternativas de compra e priorizar itens. | Prazo real dos fornecedores, frequência de reposição, restrições de caixa, critérios comerciais e motivos de exceções. | R04-01: explicita o conflito entre disponibilidade de produtos e dinheiro comprometido. |
| Interromper e retomar a conferência. | Frequência das interrupções, formas atuais de marcar progresso e tempo gasto para reconstruir o raciocínio. | R04-01: identifica o esforço que compete com a análise da compra. |
| Avaliar a decisão depois do pedido. | Como se confirma a entrega e como são percebidas faltas, sobras e vendas não atendidas até o próximo ciclo. | R04-01: distingue pedido realizado de reposição adequada. |

Na análise posterior, devem ser priorizadas a compreensão das informações, a segurança da decisão, a autonomia de Mariana e a redução do esforço de retomada. Sua familiaridade com mensagens não demonstra domínio de planilhas, e a idade não comprova limitações perceptuais ou motoras. Essas condições precisam ser investigadas, sem atribuir dificuldades à pessoa quando também podem decorrer da organização dos registros e do trabalho.

## Cenário C02 — Investigar uma divergência de estoque sob interrupções

**Autor(a):** Victor Merker Binda — 22.125.075-6
**Persona(s) relacionada(s):** P02 — Rafael Costa; P01 — Mariana Alves, como fonte de informações e destinatária da conferência
**Necessidade relacionada:** R04-02 — manter registros de movimentação e um saldo de estoque confiáveis, identificar a origem das divergências e retomar a conferência sem omitir ou duplicar lançamentos.
**Situação da Entrega 1 relacionada:** lacunas sobre registro de movimentações, tratamento de divergências e divisão de responsabilidades, seções 2, 4 e 10. A duplicidade específica é uma construção hipotética da Entrega 4, derivada da persona P02.
**Hipóteses ainda presentes:** existência de um auxiliar separado e uso operacional recorrente (classificado como primário provisório na E3); tarefas operacionais concorrentes; registros distribuídos entre planilha, caderno e marketplace; participação de auxiliar. A duplicidade e os demais detalhes deste episódio são hipóteses de refinamento, não ocorrências observadas.

### 1. Cenário inicial

Em outro dia de trabalho, Rafael Costa, 22 anos, utiliza o computador compartilhado do comércio para atualizar uma planilha a partir dos pedidos online e das anotações deixadas por Mariana. Ele também separa encomendas e confere os produtos no estoque. Quer deixar os registros corretos para que a proprietária possa avaliar a disponibilidade e preparar as próximas compras.

Rafael encontra uma diferença entre a quantidade indicada na planilha e a quantidade que conta fisicamente de um produto. Decide reconstruir as movimentações antes de alterar o saldo. Volta aos pedidos do marketplace e ao caderno, mas os registros não apresentam a mesma identificação e nem sempre permitem reconhecer se uma saída já foi transcrita.

Uma demanda de separação de pedidos interrompe a conferência. Quando retorna, ele precisa reler parte das anotações para recuperar o ponto em que parou. A familiaridade com planilhas facilita a digitação, mas não permite determinar a origem da diferença sem comparar as fontes. Rafael adia a correção e avisa Mariana de que aquele saldo ainda não foi confirmado. A proprietária continua sem uma informação segura para concluir o planejamento da compra.

### 2. Questões de refinamento

| # | Questão | Por que precisa ser respondida | Fonte/forma de obter resposta |
|---|---|---|---|
| C02-Q1 | **Exploratória — por quê? / objetivo e evento:** por que a atualização precisa ser concluída naquele período e qual conjunto de registros está sob conferência? | Delimita a carga de trabalho e o resultado esperado; “atualizar o estoque” é amplo demais para avaliar a conclusão. | Entrevistar proprietária e auxiliar sobre o fechamento de um dia recente e examinar uma amostra autorizada dos registros. |
| C02-Q2 | **Exploratória — como? / ambiente:** como o uso do computador compartilhado e a separação de encomendas afetam a continuidade da conferência? | Identifica condições materiais e concorrência por recursos, além de caracterizar a interrupção citada no cenário inicial. | Observar uma sessão de trabalho e registrar disponibilidade do equipamento, demandas simultâneas e deslocamentos. |
| C02-Q3 | **Exploratória — o que é? / recursos e informações:** quais dados identificam uma movimentação e distinguem duas vendas de duas anotações da mesma venda? | Esclarece o objeto manipulado e seus atributos; sem essa distinção, somar ou excluir uma linha pode introduzir um erro. | Comparar pedidos e anotações anonimizados, verificando identificador, data, produto, variação, quantidade, canal e situação. |
| C02-Q4 | **Exploratória — como? / atores e dependências:** quem conhece a origem dos registros incompletos, quem pode confirmar uma correção e quem precisa receber o resultado? | Explicita responsabilidades e a dependência de conhecimento que não está escrito, sem confundir conferência operacional com autorização de compra. | Entrevistar cada pessoa envolvida e pedir exemplos de uma divergência anterior e de sua comunicação. |
| C02-Q5 | **Exploratória — como? / planejamento:** em que ordem Rafael confronta pedidos, anotações e contagem, e por que escolhe investigar antes de substituir o saldo? | Torna visível a estratégia e o critério de decisão, não apenas a sequência de digitação. | Acompanhar a reconstrução de um caso recente e pedir a explicação das alternativas consideradas. |
| C02-Q6 | **Exploratória — como? / ações e eventos:** em que ponto a interrupção acontece e quais indícios permitem saber o que foi conferido ou alterado antes de sair? | Localiza a ruptura de continuidade e o retrabalho, informação ausente da descrição genérica de uma pausa. | Observar a retomada e verificar que marcações, notas ou versões do arquivo são efetivamente usadas. |
| C02-Q7 | **Verificação / ação e precondição:** igualar o saldo da planilha à contagem física, sem localizar o lançamento responsável, permite considerar a divergência resolvida? | Verifica se a igualdade numérica também recupera a confiabilidade do histórico ou apenas esconde a diferença. | Reconciliar um caso com documentos de origem e conferir se a alteração preserva uma explicação para as movimentações. |
| C02-Q8 | **Exploratória — como? / avaliação e consequências:** quais verificações indicam que a correção terminou e como Rafael diferencia itens conferidos de pendências ao informar Mariana? | Define o término da tarefa e a comunicação do resultado, evitando tratar a correção de um item como conclusão de todo o estoque. | Acompanhar o fechamento da conferência, a comunicação à proprietária e uma consulta posterior aos registros corrigidos. |

**Cobertura explícita dos sete elementos:**

| Elemento | Questões que o investigam | O que precisa ficar claro |
|---|---|---|
| Contexto/ambiente | C02-Q2 e Q3 | Tempo, espaço, equipamentos, registros e restrições |
| Atores | C02-Q4 | Quem age, de quem depende e quem recebe o resultado |
| Objetivos | C02-Q1 e Q8 | Por que agir e qual resultado realmente atende à necessidade |
| Planejamento | C02-Q5 | Alternativas, ordem e critério para escolher o próximo passo |
| Ações | C02-Q3, Q6 e Q7 | O que a pessoa consulta, compara, registra e retoma |
| Eventos | C02-Q1 e Q6 | Gatilho da atividade e interrupções que mudam sua execução |
| Avaliação | C02-Q7 e Q8 | Precondições, verificação do desfecho e limites da conclusão |

### 3. Cenário refinado

Em outro dia de trabalho, Rafael Costa, 22 anos, utiliza o computador compartilhado do comércio para atualizar uma planilha a partir dos pedidos online e das anotações deixadas por Mariana. Ele também separa encomendas e confere os produtos no estoque. Quer deixar os registros corretos para que a proprietária possa avaliar a disponibilidade e preparar as próximas compras. **[NOVO — C02-Q1: no fim da tarde, Mariana pede o fechamento das movimentações do dia para planejar a compra da manhã seguinte. Rafael reúne quatorze registros de origem para verificar; esse conjunto pode conter referências repetidas à mesma venda.]**

**[NOVO — C02-Q2: o computador fica numa bancada próxima à área de embalagem e também é usado para consultar as encomendas que precisam sair. Rafael alterna a transcrição com a separação física dos pedidos. O espaço de trabalho não permite dedicar todo o período exclusivamente à conferência.]** Ele encontra uma diferença entre a quantidade indicada na planilha e a quantidade que conta fisicamente de um produto. Decide reconstruir as movimentações antes de alterar o saldo.

**[NOVO — C02-Q3: o item é um conjunto de três potes, tratado comercialmente como uma unidade de venda. A planilha indica oito unidades e a contagem física, dez. No marketplace, uma venda concluída possui identificador, data, descrição, quantidade e situação. No caderno, aparece “2 conjuntos de potes”, sem o identificador do pedido nem a indicação de que se trata de uma venda online já registrada. A consulta detalhada revela que duas linhas da planilha podem corresponder a essa mesma saída de duas unidades.]** Nomes semelhantes e ausência de identificação comum dificultam distinguir repetição de uma nova movimentação.

**[NOVO — C02-Q4: Mariana escreveu a anotação no caderno e conhece sua origem. Rafael pode corrigir a transcrição depois de confirmar o ocorrido com ela e confrontar o pedido; não deve inventar uma movimentação apenas para fechar a conta. Mariana também precisa receber o resultado, pois usará a informação na decisão de compra.]** Enquanto ela atende um cliente, a explicação da anotação permanece pendente.

**[NOVO — C02-Q5: Rafael planeja começar pelo pedido que possui identificação, comparar a anotação do mesmo dia e produto, verificar as duas linhas transcritas e somente depois repetir a contagem. Considera substituir oito por dez diretamente, mas descarta essa alternativa porque ainda não saberia se houve venda duplicada, entrada esquecida ou erro de contagem.]** A investigação é necessária mesmo com sua facilidade para editar a planilha.

Uma demanda de separação de pedidos interrompe a conferência. **[NOVO — C02-Q6: a solicitação chega depois de Rafael localizar a anotação suspeita, mas antes de confirmar com Mariana se ela corresponde ao pedido online. Ele ainda não marcou quais linhas comparou. Ao voltar da embalagem, relê o pedido e as duas linhas para garantir que não fará uma segunda correção sobre o mesmo registro.]** Sem essa referência, precisa reconstruir parte do raciocínio e avisa Mariana de que o saldo continua não confirmado.

**[NOVO — C02-Q7: quando pode responder, Mariana confirma que anotou no caderno a mesma venda online de duas unidades. O pedido foi efetivamente enviado, não está cancelado e não há outra saída correspondente à segunda linha. Rafael identifica que essa venda foi descontada duas vezes. Corrige a transcrição duplicada, registra numa observação a razão da alteração e repete a contagem. O saldo passa de oito para dez unidades, coincidindo com o estoque físico; não houve entrada de duas unidades, mas correção de um desconto indevido.]** A igualdade entre os valores só ganha uma explicação depois da conferência das fontes.

**[NOVO — C02-Q8: Rafael confere produto, unidade de venda, quantidade e vínculo com o pedido de origem. Informa a Mariana que aquele item foi reconciliado e registra quais anotações do conjunto de quatorze ainda precisam ser verificadas. Considera a correção do item concluída, mas não o fechamento de todas as movimentações.]** Mariana pode usar o saldo corrigido desse produto, mantendo cautela quanto aos itens pendentes. O episódio termina com recuperação parcial da informação, ao custo de consultas repetidas, interrupção e dependência da memória de quem produziu a anotação. A mesma forma de registro continua permitindo novas ambiguidades.

### 4. Elementos extraídos

| Elemento | Evidência no cenário |
|---|---|
| Ator(es) | Rafael executa a transcrição, a comparação e a correção; Mariana explica a anotação de origem e recebe o resultado para a compra. C02-Q4. |
| Objetivo(s) | Produzir um saldo e um histórico explicáveis a partir das movimentações reais; deixar claras as pendências. O objetivo não é apenas fazer dois números coincidirem. C02-Q1, Q7 e Q8. |
| Contexto | Fim de tarde, computador compartilhado próximo à embalagem, quatorze registros de origem e demanda de fechamento para a manhã seguinte. C02-Q1 e Q2. |
| Recursos/informações | Planilha, pedidos identificados no marketplace, caderno sem identificador comum e contagem física. A unidade comercial é um conjunto de três potes; uma venda de duas unidades foi transcrita duas vezes. C02-Q3 e Q7. |
| Planejamento | Partir do pedido identificado, comparar anotações e transcrições, confirmar com Mariana e recontar; rejeitar substituição arbitrária do saldo. C02-Q5. |
| Ações | Consultar o pedido, comparar linhas, procurar a origem da anotação, separar encomendas, reler os registros, corrigir a duplicidade, registrar a razão e comunicar pendências. C02-Q3 a Q8. |
| Eventos | Solicitação de fechamento por Mariana, demanda de embalagem que interrompe a comparação e posterior confirmação da origem da anotação. C02-Q1, Q6 e Q7. |
| Avaliação | Rafael confere correspondência com a movimentação real e contagem, reconhece o item como reconciliado e distingue essa conclusão das pendências do restante do conjunto. C02-Q7 e Q8. |
| Problemas/rupturas | Identificadores ausentes no caderno, duplicidade de transcrição, dependência de confirmação verbal e perda do ponto de conferência após interrupção. C02-Q3, Q4 e Q6. |
| Consequências | Saldo inicialmente subestimado, atraso, releitura e necessidade de explicação manual. Uma compra desnecessária seria um risco se Mariana usasse o valor incorreto; não é apresentada como ocorrência comprovada. C02-Q6 a Q8. |

### 5. Implicações para as próximas entregas

| Tarefa que merece análise | Informação que precisa ser coletada | Relação com a necessidade |
|---|---|---|
| Identificar uma mesma movimentação em fontes diferentes. | Identificadores existentes, variações de nomes, unidades comerciais e significado das situações de pedido usadas no negócio. | R04-02: diferencia uma venda real de cópias ou transcrições da mesma venda. |
| Registrar e reconciliar entradas e saídas. | Quem registra, em que momento, que documentos usa e como trata reserva, cancelamento, devolução e envio, quando esses casos ocorrerem. | R04-02: esclarece as regras que tornam o saldo e o histórico confiáveis. |
| Investigar uma diferença antes de corrigir. | Causas frequentes, fontes aceitas como evidência, necessidade de autorização e procedimento quando não se encontra a origem. | R04-02: evita correções que apenas ocultem uma inconsistência. |
| Interromper e retomar a conferência. | Como o trabalho em andamento é reconhecido, se outras pessoas alteram o arquivo e quais repetições ou omissões ocorrem na retomada. | R04-02: preserva a continuidade da atividade operacional. |
| Comunicar conclusão e pendências. | Quem depende do resultado, como distingue dado confirmado de estimativa e o que precisa saber sobre uma correção posterior. | R04-02: impede que uma conferência parcial seja interpretada como validação de todo o estoque. |

Na análise posterior, a prioridade é entender a precisão do registro, a prevenção e a recuperação de erros, o esforço de retomada e a comunicação entre os papéis. A facilidade de Rafael com tecnologia não elimina problemas de significado, responsabilidade ou qualidade das fontes. Também será necessário verificar se negócios reais possuem esse papel auxiliar e como realizam a tarefa quando o proprietário trabalha sozinho.

## Limites e continuidade após o feedback

O título de C02 descreve a diferença a investigar, sem declarar sua causa. A duplicidade é uma descoberta da versão refinada, em C02-Q7, e permanece um exemplo hipotético. Horários, quantidades, datas e produtos de ambos os cenários tornam os episódios analisáveis; não são parâmetros obrigatórios do sistema nem características medidas do público. Se o proprietário concentrar as tarefas hoje atribuídas a Rafael, reinterpretar C02 para esse arranjo, mantendo a necessidade de apurar evidências e comunicar pendências. A classificação revisada de P02 na E3 não confirma por si só sua existência.

## Checklist

- [x] Há um cenário completo por integrante, com autoria identificada.
- [x] Cada cenário tem título, ator, objetivo, contexto e problema.
- [x] Cada cenário possui origem rastreável na Entrega 1 e nas hipóteses retomadas pela Entrega 3, com seções e necessidades identificadas.
- [x] O texto descreve a situação atual hipotética, sem antecipar a solução.
- [x] O recorte técnico do TCC foi relacionado a uma prática humana plausível, e não à “falta de uma tela”.
- [x] Questões de refinamento acrescentam informação nova e utilizam a taxonomia da aula.
- [x] O refinamento mostra claramente o que foi adicionado e identifica a pergunta correspondente.
- [x] Contexto, atores, objetivos, planejamento, ações, eventos e avaliação estão presentes e explicitados.
- [x] Cenários são diferentes o suficiente para cobrir objetivos/problemas relevantes.
- [x] Cada cenário está ligado a persona e necessidade na matriz local de rastreabilidade.
- [x] Respostas hipotéticas, possíveis consequências e sentimentos não foram apresentados como dados coletados.
- [x] Correspondência com a Entrega 1 original e com os IDs da matriz central conferida pela equipe.

### Validação futura — não realizada nesta entrega documental

- [ ] Confrontar cenários e respostas de refinamento com entrevistas, observação ou registros de usuários reais. A elaboração e revisão dos cenários estão concluídas; a validação empírica permanece pendente.

# Entrega 4 — Cenários de análise/problema

**Data:** 08/10/2026 (versão original)
**Revisão:** 15/11/2026, aplicação do [feedback do professor](../feedbacks_professor/Feedback_Professor_Entrega04_Equipe09.md)
**Status:** 🟦 revisada após feedback
**Responsabilidade:** 1 solução completa por integrante

## Objetivo da atividade

Descrever situações atuais em que o usuário tenta alcançar um objetivo e encontra dificuldades. O cenário de análise/problema deve tornar visível **o contexto, os atores, as ações e as rupturas**, sem antecipar a interface que será projetada.

> **Regra central:** cenário de problema é a “história do problema”. Se o texto já diz “o sistema mostra”, “o aplicativo resolve” ou descreve botões/telas futuras, provavelmente está misturando problema com solução.

Sempre que possível, o cenário deve aprofundar uma **situação concreta já registrada na Entrega 1**.

### Quando o TCC não possuía interface

O cenário continua sendo uma história de **problema/atividade humana**, não uma história do futuro sistema. Descreva como o profissional realiza hoje uma atividade semelhante ou como lida atualmente com dados, resultados, configurações, logs, decisões e limitações que o tema do TCC pretende apoiar.

Exemplo: em vez de “o DBA abre o novo dashboard e executa o algoritmo”, descreva “o DBA precisa investigar uma consulta lenta, reúne informações em ferramentas distintas, compara planos manualmente e tem dificuldade para estimar o impacto de uma mudança”.

A interface da disciplina aparecerá somente depois, nos cenários de interação.

Se o integrante escolher um novo problema/situação, explique por que ele passou a ser relevante e indique a evidência que motivou sua inclusão.

Os cenários usam o prefixo `CP`, conforme a convenção de identificadores de [`../RASTREABILIDADE.md`](../RASTREABILIDADE.md), porque `C` designa os concorrentes da Entrega 2. O número acompanha a ordem dos autores na equipe.

## Cenário CP01 — Dúvida diante de uma imagem de contêiner no meio do plantão

**Autor(a):** Kawan Mark Geronimo Da Silva — 22.222.010-5  
**Persona(s) relacionada(s):** P01 — Gustavo Onofre (operador da estação de imagem)  
**Necessidade relacionada:** R01 (saber onde olhar em uma imagem densa e sobreposta), com contato com R03 (o que acontece com o que o operador conclui)  
**Situação concreta da Entrega 1 relacionada:** seção 4.5 (H13), que aprofunda as seções 4.2 (H10) e 4.4 (H12)  
**Hipóteses ainda presentes:** H01, H04, H10, H11, H12, H13, H16, H38, H39, H41 e as lacunas ?07 e ?08

**Por que esta situação.** H13 é o único relato concreto da Entrega 1 e descreve o problema que justifica o recorte: a anomalia que passa despercebida na imagem. Ela é um cenário exploratório, e não uma observação. O personagem original (Carlos) não foi investigado nem virou persona, por isso a história é contada com Gustavo (P01), a proto-persona de quem examina a imagem. Turno, horário e volume continuam suposições [H13]. O cenário não valida H10 nem H13: ele os torna narráveis para as próximas entregas.

### 1. Cenário inicial

Gustavo Onofre opera a estação de imagem de raio-X de um terminal portuário. Está no meio de um plantão noturno e, por volta das três da manhã, já examinou centenas de imagens de contêineres e caminhões que passaram pelo escâner. A cada imagem, ele tem poucos segundos para decidir se há alguma coisa ali que justifique desconfiar da carga. Faz isso olhando a imagem no software do fabricante do escâner, que oferece cores por tipo de material, realce de bordas e ajuste de contraste, mas não diz por onde começar a olhar.

Chega a imagem de um contêiner declarado como carregado de paletes de madeira. A imagem é densa, com muitos objetos sobrepostos. Em uma região, o material parece um pouco mais denso que no restante, mas a diferença é pequena e Gustavo já viu variações assim em cargas de madeira que eram regulares. Ele ajusta o contraste, liga o realce de bordas, volta à imagem original e tenta lembrar o que a carga deveria ser. Os caminhões seguintes já esperam e a próxima imagem está pronta. Cansado, ele não consegue afirmar se aquela região faz parte da carga ou se há algo escondido ali.

Gustavo conclui que não tem motivo suficiente para apontar uma suspeita e deixa o caso seguir. Ele não sabe se acertou. No resto do plantão, não terá como descobrir o que havia naquela região.

### 2. Questões de refinamento

Convenções desta seção: `[F]` fato com fonte, `[H]` hipótese, `[?]` lacuna, e `**[NOVO: ...]**` para o que o refinamento acrescenta, acompanhado de `[Q1]`, `[Q2]` etc. para vincular cada acréscimo à pergunta correspondente. Cada questão está associada a um dos **sete elementos característicos do cenário** trabalhados na disciplina (**ambiente/contexto, atores, objetivos, planejamento, ações, eventos e avaliação**), os mesmos extraídos na seção 4.

As perguntas buscam apenas informações **ainda ausentes** do cenário inicial. As respostas vêm de documentos e de fontes já analisadas nas Entregas 1 a 3. Nenhum profissional foi ouvido, por isso o que não tem fonte permanece `[H]` ou `[?]` e segue para a Entrega 7.

| # | Elemento | Questão | Por que precisa ser respondida | Fonte/forma de obter resposta |
|---|---|---|---|---|
| Q1 | Atores | Quem é Gustavo em termos institucionais (servidor da Receita Federal ou operador designado pelo recinto) e que outros atores participam quando há suspeita sobre uma carga? | O cenário inicial não diz se ele decide ou só aponta, nem quem recebe o apontamento, e isso muda o que “deixar o caso seguir” significa e quem responde por ele. | Documentos: Portaria ALF/FNS nº 9/2024 (arts. 3º e 8º), Portaria RFB nº 143/2022 (art. 14). Entrevista na Entrega 7 (H01, H39). |
| Q2 | Objetivos | Qual é o alcance formal do objetivo de Gustavo ao concluir a análise (apenas apontar suspeita à fiscalização ou decidir pela retenção/liberação) e o que torna uma conclusão defensável? | O cenário inicial fala em “decidir se há alguma coisa ali que justifique desconfiar”, mas não delimita até onde vai a atribuição formal do operador nem o custo de errar para cada lado. | Portaria ALF/FNS nº 9/2024 (art. 8º), C02 (redirecionamento de canal e desembaraço). Entrevista na Entrega 7 (H01, H12, H38, H39). |
| Q3 | Planejamento | Como o operador se prepara e que informações da declaração e ferramentas adicionais do software estão disponíveis para estruturar a conferência da imagem? | O cenário inicial cita apenas cores, bordas e contraste, mas não informa como o operador planeja a conferência nem que dados da carga declarada ele tem para orientar a busca visual. | Análise C03 da Entrega 2 e ADE Coana nº 19/2014, item 1.2.8. Entrevista para o restante (H11). |
| Q4 | Ambiente/contexto | Quais são as condições físicas de acesso, iluminação, ruído e equipamento da sala onde funciona a estação, e qual é a duração formal da escala e a meta de atendimento? | O cenário inicial já informa que é um plantão noturno às três da manhã, mas não descreve as restrições físicas da sala, o porte do monitor nem se há escala ou meta formal de liberação. | Portaria ALF/FNS nº 9/2024 (art. 3º) para a sala; análise C03 para o monitor. Entrevista, fotos ou material institucional para iluminação, ruído, duração da escala e metas (H14, H16, ?07). |
| Q5 | Eventos | Como ocorrem os eventos de chegada e transmissão das imagens à estação, quem define a ordem da fila e que eventos são disparados no pátio quando uma suspeita é comunicada? | O cenário inicial menciona que a próxima imagem está pronta, mas não explica como ela chega, quem mais a recebe em tempo real nem o que ocorre com o veículo no pátio em caso de alerta. | Portaria RFB nº 143/2022 (art. 14), Portaria ALF/FNS nº 9/2024 (art. 8º) e C03 para o fluxo. Entrevista ou observação para a ordem da fila (H04, H41). |
| Q6 | Ações | Que ações práticas Gustavo pode realizar quando os ajustes de contraste e bordas não eliminam a dúvida (como consultar dados do manifesto, pedir segunda opinião ou formalizar apontamento)? | O cenário inicial só mostra ajustes básicos de imagem e a escolha solitária entre apontar ou deixar seguir. Falta saber que outras ações cabem durante o exame. | Portaria ALF/FNS nº 9/2024 (art. 8º) e C03 (anotações e dados do manifesto). Entrevista para práticas informais, como pedir segunda opinião (H11, H12). |
| Q7 | Avaliação | Como o resultado da decisão é avaliado posteriormente e que mecanismos de consulta ou retorno existem para Gustavo saber o que foi encontrado nas cargas apontadas ou liberadas? | O cenário inicial termina dizendo que ele não terá como descobrir o que havia na região. É preciso saber o que fica armazenado e se há retorno institucional sobre o desfecho. | Portaria ALF/FNS nº 9/2024 (art. 5º) para o que fica guardado. Entrevista sobre retorno de desfecho (H38, ?08). |

### 3. Cenário refinado

Gustavo Onofre opera a estação de imagem de raio-X de um terminal portuário. **[NOVO [Q1]: [F] Na unidade usada como referência (Portaria ALF/FNS nº 9/2024, Imbituba), o escâner é operado por operadores designados pelo recinto alfandegado, em sala com acesso restrito às pessoas autorizadas, e não por servidores da Receita Federal. [H] Este cenário adota esse modelo como referência exploratória, sem afirmar que vale para outros terminais. Em Santos há indício de outro modelo, com a imagem analisada por servidores da vigilância da RFB em uma central (CP02). [?] Ainda não sabemos em qual modelo Gustavo estaria nem que cargo da RFB examina as imagens (H01, H39).]** Está no meio de um plantão noturno e, por volta das três da manhã, já examinou centenas de imagens de contêineres e caminhões que passaram pelo escâner. **[NOVO [Q4]: [?] Não sabemos qual é a duração formal da escala, a meta de atendimento por hora nem as condições reais de iluminação e ruído da sala (H13, H14, H16, ?07); a hora e o volume exato permanecem suposições do cenário exploratório.]** A cada imagem, ele tem poucos segundos para decidir se há alguma coisa ali que justifique desconfiar da carga. Faz isso olhando a imagem no software do fabricante do escâner, **[NOVO [Q3, Q4]: [F] em um monitor dedicado de 22" a 24" (C03). [F] Para planejar e conduzir o exame, o software oferece zoom, inversão, realce de contornos, colorização por densidades, brilho, contraste e equalização (ADE Coana nº 19/2014, item 1.2.8) e, nos produtos analisados, visualização de dados do manifesto e anotações sobre a imagem (C03).]** que oferece cores por tipo de material, realce de bordas e ajuste de contraste, mas não diz por onde começar a olhar. **[NOVO [Q5]: [H] Os eventos de chegada das imagens acompanham a passagem dos veículos pelo escâner na ordem de chegada. [F] As imagens são transmitidas em tempo real à unidade da RFB (Portaria RFB nº 143/2022, art. 14), de modo que Gustavo não é o único que pode vê-las. [?] Não sabemos se existe fila configurável nem quem controla a ordem de atendimento (H04, H41).]**

Chega a imagem de um contêiner declarado como carregado de paletes de madeira. A imagem é densa, com muitos objetos sobrepostos. Em uma região, o material parece um pouco mais denso que no restante, mas a diferença é pequena e Gustavo já viu variações assim em cargas de madeira que eram regulares. Ele ajusta o contraste, liga o realce de bordas, volta à imagem original e tenta lembrar o que a carga deveria ser. **[NOVO [Q3, Q6]: [H] Ele procura conferir a imagem com a descrição da carga na declaração. [?] Não sabemos que informações da declaração ele tem diante dos olhos nesse momento, nem se precisa buscá-las em outro sistema ou janela (H11).]** Os caminhões seguintes já esperam e a próxima imagem está pronta. Cansado, ele não consegue afirmar se aquela região faz parte da carga ou se há algo escondido ali. **[NOVO [Q2, Q5, Q6]: O objetivo de Gustavo é chegar a uma conclusão defensável dentro do limite de sua função, mas ele tem duas saídas e nenhuma é sem custo. [F] Se desconfiar, sua ação é comunicar a suspeita à RFB, evento que interrompe imediatamente o fluxo daquele veículo e mantém a carga retida e segregada até a manifestação da fiscalização; sem manifestação nem bloqueio no Siscomex Carga em 3 dias úteis, a carga segue (Portaria ALF/FNS nº 9/2024, art. 8º). [H] Se comunicar sem base suficiente, ele retém uma carga regular e gera atrito com quem espera pela liberação (H12). [H] Se deixar seguir e houver algo escondido, a carga entra no país sem que ninguém tenha visto (H12). [H] Pedir a opinião de um colega antes de apontar é uma ação plausível, mas não há fonte sobre essa prática na unidade.]**

Gustavo conclui que não tem motivo suficiente para apontar uma suspeita e deixa o caso seguir. Ele não sabe se acertou. No resto do plantão, não terá como descobrir o que havia naquela região. **[NOVO [Q7]: [F] As imagens ficam disponíveis por 180 dias e podem ser buscadas por unidade de carga, data, hora ou placa (Portaria ALF/FNS nº 9/2024, art. 5º). Isso permite rever a imagem armazenada, mas não mostra o que a verificação física da carga encontrou para avaliar o acerto da decisão. [?] Não sabemos se quem examina a imagem recebe algum retorno sobre os casos que apontou ou deixou de apontar (H38, ?08). [H] Sem avaliação de desfecho, ele não aprende com o resultado e o próximo caso parecido recomeça do mesmo ponto.]**

### 4. Elementos extraídos

| Elemento | Evidência no cenário |
|---|---|
| Ambiente/contexto | Sala de operação do escâner com acesso restrito [F] e estação com monitor dedicado de 22" a 24" [F]; plantão noturno às 3h, cansaço e pressão de tempo [H, H13]; condições de iluminação, ruído, duração da escala e metas em aberto [?, H14, H16, ?07]. |
| Atores | Gustavo Onofre, operador da estação de imagem (P01). Quem recebe a suspeita: a RFB, que se manifesta sobre a carga [F]. Quem espera a liberação: motoristas e operadores logísticos [H]. O vínculo institucional de Gustavo depende do modelo da unidade (H01, H39). |
| Objetivos | Chegar a uma conclusão confiável e defensável sobre a compatibilidade entre a imagem radiográfica e a carga declarada (H38), decidindo sob incerteza se cabe comunicar suspeita à RFB ou liberar o fluxo do veículo. |
| Planejamento | Uso das funções de tratamento do software do fabricante (zoom, inversão, realce de contornos, pseudo-cor por densidade, brilho, contraste e equalização) [F] e consulta à descrição da carga declarada [H, H11] para orientar a inspeção visual, sem apoio de recurso que indique por onde começar a olhar. |
| Ações | Examinar a imagem; alternar filtros de contraste, realce de bordas e cor por material; confrontar visualmente a região densa com a mercadoria declarada; optar entre comunicar suspeita à RFB ou deixar o caso seguir; passar à imagem seguinte. |
| Eventos | Chegada da imagem de um contêiner declarado como paletes de madeira após passagem pelo escâner [H]; transmissão em tempo real à RFB [F]; fila de veículos aguardando no pátio [H]; em caso de comunicação de suspeita, interrupção do fluxo do veículo e retenção da carga por até 3 dias úteis aguardando manifestação da RFB [F]. |
| Avaliação | Dúvida não resolvida pela pequena diferença de densidade em imagem sobreposta (H10); impossibilidade de avaliar se a liberação foi um acerto ou um falso negativo [H, H12]; imagens guardadas por 180 dias para consulta [F], mas sem retorno conhecido sobre o desfecho da fiscalização para calibrar decisões futuras [?, H38, ?08]. |

### 5. Implicações para as próximas entregas

Estas são perguntas e tarefas candidatas, e não decisões. A forma de apoiar cada uma só entra a partir das Entregas 6 e 9.

**Tarefas que merecem análise na Entrega 5, se a investigação sustentar:**

- A02: examinar a região de uma imagem e concluir se é compatível com a carga declarada. É a tarefa central do cenário, e liga a R01.
- A03: comunicar ou registrar a conclusão a quem decide. A forma depende de H39 e liga a R03.
- Acompanhar o desfecho de um caso apontado ou não apontado. Ainda não tem ID: só vira atividade se a Entrega 7 mostrar que o retorno existe ou faz falta.

**Informações a coletar na Entrega 7** (todas pendentes, nenhuma pode ser respondida por protótipo):

1. Quem examina a imagem em outras unidades, e se essa pessoa pode reter ou só apontar (H01, H39).
2. Se existe fila e quem decide a ordem de exame (H04, H41).
3. Que informações da declaração a pessoa usa junto da imagem e onde as consulta (H11).
4. O que a pessoa faz quando fica em dúvida, e se há segunda opinião ou protocolo (H12).
5. Se há retorno sobre o desfecho dos casos, e como chega (H38, ?08).
6. Condições reais de turno, iluminação e ruído (H14, H16) e se há metas de liberação (?07).

**Cadeia de rastreabilidade:** CP01 liga P01 → R01 → A02 em [`RASTREABILIDADE.md`](../RASTREABILIDADE.md). O cenário não confirma H10 nem H13 e não altera o estado das hipóteses.

---

## Cenário CP02 — Decidir sobre uma carga bloqueada por suspeita na imagem do escâner

**Autor(a):** Gabriel Albertini Pinheiro — 22.122.094-8  
**Persona(s) relacionada(s):** P02, Dr. Eduardo Resende (Auditor-Fiscal)  
**Necessidade relacionada:** R03  
**Situação concreta da Entrega 1 relacionada:** nova situação justificada. A Entrega 1 narra só o lado de quem examina a imagem (seção 4.5). Este cenário trata de quem decide e formaliza, papel que passou a existir no projeto com H39 e que tem base na análise C02 da Entrega 2 e nas normas da RFB citadas na Entrega 3. Liga-se à atividade A03 (seção 3.2).  
**Hipóteses ainda presentes:** H01, H06, H08, H11, H17, H18, H32, H39 e a lacuna ?08

O cenário se passa na Alfândega do Porto de Santos. Nenhum Auditor-Fiscal foi entrevistado: a narrativa é hipotética `[H]`, salvo onde indicado `[F]`.

### 1. Cenário inicial

Atores: Dr. Eduardo Resende (Auditor-Fiscal), servidor da vigilância que analisou a imagem, importador.

Dr. Eduardo Resende, Auditor-Fiscal na Alfândega do Porto de Santos, recebe uma declaração de importação cuja carga está bloqueada porque a imagem do escâner levantou suspeita. Ele precisa decidir o que fazer com essa carga e formalizar a decisão. Abre a declaração no Siscomex e lê o que a mercadoria declara ser. Sabe que existe uma suspeita, mas não sabe o que foi visto na imagem nem em que parte do contêiner. A imagem não está junto da declaração. Ele procura quem fez o bloqueio para entender o motivo e recebe uma descrição curta, que tenta relacionar com a mercadoria declarada. Sem prática de leitura de radiografia, não consegue avaliar sozinho se a suspeita se sustenta. Na dúvida, determina a verificação física. A verificação não encontra irregularidade, a carga é liberada com atraso, e quem analisou a imagem não fica sabendo do resultado.

### 2. Questões de refinamento

As questões seguem os **sete elementos característicos do cenário** vistos em aula (**ambiente/contexto, atores, objetivos, planejamento, ações, eventos e avaliação**) e perguntam apenas o que está ausente do cenário inicial. Só documentos, normas e matérias históricas foram usados nas respostas; como as matérias sobre Santos são de 2013 e 2015, o funcionamento atual depende de confirmação empírica na Entrega 7 e o que não tem fonte atual fica marcado como `[H]` ou `[?]`.

| # | Elemento | Questão | Por que precisa ser respondida | Fonte/forma de obter resposta |
|---|---|---|---|---|
| Q1 | Ambiente/contexto | Em que setor da Alfândega de Santos as imagens de escâner são analisadas e em que regime de funcionamento? | Contextualiza o ambiente institucional de onde parte o apontamento que chega a P02. | `[F]` A Tribuna, 2013 e 2015 (registro histórico): as imagens eram analisadas na Central de Operações e Vigilância (COV), na sede da Alfândega, em plantão de 24 horas. `[F]` Portaria ALF/STS nº 197/2025, art. 34: a vigilância remota e a verificação do uso de inspeção não invasiva competem à Equipe de Vigilância e Plantão (Eqvig). `[?]` Cargo desses servidores e se a COV opera hoje como descrito em 2013. |
| Q2 | Atores | Quem tem atribuição para bloquear ou liberar a carga a partir da imagem antes do despacho? | Identifica os atores envolvidos e separa o bloqueio operacional da decisão formal do despacho (H39). | `[F]` A Tribuna, 2013 (registro histórico): os servidores da COV podiam consultar os sistemas da Receita e liberar ou bloquear cargas de importação e exportação. `[?]` Em que sistema o bloqueio é feito atualmente. |
| Q3 | Objetivos | Quem responde pelo objetivo de decidir o despacho aduaneiro, a que equipe pertence e qual é o alcance formal dessa decisão? | Confirma o objetivo institucional de P02 e a distância organizacional entre quem decide o despacho e quem viu a imagem. | `[F]` Manual de Despacho de Importação (C02): o Auditor-Fiscal responde pelo desembaraço. `[F]` Portaria ALF/STS nº 197/2025, art. 1º: a Equipe de Despacho Aduaneiro de Importação (Edaim) fica na Divisão de Despacho, e a Eqvig em outra divisão. `[H]` P02 atua na Edaim. |
| Q4 | Eventos | Como o evento de bloqueio por suspeita na imagem é comunicado da vigilância ao auditor responsável pelo despacho? | É o evento de transição em que a informação sobre a anomalia pode se perder. | `[?]` Não encontrado para Santos (lacuna ?08). `[F]` Em Imbituba, o recinto comunica a suspeita à RFB com interrupção do fluxo (Portaria ALF/FNS nº 9/2024, art. 8º), o que vale para uma unidade. Investigar na Entrega 7. |
| Q5 | Planejamento | O auditor do despacho tem acesso à imagem do escâner e como ele planeja a verificação da suspeita antes de decidir? | Define se o planejamento da análise inclui inspecionar diretamente a evidência visual ou apenas ler o relato de terceiros. | `[F]` A Tribuna, 2013 (registro histórico), fala do inspetor: o servidor responsável pelo despacho precisa ter convicção para liberar, e "algumas vezes, apenas a imagem do escâner pode ser suficiente". `[F]` A norma nacional prevê software de análise em estações de trabalho da RFB (ADE Coana nº 19/2014). `[?]` Onde e como o auditor acessa a imagem hoje, e se sabe interpretá-la. |
| Q6 | Planejamento | Que informações da declaração e do dossiê ele reúne para planejar o confronto com a suspeita apontada na imagem? | Define quais dados documentais precisam ser articulados no momento da decisão (H11). | `[F]` C02: o despacho se apoia no dossiê de documentos, e a seleção do canal considera natureza e características da mercadoria, origem e habitualidade do importador. `[?]` Quais desses dados o auditor de fato usa diante de uma suspeita de imagem. |
| Q7 | Ações | Que ações formais ele pode executar no sistema depois de analisar a suspeita? | Delimita as ações possíveis para concluir a tarefa (H06). | `[F]` C02: exigência fiscal com motivo e prazo, verificação física e desembaraço, e a declaração em canal verde pode ser redirecionada quando há indício de irregularidade. `[F]` A Tribuna, 2013 (registro histórico): a conferência física podia ser presencial ou remota, via COV. `[?]` Qual ato é usado hoje quando a origem da suspeita é a imagem. |
| Q8 | Ambiente/contexto | Por quanto tempo a carga permanece retida no ambiente portuário enquanto o auditor analisa e decide? | Caracteriza a pressão temporal do contexto operacional e o custo de uma retenção prolongada (H08). | `[?]` Não encontrado para Santos. `[F]` Em Imbituba, a carga segue se a RFB não se manifestar em 3 dias úteis (Portaria ALF/FNS nº 9/2024, art. 8º). |
| Q9 | Eventos | Com que frequência eventos de cargas bloqueadas por imagem chegam à equipe de despacho? | Indica se esse evento é rotina ou exceção, o que muda a prioridade da tarefa. | `[F]` A Tribuna, 2015 (registro histórico): 16 escâneres nos terminais, e desde setembro de 2013 a Receita determinou a inspeção de todas as cargas de importação no desembarque. `[?]` Quantas imagens viram suspeita hoje e quantas chegam ao despacho. |
| Q10 | Avaliação | O que fica registrado para avaliação posterior da decisão, e quem recebe retorno sobre o desfecho da verificação física? | Sustenta a avaliação e a rastreabilidade do ato (H17, H32) e mostra se quem analisou a imagem consegue avaliar o acerto do bloqueio. | `[F]` A Tribuna, 2013 (registro histórico): imagens guardadas por 90 dias na COV e dados de controle por cinco anos em Santos. `[F]` C02: a decisão com valor jurídico é registrada no Siscomex. `[?]` Se a suspeita de imagem fica vinculada à declaração e se há retorno a quem a analisou. |

### 3. Cenário refinado

Atores: Dr. Eduardo Resende (Auditor-Fiscal), servidor da vigilância que analisou a imagem, importador.

Dr. Eduardo Resende, Auditor-Fiscal na Alfândega do Porto de Santos, **[NOVO [Q3]: `[F]` responde formalmente pela decisão do despacho aduaneiro (C02) e `[H]` atua na equipe de despacho de importação (Edaim), que fica em uma divisão diferente da equipe de vigilância (Eqvig) `[F]` (Portaria ALF/STS nº 197/2025)]**. Ele recebe uma declaração de importação cuja carga está bloqueada porque a imagem do escâner levantou suspeita. **[NOVO [Q1, Q2, Q9]: `[F]` Segundo registros históricos de Santos (A Tribuna, 2013 e 2015), a imagem era analisada por servidores da Receita na Central de Operações e Vigilância (COV), em plantão de 24 horas, com atribuição para bloquear a carga, competindo hoje à Eqvig a vigilância remota (Portaria ALF/STS nº 197/2025, art. 34). `[?]` Não sabemos se a COV segue operando do mesmo modo nem com que frequência esses bloqueios chegam hoje ao despacho.]**

Ele precisa decidir o que fazer com essa carga e formalizar a decisão. Abre a declaração no Siscomex e lê o que a mercadoria declara ser, **[NOVO [Q6]: `[F]` planejando a conferência a partir dos documentos do dossiê, da natureza da mercadoria, da origem e do histórico do importador (C02), `[?]` embora ainda não saibamos quais desses itens ele prioriza diante de uma suspeita radiográfica]**. Sabe que existe uma suspeita, mas não sabe o que foi visto na imagem nem em que parte do contêiner. **[NOVO [Q4]: `[H]` O evento de bloqueio não chegou a ele acompanhado de uma explicação detalhada; `[?]` como a suspeita passa da vigilância para o despacho em Santos é uma lacuna que a equipe ainda precisa apurar na Entrega 7 (?08).]**

A imagem não está junto da declaração. **[NOVO [Q5]: `[F]` Embora haja registro histórico de que o servidor do despacho pode se apoiar na imagem do escâner para formar convicção (A Tribuna, 2013) e previsão normativa de software de análise em estações da RFB (ADE Coana nº 19/2014), `[H]` a equipe supõe que, para isso, ele precisa buscá-la fora do Siscomex, em outro sistema; `[?]` onde e como o auditor acessa a imagem atualmente segue sem resposta.]** Ele procura quem fez o bloqueio para entender o motivo e recebe uma descrição curta, que tenta relacionar com a mercadoria declarada. Sem prática de leitura de radiografia, não consegue avaliar sozinho se a suspeita se sustenta.

**[NOVO [Q7, Q8]: `[F]` As ações formais de que ele dispõe no Siscomex são registrar uma exigência fiscal com motivo e prazo, determinar a verificação física ou desembaraçar a declaração (C02). `[?]` Enquanto não decide, a carga permanece retida no terminal por prazo que ainda não foi apurado para Santos (H08).]** Na dúvida, determina a verificação física. **[NOVO [Q10]: `[H]` Ao justificar o ato no Siscomex, escreve o motivo com as próprias palavras, a partir do relato que recebeu, porque a análise da imagem não estaria vinculada à declaração; `[?]` se esse vínculo existe hoje é pergunta em aberto.]**

A verificação não encontra irregularidade, a carga é liberada com atraso, e quem analisou a imagem não fica sabendo do resultado. **[NOVO [Q10]: `[F]` A decisão fica registrada no Siscomex (C02) e há referência histórica de guarda das imagens por 90 dias na COV (A Tribuna, 2013), mas `[H]` nada vincula a imagem ao resultado da verificação física para permitir a avaliação do acerto por quem originou o alerta `[?]` (?08).]**

A base de cada trecho novo está na tabela da seção 2, na questão indicada entre colchetes (`[Q1]` a `[Q10]`), com `[F]`, `[H]` ou `[?]`.

### 4. Elementos extraídos

| Elemento | Evidência no cenário |
|---|---|
| Ambiente/contexto | Alfândega do Porto de Santos; equipe de despacho (Edaim) e equipe de vigilância (Eqvig) alocadas em divisões diferentes `[F]`; funcionamento atual da COV em aberto `[?]`; carga retida no terminal aguardando decisão por tempo ainda não apurado em Santos `[?, H08]`. |
| Atores | Dr. Eduardo Resende, Auditor-Fiscal responsável pelo despacho de importação (P02) `[F, H]`; servidor da vigilância que analisou a imagem e bloqueou a carga `[F, ?]`; importador que aguarda a liberação. |
| Objetivos | Decidir sobre a carga bloqueada com convicção suficiente para sustentar o ato administrativo e formalizá-lo com justificativa no Siscomex `[F, H06]`. |
| Planejamento | Consulta à declaração, ao dossiê de documentos e aos dados da mercadoria e do importador no Siscomex `[F]`; necessidade de localizar a imagem radiográfica fora do Siscomex `[H, ?]` e de obter o relato de quem efetuou o bloqueio para planejar o confronto documental (H11). |
| Ações | Abrir e ler a declaração e o dossiê; procurar o autor do bloqueio para obter o motivo; tentar confrontar o relato com a mercadoria declarada; escolher entre exigência fiscal, verificação física ou desembaraço `[F]`; redigir manualmente o motivo do ato no Siscomex `[H]`. |
| Eventos | Recebimento de declaração bloqueada por suspeita em imagem de escâner `[H]`; comunicação da suspeita entre vigilância e despacho sem detalhamento visual anexo `[H, ?08]`; realização da verificação física sem constatação de irregularidade e liberação da carga com atraso `[H]`. |
| Avaliação | Dificuldade de avaliar a procedência da suspeita sem ver a região indicada e sem prática de leitura radiográfica `[H]`; decisão formalizada sem vínculo direto com a evidência visual `[H, ?]`; ausência de retorno sobre o resultado da verificação física a quem analisou a imagem na vigilância `[H, ?08]`. |

### 5. Implicações para as próximas entregas

Tarefas que merecem análise na Entrega 5:

- entender por que uma carga foi bloqueada a partir da imagem;
- confrontar o que a imagem indica com o que a declaração descreve;
- decidir e formalizar o ato com motivo.

Informações a coletar na Entrega 7:

- como a suspeita passa da vigilância para o despacho em Santos (Q4, ?08);
- se o auditor do despacho abre a imagem e como (Q5);
- que ato é usado quando a suspeita vem da imagem (Q7);
- tempo de retenção e volume de casos (Q8, Q9);
- se existe retorno a quem analisou a imagem (Q10);
- se a COV funciona hoje como descrito em 2013 e que cargo analisa as imagens (Q1).

---

## Cenário CP03 — Verificação física no pátio sem localização da suspeita apontada na imagem

**Autor(a):** Alexandre Domiciano Pierri — 22.125.061-6  
**Persona(s) relacionada(s):** P03 – Marcos Oliveira (Agente de Campo / Fiscal de Pátio e Vistoria Física, proto-persona exploratória de stakeholder impactado pelo apontamento)  
**Necessidade relacionada:** R03 (registrar o apontamento com informação suficiente para que a etapa seguinte saiba o que foi visto e onde), com reflexo indireto de R01  
**Situação concreta da Entrega 1 relacionada:** Seção 4.4 / H12 (consequência operacional de encaminhar um contêiner para vistoria física) e H28/H42 (como o apontamento da análise de imagem instrui quem executa a verificação física)  
**Hipóteses ainda presentes:** H03, H12, H17, H28, H31, H37, H42 e a lacuna ?08  

**Enquadramento no escopo do projeto.** Conforme registrado em [`RASTREABILIDADE.md`](../RASTREABILIDADE.md), o recorte principal da interface de IHC concentra-se na estação de análise de imagem (P01, H01) e na decisão sobre a carga (P02, H39). O perfil P03 permanece como proto-persona exploratória de stakeholder secundário (H03), pois ainda não há evidência de que quem realiza a verificação física no pátio utilize diretamente a solução (H42 aberta para a Entrega 7). Este cenário investiga a ponta final da cadeia do problema humano: o que acontece na verificação física quando a suspeita gerada a partir do raio-X chega sem indicação de qual parte do contêiner motivou a retenção. Toda a narrativa é exploratória `[H]`, salvo onde há norma ou documento citado `[F]`.

### 1. Cenário inicial

Durante o turno da noite em um terminal portuário, Marcos Oliveira (P03) recebe uma solicitação de verificação física para um contêiner refrigerado (*reefer*) mantido em retenção após passar pelo escâner. A indicação vinculada ao processo informa apenas que houve uma inconsistência de densidade na imagem de raio-X, sem especificar em que parte do contêiner (porta, meio ou fundo), em que altura ou que tipo de divergência chamou a atenção de quem analisou a imagem.

Marcos desloca-se até o pátio sob iluminação artificial precária e ruído intenso de maquinário pesado. Acompanhado pela equipe de apoio, ele precisa romper os lacres e acompanhar o descarregamento manual de dezenas de caixas de carne congelada na tentativa de localizar o ponto que motivou a suspeita. Sem uma descrição que situe a região da divergência dentro da unidade de carga, a equipe gasta mais de três horas esvaziando dois terços do contêiner até constatar que a diferença de densidade decorria de acúmulo de gelo junto à estrutura interna de refrigeração, sem irregularidade na mercadoria.

O processo prolonga a permanência da carga no pátio, gera atrito com o operador logístico pelo risco à conservação do produto refrigerado e exige esforço físico elevado na movimentação de uma carga regular. Ao concluir a conferência e registrar o resultado, Marcos percebe que uma descrição clara de onde estava a suspeita na imagem teria evitado a retirada de grande parte da mercadoria.

---

### 2. Questões de refinamento

As perguntas abaixo cobrem os **sete elementos característicos do cenário** (**ambiente/contexto, atores, objetivos, planejamento, ações, eventos e avaliação**) e buscam apenas informações **ainda ausentes** do cenário inicial. Como nenhuma entrevista ou observação de campo foi realizada até o momento, as respostas apoiam-se exclusivamente em normas e documentos já levantados (`[F]`), mantendo hipóteses como `[H]` e dúvidas dependentes da Entrega 7 como `[?]`.

| # | Elemento | Questão | Por que precisa ser respondida | Fonte/forma de obter resposta |
|---|---|---|---|---|
| Q1 | Atores | Quem formalmente conduz, acompanha e executa a verificação física de uma carga retida no recinto alfandegado? | O cenário inicial fala em “agente de campo” e “equipe de apoio”, mas não distingue o papel da autoridade aduaneira, dos trabalhadores do recinto e do representante do importador. | `[F]` Decreto nº 6.759/2009 (Regulamento Aduaneiro) e Manual de Despacho de Importação (C02): a conferência física é realizada pela fiscalização aduaneira na presença do importador ou de seu representante, cabendo ao depositário a movimentação da carga. `[?]` Qual cargo específico conduz a vistoria em cada unidade e como P03 se insere nessa divisão (H42). |
| Q2 | Objetivos | Qual é o objetivo institucional da verificação física determinada após uma suspeita e o que precisa ser respondido ao final dela? | Esclarece para que serve a verificação dentro do despacho aduaneiro e qual decisão depende do seu resultado. | `[F]` Manual de Despacho de Importação (C02): a verificação física visa identificar a mercadoria e constatar sua conformidade com a declaração para subsidiar o desembaraço ou a exigência/apreensão. `[?]` Como o objetivo é delimitado quando a conferência é motivada apenas por suspeita no escâner. |
| Q3 | Eventos | Que eventos formais desencadeiam a verificação física após a passagem pelo escâner e que condições precisam ocorrer antes da abertura do contêiner? | O cenário inicial parte da ordem já recebida, sem explicitar como a retenção vira verificação física nem o agendamento prévio. | `[F]` Portaria ALF/FNS nº 9/2024 (art. 8º): a comunicação de suspeita interrompe o fluxo do veículo e mantém a carga retida e segregada até manifestação da RFB. `[F]` C02: a verificação física passa por agendamento antes da realização. `[?]` Como o evento de agendamento ocorre quando a retenção parte do escâner. |
| Q4 | Planejamento | Que documentos e informações chegam atualmente à equipe responsável pela verificação física para planejar a inspeção da carga? | Permite saber se quem vai ao pátio recebe a imagem do escâner, um relato textual ou apenas os dados da declaração. | `[F]` C02: o despacho conta com a declaração e o dossiê de documentos. `[?]` Se algum recorte da imagem radiográfica ou descrição da região suspeita acompanha o pedido de verificação física hoje (H28, H31, ?08). Entrevista na Entrega 7. |
| Q5 | Ambiente/contexto | Em que local do recinto ocorre a verificação física e se existe possibilidade de acompanhamento remoto pela fiscalização? | O cenário inicial já menciona turno noturno, iluminação precária e ruído no pátio, mas não informa as exigências normativas da área de conferência nem se há monitoramento por câmeras. | `[F]` A Tribuna, 2013 (registro histórico de Santos): a conferência física pode ser acompanhada presencialmente no terminal ou remotamente, por câmeras, a partir da COV. `[?]` Condições físicas reais da área de verificação de cargas refrigeradas e uso de equipamentos em campo (Entrega 7). |
| Q6 | Ações | Como a desova e a conferência são executadas quando não há indicação espacial da suspeita e onde o resultado da verificação é formalizado? | Detalha as ações humanas de abertura, inspeção e registro sem presumir uma interface futura. | `[F]` C02: após a realização da verificação física, o resultado é registrado no fluxo do despacho no Siscomex para permitir o desembaraço ou nova exigência. `[?]` Se existe procedimento padrão para desova parcial ou total e como o servidor anota as constatações durante o ato no pátio (H37, H42). |
| Q7 | Avaliação | Como o resultado da verificação física é avaliado e se há retorno para quem apontou a suspeita na estação de imagem? | O cenário inicial mostra um falso positivo (gelo na estrutura de refrigeração), mas não explica se esse desfecho realimenta a triagem por imagem. | `[F]` Portaria ALF/FNS nº 9/2024 (art. 5º): as imagens permanecem armazenadas por 180 dias para consulta. `[?]` Se o resultado da verificação física fica vinculado à imagem ou retorna a quem operou o escâner (H17, H38, ?08). |

---

### 3. Cenário refinado

Durante o turno da noite em um terminal portuário, Marcos Oliveira (P03) recebe uma solicitação de verificação física para um contêiner refrigerado (*reefer*) mantido em retenção após passar pelo escâner. **[NOVO [Q1, Q3]: `[F]` Na referência normativa de Imbituba, quando há suspeita na inspeção não invasiva, o fluxo do veículo é interrompido e a carga fica retida e segregada aguardando manifestação da RFB (Portaria ALF/FNS nº 9/2024, art. 8º), e no fluxo do despacho a verificação física passa por agendamento e exige a presença do importador ou de seu representante ao lado da fiscalização e da equipe do depositário que movimenta a carga (Decreto nº 6.759/2009; C02). `[?]` Ainda não sabemos qual é o cargo exato de quem conduz a vistoria em campo nem como o agendamento ocorre nos casos vindos do escâner (H42).]** A indicação vinculada ao processo informa apenas que houve uma inconsistência de densidade na imagem de raio-X, sem especificar em que parte do contêiner (porta, meio ou fundo), em que altura ou que tipo de divergência chamou a atenção de quem analisou a imagem. **[NOVO [Q4]: `[F]` Os dados da mercadoria declarada e do dossiê existem no processo de despacho (C02), mas `[H]` a equipe do projeto supõe que o apontamento da imagem chega à etapa de verificação física apenas como observação textual curta, sem indicação espacial da região suspeita; `[?]` que informações exatas chegam a quem executa a vistoria é uma lacuna a investigar na Entrega 7 (H28, H31, ?08).]**

Marcos desloca-se até o pátio sob iluminação artificial precária e ruído intenso de maquinário pesado. **[NOVO [Q5]: `[F]` Há registro histórico em Santos de que a conferência física em terminais pode ocorrer de forma presencial ou com acompanhamento remoto por câmeras a partir da central de vigilância (A Tribuna, 2013). `[?]` Não sabemos em que condições físicas de área coberta, temperatura e comunicação ocorrem hoje as verificações presenciais de contêineres refrigerados na unidade estudada.]** Acompanhado pela equipe de apoio, **[NOVO [Q2, Q6]: `[F]` cujo objetivo formal é verificar a identidade e a conformidade da mercadoria declarada para subsidiar a decisão do despacho (C02), `[H]` Marcos não dispõe de indicação sobre qual seção do contêiner motivou a dúvida e, por isso, inicia a retirada da carga a partir da porta. `[?]` Não sabemos se há procedimento operacional padrão que defina desova parcial ou total nesses casos.]** Ele precisa romper os lacres e acompanhar o descarregamento manual de dezenas de caixas de carne congelada na tentativa de localizar o ponto que motivou a suspeita. Sem uma descrição que situe a região da divergência dentro da unidade de carga, a equipe gasta mais de três horas esvaziando dois terços do contêiner até constatar que a diferença de densidade decorria de acúmulo de gelo junto à estrutura interna de refrigeração, sem irregularidade na mercadoria. **[NOVO [Q4, Q6]: `[H]` Se a comunicação da suspeita informasse que a diferença de densidade estava concentrada junto à parede do fundo, na altura do equipamento de refrigeração, a conferência poderia ter direcionado a atenção para essa estrutura antes de retirar a maior parte da carga.]**

O processo prolonga a permanência da carga no pátio, gera atrito com o operador logístico pelo risco à conservação do produto refrigerado e exige esforço físico elevado na movimentação de uma carga regular. Ao concluir a conferência e registrar o resultado **[NOVO [Q6, Q7]: `[F]` para que o despacho siga no Siscomex rumo ao desembaraço (C02), `[?]` ainda não sabemos se Marcos faz anotações em papel ou formulário próprio no pátio antes do registro no sistema na mesa de trabalho (H37, H42), nem se quem apontou a suspeita na estação de imagem recebe retorno de que o caso era apenas gelo acumulado no equipamento (H17, H38, ?08)]**, Marcos percebe que uma descrição clara de onde estava a suspeita na imagem teria evitado a retirada de grande parte da mercadoria.

---

### 4. Elementos extraídos

| Elemento | Evidência no cenário |
|---|---|
| **Ambiente/contexto** | Área de verificação física em terminal portuário durante turno noturno, sob iluminação artificial precária e ruído de maquinário `[H]`; contêiner refrigerado (*reefer*) retido e segregado após passagem pelo escâner `[F, H]`; possibilidade histórica de acompanhamento presencial ou remoto `[F]` e condições reais de campo em aberto `[?]`. |
| **Atores** | Marcos Oliveira (P03, proto-persona exploratória de quem conduz a vistoria no pátio) `[H, H42]`; equipe do depositário responsável pela movimentação física das caixas `[F]`; representante do importador `[F]`; operador de imagem e responsável pelo despacho nas etapas anteriores `[F, H]`. |
| **Objetivos** | Verificar fisicamente a carga retida para confirmar se a suspeita de densidade corresponde a uma irregularidade ou se a mercadoria está conforme a declaração, permitindo concluir o despacho com segurança `[F, H]`. |
| **Planejamento** | Consulta aos dados da declaração de importação `[F]` e à observação de retenção vinda da análise de raio-X `[H]`; ausência de informação sobre qual região do contêiner (porta, meio, fundo ou altura) motivou a suspeita `[H, ?08]`, impedindo planejar uma conferência direcionada. |
| **Ações** | Deslocar-se ao setor de vistoria; romper lacres; conduzir o descarregamento manual a partir da porta `[H]`; inspecionar as caixas e o interior do contêiner; identificar que a densidade atípica vinha de gelo acumulado na estrutura de refrigeração `[H]`; registrar o resultado da verificação para liberação no despacho `[F, ?]`. |
| **Eventos** | Retenção e segregação do contêiner após comunicação de suspeita no escâner `[F]`; agendamento da verificação física `[F]`; mais de três horas de desova de dois terços da carga congelada até localizar a causa da divergência `[H]`. |
| **Avaliação** | Constatação de falso positivo (acúmulo de gelo no sistema de refrigeração e não ilícito na carga) após esforço físico e atraso prolongado `[H]`; falta de vínculo conhecido que devolva esse resultado a quem analisou a imagem do escâner para evitar repetições em casos semelhantes `[H, ?08]`. |

---

### 5. Implicações para as próximas entregas

Como P03 é um stakeholder cuja interação direta com a solução não está confirmada no escopo (H42 aberta), este cenário contribui principalmente para entender **o que precisa constar no registro produzido nas etapas anteriores (CP01 e CP02)** e para preparar a investigação da Entrega 7.

* **Tarefas candidatas para análise na Entrega 5 (em caráter exploratório condicionado a H42):** modelar o trabalho atual de conferência física no pátio e registro do resultado (T07 a T09), sem presumir aplicativos móveis nem telas da solução futura, para explicitar quais informações fazem falta quando a carga é aberta.
* **Informações a coletar na Entrega 7 (entrevistas e documentos):**
  1. Quem conduz presencialmente a verificação física nas unidades aduaneiras e se esse profissional tem contato com sistemas de imagem ou apenas com o despacho (H03, H42).
  2. Que informações acompanham hoje um pedido de verificação física motivado por escâner: se vai apenas texto, recorte da imagem ou indicação de posição no contêiner (H28, H31, ?08).
  3. Como as constatações feitas durante a vistoria no pátio são anotadas e transferidas para o sistema de despacho (H37).
  4. Se o resultado da verificação física retorna para quem examinou a imagem de raio-X (H17, H38, ?08).

---

## Referências

Fontes do cenário CP01:

- BRASIL. Receita Federal. **Portaria RFB nº 143, de 11 de fevereiro de 2022**. Art. 14, sobre equipamentos de inspeção não invasiva e transmissão das imagens à RFB.
- BRASIL. Receita Federal. Alfândega em Florianópolis. **Portaria ALF/FNS nº 9, de 22 de agosto de 2024**. Arts. 3º, 5º e 8º. Norma de uma unidade (Imbituba), e não regra nacional.
- BRASIL. Receita Federal. Coordenação-Geral de Administração Aduaneira. **Ato Declaratório Executivo Coana nº 19, de 6 de outubro de 2014**. Item 1.2.8, sobre funções do software de análise de imagem do escâner. As três normas foram lidas na reprodução do site normasbrasil.com.br, e não no Diário Oficial da União (ver [Entrega 3](03_personas_contexto_jornada.md#referências)).
- Análises C02 e C03 da [Entrega 2](02_analise_concorrencia.md).
- BARBOSA, Simone D. J.; SILVA, Bruno S. **Interação Humano-Computador**. Elsevier/Campus. Estrutura de cenário (título, objetivo, contexto, recursos, atores, episódios).

Fontes do cenário CP02:

- A TRIBUNA. **Novo sistema de fiscalização deve agilizar os processos de liberação de cargas**. Santos, 2013. Lida em reprodução de terceiros: https://contadores.cnt.br/projetos/48/noticias/tecnicas/2013/12/04/novo-sistema-de-fiscalizacao-deve-agilizar-os-processos-de-liberacao-de-cargas.html. Acesso em: 08/10/2026.
- A TRIBUNA. **Tecnologia adotada no Porto de Santos afasta quadrilhas**. Santos, 24/06/2015. Lida em reprodução no site do Setcesp: https://setcesp.org.br/noticias/tecnologia-adotada-no-porto-de-santos-afasta-quadrilhas/. Acesso em: 08/10/2026.
- BRASIL. Receita Federal. Alfândega do Porto de Santos. **Portaria ALF/STS nº 197, de 24 de setembro de 2025**. Altera a Portaria ALF/STS nº 7, de 28 de janeiro de 2021, sobre a organização interna da Alfândega. Lida em https://www.normasbrasil.com.br/norma/portaria-197-2025_483927.html, e não no Diário Oficial da União. Acesso em: 08/10/2026.
- Manual de Despacho de Importação, Portaria ALF/FNS nº 9/2024 e ADE Coana nº 19/2014: referências completas nas Entregas 2 e 3.

As duas matérias são de jornal e têm mais de dez anos. Sustentam o que se dizia sobre Santos em 2013 e 2015, e não o funcionamento atual.

Fontes do cenário CP03:

- BRASIL. Presidência da República. **Decreto nº 6.759, de 5 de fevereiro de 2009** (Regulamento Aduaneiro). Disposições sobre a conferência física e fiscalização aduaneira de mercadorias.
- BRASIL. Receita Federal. **Manual de Despacho de Importação (MDI)**. Diretrizes sobre canais de parametrização e verificação física (análise C02 da Entrega 2).
- Portaria ALF/FNS nº 9/2024 e A Tribuna (2013): referências completas nos cenários CP01 e CP02.
- Entregas 1, 2 e 3 do projeto de IHC (especificamente as hipóteses H12, H28, H42 e a caracterização exploratória de P03).

## Checklist

- [x] Há um cenário completo por integrante.
- [x] Cada cenário tem título, ator, objetivo, contexto e problema.
- [x] O cenário possui origem rastreável na Entrega 1 ou justifica claramente a inclusão de uma nova situação.
- [x] O texto descreve a situação atual, sem antecipar a solução.
- [x] Para TCC sem interface original, o cenário descreve uma prática humana plausível relacionada à contribuição técnica, e não “a falta de uma tela”.
- [x] Questões de refinamento acrescentam informação nova.
- [x] O refinamento mostra claramente o que foi adicionado/alterado.
- [x] Cenários são diferentes o suficiente para cobrir objetivos/problemas relevantes.
- [x] Cada cenário está ligado a persona/necessidade na matriz de rastreabilidade.

## Histórico de revisão

| Data | Versão | Alteração | Motivo |
|---|---|---|---|
| 08/10/2026 | 1.0 | Entrega original dos cenários de análise/problema (CP01, CP02 e CP03). | Entrega 4 da disciplina. |
| 25/10/2026 | 1.1 | Alinhamento das questões de refinamento e dos elementos extraídos aos sete elementos característicos do cenário (ambiente/contexto, atores, objetivos, planejamento, ações, eventos e avaliação) em CP01, CP02 e CP03; padronização dos marcadores `[Q1]`–`[Q10]` nos cenários refinados; ajuste de perguntas repetidas do cenário inicial; renomeação de C03 para CP03 e reescrita sem antecipação de solução nem fatos sem fonte, alinhada a H42 em `RASTREABILIDADE.md`. | [Feedback do professor da Entrega 4](../feedbacks_professor/Feedback_Professor_Entrega04_Equipe09.md), correções 1 a 13. |
| 15/11/2026 | 1.2 | Conferência das correções registradas em 25/10/2026 e alinhamento do status para revisada após feedback; conteúdo dos cenários preservado. | [Feedback do professor](../feedbacks_professor/Feedback_Professor_Entrega04_Equipe09.md), conferência das correções já registradas. |

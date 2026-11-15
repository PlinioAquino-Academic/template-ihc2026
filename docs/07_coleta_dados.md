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

**De quem/fontes:** [H] I01 observa intérpretes de radiografias de carga em contexto autorizado, para conhecer estratégias, dificuldades e ferramentas efetivamente utilizadas (H05/H09/H30/H43). Documentos de fabricantes e pesquisadores continuam fonte complementar, sem substituir a experiência observada. Excluir radiologia médica e materiais sem autoria.

**Ética:** observação em I01 depende de consentimento e autorização institucional, sem fotos ou gravação de telas; interromper notas diante de dado sigiloso. Em simulação com proxy, usar somente dados fictícios. Citar as fontes e respeitar a licença das imagens. Não publicar nomes de operadores, placas ou cargas identificáveis. O destaque do modelo deve ser apresentado como apoio à análise, sem atribuir a ele uma capacidade de identificar ilícitos que o TCC não demonstrou.

### A02 — registro e responsabilidades

**Autor(a):** Gabriel Albertini Pinheiro — 22.122.094-8

| Dados a coletar | Por que coletar / decisão de design | Hipóteses/lacunas |
|---|---|---|
| Responsabilidades do recinto, de quem analisa e da fiscalização | Separar o parecer técnico da decisão sobre a carga. | H01, H39 |
| Dados vinculados à imagem e forma de transmissão | Identificar o caso corretamente e evitar entrada manual desnecessária. | H11, H26 |
| Registro e encaminhamento da suspeita | Definir o conteúdo do parecer e sua relação com o processo. | H06, H28, H32, ?08 |

**De quem/fontes:** [H] investigar com participantes de análise/decisão em I02/I03 o entendimento do resultado e a comunicação/registro efetivos; I01 complementa com observação da passagem entre ferramentas e papéis. Manuais públicos continuam evidência secundária, respeitando alcance/data; uma orientação local não vale para todos os portos.

**Ética:** I02 exige consentimento e análise por perfil, sem avaliar competência pessoal; I03 registra apenas notas autorizadas. Não acessar declarações fiscais, processos identificáveis ou telas restritas. Usar apenas campos e procedimentos públicos. O PDF do protótipo é um registro de apoio, sem valor de autorização para desembaraço.

### A03 — conferência física

**Autor(a):** Alexandre Domiciano Pierri — 22.125.061-6

| Dados a coletar | Por que coletar / decisão de design | Hipóteses/lacunas |
|---|---|---|
| Atores e finalidade da verificação física | Delimitar o papel de P03. | H03, H39, H42 |
| Informações usadas para localizar e verificar a suspeita | Investigar o que precisa acompanhar o parecer. | H28, ?08 |
| Registro do achado e retorno a quem analisou a imagem | Investigar a comunicação entre análise e conferência. | H17, H38, ?08 |

**De quem/fontes:** [H] I03 investiga com quem tem experiência direta na conferência que informações recebe, dificuldades e coordenação entre papéis. Documentação institucional complementa a definição de responsabilidades. A existência de conferência física não demonstra uso da Mesa por P03 (H42).

**Ética:** não usar fotos de apreensões ou operações identificáveis. Os episódios dos cenários anteriores continuam ficcionais. [F] Ainda não houve contato com participantes; [H] I03 prevê contato autorizado, sem gravação, respeitando o direito de não responder e a exclusão por código.

### Procedimento de exclusão por código, antes de aplicar

[H] Cada responsável emite um código aleatório de 12 caracteres hexadecimais por sessão/resposta, sem nome ou contato associado, registra-o no próprio instrumento/notas e entrega uma cópia ao participante no convite privado. I02 precisa de campo próprio no Forms para o código antes da aplicação; sem esse vínculo, não é possível prometer localização de uma resposta específica. I01/I03 usam o código no cabeçalho da ficha. Não publicar códigos ou respostas brutas no GitHub.

[H] Responsáveis por pedidos: Gabriel para I02, Alexandre para I03 e Kawan para I01. Um pedido deve conter somente instrumento e código; o responsável localiza o registro correspondente, exclui a resposta/notas e eventuais cópias de trabalho e confirma a exclusão pelo canal privado. Não exigir nome para localizar o registro. Definir e comunicar uma data exata de exclusão antes de cada convite: pelo menos sete dias após a sessão, sem consolidação antes dessa data. Quem consolidar verifica os pedidos antes de gerar a síntese. Informar essa data e que após anonimização/consolidação irreversível o vínculo individual não poderá ser recuperado.

**Canal privado:** [unifkasilva@fei.edu.br](mailto:unifkasilva@fei.edu.br), caixa de Kawan para receber os pedidos de exclusão. Informar somente instrumento e código. Kawan encaminha o pedido ao responsável pelo instrumento sem publicar contato ou conteúdo da resposta. Não são aceitos pedidos em issues públicas com dados da pesquisa.

**Prazo operacional:** [H] o responsável calcula a data calendário de sete dias após a sessão, às 23h59 no fuso America/Sao_Paulo, e a escreve no convite e no consentimento antes da participação. Exemplo de cálculo, sem sessão realizada: uma sessão em 20/11/2026 terá prazo em 27/11/2026 às 23h59. Não consolidar antes do prazo informado. Se houver alteração de agenda, informar a nova data antes do consentimento.

[?] **Pendência anterior à aplicação:** configurar o campo de código e o contato/prazo em I02 e verificar o fluxo online. Não houve aplicação, geração de códigos reais ou pedido de exclusão. A coleta permanece impedida até esses pontos serem concluídos.

**Armazenamento e privacidade:** referências e sínteses sem dados pessoais permanecem no repositório. Cópias de trabalho serão mantidas apenas quando a licença permitir e descartadas até 90 dias após o encerramento da disciplina. Se houver aplicação dos instrumentos abaixo, respostas e consentimentos ficarão restritos à equipe, identificados por códigos, com descarte no mesmo prazo. Não serão solicitados nome, empregador, unidade exata ou informações sigilosas.

## Parte B — instrumentos de coleta

### I01 — investigação contextual

**Autor(a):** Kawan Mark Geronimo Da Silva — 22.222.010-5.<br>
**Técnica:** investigação contextual, distinta do questionário I02 e da entrevista I03.<br>
**Situação:** [H] instrumento planejado, não aplicado. A pesquisa documental ED01–ED05 é complementar, não cumpre esta responsabilidade individual.

**Objetivo:** compreender a atividade situada de exame e registro: sequência real, informações consultadas, alternância entre ferramentas, interrupções, dúvidas e comunicação com quem decide (H01/H05/H11/H16/H28/H30/H31/H39/H41/?08). Observar o trabalho e esclarecer brevemente a ação no seu contexto, sem conduzir uma entrevista isolada da atividade.

**Público/recrutamento:** planejar três sessões individuais: duas com adultos que interpretam radiografias de carga (P01) e uma com quem recebe a análise para decidir (P02). Incluir experiência direta na respectiva atividade e autorização institucional para observação; excluir menores, quem não consentir e situações em que não seja possível evitar dados sigilosos. Convidar por contato institucional autorizado, informando finalidade acadêmica, duração de 45–60 minutos, ausência de avaliação individual e proibição de fornecer dados de operações. Não abordar profissionais durante fiscalização nem coletar contato no instrumento.

**Alternativa de acesso:** [?] recrutamento profissional ainda não disponível. Se for utilizado adulto de logística/área próxima, realizar somente simulação com caso fictício e registrar `proxy/simulação`. A simulação permite verificar entendimento e coordenação proposta; não demonstra rotina, frequência, pressão ou prática de P01/P02. Não misturar seus registros com os profissionais. Não realizar observação real sem as autorizações necessárias.

**Abertura/consentimento a ler:** “Sou integrante da equipe 09 de IHC da FEI. Queremos entender como informações e ferramentas apoiam o exame de imagens de cargas e o registro da conclusão. A sessão dura de 45 a 60 minutos e não avalia seu desempenho pessoal. Participar é voluntário; pode pular explicações, pedir pausa ou encerrar sem prejuízo. Usaremos somente notas anonimizadas, sem gravação, fotografias, nomes, placas, empresas, números de processo ou cópias de telas operacionais. Não mostre informações sigilosas; interromperemos o registro se elas surgirem. As notas ficarão restritas à equipe e serão descartadas até 90 dias após o encerramento da disciplina. Antes de começar, você receberá código, prazo e canal privado para pedir exclusão, pelo canal unifkasilva@fei.edu.br, até a data calendário informada no convite (sete dias após a sessão). Você autoriza a observação e as notas escritas?” Registrar sim/não; se não, encerrar sem notas de trabalho.

**Procedimento padronizado:**

1. Confirmar critério de inclusão e permissão; preparar ficha sem identificação pessoal. Distinguir profissional em contexto real de proxy em simulação. Entregar código e informar prazo/canal de exclusão antes do consentimento. Confirmar que convite e consentimento informam o contato e a data limite antes de aplicar.
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

**Procedimento planejado:** [H] Gabriel convida adultos por contato privado autorizado, sem coletar contato no questionário. Planejar um piloto com três pessoas por estrato (operadores de radiografias de carga, profissionais de áreas próximas, pessoas sem experiência direta; total inicial 9), sem tratar essa conveniência como amostra representativa. Reservar 5–10 minutos. Apresentar a abertura, fornecer código/prazo/canal de exclusão e obter consentimento; recusa encerra antes das perguntas. Mostrar o mesmo estímulo a todos, sem explicar as respostas esperadas. Permitir pular questões e encerrar.

**Estímulo visual:** [H] inserir na seção de exemplo do Forms a [prancha original efetivamente usada no walkthrough](../assets/06_prototipos/mesa_inspecao.png), com visualização ampliável e identificação da versão. Ela contém radiografia, mapa, região marcada e o cartão “94% · limiar 70%”. Não substituir a imagem por uma descrição textual. O participante deve poder voltar à mesma imagem enquanto responde. A escolha dessa versão explora a ambiguidade detectada em OBS-03; não presume que seus componentes serão mantidos. Comparar alternativas, inclusive sem número, em rodada posterior, sem misturar estímulos nesta coleta.

**Verificação antes da aplicação:** [F] a captura preservada em `assets/07_coleta/i02_questionario.png` documenta a versão original, com descrição textual. [?] A inserção da imagem no Forms ainda precisa ser executada e verificada em sessão sem login, em computador e celular. Não iniciar coleta enquanto essa pendência existir. Não houve atualização online nem nova captura nesta revisão, pois o controle de navegador está indisponível.

**Abertura/consentimento planejado para o Forms:** “Somos a equipe 09 da disciplina de IHC da FEI. Estudamos como as pessoas interpretam informações em uma interface de apoio à análise de imagens de cargas. A participação dura de 5 a 10 minutos; não avalia sua competência pessoal nem exige relatar uma operação real. Participar é voluntário, pode pular perguntas ou interromper sem prejuízo. Não informe nomes, empresas, unidades ou operações identificáveis. As respostas serão usadas em análise acadêmica anonimizada, ficarão restritas à equipe e serão descartadas até 90 dias após o encerramento da disciplina. Antes de responder, guarde seu código e consulte no convite a data limite de sete dias após a sessão; pedidos de exclusão pelo código devem ser enviados a unifkasilva@fei.edu.br. Você aceita participar?” **Sim / Não (encerrar).** [?] Aplicar esta abertura ao formulário online e conferir o fluxo antes da coleta; o texto aqui é protocolo, não reprodução das perguntas de pesquisa.

**Alternativas de design em aberto:** [H31/H37] a análise pode recomendar retirar o score, substituir por indicação qualitativa ou rever o limiar. A resposta sobre o número é exploratória: não há significado operacional validado de “94%”. Não classificar a resposta do participante como errada apenas por divergir da intenção ainda não demonstrada da equipe. O esclarecimento sobre limites deve ocorrer após as respostas, sem ensinar a resposta previamente.

**Estímulo visual planejado:** o mesmo estado real do protótipo para todos, conforme protocolo abaixo. O conteúdo das perguntas fica exclusivamente no [questionário online](https://docs.google.com/forms/d/e/1FAIpQLSdSndNp5FioH8sv7jDSutkHYdAmeOqOeKNn247wJcviVF-Pkg/viewform), conforme a orientação específica do professor. Não há cópia das perguntas nem código que as reproduza no repositório.

**Encerramento e análise:** esclarecer que o resultado não comprova ilícito nem autoriza liberação da carga. Fornecer um código para solicitar exclusão antes da consolidação. Analisar em três estratos separados: (1) intérpretes de radiografias de carga, (2) profissionais de áreas próximas sem essa tarefa direta, (3) IA ou ausência de experiência no domínio. Apresentar contagens e dúvidas por estrato, sem média conjunta ou afirmação de validação de P01 a partir de (2)/(3). Pessoas de IA sem prática de carga não integram automaticamente o perfil profissional. Em (1), investigar vocabulário e utilidade percebida no contexto relatado; em (2)/(3), somente ambiguidade e compreensão geral. Nenhum estrato demonstra desempenho do algoritmo ou aceitação profissional representativa. Se alguém não informar perfil, manter `não informado`, sem inferir sua experiência.

### I03 — entrevista semiestruturada

**Autor(a):** Alexandre Domiciano Pierri — 22.125.061-6<br>
**Objetivo:** aprofundar a comunicação entre análise da imagem, decisão e conferência física.<br>
**Público:** profissional de inspeção de cargas ou área aduaneira/logística, respondendo sobre atividades que conhece diretamente.<br>
**Situação:** roteiro preparado, não aplicado.

**Recrutamento:** [H] Alexandre planeja três entrevistas individuais com adultos: um intérprete de radiografias de carga, um responsável por decisão/despacho e um participante da conferência física, todos com experiência direta na atividade sobre a qual falam. Convidar por canal privado autorizado, informando finalidade, 20–30 minutos e ausência de identificação. Se o acesso for somente a perfil próximo, registrar a relação e limitar a análise ao que conhece, sem atribuir sua fala ao papel profissional não exercido.

**Abertura/consentimento a ler:** “Sou integrante da equipe 09 de IHC da FEI. Esta entrevista acadêmica procura compreender como a análise da imagem, o registro de uma suspeita e a decisão/conferência se comunicam. A conversa dura de 20 a 30 minutos e não avalia seu desempenho. Participar é voluntário; pode deixar de responder, pedir pausa ou encerrar sem prejuízo. Peço autorização somente para notas escritas, sem áudio, vídeo ou fotografias. Não conte nomes, empresas, números de processos ou detalhes sigilosos de operações. Se isso surgir, interromperei a anotação e pedirei um exemplo genérico. As notas anonimizadas ficarão restritas à equipe e serão descartadas até 90 dias após o encerramento da disciplina. Você receberá um código e a data limite de sete dias após a sessão. Para pedir exclusão antes da consolidação, envie somente instrumento e código a unifkasilva@fei.edu.br até essa data. Ao final, recapitularei as notas para que possa corrigir minha compreensão. Você aceita a entrevista e autoriza as notas?” Registrar sim/não; recusa encerra sem notas de conteúdo.

**Procedimento:** confirmar inclusão e entregar código/prazo/canal; ler abertura e registrar consentimento; conduzir o roteiro com aprofundamentos; registrar paráfrases por tópico e marcar experiência direta ou suposição; recapitular, aceitar correções, agradecer e reafirmar exclusão/descarte. Antes da aplicação, conferir que unifkasilva@fei.edu.br e a data limite calculada para a sessão constam no convite e no consentimento. O roteiro textual abaixo é a referência para o entrevistador; o formulário online I03 é apenas apoio para notas e ainda precisa ser sincronizado e verificado com esta abertura.

**Orientação de condução:** [H] usar o roteiro como guia flexível, seguindo a sequência relatada pelo participante. Para resposta geral, pedir “Pode descrever a última ocorrência sem identificar a operação?”, “O que acontece depois?”, “Que informação consulta?”, “Quem recebe?” e “Isso acontece no seu trabalho ou é uma possibilidade que imagina?”. Pedir exemplos sanitizados e separar prática observada pelo participante de opinião. Não oferecer termos da solução para completar a resposta nem insistir se houver sigilo. Registrar duração aproximada e notas com código, papel amplo, tópico, paráfrase, experiência direta/suposição e correções da recapitulação.

**Roteiro:**

1. Com quais atividades de inspeção ou despacho você tem experiência direta?
2. Quem opera o escâner? Quem interpreta a imagem? Quem registra o apontamento? Quem decide e quem formaliza o ato? Perguntar uma função por vez e, para cada passagem, “Como a informação chega à próxima pessoa?”. Só depois verificar quais papéis coincidem no contexto do participante, sem sugerir que sejam necessariamente pessoas distintas.
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

Os instrumentos estão publicados, mas **não foram aplicados**. A verificação percorreu as seções sem enviar respostas. O protocolo e os [links de edição](../instrumentos/07_coleta/README.md) estão preservados. As perguntas de I02 ficam somente no Google Forms; o roteiro de I03 continua textual para apoiar o entrevistador.

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
- [x] Três métodos permitidos e distintos planejados: investigação contextual, questionário e entrevista.
- [ ] I02 com estímulo visual, abertura e código atualizados e verificados online.
- [x] Canal privado de exclusão definido: unifkasilva@fei.edu.br; data limite calculada e informada antes de cada convite.
- [ ] I03 online sincronizado com a abertura e os aprofundamentos do protocolo.
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

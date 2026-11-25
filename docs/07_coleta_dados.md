# Entrega 7 — Coleta de dados, necessidades e aspectos éticos

**Data:** 23/10/2026

**Revisão:** 25/11/2026

**Equipe:** 14 — Estoque com ML

**Status:** planejamento e instrumentos revisados. O formulário I01 existe no Drive da equipe. Para concluir a entrega, falta inserir o link público de resposta e verificar o acesso como participante. A equipe ainda não registrou piloto, coleta ou análise de respostas.

**Responsabilidade:** 1 solução integrada por equipe, com partes individuais conforme o modelo da atividade.

## Objetivo da atividade

Investigar como responsáveis por pequenos comércios decidem reposições e conferem divergências para revisar P01 (Mariana), P02 (Rafael) e as tarefas T01/T02 da [Entrega 5](05_analise_tarefas.md). As personas são de expectativa, não participantes reais.

A Parte A segue as cinco categorias dos slides 2–7 de **CC8122-Identificacao Necessidades-A.pdf**: usuário, tecnologia, domínio, tarefas e motivações/valores. A Parte B utiliza questionário e entrevista conforme **CC8122-Identificacao Necessidades-B.pdf**, slides 2–9 e 20–21. A amostragem e os instrumentos abaixo são propostas específicas da equipe.

### Continuidade com as entregas anteriores

| Referência | Conteúdo preservado e aplicação na coleta |
|---|---|
| [E1 — problema](01_conhecendo_o_problema.md) | Investigar pequenos comércios e os relatos limitados de contagem e ruptura, sem apresentar hipóteses como fatos |
| [E2 — concorrência](02_analise_concorrencia.md) | RC02/RC07/RC08 orientam unidade, vocabulário e incerteza; RC09/RC11 orientam revisão e fontes de dados. Recursos dos concorrentes não comprovam necessidades locais |
| [E3 — personas e jornada](03_personas_contexto_jornada.md) | Paulo — Mariana/P01; Victor — Rafael/P02. Investigar autonomia, ajuda e interrupções sem deduzir habilidade pela idade |
| [E4 — cenários](04_cenarios_problema.md) | E4-C01/R04-01: disponibilidade, prazo, recursos e acompanhamento. E4-C02/R04-02: fontes, causa da divergência e comunicação |
| [E5 — tarefas](05_analise_tarefas.md) | T01 continua com Paulo e T02 com Victor. A coleta investiga a rotina que fundamenta esses modelos |
| [E6 — protótipo](06_prototipacao_papel.md) | A primeira versão de PF01/PF02 cobria parte de T01/T02. A revisão acrescentou cartões com os desfechos de reposição e conferência. A coleta investiga se os termos, dados e decisões fazem sentido na rotina dos participantes. |

## Hipóteses e lacunas prioritárias herdadas da Entrega 1

Mantêm-se as descrições por extenso da [rastreabilidade](../RASTREABILIDADE.md), sem recuperar códigos antigos.

| Hipótese/lacuna | Evidência atual | Decisão dependente da resposta | Prioridade |
|---|---|---|---|
| Responsável pelo estoque como usuário prioritário; apoio operacional de um auxiliar | Papéis hipotéticos de E1/E3 | Quem executa T01/T02 e quem autoriza alterações | Alta |
| Processo e dados atuais; registros distribuídos entre ferramentas | Relatos da equipe sobre contagem e ruptura; processo completo desconhecido | Fontes, entrada de dados e necessidade de consolidação | Alta |
| Conhecimento comercial e familiaridade com métricas; pouca familiaridade digital de Mariana | Construção de P01 | Vocabulário, aprendizagem e ajuda | Alta |
| Compreensão dos resultados sem formação em ML; percepção de incerteza e confiança | Sem pesquisa primária | Explicação de estimativas e de informação insuficiente | Alta |
| Esforço e falhas na consolidação manual | Duplicidade fictícia em E4-C02 | Evidências para corrigir ou deixar pendente | Alta |
| Controle humano da decisão; acúmulo de tarefas e interrupções | Propostas em E3/E4 | Revisão, salvamento e retomada | Alta |
| Necessidade de histórico de previsões e decisões; vendas online | Hipóteses de E1/E3 | Histórico e canais efetivamente necessários | Média |
| Benefício das previsões para antecipar reposições | Benefício esperado, não medido | Investigar utilidade percebida; efeito real requer acompanhamento posterior | Média |
| Escopo formal do TCC | Recomendação calculada não confirmada | Confirmar dados, horizonte e funções com orientador | Alta |

## Parte A — necessidades e requisitos de IHC

### A01 — Paulo Andre de Oliveira Hirata

**Autor(a):** Paulo Andre de Oliveira Hirata — 22.125.072-3.

**Foco:** P01, E4-C01, R04-01 e T01: analisar um produto e registrar uma decisão de reposição.

#### Que dados coletar?

| Categoria / dados a coletar | Hipótese/lacuna relacionada | Necessidade e decisão de design |
|---|---|---|
| Usuário: função, experiência e faixa etária opcional | Usuário prioritário; pouca familiaridade digital | Descrever diversidade sem inferir habilidade pela idade |
| Tecnologia: dispositivos, ferramentas, conexão e autonomia | Registros distribuídos; processo atual | Definir plataforma, entrada de dados e ajuda compatíveis com a rotina |
| Domínio: significado de saldo, reserva e previsão | Conhecimento comercial e familiaridade com métricas | Distinguir disponibilidade, quantidade física e estimativa |
| Tarefas: última reposição, frequência, critérios, responsáveis e interrupções | Controle humano; acúmulo de tarefas | Definir sequência, revisão e retomada de T01 |
| Motivações/valores: prioridades, confiança, receios e aprendizagem | Benefício das previsões; percepção de incerteza | Investigar utilidade e formas de explicação e aprendizado |

#### De quem coletar?

Adultos que participam diretamente de decisões de reposição em pequenos comércios e fizeram isso nos últimos três meses. Incluir usuários de caderno, planilha ou sistema com diferentes níveis de autonomia digital; não exigir idade semelhante à persona. Proprietários definem critérios comerciais; funcionários descrevem a execução. Clientes e fornecedores são afetados por falta/excesso, mas não substituem usuários diretos nesta amostra.

#### Aspectos éticos

Dificuldades podem causar constrangimento. Explicar que não se avalia competência profissional. Não pedir faturamento, dívidas, margens ou nomes de clientes. Oferecer leitura assistida literal, sem orientar respostas, e registrar a modalidade para análise.

### A02 — Victor Merker Binda

**Autor(a):** Victor Merker Binda — 22.125.075-6.

**Foco:** P02, E4-C02, R04-02 e T02: investigar uma divergência e registrar correção justificada ou pendência.

#### Que dados coletar?

| Categoria / dados a coletar | Hipótese/lacuna relacionada | Necessidade e decisão de design |
|---|---|---|
| Usuário: papel, experiência e autonomia para alterar registros | Apoio operacional de um auxiliar | Confirmar se há auxiliar ou se o proprietário acumula tarefas |
| Tecnologia: fontes, transcrição, identificadores e dispositivos | Registros distribuídos; processo atual | Definir consulta de evidências e identificação de produtos |
| Domínio: unidade comercial, reserva, devolução e duplicidade | Conhecimento comercial e familiaridade com métricas | Evitar confusão entre produtos e unidades |
| Tarefas: conferência, causa, autorização, correção, pausa e comunicação | Esforço e falhas; interrupções | Determinar quando corrigir e quando deixar pendente |
| Motivações/valores: confiança no saldo, receio de apagar dados e ajuda | Controle humano; necessidade de histórico | Projetar revisão e alteração rastreável sem atribuir culpa ao usuário |

#### De quem coletar?

Adultos que registram movimentações ou conferem estoque e fizeram uma conferência nos últimos três meses. Buscar auxiliares e proprietários que trabalham sozinhos. A gestão esclarece autorização e processos; equipe técnica e orientador delimitam viabilidade e escopo. O processo efetivo é definido pela organização investigada, não pela persona.

#### Aspectos éticos

Relatos de erros podem expor funcionários. Entrevistar sem chefia acompanhando quando possível, não fornecer relatos individuais ao empregador e não copiar telas identificáveis. Aceitar exemplos sem nomes e sem informações comerciais reservadas.

### Proteções comuns e consentimento

Os quatro princípios do material A, pp. 10–11, orientam as medidas desta coleta. A referência à Resolução 196/96 nos slides é histórica: sua revogação consta da [Resolução CNS 466/2012](https://www.gov.br/conselho-nacional-de-saude/pt-br/atos-normativos/resolucoes/2012/resolucao-no-466.pdf/view). Conferir com o docente o enquadramento institucional antes da aplicação; este plano não declara aprovação ética.

| Princípio (material A) | Como é aplicado nesta coleta |
|---|---|
| Não maleficência — evitar danos previsíveis, imediatos ou tardios | Não perguntar faturamento, dívidas, margens, dados de clientes nem diagnósticos; não relatar ao empregador o desempenho individual de um funcionário; não registrar áudio, vídeo ou tela |
| Justiça e equidade — relevância social e cuidado com participantes vulneráveis | Não recrutar por pressão hierárquica ou familiar; entrevistar sem chefia presente quando possível; oferecer leitura assistida a quem tiver dificuldade de leitura, em vez de excluir a pessoa |
| Autonomia — consentimento livre e esclarecido e proteção de grupos vulneráveis | Convite com objetivo, duração, riscos e contato; aceite registrado; apenas maiores de 18 anos; qualquer pergunta pode ser pulada e a participação interrompida sem prejuízo |
| Beneficência — ponderar riscos e benefícios | Coletar apenas o necessário para rever personas e tarefas; informar que não há benefício individual garantido; o benefício esperado é melhorar o projeto, não resolver o estoque do participante |

Medidas práticas decorrentes, aplicáveis aos dois instrumentos:

- Participação voluntária, com possibilidade de pular perguntas ou desistir sem prejuízo. Não pressionar familiares, subordinados ou colegas.
- Usar códigos sem identificação pessoal. No questionário, a pessoa pode usar o código do convite ou criar e guardar um código próprio. O preenchimento é opcional. Na entrevista, o aplicador entrega o código da sessão. Guardar contatos de recrutamento separadamente das respostas.
- Nesta versão, registrar apenas respostas e notas autorizadas, sem áudio, vídeo ou captura de tela. Gravações futuras exigem autorização específica e revisão do protocolo.
- Armazenar em pasta restrita à equipe, protegida por senha. Compartilhar com docente somente síntese sem identificação. Não colocar dados brutos no GitHub.
- Remover nomes de pessoas, estabelecimentos e detalhes que permitam identificação indireta. Código é pseudonimização, não anonimização automática.
- Prazo proposto: apagar respostas individuais e contatos até 90 dias após a avaliação final da disciplina, salvo exigência institucional comunicada previamente; conservar síntese efetivamente anonimizada.
- Informar o contato do aplicador — victor.merker.bindaa@gmail.com — no convite e fornecer código de sessão. Permitir retirada enquanto o registro puder ser localizado; explicar que após anonimização irreversível não será possível localizar respostas individuais.

**Apresentação e consentimento, para ambos os instrumentos:**

**Contato para dúvidas e retirada de respostas:** Victor Merker Binda — victor.merker.bindaa@gmail.com (endereço confirmado pelo integrante).

> Somos Paulo Andre de Oliveira Hirata e Victor Merker Binda, estudantes de IHC da FEI. Queremos entender como as pessoas controlam o estoque e decidem reposições. Estimamos de 10 a 15 minutos para o questionário e de 20 a 30 minutos para a entrevista. A participação é voluntária. Falar de dificuldades pode gerar desconforto. Você pode pular perguntas após a triagem ou parar a qualquer momento. Não pedimos dados de clientes nem valores financeiros. Não haverá gravação. Só a equipe terá acesso aos registros individuais e os apagará até 90 dias após a avaliação final da disciplina. O relatório trará uma síntese sem identificação. Não há benefício individual garantido. Para tirar dúvidas ou solicitar retirada enquanto o registro puder ser localizado, escreva para victor.merker.bindaa@gmail.com e informe seu código. Você aceita participar?

Confirmar consentimento, maioridade e experiência recente antes das perguntas de pesquisa. Diante de recusa, encerrar. No questionário, orientar a pessoa a fechar a página sem enviar. Na entrevista, encerrar sem iniciar a ficha de respostas.

## Parte B — ferramentas de coleta

Cada integrante prepara uma técnica completa e diferente: Paulo, questionário; Victor, entrevista semiestruturada. O questionário descreve práticas e prioridades de forma comparável; a entrevista aprofunda a sequência e as evidências de um episódio. Ambos investigam necessidades; ainda não são testes de usabilidade do protótipo.

### Escolha dos métodos entre as alternativas do material B

O material B, p. 2, lista sete métodos de coleta. A escolha considerou objetivo, acesso a participantes e prazo, atendendo à orientação de p. 20 de não adotar um método qualquer.

| Método (material B) | Decisão | Justificativa |
|---|---|---|
| Entrevista (p. 3) | **Adotado — I02** | É o método da lista que permite detalhar a sequência de um episódio real de conferência e as evidências consultadas, necessário para T02. Contrapartida: exige treinar o entrevistador e leva tempo por participante |
| Questionário (p. 6) | **Adotado — I01** | Descreve práticas, ferramentas e prioridades de forma comparável entre pessoas, com baixo custo por participante, cobrindo a diversidade de rotinas de T01. Contrapartida: respostas mais superficiais |
| Grupo de foco (p. 10) | Não adotado nesta entrega | Exige reunir de três a dez pessoas no mesmo horário e moderação experiente; além disso, relatar erros de estoque diante de colegas ou da chefia agrava o risco ético descrito em A02 |
| Brainstorming de necessidades e desejos (p. 12) | Não adotado nesta entrega | Pressupõe de 8 a 12 usuários reunidos e explora desejos, enquanto esta etapa precisa primeiro descrever a rotina atual |
| Classificação de cartões (p. 13) | Adiado para o redesenho | Informa arquitetura de informação, menus e navegação; torna-se útil depois que a coleta definir vocabulário e agrupamentos para E9–E11 |
| Estudo de campo (p. 15) | Adiado | Registraria interrupções e distrações no próprio comércio, o que fortaleceria as hipóteses de E3/E4, mas depende de autorização do estabelecimento e de disponibilidade não assegurada nesta etapa |
| Investigação contextual (p. 17) | Adiado | O modelo mestre-aprendiz exigiria acompanhar o trabalho em execução; mesma restrição de acesso do estudo de campo, com envolvimento ainda maior do investigador |

Os dois métodos adotados são declarativos: registram o que a pessoa relata, não o que faz. Observação em contexto, se viável em etapa posterior, poderá confrontar esses relatos.

### Instrumento, protocolo e amostra (material B, p. 20)

- **Instrumento:** o material usado para realizar a coleta. Aqui são o formulário de I01, o roteiro e o formulário de notas de I02, mais o convite e o texto de consentimento.
- **Protocolo de execução:** é o instrumento mais importante porque o mesmo questionário ou roteiro produz dados diferentes conforme a forma de aplicar. Ordem das perguntas, leitura literal, sondagens permitidas, o que o aplicador não pode explicar e o registro da modalidade determinam se as respostas de pessoas diferentes são comparáveis e se o viés do aplicador fica controlado. Os procedimentos padronizados de I01 e I02 cumprem essa função e devem ser seguidos sem improviso; qualquer desvio é anotado na ficha de análise.
- **Amostra:** depende do método e do contexto do projeto. O questionário admite mais participantes porque o custo por resposta é baixo; a entrevista é limitada pelo tempo de condução e de análise. Por isso I01 propõe 8–12 e I02 propõe 3–4 pessoas, por conveniência. Nenhuma das faixas é amostra probabilística nem quantidade prescrita pelos slides.

### Instrumento I01 — Questionário sobre decisão de reposição

**Autor(a):** Paulo Andre de Oliveira Hirata — 22.125.072-3.

**Técnica:** questionário.

**Objetivo:** caracterizar práticas, critérios e necessidades ligadas a T01.

**Público:** A01. **Duração estimada:** 10–15 minutos, a conferir no piloto.

**Amostra planejada (proposta exploratória da equipe, não quantidade exigida nos slides):** 8–12 participantes por conveniência, buscando diversidade de ferramentas e autonomia digital. Não representa estatisticamente todos os pequenos comércios.

#### Procedimento padronizado de aplicação

**Link para responder:**

1. Publicar o questionário na conta da equipe, conforme o [instrumento I01](../instrumentos/07_questionario_reposicao.gs). Copiar o link de resposta para o campo acima. Manter a edição e os resultados restritos à equipe.
2. Abrir esse endereço em janela anônima, sem conta conectada. Se o Google restringir o acesso à instituição, ajustar o acesso de participante para “qualquer pessoa com o link” e repetir o teste. Conferir que o participante consegue responder sem login ou e-mail e que o encerramento mostra agradecimento e contato. Usar códigos de teste ao verificar o envio. Conferir o recebimento na área privada e separar esses registros da coleta.
3. Percorrer a recusa, a menoridade e a falta de experiência recente. Cada percurso deve encerrar antes do perfil. Depois, testar quem não usa registros, quem usa uma planilha mas nunca encontrou divergência e quem relata uma diferença. Repetir pulando as opcionais e escolhendo “não sei” e “prefiro não responder”. Conferir os destinos na tabela abaixo.
4. Fazer um piloto com uma pessoa elegível. Anotar versão, modalidade, duração do início ao envio ou à interrupção, perguntas que precisaram ser relidas e em que ponto a pessoa quis parar. No fim, perguntar qual questão deu mais trabalho. Se o percurso ultrapassar 15 minutos ou houver sinal de cansaço, rever primeiro as sondagens complementares (Q09a, Q12a e Q14b), ajustar o convite e repetir a medição. Guardar o piloto separado da amostra principal.
5. Na aplicação, enviar o link de resposta e oferecer um código de retirada. Na leitura assistida, ler o enunciado e as alternativas literalmente e aguardar a resposta. Registrar versão e modalidade. Desidentificar os relatos antes de compartilhar a síntese.

#### Estrutura e lógica do questionário

| Bloco | O que a pessoa encontra | Encaminhamento |
|---|---|---|
| Entrada | Objetivo, duração prevista, privacidade, contato e consentimento. Em seguida, maioridade e participação em decisão de reposição nos últimos três meses (Q01). | Só três respostas afirmativas abrem o perfil. Os demais percursos terminam com a orientação de fechar a página. |
| Perfil e registros | Código opcional, modalidade, papel, experiência, faixa etária (Q02–Q04) e uso de registros (Q05). | Quem mantém ou consulta registros pode indicar várias fontes (Q05a). Só esse grupo recebe Q11. Apenas uma divergência relatada em Q11 abre Q11a. |
| Tecnologia | Dispositivo usado (Q06), conexão e autonomia (Q06a/Q07). | Quem usa dispositivo digital vê conexão e autonomia. Quem não usa, pula ou prefere não responder segue para a rotina. |
| Última reposição | Frequência (Q08) e critérios lembrados livremente (Q09). Na página seguinte aparecem prazo e recursos (Q09a), interrupções (Q10), registro e acompanhamento (Q12/Q12a). | Registrar separadamente o que apareceu na lembrança inicial e o que surgiu depois da sondagem. |
| Disponibilidade e estimativa | Unidades físicas e reservadas (Q13) e interpretação de uma estimativa de vendas (Q14). | Somente na página seguinte aparecem os pedidos de contexto adicional e de utilidade percebida (Q14a/Q14b). |
| Prioridades e encerramento | Importância de quatro aspectos da ferramenta (Q15), dificuldades de leitura, formas de aprender e melhoria desejada (Q16a/Q16/Q17). | Cada item pode ficar em branco. Após o envio, a pessoa recebe agradecimento e contato para dúvidas ou retirada. |

Os códigos das perguntas acompanham sua versão de origem. Q11 foi agrupada com as fontes de estoque para que quem não consulta registros possa pular as perguntas sobre divergência.

#### Tipos de pergunta utilizados

Classificação conforme o material B, pp. 5 e 7–9.

| Tipo (material B) | Perguntas de I01 | Motivo da escolha |
|---|---|---|
| Fechada — escolha de um valor (p. 7) | Q01, Q03, Q05, Q06, Q06a, Q07, Q08 e Q11 | Permite comparar respostas e encaminhar para as perguntas pertinentes |
| Fechada — escolha de vários valores (p. 7) | Q02, Q05a e Q16 | A pessoa pode indicar mais de um papel, fonte de registro ou forma de aprender |
| Fechada — faixa de valores (p. 7) | Q04, faixa etária; Q10, contagem de interrupções em faixas | Evita pedir idade exata e reduz erro de memória em contagens |
| Escala de importância de cinco pontos (p. 8) | Q15, uma resposta opcional por aspecto | Descreve a importância atribuída a cada aspecto, com a alternativa “não se aplica” |
| Diferenciais semânticos (p. 8) | Não utilizado nesta entrega | Os pares de adjetivos do exemplo do slide avaliam a impressão sobre uma interface existente; esta coleta ainda investiga a rotina atual. O recurso fica reservado às avaliações das E12–E14 |
| Aberta (pp. 5 e 9) | Q09, Q09a, Q11a, Q12, Q12a, Q13 como resposta curta numérica com opção “não sei”, Q14, Q14a, Q14b, Q16a, Q17 e os campos “outra/qual?” das fechadas | Exploram critérios, significados e dificuldades sem restringir o tipo ou o tamanho da resposta nem sugerir alternativas |

Q09 abre espaço para lembrar a decisão antes de mencionar prazo e recursos em Q09a. Q14 pede a interpretação da estimativa antes de Q14a e Q14b perguntarem sobre informações adicionais e utilidade. I02 permite aprofundar um episódio que o questionário descreve brevemente.

#### Como os dados serão analisados

Apresentar contagens e denominadores válidos por pergunta. Separar pergunta pulada pela lógica, omissão voluntária, “não sei” e “não se aplica”. Em Q15, apresentar distribuição e mediana por aspecto, excluindo “não se aplica” e omissões do cálculo. Uma nota alta identifica um tema a investigar. Antes de propor um requisito, confrontá-la com um episódio concreto e considerar também relatos contrários.

Agrupar relatos por critérios comerciais, qualidade dos dados, confiança, ferramentas e ajuda. Na codificação, separar **espontânea** (Q09) de **estimulada** (Q09a). Em Q13, registrar a quantidade informada (4 unidades no exemplo), a dúvida expressa ou a omissão. Só codificar o raciocínio quando a própria pessoa o explicar. Em Q14, registrar a interpretação inicial da frase, que já informa que os valores podem variar. Distingui-la de Q14a/Q14b, que pedem contexto e utilidade. Q13 e Q14 medem compreensão dos exemplos. Avaliar desempenho com a interface exigiria observar o uso do protótipo. Guardar situações em que a estimativa seria pouco útil e comparar as modalidades de preenchimento apenas de forma descritiva.

### Instrumento I02 — Entrevista semiestruturada sobre conferência

**Autor(a):** Victor Merker Binda — 22.125.075-6.

**Técnica:** entrevista semiestruturada.

**Por que semiestruturada (material B, p. 3):** a entrevista estruturada fixaria ordem e texto e impediria aprofundar um episódio inesperado; a não estruturada dificultaria comparar relatos entre participantes e exigiria mais experiência do entrevistador. O roteiro fixo E01–E12 garante os mesmos temas em todas as sessões, e as sondagens previstas permitem detalhar o caso relatado. Como o material alerta que é necessário treinar os entrevistadores, o piloto também serve para o aplicador exercitar sondagem neutra e registro simultâneo.

**Objetivo:** compreender evidências, responsabilidades, correções e pendências em T02.

**Público:** A02. **Duração estimada:** 20–30 minutos.

**Amostra planejada (proposta exploratória da equipe, não quantidade exigida nos slides):** 3–4 participantes por conveniência; buscar auxiliares e proprietários que conferem estoque, se acessíveis. Pessoas podem responder também I01, mas a sobreposição deve ser registrada e não contada como pessoas diferentes.

#### Procedimento padronizado de aplicação

1. Preparar uma cópia da [ficha de entrevista I02](../instrumentos/07_ficha_entrevista.md) em uma pasta privada da equipe. Victor registra as notas durante a conversa e mantém o exemplo hipotético em campo próprio.
2. Fazer piloto, combinar local reservado e horário adequado, apresentar consentimento e confirmar conferência nos últimos três meses.
3. Começar pela última conferência real. Usar sondagens como “O que aconteceu depois?” e “Como você soube disso?”. Deixar a pessoa nomear fontes, causas, pessoas e decisões antes de pedir detalhes. Se uma prática nunca ocorreu, registrar essa ausência e avançar.
4. Separar paráfrase de fala literal. Não solicitar acesso a sistemas reais. Em interrupção, oferecer retomada ou encerramento.
5. Ler um resumo ao participante para confirmar entendimento, aceitar correções, agradecer e fornecer código/contato. Revisar e desidentificar as notas.

#### Roteiro completo

| Pergunta | Sondagem / dado procurado |
|---|---|
| E01. Qual sua função e como participa da conferência? | Experiência; outras pessoas; proprietário sozinho ou auxiliar; ferramentas e dispositivos utilizados |
| E02. Como foi a última conferência, do começo ao fim? | Gatilho, sequência, ferramentas, duração aproximada e término |
| E03. Como identifica que dois registros tratam do mesmo produto e unidade de venda? | Código, nome, tamanho, kit e ambiguidades |
| E04. Você se lembra de uma conferência em que encontrou uma diferença? Se sim, conte o que aconteceu. | Distinguir “nunca encontrei”, “não me lembro” e recusa. Sem episódio, pular E05–E07 e seguir para E08. |
| E05. Naquela ocasião, o que você consultou ou fez em seguida? | Retomar as fontes citadas pela pessoa. Perguntar o que cada uma permitiu descobrir. |
| E06. Como terminou esse caso? Quem participou dessa decisão? | Se a pessoa mencionar uma alteração, perguntar como decidiram fazê-la e quem a realizou. Registrar também se ninguém alterou o estoque. |
| E07. Naquele momento, ficou algo por esclarecer? | Se sim, perguntar o que aconteceu depois. Se tudo foi esclarecido, registrar o encerramento e avançar. |
| E08. Já precisou parar uma conferência no meio? | Se sim, perguntar sobre a última vez e como retomou, caso tenha retomado. Registrar também a ausência de interrupção. |
| E09. Ao terminar a conferência, você costuma registrar ou contar a alguém o que aconteceu? | Se sim, pedir um exemplo. Trabalhar sozinho ou encerrar sem registro também são respostas válidas. |
| E10. O que faz confiar ou desconfiar do saldo? | Origem, atualização e consequências de erro, sem valores financeiros |
| E11. Que dificuldades encontra ao aprender ou usar ferramentas dessa tarefa? Como prefere ajuda? | Admitir ausência de dificuldade; vocabulário, leitura, autonomia e receios de alterar registros |
| E12. Exemplo separado do relato: um registro mostra 8 conjuntos e uma contagem mostra 10. O que você faria, se fizesse algo? | Usar só depois de explorar e resumir a rotina real de E01–E11. Perguntar “O que levaria você a fazer isso?”. Guardar a resposta como hipotética. |

**Encerramento:** antes de E12, resumir o episódio e perguntar “Foi assim mesmo? Faltou algo?”. Se não houve divergência, confirmar o que a pessoa relatou sobre a rotina normal. E12 é opcional e fica em campo próprio. Ao final, abrir espaço para correções, agradecer e entregar o código e o contato da equipe.

#### Como os dados serão analisados

Codificar episódios por identificação/unidade, fonte, causa, confirmação, autorização, correção, pendência, interrupção e comunicação. A equipe consolida a codificação e resolve divergências consultando as notas. Preservar casos contrários e distinguir relato, interpretação e proposta de design. Recorrência nesta amostra não representa prevalência nem prova saturação.

## Síntese

| Evidência futura | Hipóteses/lacunas investigadas | Consequência |
|---|---|---|
| I01 Q01–Q12; I02 E01–E09 | Usuário prioritário, auxiliar, processo atual, registros distribuídos, vendas online, interrupções e falhas manuais | Rever personas, contexto e T01/T02 |
| I01 Q07/Q13–Q17; I02 E03/E10–E12 | Familiaridade digital, vocabulário, compreensão e confiança | Rever explicações, rótulos, ajuda e metas MU02/MU05/MU06 da E8 |
| I01 Q09/Q09a/Q12/Q12a/Q15; I02 E06–E10 | Controle humano e histórico | Definir revisão, rastreabilidade e retomada |
| Consulta ao orientador/documentação técnica | Escopo formal do TCC | Confirmar horizonte e eventual cálculo de reposição |

Atualizar a [rastreabilidade](../RASTREABILIDADE.md) somente depois de interpretar respostas reais. Para cada hipótese, registrar instrumento, pergunta, código da evidência, relatos favoráveis e contrários, limitações e decisão fundamentada. A ausência de dados mantém a hipótese aberta. Publicar o formulário e testar a navegação são marcos de preparação. Questionários e entrevistas também estão sujeitos a vieses de memória e de resposta socialmente desejável.

**Situação atual:** nenhum participante ou resultado reportado; nenhuma hipótese confirmada. Benefício real sobre falta/excesso exige acompanhamento posterior.

### Registro e configuração dos instrumentos

**Convite de recrutamento, em versão final:** “Somos estudantes de IHC da FEI e estamos estudando a rotina de estoque de pequenos comércios. Procuramos pessoas adultas que tenham participado de reposição ou conferência nos últimos três meses. A participação é voluntária, sem gravação e sem solicitar valores financeiros ou dados de clientes. O questionário leva aproximadamente 10–15 minutos; a entrevista, 20–30 minutos. Você pode recusar ou interromper sem prejuízo. Dúvidas e pedidos de retirada podem ser enviados a victor.merker.bindaa@gmail.com. Podemos explicar o estudo?” O convite é enviado por Victor Merker Binda, pelo endereço acima, que fica disponível para dúvidas e retirada; não publicar contatos de participantes.

| Configuração | I01 — questionário | I02 — entrevista |
|---|---|---|
| Título online | Estoque com ML — Rotina de reposição | Estoque com ML — Roteiro de conferência |
| Introdução | Texto breve para o participante, com objetivo, tempo previsto, privacidade, retenção, voluntariedade e contato | Apresentação adaptada à conversa, com duração da entrevista |
| Triagem obrigatória | Aceite sim/não; 18 anos ou mais sim/não; Q01. Qualquer “não” encerra antes das perguntas de pesquisa | Aceite e maioridade; confirmar conferência nos últimos três meses antes de E01 |
| Conteúdo | Q01–Q17 e subperguntas. As perguntas após a triagem são opcionais. Q05, Q06 e Q11 determinam os blocos seguintes. | E01–E12. Distinguir recusa, ausência de prática, episódio real e resposta hipotética. |
| Tipos | Q02/Q05a/Q16 admitem várias respostas. Q15 permite omitir cada aspecto separadamente. | Notas em texto livre, com campo separado para E12. |
| Privacidade | Sem coleta automática de e-mail; verificar ausência de exigência de login; desativar visualização pública de respostas | Formulário de notas restrito à equipe, sem acesso público às respostas |
| Identificação | Código opcional do convite ou criado e guardado pela pessoa para permitir retirada. Modalidade assistida/autônoma. | Código, data, duração, versão do roteiro, aceite e função. Contatos de recrutamento guardados separadamente. |
| Encerramento | Agradecer; lembrar o código e o canal para dúvidas/retirada | Ler o resumo ao participante e registrar correções de interpretação |

Na conferência dos dados, distinguir quem declarou não consultar registros de quem preferiu pular Q05. O mesmo vale para uso de dispositivos e ausência de divergência. Se uma combinação ficar ambígua, preservá-la como tal.

**Ficha mínima de análise, a preencher somente depois da aplicação:** código da pessoa; instrumento/versão; pergunta; resposta ou nota autorizada; relato real/exemplo hipotético; tema; hipótese relacionada; evidência favorável/contrária/inconclusiva; limitação; decisão de design. Para participação nos dois instrumentos, manter ligação privada entre os códigos e contar a pessoa uma única vez no total de participantes.

**Critério para encerrar a análise:** contabilizar participantes elegíveis e respostas válidas; revisar todos os temas e casos discordantes; classificar cada hipótese como sustentada no contexto, refutada, refinada ou ainda aberta; apontar o que muda nas personas/tarefas e justificar o que permanece. Não preencher percentuais, falas ou conclusões antes da coleta.

### O que ainda depende da equipe

Paulo deve inserir o link de resposta do I01, conferir o acesso externo e registrar a duração e os ajustes do piloto. Victor deve preparar a cópia privada da ficha e pilotar o roteiro da entrevista. A equipe atualizará as hipóteses depois de analisar os dados coletados.

## Checklist

- [ ] Cinco categorias de dados e perfis específicos para cada integrante.
- [ ] Hipóteses, tarefas e decisões relacionadas.
- [ ] Ética, consentimento e análise contextualizados.
- [ ] Duas técnicas distintas, incluindo o questionário obrigatório.
- [ ] Escolha dos métodos justificada diante das alternativas do material B.
- [ ] Tipos de pergunta e protocolo de execução explicitados.
- [ ] Contato para dúvidas e retirada, convite e consentimento disponíveis.
- [ ] Questionário publicado com link de resposta neste documento e acesso externo testado.
- [ ] Ficha privada de notas da entrevista preparada.
- [ ] Pilotos realizados e duração, dificuldades e ajustes registrados.
- [ ] Recrutamento e aplicação realizados.
- [ ] Respostas analisadas e hipóteses atualizadas com evidências.

## Referências

- Material da disciplina, identificado como Barbosa e Silva (2010): **CC8122-Identificacao Necessidades-A.pdf**, pp. 2–13, com os princípios éticos nas pp. 10–11; **CC8122-Identificacao Necessidades-B.pdf**, p. 2 para o conjunto de métodos, pp. 3–9 para entrevista, questionário e tipos de pergunta, pp. 10–19 para os métodos não adotados nesta etapa e pp. 20–21 para instrumento, protocolo, amostra e ferramenta online.
- **Planejamento Avaliacao IHC.pdf**, pp. 25–26 e 33–36: preparação, piloto e limites de interpretação.
- Entregas [1](01_conhecendo_o_problema.md), [2](02_analise_concorrencia.md), [3](03_personas_contexto_jornada.md), [4](04_cenarios_problema.md), [5](05_analise_tarefas.md) e [6](06_prototipacao_papel.md).

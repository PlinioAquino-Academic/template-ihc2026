# Feedback do Professor > Entrega 04 > Equipe 09

> **Status das correções (atualizado em 25/10/2026 por Kawan)**
>
> | # | Correção | Responsável | Status | Onde foi tratado |
> |---|---|---|---|---|
> | 1 | Cobrir formalmente os sete elementos característicos do cenário (ambiente/contexto, atores, objetivos, planejamento, ações, eventos e avaliação) | Equipe | Aplicado | `docs/04_cenarios_problema.md` (seções 2 e 4 de CP01, CP02 e CP03) |
> | 2 | Substituir a taxonomia paralela de CP01 pelos sete elementos característicos | Kawan | Aplicado | `docs/04_cenarios_problema.md` (CP01, seções 2 e 4) |
> | 3 | Garantir que as questões perguntem apenas o que está ausente do cenário inicial | Kawan e Alexandre | Aplicado | `docs/04_cenarios_problema.md` (Q4 de CP01 e Q1–Q7 de CP03) |
> | 4 | Vincular cada acréscimo do cenário refinado de CP01 com `[Q1]`–`[Q7]` | Kawan | Aplicado | `docs/04_cenarios_problema.md` (CP01, seção 3) |
> | 5 | Padronizar colchetes `[Q1]`–`[Q10]` e mapear os sete elementos em CP02 | Gabriel | Aplicado | `docs/04_cenarios_problema.md` (CP02, seções 2, 3 e 4) |
> | 6 | Expandir as questões de refinamento de CP03 para cobrir todos os sete elementos | Alexandre | Aplicado | `docs/04_cenarios_problema.md` (CP03, seção 2, Q1–Q7) |
> | 7 | Retirar respostas factuais sem evidência de CP03 e marcar hipóteses/lacunas com `[H]` e `[?]` | Alexandre | Aplicado | `docs/04_cenarios_problema.md` (CP03, seções 2, 3 e 4) |
> | 8 | Reformular CP03 sem definir o problema como ausência de ROI/mapa residual | Alexandre | Aplicado | `docs/04_cenarios_problema.md` (CP03, seções 1 a 5) |
> | 9 | Alinhar CP03 com `RASTREABILIDADE.md` sobre P03 e H42, sem terminal móvel | Alexandre | Aplicado | `docs/04_cenarios_problema.md` (CP03) e `RASTREABILIDADE.md` (H42, P03, R03) |
> | 10 | Padronizar o identificador `C03` para `CP03` | Alexandre | Aplicado | `docs/04_cenarios_problema.md` (título e referências de CP03) |
> | 11 | Manter explícito que a norma de Imbituba em CP01 vale para uma unidade e que H01/H39 seguem abertas | Kawan | Aplicado | `docs/04_cenarios_problema.md` (CP01, seções 2 e 3) |
> | 12 | Manter explícito em CP02 o caráter histórico das matérias de 2013 e 2015 | Gabriel | Aplicado | `docs/04_cenarios_problema.md` (CP02, seções 2 e 3) |
> | 13 | Integrar CP03 de forma coerente em `RASTREABILIDADE.md` como cenário exploratório de stakeholder (H42) | Equipe | Aplicado | `RASTREABILIDADE.md` (H42, seção 2.1, linha R03 e seção 5) |

A equipe apresentou três cenários de análise/problema, um por integrante, e para cada um existe uma versão inicial e uma versão refinada. Portanto, a responsabilidade de autoria individual foi contemplada no nível quantitativo.

A qualidade, porém, é bastante desigual: CP01 e CP02 mostram uma evolução importante em relação às entregas anteriores: a equipe passou a separar melhor fatos, hipóteses e lacunas, corrigiu parte da confusão entre quem examina a imagem e quem toma a decisão formal e buscou fontes específicas do domínio. Esses dois cenários estão próximos da finalidade correta de um cenário de análise/problema: narrar uma situação atual, concreta e problemática sem depender da interface futura.

O principal problema da Entrega 04 está no **formalismo do refinamento**. Não basta existir uma lista de perguntas. Para cada cenário refinado deveria haver, no mínimo, uma questão nova para cada elemento característico do cenário - **ambiente/contexto, atores, objetivos, planejamento, ações, eventos e avaliação** - e cada resposta incorporada ao cenário refinado deveria ser identificada pelo número da respectiva questão. Isso não foi atendido integralmente em nenhum dos três cenários.

CP03 é o caso mais crítico. Além de possuir somente três questões de refinamento, ele volta a transformar uma hipótese de usuário e uma solução futura em realidade corrente, utiliza informações muito específicas sem evidência e responde no cenário refinado a perguntas cuja própria tabela dizia que dependeriam de entrevista, observação, POP ou dados operacionais que não foram apresentados.

Há também uma inconsistência importante de continuidade: a rastreabilidade já havia reclassificado P03 como **proto-persona a validar / possível stakeholder**, retirando a interface móvel desse perfil do recorte até investigação de H42. Mesmo assim, o terceiro cenário volta a tratá-lo como usuário confirmado de um terminal móvel e constrói o problema em torno da ausência de um laudo visual com ROI, mapa residual e coordenadas. A Entrega 04 não deveria desfazer silenciosamente uma incerteza que a própria equipe havia acabado de registrar.

Em resumo: a equipe tem **três cenários e três refinamentos**, mas precisa corrigir o método de refinamento e revisar profundamente CP03. O ganho desta entrega deve ser entender melhor o problema atual, não usar a narrativa para tornar plausível uma solução que a equipe já gostaria de construir.

## Pontos positivos

- Há um cenário inicial por integrante, com autoria explícita.
- Os três cenários possuem nome, atores e narrativa descritiva.
- CP01 e CP02 procuram descrever situações atuais e não a futura interface.
- CP01 faz um bom esforço para manter separadas informações `[F]`, `[H]` e `[?]`.
- CP01 reconhece explicitamente que o personagem e algumas condições do plantão são exploratórios e não constituem evidência.
- CP02 melhora a distinção entre quem analisa a imagem, quem bloqueia uma carga e quem formaliza uma decisão.
- CP02 utiliza o refinamento para revelar lacunas reais do fluxo de informação entre vigilância e despacho.
- A equipe registrou fontes e, em CP02, reconheceu corretamente que matérias de 2013 e 2015 não demonstram necessariamente a operação atual.
- A rastreabilidade foi atualizada com mudanças importantes de escopo e com CP01/CP02, preservando a evolução do conhecimento em vez de simplesmente apagar hipóteses anteriores.
- O texto de CP01 e CP02 mostra maturidade maior na separação entre evidência documental e aquilo que ainda precisa ser investigado com pessoas.

## Correções prioritárias

### 1. O refinamento não cobre formalmente os sete elementos característicos do cenário

Este é o principal problema de conformidade da entrega.

Para cada cenário refinado era necessário formular pelo menos uma questão para cada elemento:

- ambiente ou contexto;
- atores;
- objetivos;
- planejamento;
- ações;
- eventos;
- avaliação.

CP01 possui sete questões, mas elas foram classificadas como ator, recursos, contexto, contexto, ações, consequências e consequências. Assim, quantidade não significa cobertura: **objetivo, planejamento, eventos e avaliação não aparecem como categorias próprias**, enquanto contexto e consequências aparecem repetidos.

CP02 possui dez questões, mas não identifica explicitamente a qual elemento característico cada uma pertence. Algumas podem ser interpretadas como ator, contexto, ação ou evento, porém o formalismo exigido não fica verificável e objetivos, planejamento e avaliação não estão tratados de maneira clara.

CP03 possui apenas três questões. Portanto, independentemente da qualidade textual, ele não atende ao mínimo de uma questão para cada um dos sete elementos.

A equipe deve revisar os três refinamentos, identificar os sete elementos e garantir pelo menos uma questão **realmente nova** para cada categoria.

### 2. A equipe criou uma taxonomia própria em CP01 em lugar do formalismo solicitado

CP01 afirma que a equipe adotou uma classificação baseada em “ator, objetivo, contexto, recursos, ações, rupturas e consequências” e reconhece que ela “ainda não é a taxonomia oficial da disciplina”.

O reconhecimento é correto, mas não resolve o problema.

Para esta entrega, o refinamento deve trabalhar com os elementos estabelecidos para o método: **contexto, atores, objetivos, planejamento, ações, eventos e avaliação**.

“Recursos”, “rupturas” e “consequências” podem ser informações úteis dentro do cenário, mas não substituem planejamento, eventos e avaliação.

Sugiro que a equipe não descarte o conteúdo já produzido. Basta reorganizar as questões e acrescentar as perguntas que faltam segundo o formalismo solicitado.

### 3. As questões só são válidas quando a resposta não está no cenário inicial

Esse critério precisa ser aplicado com mais rigor.

Em CP01, por exemplo, Q4 pergunta em que condições de turno e sala o exame acontece, mas o cenário inicial já informa que se trata de plantão noturno. Há informação nova a investigar sobre sala, escala, iluminação e ruído, mas a pergunta deveria ser formulada apenas sobre aquilo que de fato está ausente.

Em CP03, Q1 pergunta quais condições do pátio afetam a leitura do laudo, embora o cenário inicial já diga que há iluminação artificial precária e ruído intenso. Novamente, a pergunta repete parcialmente o que a própria narrativa já afirmou.

Q3 pergunta pelo “impacto temporal exato” de um falso positivo, mas o cenário inicial já afirma que a equipe gasta mais de três horas. Se a duração era desconhecida, ela não deveria ter aparecido como fato no cenário inicial; se já era conhecida, não pode ser a informação nova buscada pela questão.

A equipe precisa fazer um teste simples para cada pergunta: **se eu apagar a questão, a resposta já está no cenário inicial?** Se estiver, a questão não está refinando aquele elemento.

### 4. CP01 não marca claramente na narrativa refinada qual questão está sendo respondida

CP01 usa blocos `NOVO` e associa várias afirmações a IDs de hipóteses, o que é positivo para rastreabilidade.

Porém, o método desta entrega pede outra coisa adicional: cada trecho incorporado ao cenário refinado deve indicar o **número da questão de refinamento que está respondendo**.

Em CP01, aparecem H01, H39, H13, H16 etc., mas não há marcação sistemática do tipo `[Q1]`, `[Q2]`, `[Q3]` junto às respostas.

Hipótese e questão não são a mesma coisa:

- `H01` permite rastrear uma afirmação do projeto;
- `Q1` permite verificar se o processo de refinamento do cenário foi executado.

A equipe deve manter ambos quando forem úteis.

### 5. CP02 é o refinamento mais próximo do método, mas a marcação ainda precisa ser padronizada

CP02 faz melhor essa ligação. O cenário refinado inclui referências como `(Q3)`, `(Q1, Q2)`, `(Q9)` etc.

Isso facilita bastante verificar a incorporação das respostas.

Mesmo assim, sugiro padronizar exatamente o procedimento solicitado, utilizando os números das questões entre colchetes, por exemplo `[Q3]`, e garantindo que **todas** as questões apareçam em algum trecho do refinamento.

Mais importante: CP02 ainda deve mapear explicitamente as questões aos sete elementos característicos. Ter dez perguntas não garante, sozinho, que todos os elementos foram refinados.

### 6. CP03 não atende ao número mínimo de questões de refinamento

CP03 possui somente Q1, Q2 e Q3.

Isso é insuficiente porque o refinamento deveria conter no mínimo sete perguntas, uma para cada elemento característico.

Além da quantidade, as três perguntas concentram-se principalmente em:

- ambiente de pátio;
- forma de começar a descarga;
- impacto temporal/econômico.

Não há pergunta específica e claramente identificável para:

- atores;
- objetivos;
- planejamento;
- eventos;
- avaliação.

Este cenário precisa ter a seção de questões refeita antes de ser considerado completo.

### 7. CP03 responde perguntas sem apresentar a investigação que produziria as respostas

Este é o problema conceitual mais grave do terceiro cenário.

Na tabela, a equipe afirma que as respostas serão obtidas por:

- entrevista contextual ou observação;
- POP e histórico de incidentes;
- dados de TMA e registros de vistoria.

Porém, no cenário refinado surgem imediatamente respostas muito específicas:

- chuva fina e vento forte;
- terminal móvel industrial de baixa resolução;
- procedimento “padrão empírico” de esvaziar pela porta;
- aproximadamente 12 toneladas manipuladas;
- mais de 180 minutos;
- conclusão de que bastaria acessar o painel técnico externo.

Nenhuma evidência correspondente é apresentada.

Se a equipe ainda **pretende** entrevistar ou consultar POPs, então essas respostas ainda não existem e devem permanecer como `[?]` ou `[H]`. O cenário refinado não pode inventar a resposta que a questão foi criada justamente para descobrir.

Refinar não significa preencher a lacuna com a hipótese mais plausível. Significa incorporar informação obtida ou, quando ela ainda não foi obtida, deixar a lacuna explicitamente aberta.

### 8. CP03 volta a antecipar a solução dentro do cenário de problema

O cenário inicial já afirma que o problema é a falta de:

- Região de Interesse;
- documento visual ilustrativo;
- gabarito de coordenadas;
- mapa residual;
- tipo de anomalia.

No refinamento isso cresce para mapa residual visual, ROI, profundidade, quadrantes e probabilidade de risco.

Essa formulação começa pelo componente que a equipe gostaria de fornecer e define o problema como **“a ausência da nossa solução”**.

O problema humano pode ser legítimo: a equipe de campo talvez tenha dificuldade para localizar precisamente o ponto que motivou uma vistoria. Mas isso precisa ser investigado sem assumir que a resposta obrigatória será um mapa residual, uma ROI ou um laudo visual produzido pelo futuro sistema.

O cenário deve contar a história do problema atual. A solução vem depois.

### 9. CP03 contradiz a própria rastreabilidade sobre P03

A matriz registra uma mudança importante em 06/10/2026: P03 passou a ser **proto-persona a validar, possível stakeholder**, e a interface móvel foi retirada do recorte até que H42 seja investigada.

Entretanto, CP03 o apresenta novamente como usuário direto e afirma que ele:

- recebe ordem no terminal móvel;
- consulta informação digital em campo;
- registra a liberação no terminal;
- necessitaria de dados visuais produzidos pela solução.

Isso recoloca no projeto exatamente a hipótese que havia sido corretamente reaberta.

Antes de manter CP03 como um dos três cenários centrais, a equipe precisa decidir:

1. existe evidência nova que confirmou P03 como usuário direto? Nesse caso, atualizem H42 e a rastreabilidade;
2. não existe evidência nova? Então o cenário precisa permanecer explicitamente exploratório e não pode justificar uma interface móvel ou um fluxo próprio.

### 10. A nomenclatura do terceiro cenário quebra a convenção adotada pela própria equipe

O documento estabelece corretamente que cenários de problema usam prefixo `CP`, porque `C` já foi reservado para concorrentes da Entrega 02.

Os dois primeiros são CP01 e CP02.

O terceiro aparece como **C03**, apesar de ser um cenário de problema.

Isso cria colisão semântica justamente com a convenção que a equipe criou para evitar colisões.

Deve ser corrigido para **CP03** em todos os pontos relacionados, incluindo rastreabilidade e referências futuras.

### 11. CP01 é um bom cenário exploratório, mas ainda contém uma situação inicial muito específica sem evidência

CP01 é o cenário conceitualmente mais cuidadoso da entrega porque declara explicitamente que plantão, horário, volume e cansaço são hipóteses.

Mesmo assim, o cenário inicial afirma:

- três horas da manhã;
- centenas de imagens;
- poucos segundos por decisão;
- carga de paletes de madeira;
- padrão específico de dúvida.

Esses elementos podem ser perfeitamente válidos em um cenário exploratório, desde que a equipe mantenha claro que são construções hipotéticas.

O refinamento melhora bastante isso ao marcar várias dessas premissas como desconhecidas. Esse cuidado deve ser mantido nas próximas entregas: **o cenário ajuda a formular a investigação; ele não prova que o trabalho acontece daquela forma**.

### 12. CP02 utiliza boas fontes, mas deve continuar distinguindo situação histórica de funcionamento atual

CP02 utiliza matérias de 2013 e 2015 para descrever a Central de Operações e Vigilância de Santos. A própria equipe registra corretamente que essas fontes demonstram apenas o que era descrito naquele período.

Esse cuidado precisa permanecer em qualquer tarefa ou requisito derivado do cenário.

Não se deve transformar:

> “em 2013 havia servidores da Receita analisando imagens na COV”

em:

> “o fluxo atual de Santos funciona assim”.

A Entrega 04 pode usar esse material para criar uma situação plausível e formular perguntas. A confirmação do processo atual continua sendo investigação futura.

### 13. A rastreabilidade melhorou bastante, mas CP03 ainda não está incorporado de forma coerente

A matriz registra CP01 em R01 e CP01/CP02 em R03. Também registra mudanças importantes de escopo e preserva várias hipóteses abertas.

Isso representa uma melhora significativa em relação à situação observada na Entrega 03.

Entretanto, o terceiro cenário não aparece integrado à cadeia principal da mesma forma. Isso é coerente, por um lado, com o fato de P03 estar fora do recorte principal; por outro, revela que CP03 não deveria ser apresentado no documento como se tivesse a mesma maturidade dos demais.

A equipe precisa decidir se CP03:

- permanece cenário exploratório de um stakeholder ainda não confirmado;
- entra no escopo após nova evidência;
- ou é substituído por um cenário ligado a uma persona primária e a uma necessidade já rastreada.

Não force uma terceira frente de interface apenas para que cada aluno possua “um pedaço do sistema”. A divisão de trabalho da equipe não deve determinar artificialmente o escopo de IHC.

## Recomendações de melhoria

### 1. Usar os sete elementos como checklist real do refinamento

Antes de escrever a versão refinada, cada integrante deveria conseguir responder:

- Qual pergunta nova fiz sobre o **ambiente/contexto**?
- Qual sobre os **atores**?
- Qual sobre os **objetivos**?
- Qual sobre o **planejamento**?
- Qual sobre as **ações**?
- Qual sobre os **eventos**?
- Qual sobre a **avaliação**?

Se uma categoria não possui pergunta, o refinamento ainda está incompleto.

### 2. Distinguir pergunta de investigação e resposta disponível

Nem toda pergunta precisa ser respondida agora.

Se a resposta depender de entrevista futura, o cenário refinado pode registrar:

- que a informação continua desconhecida;
- por que ela importa;
- como será investigada.

Isso é metodologicamente melhor do que produzir uma resposta plausível sem evidência.

### 3. Preservar o bom tratamento `[F]`, `[H]` e `[?]` de CP01 e estendê-lo a CP03

CP01 mostra um padrão que deveria ser aplicado de maneira uniforme.

Quando o refinamento acrescenta informação:

- `[F]` se existe evidência;
- `[H]` se ainda é hipótese;
- `[?]` se continua desconhecida.

CP03 atualmente apresenta muitas hipóteses como descrição factual.

### 4. Fazer o planejamento aparecer como atividade mental

“Planejamento” não é simplesmente uma sequência de ações.

A pergunta deve explorar como o ator decide **o que fazer antes de agir**: que pistas considera, como escolhe uma estratégia, como prioriza alternativas ou como decide pedir ajuda.

Esse elemento é particularmente importante nos três cenários porque todos envolvem decisão sob incerteza.

### 5. Fazer a avaliação aparecer como interpretação posterior do estado

“Avaliação” deve capturar como o ator interpreta o resultado de suas ações e decide se alcançou o objetivo.

Em CP01, por exemplo, a incerteza após deixar a carga seguir é uma excelente oportunidade para investigar avaliação. Em CP02, pode envolver como o auditor julga se possui base suficiente para decidir. Em CP03, se mantido, envolveria como o agente conclui que a verificação foi suficiente.

A equipe já possui material narrativo para isso; falta transformá-lo corretamente em questão de refinamento.

## Pontos que devem alimentar as próximas entregas

- H01 e H39 continuam centrais: quem examina, quem aponta, quem bloqueia e quem decide formalmente.
- H04/H41 continuam abertas: existência e ordenação de uma fila de imagens ainda não foram demonstradas.
- H11 deve orientar a investigação sobre quais informações da carga são consultadas durante a análise.
- H12 deve ser investigada em termos do que a pessoa realmente faz quando permanece em dúvida.
- H38 e ?08 são importantes para entender retorno sobre decisões e aprendizado após o caso.
- H42 deve ser resolvida antes de qualquer interface específica para P03.
- CP01 pode alimentar tarefas de análise da imagem e comunicação da suspeita, mas as partes hipotéticas não devem virar tarefas “reais” apenas porque foram narradas.
- CP02 pode alimentar tarefas de busca de evidência, interpretação e formalização da decisão, mantendo separadas as evidências documentais das práticas ainda desconhecidas.
- CP03 só deve alimentar modelagem de tarefas após corrigir o refinamento e esclarecer se P03 é realmente usuário direto.
- Os cenários devem servir como origem das tarefas da Entrega 05, não como justificativa posterior para telas ou funcionalidades já escolhidas.

## Síntese das ações recomendadas

1. **Manter os três cenários iniciais, mas revisar formalmente os três refinamentos.**
2. **Criar pelo menos uma questão nova para cada um dos sete elementos característicos em cada cenário.**
3. **Eliminar perguntas cuja resposta já esteja no cenário inicial ou restringi-las apenas à informação realmente ausente.**
4. **Marcar no cenário refinado cada resposta com `[Q1]`, `[Q2]` etc.**
5. **Preservar Hxx/?xx para rastreabilidade, sem usá-los como substitutos dos números das questões.**
6. **Refazer completamente a seção de questões de CP03, que possui apenas três perguntas.**
7. **Retirar de CP03 respostas inventadas para entrevistas, POPs e dados que ainda não foram coletados.**
8. **Reformular CP03 para narrar o problema atual sem definir a falta de ROI/mapa residual como o próprio problema.**
9. **Resolver a incoerência de P03 com a rastreabilidade antes de tratá-lo como usuário direto.**
10. **Corrigir `C03` para `CP03`.**
11. **Manter CP01 e CP02 como cenários exploratórios quando a evidência ainda for parcial ou histórica.**
12. **Só levar para a Entrega 05 tarefas que estejam suficientemente ligadas ao trabalho humano descrito e às hipóteses corretamente identificadas.**

## Parecer geral sobre a Entrega 04

A equipe evoluiu conceitualmente em relação às entregas anteriores, sobretudo em CP01 e CP02. Há mais cuidado com fontes, mais transparência sobre aquilo que permanece desconhecido e uma tentativa correta de narrar o trabalho atual antes de projetar a solução.

Entretanto, a Entrega 04 ainda não pode ser considerada metodologicamente completa porque o **refinamento não segue integralmente o formalismo exigido**. A existência de sete ou dez perguntas não basta se elas não cobrem os sete elementos característicos, e CP03 está claramente abaixo do mínimo, com apenas três questões.

O terceiro cenário também merece uma revisão substancial: ele reintroduz uma proto-persona ainda não validada como usuário direto, antecipa uma interface móvel que havia sido retirada do recorte e preenche com detalhes inventados justamente as lacunas que deveriam ser investigadas.

A direção para revisão é bastante objetiva: **menos “completar a história” e mais “usar a história para descobrir o que ainda não sabemos”**. Esse é o valor do cenário de análise/problema.

> **Conferência de situação (15/11/2026)** ([`907ef6d`](https://github.com/KawanMark/template-ihc2026/commit/907ef6d)): as correções de conteúdo registradas em 25/10/2026 permanecem no documento. O status foi alinhado para 🟦 revisada após feedback, sem refazer os artefatos já corrigidos.
>
> \- Kawan

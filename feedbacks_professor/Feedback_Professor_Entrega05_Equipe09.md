# Feedback do Professor > Entrega 05 > Equipe 09

> **Status das correções (atualizado em 25/10/2026 por Kawan)**
>
> | # | Correção | Responsável | Status | Onde foi tratado |
> |---|---|---|---|---|
> | 1 | Sublinhar graficamente as operações finais nos três diagramas HTA | Equipe | Aplicado | `assets/05_tarefas/hta_t01.svg`, `hta_t04.svg` e `HTA_ALE.svg` |
> | 2 | Incluir `Input`, `Feedback` e `Plano` na linha da tarefa 0 das três tabelas auxiliares de HTA | Equipe | Aplicado | `docs/05_analise_tarefas.md` (tabelas de T01, T04 e T07) |
> | 3 | Corrigir o Plano 3 de T07 de seleção (`3.1 / 3.2`) para sequência complementar (`3.1 > 3.2`) | Alexandre | Aplicado | `assets/05_tarefas/HTA_ALE.svg` e `docs/05_analise_tarefas.md` (T07) |
> | 4 | Remover o diagrama de T02 (`goms_t02.svg`) e manter o GOMS apenas como estrutura textual indentada | Kawan | Aplicado | `docs/05_analise_tarefas.md` (T02) e remoção de `assets/05_tarefas/goms_t02.svg` |
> | 5 | Retirar `SR2` como Selection Rule em T02 e incorporar os critérios de decisão no método `M4` | Kawan | Aplicado | `docs/05_analise_tarefas.md` (T02, método M4 e verificação) |
> | 6 | Encerrar cada método de T02 com um operador explícito de verificação (`O13`) | Kawan | Aplicado | `docs/05_analise_tarefas.md` (T02, métodos M1 a M4 e tabela de operadores) |
> | 7 | Incorporar os passos de `G1` nos métodos de T05 e explicitar verificação ao final de `M2` | Gabriel | Aplicado | `docs/05_analise_tarefas.md` (T05, métodos M1 a M3) |
> | 8 | Retirar o método da aplicação móvel futura de T08 e modelar apenas a situação atual | Alexandre | Aplicado | `docs/05_analise_tarefas.md` (T08) |
> | 9 | Definir métodos alternativos reais da situação atual e regra de seleção em T08 | Alexandre | Aplicado | `docs/05_analise_tarefas.md` (T08, M1, M2 e SR1) |
> | 10 | Encerrar cada método de T08 com operador explícito de verificação (`O8`) | Alexandre | Aplicado | `docs/05_analise_tarefas.md` (T08, M1, M2 e tabela de operadores) |
> | 11 | Explicitar em T03 a tarefa humana de gatilho anterior à avaliação de convicção | Kawan | Aplicado | `assets/05_tarefas/ctt_t03.svg` e `docs/05_analise_tarefas.md` (T03) |
> | 12 | Inserir em T06 a tarefa do usuário que dispara a necessidade de localizar a declaração no Siscomex | Gabriel | Aplicado | `assets/05_tarefas/ctt_t06.svg` e `docs/05_analise_tarefas.md` (T06) |
> | 13 | Preservar o gatilho externo e as categorias de tarefa em T09 na situação atual | Alexandre | Aplicado | `assets/05_tarefas/CTT_ALE.svg` e `docs/05_analise_tarefas.md` (T09) |
> | 14 | Remover a aplicação móvel futura de T09 e modelar a conferência física atual | Alexandre | Aplicado | `assets/05_tarefas/CTT_ALE.svg` e `docs/05_analise_tarefas.md` (T09) |
> | 15 | Alinhar T07–T09 com `RASTREABILIDADE.md` sobre P03 e H42 aberta | Equipe | Aplicado | `docs/05_analise_tarefas.md` (seleção, T07–T09 e síntese) e `RASTREABILIDADE.md` |
> | 16 | Descrever os problemas de T07–T09 pelo trabalho humano e não pela ausência do mapa residual/ROI | Alexandre | Aplicado | `docs/05_analise_tarefas.md` (T07–T09 e síntese) |
> | 17 | Marcar práticas de campo não observadas em T07–T09 como `[H]` e `[?]` em vez de `[F]` | Alexandre | Aplicado | `docs/05_analise_tarefas.md` (T07–T09) e diagramas `HTA_ALE.svg` / `CTT_ALE.svg` |
> | 18 | Formular as tarefas candidatas na síntese da equipe pelo trabalho humano, sem fixar recursos futuros | Equipe | Aplicado | `docs/05_analise_tarefas.md` (Síntese da equipe) |

A equipe cumpriu a responsabilidade quantitativa da Entrega 05: os três integrantes produziram um HTA, um GOMS e um CTT cada, totalizando nove modelagens identificadas por autor e tarefa.

Há, porém, uma diferença importante entre **entregar os nove artefatos** e **atender corretamente ao formalismo das três técnicas**. Os conjuntos de Kawan e Gabriel apresentam boa continuidade com os cenários anteriores e procuram modelar a situação atual sem transformar o algoritmo em tarefa humana. O conjunto de Alexandre é mais problemático porque volta a introduzir a solução futura - aplicativo móvel, mapa residual e integração digital - em tarefas que deveriam descrever e analisar o trabalho humano atual. Isso também contradiz a própria rastreabilidade, que mantém P03 como proto-persona a validar e afirma que não há atividade desse perfil no recorte enquanto H42 estiver aberta.

Nos HTAs, os três diagramas são estruturas hierárquicas de decomposição e não fluxogramas, o que está correto. Também não identifiquei nós decompostos em apenas um filho: quando há decomposição, aparecem dois ou mais subobjetivos. Entretanto, os três HTAs falham em dois requisitos formais importantes: **as operações finais não estão graficamente grifadas/sublinhadas conforme a notação ensinada**, e a tabela auxiliar não apresenta, na tarefa 0, os campos obrigatórios **Input, Feedback e Plano**. O ponto de início e a conclusão esperada aparecem no texto introdutório, mas isso não substitui a estrutura exigida na linha da tarefa 0 da tabela auxiliar.

Nos GOMS, todos possuem `G0`, o que é positivo. T05 é o modelo mais consistente com a técnica. T02 apresenta um diagrama GOMS, embora GOMS deva ser apresentado como organização textual indentada; o texto que acompanha o diagrama pode ser aproveitado, mas o diagrama deve ser removido. T02 também chama de `Selection Rule` um critério que não seleciona entre métodos. T08 mistura dois mundos diferentes - situação atual e solução futura - como se fossem métodos alternativos do mesmo modelo e não termina seus métodos com um operador explícito de verificação do resultado.

Nos CTTs, a identificação de tarefas abstratas, de usuário, interação e sistema está, em geral, bem encaminhada. T03 e T06 utilizam abstrações nos nós decompostos, e T09 também distingue abstração e tarefas elementares. Todos possuem processamento do sistema em algum momento. O ponto mais fraco está novamente em T09, porque ele formaliza diretamente uma aplicação móvel que ainda não está justificada no escopo. Em T06 também falta uma tarefa externa do usuário claramente anterior ao uso do sistema, que represente o evento ou situação que dispara a interação.

O principal trabalho de revisão, portanto, é **corrigir o formalismo dos HTAs, ajustar os GOMS à notação correta e retirar das tarefas de Alexandre aquilo que ainda pertence à solução futura ou a uma hipótese de usuário não validada**.

## Pontos positivos

- Os três integrantes cumpriram a quantidade mínima: cada um entregou um HTA, um GOMS e um CTT.
- As nove tarefas possuem identificação de autor.
- A numeração T01 a T09 é organizada e facilita a rastreabilidade.
- T01 e T04 representam decomposições hierárquicas reais e não foram desenhados como fluxogramas.
- Nos três HTAs, todo nó que possui decomposição apresenta dois ou mais filhos; não identifiquei decomposição artificial com apenas um filho.
- T01 e T04 possuem planos associados aos nós decompostos e utilizam sequência, alternativa e repetição/condição.
- T07 também apresenta planos para os nós decompostos.
- Todos os GOMS possuem `G0`.
- T05 apresenta métodos realmente alternativos para atingir o mesmo objetivo e regras de seleção relacionadas às condições de uso de cada método.
- T05 termina seus métodos com operações de interpretação/verificação do resultado, aproximando-se bem do formalismo esperado.
- Os CTTs apresentam legenda e operadores temporais.
- T03 e T06 distinguem tarefas de usuário, interação, aplicação/sistema e tarefas abstratas.
- T09 apresenta uma tarefa externa do usuário antes das interações digitais e inclui processamento pelo sistema.
- A equipe procurou relacionar as tarefas a personas, cenários e hipóteses, em vez de modelar funcionamento interno do algoritmo.
- A rastreabilidade de P01/P02 e das tarefas T01–T06 está significativamente mais organizada do que nas primeiras entregas.

## Correções prioritárias

### 1. Os três HTAs não utilizam corretamente a marcação gráfica das operações finais

No HTA apresentado em aula, quando um objetivo não possui filhos - isto é, quando chegamos a uma operação e a decomposição termina - essa caixa deve aparecer **grifada/sublinhada** para diferenciá-la visualmente dos objetivos que ainda foram decompostos.

Isso não ocorre em T01, T04 ou T07. As operações finais aparecem visualmente como caixas comuns, diferenciadas principalmente por legenda, cor ou estilo.

A equipe precisa corrigir os três diagramas para que todas as folhas da árvore sejam reconhecíveis pela notação do HTA sem depender da legenda.

Em T01, por exemplo, 1.1, 1.2, 2.1 a 2.4, 3.1, 3.2, 4.1 e 4.2 são operações finais e devem receber essa marcação.

O mesmo vale para as operações finais de T04 e T07.

### 2. A tabela auxiliar dos três HTAs está incompleta na tarefa 0

A tabela auxiliar do HTA não deve ser apenas uma repetição textual da árvore.

Para a **tarefa 0**, precisam aparecer obrigatoriamente:

- **Input**;
- **Feedback**;
- **Plano**.

Opcionalmente, podem aparecer ações, problemas e recomendações.

T01, T04 e T07 possuem o plano na linha 0, mas não possuem os campos explícitos de **Input** e **Feedback** na tabela auxiliar.

É verdade que a descrição anterior ao diagrama informa “ponto de início” e “conclusão esperada”. Isso ajuda a compreender a tarefa, mas não substitui o formalismo da tabela auxiliar.

A equipe precisa inserir esses elementos na linha da tarefa 0.

Exemplo do raciocínio - não para copiar literalmente: o `Input` de T01 é aquilo que ativa a tarefa do operador; o `Feedback` é aquilo que permite ao operador reconhecer que a tarefa terminou e qual estado foi produzido.

Nas tarefas filhas, não acrescentem `Input` e `Feedback`. Se houver algo equivalente, ele deve ser descrito como ação, problema ou recomendação de interação.

### 3. Os planos do HTA estão bons em T01 e T04, mas T07 possui uma inconsistência no Plano 3

O Plano 3 de T07 é escrito como:

`3.1 / 3.2`

Isso representa uma **seleção entre 3.1 ou 3.2**.

Entretanto, o próprio texto afirma que, se houver divergência, deve haver registro detalhado, e as subtarefas são:

- 3.1 registrar a divergência;
- 3.2 capturar evidências fotográficas.

Essas duas ações parecem complementares, e não alternativas mutuamente exclusivas. Se há divergência, é plausível que seja necessário registrar **e** capturar a evidência.

Portanto, a equipe precisa revisar o plano de 3. O operador `/` somente é correto se realmente houver uma escolha em que executar 3.1 desabilita 3.2 ou vice-versa.

Esse é exatamente o tipo de detalhe em que o plano do HTA revela se a equipe compreendeu a tarefa ou apenas desenhou uma árvore.

### 4. T02 não deve possuir diagrama GOMS

A equipe incluiu `goms_t02.svg` e uma seção intitulada “Diagrama”.

Isso não está de acordo com o formato trabalhado para GOMS nesta disciplina.

GOMS deve ser apresentado como **estrutura textual indentada**, evidenciando:

- `GOAL 0`;
- demais Goals;
- Methods quando houver caminhos alternativos para atingir um Goal;
- Operators;
- Selection Rules quando houver mais de um Method possível.

A parte textual de T02 já contém boa parte disso e pode ser mantida e melhor organizada. O diagrama deve ser removido do modelo GOMS.

Não transformem GOMS em árvore visual. A clareza da técnica está justamente na estrutura hierarquizada do texto.

### 5. Em T02, `SR2` não é uma Selection Rule no sentido de GOMS

A própria equipe escreve:

> “SR2 não escolhe entre métodos: ela organiza os critérios de decisão.”

Essa frase já identifica o problema.

Se não há dois ou mais métodos concorrentes para atingir aquele Goal, não existe regra de **seleção entre métodos**.

No G3, há apenas M4. As condições:

- compatível → não apontar;
- incompatível → apontar;
- dúvida → pedir segunda opinião ou concluir sob incerteza;

representam lógica interna do método, não uma Selection Rule entre métodos distintos.

A equipe deve retirar `SR2` da categoria de Selection Rule e incorporá-la à descrição do método ou, caso descubra caminhos realmente alternativos para atingir G3, modelar os métodos e então criar a regra de seleção correspondente.

### 6. T02 precisa encerrar os métodos com operadores explícitos de verificação

No formalismo usado em aula, quando um método contém uma sequência de operadores externos, é importante terminar com uma primitiva interna que permita ao usuário **verificar se o objetivo daquele método foi alcançado**.

Em M1, o modelo termina em “reter quais regiões seguem em dúvida”.

Em M2 e M3, termina em comparação.

Em M4, termina na conclusão.

Há operadores cognitivos, mas não fica sistematicamente explícita a verificação final de sucesso de cada método.

A equipe deve revisar cada método e perguntar:

> “Qual é a última atividade mental pela qual o usuário reconhece que este método atingiu o Goal?”

Esse operador precisa aparecer explicitamente no final da sequência.

### 7. T05 é o GOMS mais consistente, mas G1 pode ser simplificado

T05 apresenta corretamente:

- `G0`;
- três métodos alternativos;
- regras de seleção distintas;
- operadores de espera, consulta, percepção e decisão;
- verificação ao final dos caminhos.

É o GOMS mais próximo do formalismo esperado.

Entretanto, há um `G1: identificar quem fez o bloqueio` com operadores descritos separadamente, enquanto os métodos M1 e M3 reutilizam G1.

Isso é aceitável como decomposição, mas a equipe deve verificar se G1 realmente precisa ser uma submeta formal ou se poderia simplesmente fazer parte da sequência de operadores dos métodos que dependem dessa identificação.

O ponto aqui é de clareza, não um erro grave.

### 8. T08 mistura situação atual e proposta futura dentro do mesmo GOMS

Este é um problema conceitual importante.

T08 apresenta:

- M1 - “Registro Digital Integrado via Aplicativo Móvel (Proposição de Design)”;
- M2 - “Registro Manual Tradicional em Papel e Rádio (Situação Atual)”.

Depois cria uma Selection Rule dizendo para usar M1 quando o aplicativo estiver disponível e M2 quando houver contingência.

Isso pressupõe que a aplicação móvel já exista como uma maneira operacional de atingir G0.

Ela não existe. É uma proposta de design.

O GOMS da Entrega 05 deve modelar a tarefa humana no contexto que a equipe está analisando, e não colocar a solução futura como um método já disponível.

Se a intenção é modelar a situação atual, mantenham apenas métodos atuais sustentados.

Se futuramente quiserem comparar o modelo atual com um modelo da solução projetada, façam dois modelos claramente distintos e indiquem que o segundo representa o cenário futuro. Não misturem ambos em uma única Selection Rule.

### 9. T08 não encerra seus métodos com verificação do resultado

No M1, a sequência termina em “Confirmar e Enviar Termo” / transmissão.

No M2, termina em redigitação posterior.

Falta o operador interno em que o usuário verifica que:

- o termo foi efetivamente registrado;
- as evidências foram associadas ao caso correto;
- o envio foi aceito ou concluído;
- o objetivo `G0` foi alcançado.

Esse operador de verificação deve fechar os métodos.

### 10. T08 também apresenta operadores que pertencem diretamente à solução ainda não validada

O1 a O5 incluem:

- mapa residual em terminal móvel;
- campos estruturados por toque;
- câmera integrada;
- botão “Confirmar e Enviar Termo”;
- transmissão síncrona.

Tudo isso é apresentado corretamente como `[H] Proposta`, mas o problema permanece: são operações da solução futura, e não da tarefa atual.

A marca `[H]` não transforma automaticamente uma solução futura em método válido do trabalho corrente.

A equipe precisa retirar essa parte da modelagem atual ou separá-la formalmente como modelo futuro, a ser tratado em etapa posterior.

### 11. T03 possui boa estrutura CTT, mas o disparador externo pode ficar mais explícito

T03 apresenta uma tarefa de usuário - “Avaliar convicção e definir manifestação” - antes da interação com o sistema, e depois possui tarefas de aplicação como registrar liberação, emitir segregação e transmitir notificação.

Isso atende boa parte do raciocínio temporal esperado.

[Entretanto, “Avaliar convicção” é uma atividade mental. Se o requisito de “ação externa que motiva o usuário a usar o sistema” for interpretado estritamente como um evento/tarefa externa anterior, sugiro explicitar no CTT algo como o recebimento/conclusão do exame que dispara a necessidade de registrar a manifestação.]

A observação acima não compromete toda a modelagem, mas melhoraria a representação do início real da tarefa.

### 12. T06 precisa explicitar a tarefa externa que dispara o uso do Siscomex

T06 começa praticamente com a interação “Localizar a declaração pelo número”, seguida da escolha do ato e do registro.

Falta um nó anterior, de tarefa do usuário fora do sistema ou evento do contexto, que explique **por que o auditor iniciou aquela interação**.

O CTT precisa representar não apenas o que acontece depois que a pessoa já está na tela, mas também a situação que ativa o uso do sistema.

A equipe deve identificar esse disparador a partir de CP02/T04 e inseri-lo antes da primeira tarefa de interação.

### 13. Os CTTs de T03 e T06 utilizam corretamente abstrações nos nós decompostos

Este ponto deve ser preservado.

Nos dois diagramas, quando um nó é decomposto em outras tarefas, ele aparece como tarefa abstrata, usando a representação em nuvem/equivalente da legenda.

Isso está alinhado ao formalismo de CTT.

Também há tarefas de sistema claramente identificadas, atendendo à necessidade de representar o processamento que ocorre depois das ações humanas.

### 14. T09 possui tipos de tarefa e processamento do sistema, mas modela uma solução que ainda não pertence ao recorte confirmado

T09 contém:

- tarefa externa do usuário: deslocar-se e abrir o contêiner;
- tarefa abstrata: inspecionar e registrar carga;
- tarefa de interação: capturar fotos e dados no aplicativo móvel;
- tarefa do sistema: anexar fotos ao processo eletrônico;
- relações `>>`, `[]>>` e `|||`.

Formalmente, há elementos importantes do CTT.

O problema é anterior à notação: o modelo parte de uma aplicação móvel que ainda não está justificada pelo projeto.

A própria matriz de rastreabilidade informa que P03 é **proto-persona a validar, possível stakeholder** e que:

> “Nenhuma atividade [está] no recorte enquanto H42 estiver aberta.”

Mesmo assim, T07, T08 e T09 foram construídos para esse perfil.

Isso precisa ser resolvido antes de utilizar essas três tarefas como base para protótipos.

### 15. Há uma contradição explícita entre T07–T09 e `RASTREABILIDADE.md`

A rastreabilidade registra P03 como proto-persona a validar e afirma que não existe atividade desse perfil no recorte enquanto H42 permanecer aberta.

Na mesma linha, entretanto, referencia T07, T08 e T09.

Essa situação deixa o projeto em dois estados ao mesmo tempo:

- P03 não pertence ao recorte;
- P03 possui três tarefas detalhadas e uma aplicação móvel.

A equipe precisa escolher uma interpretação coerente.

Se H42 foi validada com nova evidência, registrem a evidência e mudem o estado da hipótese.

Se H42 continua aberta, T07–T09 não devem alimentar o fluxo principal do projeto e precisam ser tratados, no máximo, como exploração provisória.

### 16. T07 volta a definir o problema atual como ausência da solução desejada

Na coluna de problemas do HTA aparecem expressões como:

- “ausência de mapa residual”;
- “falta de indicação de profundidade da ROI”;
- “fotos sem vínculo automático”;
- “retrabalho de redigitação”.

Algumas podem representar problemas reais, mas a formulação ainda parte muito diretamente da solução que a equipe quer construir.

O HTA deve identificar problemas do trabalho atual. Depois, o projeto discute diferentes soluções possíveis.

Por exemplo, a dificuldade humana pode ser “localizar com precisão a região que motivou a vistoria”; “mapa residual” é uma das possíveis respostas, não o problema em si.

### 17. Parte das afirmações de T07–T09 continua sem sustentação suficiente

T07 e T08 tratam como fatos:

- anotações em bloco de papel;
- fotografias em aparelhos particulares;
- rádio portátil;
- redigitação posterior;
- procedimentos específicos no pátio.

Esses pontos já eram problemáticos em CP03 e continuam sem nova evidência apresentada.

Não transformem uma afirmação do cenário em fato apenas porque ela foi reutilizada na análise de tarefas.

Se não houve investigação adicional, mantenham como `[H]` ou `[?]`.

### 18. A síntese da equipe volta a antecipar decisões da interface futura

Na síntese aparecem propostas como:

- examinar radiografia “assistido pelo mapa residual”;
- exportar ROI residual para dossiê;
- ferramenta de campo.

Esses elementos podem ser oportunidades de projeto, mas a modelagem de tarefas desta entrega deveria primeiro consolidar o trabalho humano que precisa ser suportado.

A análise de tarefas deve alimentar a solução. A solução não deve retroativamente determinar quais tarefas parecem importantes.

## Recomendações de melhoria

### 1. Refazer os HTAs começando pela notação, não pelo conteúdo textual

O conteúdo de T01 e T04 é aproveitável. O problema principal é formal.

Para cada HTA, façam uma revisão mecânica:

- todo nó decomposto possui pelo menos dois filhos?
- todo nó decomposto possui plano?
- toda operação final está grifada?
- o plano usa corretamente `>`, `/` ou `+`?
- a tarefa 0 tem `Input`, `Feedback` e `Plano` na tabela auxiliar?
- tarefas filhas não possuem `Input` ou `Feedback`?

Essa conferência resolverá boa parte dos problemas sem reescrever o trabalho inteiro.

### 2. Não usar “verificação” apenas como texto de autoavaliação do aluno

As seções intituladas “Verificação do HTA” e “Verificação do GOMS” ajudam a equipe a revisar o trabalho, mas não substituem os elementos formais do método.

Dizer “o plano está correto” não torna o plano correto.

Dizer “as subtarefas são suficientes” não substitui a checagem da árvore.

O valor está no artefato, não na declaração de que ele foi conferido.

### 3. Manter GOMS textual e enxuto

T02 mostra que a equipe investiu bastante energia em transformar o GOMS em visualização gráfica.

Essa energia seria melhor utilizada deixando o texto indentado mais rigoroso.

Um GOMS bem escrito deve permitir enxergar rapidamente:

`GOAL → METHOD → OPERATORS → verificação`

e, quando houver alternativas:

`METHOD A / METHOD B → SELECTION RULE`.

### 4. Separar modelos da situação atual e da solução futura

Essa recomendação vale especialmente para Alexandre.

Não use:

- “método atual”;
- “método do aplicativo futuro”;

como se fossem alternativas disponíveis hoje.

Primeiro modelem o trabalho atual.

Depois, quando houver protótipo, será possível criar um modelo futuro e comparar:

- passos eliminados;
- novos operadores;
- mudança de carga cognitiva;
- novas dependências;
- novos pontos de erro.

Essa comparação será muito mais útil do que misturar os dois estados agora.

### 5. Usar a Entrega 05 para testar a coerência das personas

Se uma persona ainda não possui atividade confirmada no recorte, tentar construir HTA, GOMS e CTT para ela deveria acender um alerta.

A dificuldade de modelar P03 não é apenas um problema desta entrega; é evidência de que o papel ainda não está suficientemente sustentado.

Isso é um resultado legítimo da análise de tarefas.

## Pontos que devem alimentar as próximas entregas

- T01/T02 podem alimentar o futuro fluxo de análise da radiografia, desde que as hipóteses sobre a prática real do operador continuem identificadas.
- T03 pode alimentar o estudo da formalização da suspeita e da ausência de retorno ao operador.
- T04/T05/T06 oferecem uma base interessante para a relação entre vigilância, evidência da imagem e decisão formal do Auditor-Fiscal.
- A separação entre P01 e P02 continua sendo uma das descobertas mais importantes do projeto e deve ser preservada.
- H39 e ?08 continuam centrais para o fluxo entre quem examina e quem decide.
- O acesso de P02 à imagem, sua competência para interpretá-la e o canal de contato com a vigilância continuam lacunas importantes.
- H42 precisa ser investigada antes que T07–T09 sejam convertidos em interface, MoLIC ou protótipo.
- A solução móvel para P03 não deve entrar automaticamente nas próximas entregas.
- Os futuros modelos conceituais e de interação devem nascer das tarefas validadas, e não de recursos como mapa residual, slider, app móvel ou painel já imaginados.
- Na avaliação futura, será interessante comparar quantitativamente métodos atuais e métodos propostos somente depois que ambos estiverem formalmente separados.

## Síntese das ações recomendadas

1. **Manter o registro de que os nove artefatos foram entregues, mas revisar o formalismo antes de considerar a Entrega 05 concluída.**
2. **Grifar/sublinhar todas as operações finais nos três diagramas HTA.**
3. **Adicionar `Input`, `Feedback` e `Plano` à tarefa 0 nas três tabelas auxiliares de HTA.**
4. **Revisar o Plano 3 de T07, pois 3.1 e 3.2 parecem sequenciais/complementares e não alternativas.**
5. **Remover o diagrama de T02 e manter GOMS apenas como estrutura textual indentada.**
6. **Retirar `SR2` de T02 como Selection Rule, a menos que sejam definidos métodos realmente alternativos para G3.**
7. **Adicionar operadores finais explícitos de verificação aos métodos de T02.**
8. **Preservar T05 como referência interna do grupo para a estrutura de GOMS, fazendo apenas ajustes de clareza.**
9. **Retirar de T08 o método da aplicação móvel futura ou separá-lo em um modelo futuro independente.**
10. **Adicionar verificação final aos métodos de T08.**
11. **Explicitar em T06 uma tarefa/evento externo que dispare o uso do sistema.**
12. **Manter as abstrações e tarefas de sistema já bem representadas em T03 e T06.**
13. **Resolver H42 antes de utilizar T07–T09 como base das próximas entregas.**
14. **Reclassificar como hipótese os detalhes de trabalho de campo que continuam sem evidência.**
15. **Revisar a rastreabilidade para eliminar a contradição “P03 sem atividade no recorte” versus T07–T09.**
16. **Evitar que oportunidades de solução, como mapa residual e aplicativo móvel, sejam apresentadas como descrição do problema ou da tarefa atual.**

## Parecer geral sobre a Entrega 05

A equipe realizou um volume significativo de trabalho e cumpriu a responsabilidade de produzir nove modelagens. T01–T06 mostram uma evolução relevante na compreensão dos dois papéis mais importantes do projeto: quem analisa a imagem e quem toma/formaliza a decisão. Essa separação está tornando o projeto de IHC mais coerente.

Entretanto, a entrega precisa de revisão formal. **Os HTAs ainda não seguem completamente a notação ensinada, T02 não deveria possuir diagrama, parte dos GOMS precisa melhorar o fechamento por verificação e T06 precisa representar melhor o disparador externo do uso do sistema.**

O problema mais estrutural permanece em T07–T09. A equipe está modelando em detalhes uma pessoa que a própria rastreabilidade afirma ainda não estar confirmada no recorte e, ao mesmo tempo, introduz uma aplicação móvel futura dentro das tarefas atuais. Isso precisa ser resolvido antes de avançar.

A boa notícia é que grande parte do conteúdo de T01–T06 pode ser preservada. A revisão necessária é principalmente de **formalismo, coerência metodológica e separação entre trabalho atual e solução futura**. Em análise de tarefas, uma árvore bonita não salva um plano errado - e um aplicativo que ainda não existe não pode aparecer como se já fosse um método de trabalho disponível.

> **Conferência de situação (15/11/2026)** ([`907ef6d`](https://github.com/KawanMark/template-ihc2026/commit/907ef6d)): as correções de conteúdo registradas em 25/10/2026 permanecem no documento. O status foi alinhado para 🟦 revisada após feedback, sem refazer os artefatos já corrigidos.
>
> \- Kawan

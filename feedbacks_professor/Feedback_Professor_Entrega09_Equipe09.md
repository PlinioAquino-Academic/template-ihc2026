# Feedback do Professor > Entrega 09 > Equipe 09

## Avaliação geral

A equipe entregou os quatro grupos de artefatos esperados para esta etapa:

- três Cenários de Interação, com autoria individual;
- Design Centrado na Comunicação associado aos três cenários;
- um Mapa de Objetivos consolidado da equipe;
- um Esquema Conceitual de Signos consolidado.

Portanto, a **quantidade mínima de artefatos foi contemplada**.

A qualidade, entretanto, não é uniforme. O Esquema Conceitual de Signos é a parte mais madura da entrega: a equipe identifica origem, significado, conteúdo, restrição, valor padrão e mecanismos de prevenção/recuperação e demonstra preocupação em separar resultado do modelo, julgamento humano e decisão aduaneira.

Os principais problemas estão no **Cenário de Interação** e, principalmente, no **Mapa de Objetivos**.

Nos três Cenários de Interação, a equipe não fez de maneira suficientemente direta a evolução das narrativas CP01, CP02 e CP03. Em vez de preservar o cenário de problema e substituir trechos problemáticos por uma intervenção da solução, foram criadas “versões iniciais” bastante resumidas e depois novos cenários refinados. Com isso, perde-se a correspondência visual e textual entre o problema original e a solução projetada.

No Mapa de Objetivos, a equipe produziu um diagrama hierárquico organizado, porém **não utilizou o formalismo trabalhado na aula**. O mapa deveria distinguir objetivos finais de objetivos instrumentais, inclusive instrumentais diretos e indiretos quando pertinente, representar quem possui cada objetivo e utilizar as relações de instrumentação. O diagrama atual funciona muito mais como árvore de decomposição de funcionalidades/ações.

O Design Centrado na Comunicação está estruturalmente próximo do material teórico para CI01, mas precisa ser revisto em CI02 e CI03 porque parte das “falas” não corresponde claramente a uma conversa real de um usuário com a interface. Em ambos os casos, o usuário parece receber um documento estático ou ser destinatário externo, mas o artefato é escrito como se houvesse uma interação dinâmica com o sistema.

Por fim, há uma inconsistência objetiva na rastreabilidade: a seção específica da Entrega 09 registra CI01–CI03, O01–O09 e S01–S12, mas a cadeia principal R01/R03 ainda mantém a coluna “Cenário de interação / signos” como `PENDENTE`.

A entrega tem bastante conteúdo útil. A correção necessária é principalmente **de formalismo e coerência conceitual**, não de quantidade.

## Pontos positivos

- Foram apresentados três Cenários de Interação, um por integrante.
- Cada cenário identifica autor e cenário de problema de origem.
- A equipe preserva a distinção entre P01, P02 e P03 construída nas entregas anteriores.
- CI01 está claramente relacionado a CP01 e às tarefas T01–T03.
- CI02 mantém a separação entre parecer de apoio e decisão formal do despacho.
- CI03 respeita H42 ao manter P03 como destinatário externo, sem recriar uma interface móvel para o agente de campo.
- Os cenários evitam, em grande parte, widgets específicos como dropdowns, botões ou componentes visuais detalhados.
- Há preocupação em descrever ações do usuário e respostas do sistema.
- O Design Centrado na Comunicação usa a convenção `U` e `D` e associa signos às falas.
- Os tópicos e subtópicos de CI01 formam uma sequência comunicativa compreensível.
- A equipe consolidou os objetivos em um único artefato e eliminou duplicidades como O02, O07 e O08.
- O mapa possui fonte editável em Mermaid e SVG versionado no repositório.
- O Esquema Conceitual de Signos está em uma tabela única.
- Os signos diferenciam dados do caso, imagem, processamento, resultado do modelo, marcações humanas, conclusão, autoria e documento.
- A equipe explicita corretamente que resultado do modelo não equivale a diagnóstico de ilícito.
- A equipe também evita converter os canais aduaneiros em níveis de risco da IA.
- As categorias PP, PA, AL, RA e CE são explicadas e utilizadas.
- Há bons mecanismos de prevenção e recuperação, especialmente nos signos de comentário, justificativa e exportação.
- A síntese para a Entrega 10 procura manter continuidade de nomes e identificadores.
- A Entrega 09 mantém fora do recorte dashboard, CRUD, administração e histórico agregado quando não há objetivo que os justifique.

## Correções prioritárias

### 1. Os Cenários de Interação não foram construídos como evolução direta dos Cenários de Problema

Este é o principal problema da seção 1.

A orientação para Cenário de Interação é partir do Cenário de Análise/Problema e produzir uma versão em que a intervenção da solução resolve ou reduz os problemas observados.

O documento deveria permitir comparar claramente:

> **cenário de problema → cenário de interação**

e enxergar quais trechos foram substituídos, removidos ou acrescentados.

A equipe, entretanto, criou para cada CI uma “Versão inicial” de poucas linhas, bastante diferente do texto completo de CP01, CP02 e CP03.

Por exemplo, CP01 contém uma narrativa extensa envolvendo:

- plantão noturno;
- imagem densa;
- sobreposição;
- uso de contraste e bordas;
- dúvida;
- pressão das imagens seguintes;
- decisão de não apontar;
- ausência de retorno posterior.

CI01 não preserva essa narrativa para mostrar, dentro dela, onde a solução intervém. A “Versão inicial” já começa resumindo o problema e introduzindo a solução.

O mesmo ocorre em CI02 e CI03.

A equipe precisa voltar aos textos completos de CP01–CP03 e produzir uma **evolução textual reconhecível**, destacando as alterações da solução sobre o cenário original.

### 2. As “Questões de refinamento” repetem um formalismo da Entrega 04 que não substitui o Cenário de Interação

A Entrega 09 adiciona novamente:

- versão inicial;
- questões de refinamento;
- respostas;
- cenário refinado.

Esse mecanismo foi útil para os Cenários de Análise/Problema, mas não é o núcleo metodológico desta entrega.

Aqui a pergunta principal é:

> “Como a intervenção projetada modifica a situação problemática?”

As questões Q1–Q3 podem ser mantidas como apoio interno de projeto, mas não devem substituir a construção direta do Cenário de Interação a partir do Cenário de Problema.

Neste momento, elas tornam a seção mais longa sem resolver a principal falha: a ausência de correspondência clara entre o texto original e o texto transformado.

### 3. CI01 possui uma boa solução conceitual, mas precisa preservar melhor o problema original

O conteúdo proposto em CI01 é coerente:

- contextualizar a carga;
- mostrar resultado do modelo com seus limites;
- permitir comparação;
- registrar região;
- registrar comentário;
- separar conclusão humana do resultado automático;
- impedir emissão incompleta.

Esses elementos fazem sentido para o problema de CP01.

O que precisa ser corrigido é a forma de apresentação.

A equipe deveria mostrar, dentro da narrativa original, como a intervenção altera momentos como:

- “não sabe por onde começar”;
- “tenta lembrar o que a carga deveria ser”;
- “não consegue afirmar se aquela região faz parte da carga”;
- “deixa o caso seguir”;
- “não sabe se acertou”.

Assim ficará evidente que o Cenário de Interação resolve aspectos concretos do Cenário de Problema.

### 4. CI02 precisa deixar claro se P02 realmente interage com a Mesa ou apenas lê um documento produzido por P01

CI02 afirma que Eduardo:

- recebe o parecer;
- confere identificação, autoria e data;
- relaciona região, comentário e carga;
- solicita esclarecimento por canal institucional se houver problema.

Isso é coerente como **uso de uma informação produzida pela solução**.

Porém, não fica claro se P02:

- abre o parecer em alguma interface da Mesa;
- recebe apenas um PDF;
- consulta o documento em outro sistema;
- utiliza a Mesa diretamente;
- não utiliza a Mesa.

Essa distinção é importante porque a Entrega 09 está modelando interação.

Se P02 não utiliza diretamente a Mesa, o cenário deve explicar que a solução produz um artefato comunicativo destinado a P02 e delimitar onde termina a interação com a Mesa.

Se P02 realmente interage com alguma interface, essa interação precisa aparecer explicitamente.

### 5. CI03 é uma intervenção válida sobre CP03, mas não é propriamente um cenário de interação de P03

A equipe corrigiu corretamente o problema das entregas anteriores e não voltou a criar uma tela móvel para Marcos.

Isso é positivo.

Entretanto, CI03 é chamado de cenário de interação enquanto o próprio texto afirma que:

> P03 é destinatário externo.

Quem efetivamente usa a Mesa nesse cenário é “o responsável”, isto é, P01/P02.

Então existem duas possibilidades metodologicamente coerentes:

1. CI03 é um Cenário de Interação de P01/P02 que prepara um artefato para apoiar P03; nesse caso, os atores usuários da interface precisam ser explicitados;
2. CI03 continua centrado em P03, mas então deve ser tratado como cenário de uso do **resultado da intervenção**, e não como se Marcos tivesse uma conversa direta com a Mesa.

A equipe precisa escolher e deixar isso claro.

### 6. O Design Centrado na Comunicação de CI01 está próximo da teoria

CI01 apresenta:

- tópico;
- subtópicos;
- falas do usuário;
- falas do preposto;
- signos;
- intenção.

Essa estrutura está alinhada ao formalismo do Design Centrado na Comunicação.

As conversas “caso”, “análise”, “comparação”, “registro” e “exportação” também são coerentes com o objetivo de P01.

Esse é o melhor dos três conjuntos e pode servir como referência interna para a revisão dos demais.

### 7. CI02 e CI03 usam falas que não correspondem claramente a uma conversa real usuário–sistema

Em CI02 aparece, por exemplo:

> U: “Qual foi o motivo da suspeita?”  
> D, no parecer: “Caso, responsável, região e comentário.”

Em CI03:

> U: “O documento identifica a carga e a região observada?”  
> D, no parecer: “Imagem numerada e comentário correspondente.”

Essas frases representam bem a **informação que o documento precisa comunicar**, mas não necessariamente uma conversa que o usuário consegue travar com o preposto do sistema.

Se o usuário apenas abre e lê um PDF, ele não está literalmente perguntando ao sistema e recebendo uma nova resposta.

A Engenharia Semiótica permite pensar a interface como comunicação do designer, mas o Design Centrado na Comunicação desta atividade deve representar as conversas que a solução efetivamente suporta.

A equipe deve revisar CI02/CI03 para modelar a interação real:

- abrir/consultar o parecer;
- localizar a informação;
- interpretar signos;
- perceber limites;
- reconhecer informação insuficiente;

ou declarar explicitamente que o parecer é um artefato de comunicação estático e modelar essa situação de maneira consistente.

### 8. A seção de Design Centrado na Comunicação deveria deixar mais clara a autoria individual

A quantidade mínima exige uma solução por integrante.

A equipe possui conteúdo correspondente a CI01, CI02 e CI03, portanto o material existe.

Contudo, tudo foi colocado em uma única tabela.

Sugiro dividir em:

- DCC01 - associado a CI01 - autor Kawan;
- DCC02 - associado a CI02 - autor Gabriel;
- DCC03 - associado a CI03 - autor Alexandre.

Isso torna a responsabilidade individual verificável e facilita comparar cenário e conversa.

### 9. O Mapa de Objetivos não segue o formalismo ensinado

Este é o maior problema conceitual da Entrega 09.

O mapa atual é uma árvore:

> “Analisar e comunicar um achado na radiografia”  
> ↓  
> O01 / O06 / O09  
> ↓  
> O02 / O03 / O04 / O05 / O07 / O08

Visualmente e conceitualmente, isso se aproxima de uma **decomposição hierárquica de tarefas ou funcionalidades**.

O Mapa de Objetivos trabalhado em aula possui outra finalidade:

- representar o que o usuário deseja realizar;
- diferenciar objetivos finais;
- diferenciar objetivos instrumentais;
- distinguir, quando pertinente, instrumental direto e instrumental indireto;
- representar a relação “instrumenta”;
- associar os objetivos aos papéis dos usuários.

O SVG atual não apresenta essa classificação.

### 10. O mapa não distingue objetivo final de objetivo instrumental

No diagrama teórico, objetivos finais e instrumentais possuem representações diferentes.

Na entrega, O01–O09 aparecem praticamente com o mesmo estatuto.

É necessário decidir, por exemplo:

- quais objetivos são razão para o usuário utilizar a solução;
- quais existem apenas para permitir alcançar outro objetivo;
- quais são instrumentais durante a interação;
- quais preparam uma ação futura.

Não basta colocar um objetivo “embaixo” de outro.

A relação precisa possuir significado de instrumentação.

### 11. O mapa não representa instrumental direto e indireto

A teoria diferencia:

- objetivo instrumental direto;
- objetivo instrumental indireto.

Essa distinção pode ser particularmente útil neste projeto.

Um objetivo de P01 pode instrumentar imediatamente a conclusão de sua análise.

Já preparar um parecer para que P02 ou outro ator tome uma decisão futura pode ter caráter instrumental indireto.

A equipe não precisa forçar todos os objetivos a essas categorias, mas deve demonstrar que avaliou a relação conforme o formalismo ensinado.

### 12. O mapa precisa representar claramente os papéis

No exemplo apresentado em aula, os objetivos são associados aos papéis que podem persegui-los.

O mapa da equipe apresenta CI01, CI02 e CI03 nas caixas, mas não representa diretamente P01/P02/P03 segundo o formalismo do mapa.

Isso é especialmente importante porque:

- O02 aparece para mais de um papel;
- O07/O08 aparecem em mais de um cenário;
- O09 envolve P01/P02 e um destinatário P03.

O papel não deve ser inferido apenas pelo cenário.

### 13. Alguns objetivos descrevem como a solução funciona, e não apenas o que o usuário deseja alcançar

A teoria orienta a representar o que o usuário deseja realizar **sem considerar como fará isso**.

Alguns objetivos atuais já incorporam solução:

- “Examinar o caso **com apoio visual**”;
- “Comparar original **e mapa**”;
- “Concluir **e exportar** parecer”.

“Mapa” e “exportar” são decisões da solução.

A equipe precisa rever se o objetivo humano existe independentemente desses mecanismos.

O mapa deve capturar a intenção do usuário; a interface e os signos explicam como essa intenção será apoiada.

### 14. O objetivo raiz também precisa ser tratado segundo a teoria

“Analisar e comunicar um achado na radiografia” funciona como um bom resumo do projeto, mas não está classificado como:

- objetivo final de qual papel;
- agrupamento conceitual;
- objetivo compartilhado.

Se permanecer no mapa, sua função precisa ficar explícita.

Caso seja apenas um título/agregador, não deve parecer um objetivo da mesma natureza dos demais.

### 15. O dicionário de objetivos é útil, mas prioridade não substitui classificação

A tabela de O01–O09 informa:

- objetivo;
- persona;
- cenário;
- prioridade.

Isso é útil para rastreabilidade.

Porém, falta justamente o que é central no método:

- final;
- instrumental;
- instrumental direto;
- instrumental indireto.

Sugiro acrescentar essa classificação ao dicionário e reconstruir o diagrama com a notação correspondente.

### 16. O Esquema Conceitual de Signos é a parte mais forte da entrega

A equipe produziu uma tabela única com:

- grupo;
- signo;
- origem;
- significado;
- conteúdo;
- restrição;
- padrão;
- prevenção;
- recuperação.

Isso está bastante próximo do modelo teórico.

Também há boa preocupação em explicar as siglas PP/PA/AL/RA/CE.

O esquema é suficientemente rico para apoiar a próxima entrega.

### 17. Alguns “signos” agregam conceitos diferentes demais em uma única linha

Apesar da boa estrutura, alguns itens precisam ser decompostos.

Exemplos:

- S01 - “Identificação e carga declarada”;
- S04 - “Resultado do modelo”, contendo rótulo, indicador e limiar;
- S06 - “Modo e ajustes”, incluindo sobreposição, lado a lado, zoom e tratamentos;
- S11 - “Responsável e data”.

Quando duas informações possuem:

- origens diferentes;
- tipos de conteúdo diferentes;
- valores padrão diferentes;
- restrições diferentes;

elas deveriam ser signos separados ou aparecer como composição explícita de um signo maior.

S11 é o exemplo mais claro:

- responsável vem do usuário;
- data vem do sistema.

Colocá-los no mesmo signo dificulta definir origem, valor padrão e prevenção corretamente.

### 18. A coluna “Origem” precisa ser padronizada conceitualmente

A equipe usa valores como:

- “Dados do caso”;
- “Arquivo do caso”;
- “Sistema”;
- “Modelo ou simulação declarada”;
- “Usuário”.

Isso descreve de onde o dado parece vir, mas não segue uma taxonomia uniforme.

O próprio modelo da atividade pede distinguir informação:

- fornecida pelo usuário;
- produzida pela aplicação/sistema;
- derivada do domínio.

A equipe deve adotar uma classificação uniforme e, se necessário, usar “observações” para detalhar a fonte específica.

### 19. S04 ainda consolida indicador/limiar que permanece hipótese de design

A equipe foi cuidadosa ao escrever “quando disponíveis” e ao afirmar que o valor não representa probabilidade comprovada de contrabando.

Isso é positivo.

Entretanto, o projeto ainda não demonstrou que o usuário necessita:

- de score numérico;
- de limiar visível;
- dessa forma específica de representação.

Portanto, o esquema não deve dar a esses elementos a aparência de requisito consolidado.

Eles podem ser mantidos como signos candidatos ou explicitamente provisórios até a avaliação.

### 20. Os mecanismos de prevenção e recuperação estão, em geral, bem aplicados

Há bons exemplos:

- impedir análise de arquivo inválido;
- impedir exportação sem comentário;
- exigir conclusão;
- exigir justificativa;
- manter dados após falha de exportação;
- orientar ação externa quando o problema não pode ser resolvido na própria interface.

Isso demonstra compreensão razoável das categorias de ruptura comunicativa.

A equipe deve apenas tomar cuidado para não classificar uma operação normal como recuperação.

Por exemplo, restaurar zoom ou ocultar um mapa pode ser apenas uma ação normal de visualização, a menos que esteja realmente sendo usada para recuperar uma ruptura.

### 21. A rastreabilidade da Entrega 09 está internamente inconsistente

A seção `2.3 Modelo conceitual da Entrega 9` registra corretamente:

- CI01–CI03;
- O01–O09;
- S01–S12.

Logo depois, a tabela principal de rastreabilidade ainda apresenta:

- R01 → “Cenário de interação / signos” = `PENDENTE`;
- R03 → “Cenário de interação / signos” = `PENDENTE`.

E a frase abaixo da tabela afirma que esses campos pertencem a entregas “ainda não realizadas”.

Isso contradiz diretamente a própria seção 2.3 e o estado “concluída” da Entrega 09.

A matriz precisa ser atualizada:

- R01 deve apontar para CI01 e os signos pertinentes;
- R03 deve apontar para CI01/CI02/CI03 e seus signos pertinentes;
- a observação sobre campos pendentes deve ser atualizada.

### 22. A rastreabilidade ainda utiliza “mapa residual” em R01/R03 enquanto a Entrega 09 trabalha com “mapa de atenção”

A equipe já registrou em entregas anteriores que mapa residual e mapa de atenção não são equivalentes.

Mesmo assim, R01 e R03 continuam descrevendo a capacidade técnica como “mapa residual”, enquanto a Entrega 09 usa S05 “Mapa de atenção”.

Isso pode ser correto se o TCC realmente evoluiu tecnicamente, mas precisa estar claro qual capacidade está sendo projetada na interface atual.

Não mantenham dois termos diferentes para o mesmo componente sem explicar:

- qual pertence à versão técnica atual;
- qual pertence à hipótese anterior;
- qual será efetivamente apresentado ao usuário.

## Recomendações de melhoria

### 1. Refazer os Cenários de Interação a partir do texto completo de CP01–CP03

Não é necessário inventar novos cenários.

Copiem a estrutura narrativa dos cenários de problema e alterem apenas aquilo que muda com a intervenção.

Destaquem claramente:

- o problema removido;
- a nova ação do usuário;
- a resposta do sistema;
- o novo resultado da situação.

Assim ficará evidente a evolução.

### 2. Separar os três DCCs

Criem DCC01, DCC02 e DCC03, cada um identificado por:

- autor;
- cenário;
- usuário/papel;
- tópico;
- subtópicos;
- falas;
- signos.

Isso facilitará verificar a responsabilidade individual.

### 3. Não inventar diálogo quando existe apenas leitura de documento

Se P02 ou P03 apenas recebe um parecer, modele com precisão o que a interface realmente oferece.

Não escreva uma pergunta do usuário e uma resposta dinâmica do sistema se essa ação não existe.

### 4. Reconstruir o Mapa de Objetivos usando o formalismo da aula

Este é o item que mais precisa de revisão.

O novo mapa deve mostrar:

- papéis;
- objetivos finais;
- objetivos instrumentais;
- instrumentais diretos/indiretos quando aplicável;
- relações de instrumentação.

Evitem representar apenas uma árvore de “passos”.

### 5. Reformular objetivos que já contêm detalhes da solução

Perguntem para cada Oxx:

> “Esse objetivo ainda existiria se eu trocasse completamente a interface?”

Se a resposta for não, provavelmente o texto está descrevendo a solução, e não o objetivo humano.

### 6. Refinar a granularidade dos signos

Separem signos quando:

- têm origens distintas;
- possuem restrições distintas;
- exigem valores padrão diferentes;
- têm prevenção/recuperação diferentes.

Isso deixará o esquema mais útil para MoLIC e Figma.

## Pontos que devem alimentar as próximas entregas

- CI01 é a base mais madura para a construção do MoLIC.
- CI02 precisa definir claramente se P02 usa a Mesa ou apenas um parecer externo.
- CI03 deve continuar respeitando H42 e não criar interface para P03 sem evidência.
- O mapa de objetivos precisa ser corrigido antes de ser usado como referência de MoLIC.
- O01–O09 não devem ser propagados automaticamente para a Entrega 10 antes da revisão de final/instrumental.
- S01–S12 podem alimentar MoLIC, mas alguns precisam ser decompostos.
- O score/limiar deve permanecer hipótese até avaliação.
- A distinção resultado do modelo versus conclusão humana deve ser preservada.
- A distinção parecer versus decisão formal deve permanecer explícita.
- A rastreabilidade R01/R03 deve deixar de marcar a Entrega 09 como pendente.
- A terminologia “mapa residual” versus “mapa de atenção” precisa ser normalizada conforme a contribuição técnica atual.
- Os futuros diagramas MoLIC devem representar conversas que realmente podem ocorrer, não diálogos fictícios com documentos estáticos.

## Síntese das ações recomendadas

1. **Manter como atendida a quantidade de três Cenários de Interação, mas refazer sua construção como evolução direta de CP01–CP03.**
2. **Usar o texto completo do Cenário de Problema e destacar claramente as partes alteradas pela solução.**
3. **Tratar as questões Q1–Q3 apenas como apoio, não como substituição do método de Cenário de Interação.**
4. **Clarificar se P02 interage com a Mesa ou apenas recebe o parecer.**
5. **Clarificar os atores usuários da interface em CI03.**
6. **Separar o Design Centrado na Comunicação em três contribuições identificáveis por autor.**
7. **Revisar CI02/CI03 para não simular conversa dinâmica quando há apenas leitura de um documento.**
8. **Refazer o Mapa de Objetivos conforme a teoria de objetivos finais e instrumentais.**
9. **Representar instrumental direto/indireto quando fizer sentido e associar explicitamente os papéis.**
10. **Retirar detalhes de solução dos objetivos, como “mapa”, “apoio visual” e “exportar”, quando não forem o objetivo humano em si.**
11. **Manter o Esquema Conceitual de Signos como base, pois é a parte mais consistente da entrega.**
12. **Separar signos agregados, principalmente S01, S04, S06 e S11.**
13. **Padronizar a coluna Origem em domínio/usuário/aplicação, detalhando a fonte nas observações.**
14. **Manter indicador/limiar como elemento provisório, não requisito confirmado.**
15. **Atualizar R01/R03 em `RASTREABILIDADE.md` para registrar os Cenários de Interação e signos já produzidos.**
16. **Corrigir a frase que ainda afirma que a Entrega 09 está pendente.**
17. **Normalizar a terminologia mapa residual versus mapa de atenção antes da Entrega 10.**

## Parecer geral sobre a Entrega 09

A equipe realizou um trabalho extenso e existe uma boa base conceitual para continuar. O **Esquema Conceitual de Signos** demonstra cuidado e pode ser aproveitado quase integralmente, com ajustes de granularidade e origem.

Os dois pontos que realmente precisam ser refeitos são mais fundamentais:

- **Cenários de Interação devem ser uma evolução reconhecível dos Cenários de Problema**;
- **Mapa de Objetivos precisa seguir o formalismo de objetivos finais e instrumentais da aula, e não uma árvore de decomposição de tarefas.**

O Design Centrado na Comunicação está bem encaminhado em CI01, mas precisa ficar mais rigoroso em CI02/CI03 para representar apenas conversas que a interface realmente suporta.

A equipe está próxima de ter um modelo conceitual consistente, mas não deve confundir uma documentação muito organizada com aderência automática ao método. Nesta entrega, a diferença é importante: **árvore de objetivos não é Mapa de Objetivos, e uma narrativa nova não é necessariamente a evolução do Cenário de Problema**.

# Feedback do Professor > Entrega 06 > Equipe 09

> **Status da aplicação (15/11/2026):** revisão solicitada para as entregas da equipe, na branch `feedbacks`. Autoria acadêmica preservada; aplicação registrada por Kawan. O texto do professor está intacto, com anotações em blocos de citação. 🟦 indica revisão; pendências de configuração/verificação online e lacunas de evidência permanecem explícitas.
>
> | Item do parecer | Situação nesta rodada | Commit(s) / referência |
> |---|---|---|
> | Correção 1: PF02 declara cobrir T03–T06, mas o protótipo não cobre efetivamente todas essas tarefas | ✅ Aplicado | [`7478605`](https://github.com/KawanMark/template-ihc2026/commit/7478605d754b82ca3ab0ae9c9a31f3ea2aed622b) |
> | Correção 2: P02 aparece no escopo, mas sua interação não está claramente representada | ✅ Aplicado | [`55840c5`](https://github.com/KawanMark/template-ihc2026/commit/55840c52ab1eceab76fd5f6b445fe82e517afdf4) |
> | Correção 3: Os estados PP01–PP06 estão bem descritos no texto, mas não estão todos visualmente demonstrados em `assets/06_prototipos/` | ✅ Aplicado | [`cb04295`](https://github.com/KawanMark/template-ihc2026/commit/cb042954f1d03d37794e726c18feaf26deaf0485) |
> | Correção 4: A entrega mostra a versão anterior ao walkthrough, mas não mostra de forma suficientemente direta a versão revisada | ✅ Aplicado | [`2d7474d`](https://github.com/KawanMark/template-ihc2026/commit/2d7474d4370683a99b58355a3f5956a0c657ad3d) |
> | Correção 5: Há uma pequena inconsistência entre a versão visual posterior dos estados e as alterações descritas na seção 5 | ✅ Aplicado | [`01a4557`](https://github.com/KawanMark/template-ihc2026/commit/01a4557bb25584e0ee55a54bc75d134267d5a308) |
> | Correção 6: A associação de “veredito final” à Mesa de inspeção ainda merece revisão | ✅ Aplicado | [`c79795b`](https://github.com/KawanMark/template-ihc2026/commit/c79795b9f934ce8db55f97196826feacfe2408e4) |
> | Correção 7: O índice “94% · limiar 70% (calibrado)” continua semanticamente forte demais | ✅ Aplicado | [`5d018c1`](https://github.com/KawanMark/template-ihc2026/commit/5d018c101d9dd9a1dc7563330613d54612d0d59a) |
> | Correção 8: O walkthrough foi realizado e está documentado, mas a evidência da sessão ainda é principalmente relato da própria equipe | 🟨 Tratado com lacunas de registro | [`8653884`](https://github.com/KawanMark/template-ihc2026/commit/865388421d7754e904150df5de8d457d50df69ef) |
> | Correção 9: O participante do walkthrough é adequado para esta iteração, mas não valida o domínio profissional | ✅ Aplicado | [`8653884`](https://github.com/KawanMark/template-ihc2026/commit/865388421d7754e904150df5de8d457d50df69ef) |
> | Correção 10: A prancha possui detalhes que começam a se aproximar de média fidelidade | ✅ Aplicado | [`3703be7`](https://github.com/KawanMark/template-ihc2026/commit/3703be7b8c315ca947391d21d4e6ade3087b32d9) |
> | Correção 11: Algumas ferramentas da prancha precisam continuar rastreadas como hipóteses, não como requisitos | ✅ Aplicado | [`3703be7`](https://github.com/KawanMark/template-ihc2026/commit/3703be7b8c315ca947391d21d4e6ade3087b32d9) |
> | Correção 12: A equipe corrigiu corretamente o problema de P03 observado na Entrega 05 | ℹ️ Preservado e conferido | [`0e92077`](https://github.com/KawanMark/template-ihc2026/commit/0e92077) |
> | Correção 13: A rastreabilidade da Entrega 06 está atualizada e registra o ciclo de revisão | ✅ Aplicado | [`7478605`](https://github.com/KawanMark/template-ihc2026/commit/7478605d754b82ca3ab0ae9c9a31f3ea2aed622b) |
>
> \- Kawan


## Avaliação geral

A equipe apresentou uma solução integrada de prototipação de baixa fidelidade e **há material visual do protótipo dentro do próprio repositório**, em `assets/06_prototipos/`: a prancha `mesa_inspecao.png` e o arquivo editável `mesa_inspecao.tldr`. Portanto, o requisito essencial de existir uma representação visual do protótipo foi atendido.

O documento também está preenchido em todas as seções previstas: escopo, famílias de interface, fluxos escolhidos, telas/estados, simulação/walkthrough, alterações posteriores e checklist. O item 4 não foi deixado como intenção futura: há uma simulação descrita com uma pessoa que não participou da criação das telas, uma tarefa apresentada, seis observações e consequências de design. Isso está conceitualmente alinhado ao objetivo desta entrega de construir, simular, observar e revisar.

A entrega também corrige um problema importante das etapas anteriores: P03 continua como stakeholder sem tela própria, e a solução se concentra em P01/P02. Essa decisão está coerente com a rastreabilidade atual.

Os principais pontos de revisão estão em três aspectos. Primeiro, a documentação declara que PF02 cobre T03–T06, mas o protótipo mostrado cobre principalmente o trabalho de P01 de analisar, marcar e produzir um parecer; as tarefas T04–T06 de P02, relacionadas a compreender o bloqueio e formalizar uma decisão no processo de despacho, não aparecem efetivamente como fluxo de interação. Segundo, a pasta da Entrega 06 possui uma única prancha principal; os estados PP01–PP06 estão muito melhor documentados textualmente do que visualmente dentro desta entrega. Terceiro, a figura preservada é deliberadamente a versão anterior ao walkthrough, então ainda contém rótulos que o próprio teste identificou como inadequados, como “Liberar carga” e “Inspeção física”. A decisão de manter a versão antiga para comparação é válida, mas a entrega deveria permitir visualizar também a versão revisada, para demonstrar o ciclo completo de prototipação.

De modo geral, a Entrega 06 está **bem mais madura metodologicamente** do que as primeiras entregas do grupo. Há protótipo, há rastreabilidade, há simulação e há revisão. O que falta é tornar a correspondência entre tarefa, persona, estado visual e alteração pós-walkthrough mais precisa.

## Pontos positivos

- O protótipo visual está versionado no repositório em `assets/06_prototipos/`.
- Existe uma imagem diretamente visualizável e também um arquivo editável do tldraw.
- O arquivo `.tldr` contém páginas adicionais de arquitetura e fluxo, demonstrando que a equipe preservou o material de elaboração.
- O protótipo continua com aparência de baixa fidelidade e prioriza estrutura de interação, sem investir em acabamento visual de produto final.
- A equipe evita criar dashboard, CRUD, login e administração apenas para “completar” o sistema.
- Os dois fluxos priorizados estão associados a atividades relevantes do projeto.
- A equipe usa identificadores próprios para os estados do protótipo (`PP01` a `PP06`), evitando colisão com as personas.
- Há caminho principal e caminhos de erro/retorno descritos.
- O protótipo inclui um estado inicial, estado de análise, comparação, marcação, parecer e prevenção de erro.
- O item 4 registra uma simulação com uma pessoa externa à elaboração das telas.
- A pessoa recebeu uma tarefa concreta e foi solicitada a indicar onde clicaria, o que entendia e o que esperava acontecer.
- Foram registradas seis observações específicas, e não apenas opiniões genéricas como “gostei” ou “ficou fácil”.
- Cada observação foi transformada em uma consequência de design.
- A seção 5 demonstra iteração: as críticas do walkthrough geraram decisões de modificação.
- OBS-04 é particularmente importante porque detectou uma ruptura conceitual real: “Liberar carga” e “Inspeção física” davam à interface do operador uma autoridade que o projeto já havia separado de P01.
- OBS-03 também é um bom resultado do walkthrough: o participante interpretou a porcentagem do modelo como probabilidade de um tipo de ilícito, mostrando que a informação técnica precisa ser comunicada com mais cuidado.
- A equipe registra explicitamente que o walkthrough com colega é apenas uma avaliação formativa e não substitui participantes finais.
- A rastreabilidade registra a criação do protótipo, a simulação e as mudanças decorrentes, mantendo continuidade longitudinal.
- A decisão de deixar P03 sem tela própria está coerente com a hipótese H42 ainda aberta.

## Correções prioritárias

### 1. PF02 declara cobrir T03–T06, mas o protótipo não cobre efetivamente todas essas tarefas

Na seção 2, PF02 é descrito como:

> marcar região, descrever achado, revisar conclusão e exportar parecer - relacionado a T03–T06.

Essa associação está ampla demais.

T03 pertence a P01 e trata da comunicação/registro da conclusão do exame da imagem.

Já T04, T05 e T06 pertencem a P02 e tratam de outro momento do processo:

- decidir sobre uma carga bloqueada;
- entender por que a carga foi bloqueada;
- formalizar o ato no despacho.

A “Mesa de inspeção” apresentada na Entrega 06 modela principalmente o trabalho de P01. Ela mostra radiografia, ferramentas de análise, indicação do modelo, regiões marcadas, observações e emissão de parecer.

Ela **não representa claramente o fluxo de P02 para receber esse parecer, compreender o motivo do bloqueio, confrontar a informação com o processo e formalizar sua decisão**.

A equipe deve escolher uma das duas alternativas:

- restringir PF02 ao que realmente está prototipado, provavelmente T03 e partes preparatórias que produzem informação para P02; ou
- criar e documentar um fluxo específico de P02, caso T04–T06 realmente façam parte do recorte desta prototipação.

Não é necessário criar mais telas apenas para “cumprir quantidade”. O importante é não declarar cobertura de uma tarefa que a interface não permite executar.


> **✅ Aplicado** ([`7478605`](https://github.com/KawanMark/template-ihc2026/commit/7478605d754b82ca3ab0ae9c9a31f3ea2aed622b)): Correção 1: PF02 cobre T03 de P01; emitir o PDF não executa T04–T06 de P02. Ajusta a cobertura declarada na entrega e na matriz.
>
> \- Kawan

### 2. P02 aparece no escopo, mas sua interação não está claramente representada

A seção 1 afirma:

> P01 examina a imagem; P02 recebe o parecer para apoiar a decisão no despacho.

Isso é coerente com o projeto.

Porém, a prancha da Mesa de inspeção mostra essencialmente a interface de P01. O botão de exportar PDF produz um artefato que poderá chegar a P02, mas o que P02 faz com esse artefato não está representado.

Isso cria uma diferença importante entre:

- **persona afetada pelo resultado do protótipo**;
- **persona que efetivamente utiliza a interface prototipada**.

A equipe precisa explicitar essa diferença.

Se P02 não interage diretamente com a Mesa de inspeção nesta versão, indiquem isso claramente: o protótipo cobre P01 e produz uma saída destinada a P02.

Isso seria metodologicamente mais preciso do que afirmar que a interface cobre P01/P02 indistintamente.


> **✅ Aplicado** ([`55840c5`](https://github.com/KawanMark/template-ihc2026/commit/55840c52ab1eceab76fd5f6b445fe82e517afdf4)): Correção 2: identifica usuário direto, artefato de saída, encaminhamento externo e limite da participação de P02.
>
> \- Kawan

### 3. Os estados PP01–PP06 estão bem descritos no texto, mas não estão todos visualmente demonstrados em `assets/06_prototipos/`

A seção 3 descreve seis estados:

- PP01 - sem imagem;
- PP02 - resultado disponível;
- PP03 - comparação;
- PP04 - região marcada;
- PP05 - parecer;
- PP06a/PP06b - erro e retorno.

A descrição textual é boa e deixa claros vários controles e transições.

Entretanto, o material visual da Entrega 06 em `assets/06_prototipos/` apresenta principalmente uma única prancha da Mesa de inspeção. Na própria prancha é possível compreender a ideia geral da interface, mas não observar claramente todas as mudanças entre PP01, PP02, PP03, PP04, PP05 e PP06.

O arquivo editável mantém páginas auxiliares, o que é positivo, e o repositório atual também possui representações posteriores dos estados em outras entregas. Mesmo assim, para esta entrega, o ideal seria preservar em `assets/06_prototipos/` uma prancha ou conjunto de imagens que permita reconhecer visualmente os estados principais e os erros/retornos.

A prototipação em papel não precisa de dezenas de telas. Mas, se a documentação afirma que existem seis estados, o leitor deveria conseguir enxergar esses estados, não apenas imaginá-los a partir de uma descrição.


> **✅ Aplicado** ([`cb04295`](https://github.com/KawanMark/template-ihc2026/commit/cb042954f1d03d37794e726c18feaf26deaf0485)): Correção 3: permite visualizar PP01–PP06 diretamente na Entrega 6, sem depender dos diretórios das entregas futuras.
>
> \- Kawan

### 4. A entrega mostra a versão anterior ao walkthrough, mas não mostra de forma suficientemente direta a versão revisada

A seção 5 afirma corretamente:

> “São decisões para a próxima versão; a figura mantém o esboço original para permitir a comparação.”

Preservar o “antes” é uma boa prática.

O problema é que a atividade não termina em observar. O ciclo é:

**construir → simular → observar → revisar**.

O texto descreve muito bem o “depois”, mas a Entrega 06 mostra visualmente sobretudo o “antes”.

Isso é particularmente perceptível porque a prancha ainda apresenta:

- “Liberar carga”;
- “Inspeção física”;
- porcentagem/limiar com pouca explicação;
- comparação dependente de tecla pressionada.

Esses são justamente pontos que o walkthrough levou a equipe a mudar.

Sugiro manter a imagem original e acrescentar uma imagem da versão pós-walkthrough, ainda em baixa fidelidade. Assim a equipe demonstra visualmente que a revisão realmente foi incorporada.


> **✅ Aplicado** ([`2d7474d`](https://github.com/KawanMark/template-ihc2026/commit/2d7474d4370683a99b58355a3f5956a0c657ad3d)): Correção 4 e recomendações 1/2: preserva o antes e torna visíveis as seis alterações posteriores ao walkthrough, sem alegar novo teste.
>
> \- Kawan

### 5. Há uma pequena inconsistência entre a versão visual posterior dos estados e as alterações descritas na seção 5

O repositório atual possui uma representação posterior de PP01–PP06 em outro diretório, utilizada como referência para as entregas seguintes.

Nessa representação, o quadro PP05 ainda apresenta “Liberar carga” e “Inspeção física”, enquanto a própria Entrega 06 declara que esses rótulos deveriam ser substituídos por termos como “Sem ressalvas na imagem” e “Suspeita apontada”.

Ao mesmo tempo, o bloco de melhorias da mesma representação já descreve a terminologia corrigida.

Isso significa que o documento textual aprendeu com OBS-04, mas a atualização visual ainda não foi propagada de forma uniforme.

A equipe precisa sincronizar os artefatos para que a decisão registrada na seção 5 apareça também nas representações visuais reutilizadas depois.


> **✅ Aplicado** ([`01a4557`](https://github.com/KawanMark/template-ihc2026/commit/01a4557bb25584e0ee55a54bc75d134267d5a308)): Correção 5: a referência posterior usa os mesmos estados revisados; mantém os originais testados sem propagar os rótulos institucionais ambíguos.
>
> \- Kawan

### 6. A associação de “veredito final” à Mesa de inspeção ainda merece revisão

A própria simulação revelou que o participante interpretou o painel como uma decisão formal sobre a carga.

Mesmo depois da revisão textual, a estrutura da prancha continua chamando a área de **“Veredito final”**.

Esse termo ainda pode sugerir decisão administrativa definitiva, exatamente o problema identificado em OBS-04.

A equipe precisa verificar se “parecer”, “conclusão da análise da imagem” ou outra expressão do vocabulário profissional representa melhor o que P01 realmente produz.

O importante é que a interface comunique claramente:

> “Esta é a conclusão técnica da análise da imagem.”

e não:

> “Esta é a decisão final sobre a carga.”


> **✅ Aplicado** ([`c79795b`](https://github.com/KawanMark/template-ihc2026/commit/c79795b9f934ce8db55f97196826feacfe2408e4)): Correção 6: a conclusão de P01 é um parecer técnico e não um veredito administrativo sobre a carga.
>
> \- Kawan

### 7. O índice “94% · limiar 70% (calibrado)” continua semanticamente forte demais

O walkthrough mostrou isso de forma excelente: o participante perguntou se o número representava chance de ser droga ou arma.

Isso confirma que a informação não é autoexplicativa.

A seção 5 propõe acrescentar explicação, o que é correto. Entretanto, é necessário revisar também se o **score deve aparecer dessa forma**.

A equipe ainda precisa investigar:

- o que exatamente esse valor representa;
- se o modelo efetivamente produz uma medida interpretável dessa maneira;
- se o usuário precisa do valor numérico;
- se o limiar tem significado operacional;
- que decisão humana esse número apoia.

“94%” produz uma sensação muito forte de certeza, mesmo quando a equipe escreve que o resultado não comprova ilícito.

Mantenham isso como hipótese de design a ser investigada, não como requisito consolidado.


> **✅ Aplicado** ([`5d018c1`](https://github.com/KawanMark/template-ihc2026/commit/5d018c101d9dd9a1dc7563330613d54612d0d59a)): Correção 7: não consolida os valores ilustrativos como probabilidade ou limiar calibrado de domínio.
>
> \- Kawan

### 8. O walkthrough foi realizado e está documentado, mas a evidência da sessão ainda é principalmente relato da própria equipe

O item 4 atende ao requisito básico: existe participante externo à elaboração, tarefa, percurso, observações e consequência para o design.

Isso deve ser preservado.

Para aumentar a qualidade metodológica, seria útil registrar também dados mínimos da sessão:

- data;
- duração aproximada;
- perfil do participante;
- forma de realização;
- registro utilizado pelo observador;
- eventualmente foto do arranjo ou notas anonimizadas, se apropriado.

Não é necessário identificar nominalmente o participante.

Atualmente, as seis “evidências registradas” são paráfrases do que ocorreu. São úteis, mas dependem inteiramente do relato posterior da equipe.

Esta é uma recomendação de melhoria, não uma exigência de repetir o walkthrough.


> **🟨 Tratado com lacunas de registro** ([`8653884`](https://github.com/KawanMark/template-ihc2026/commit/865388421d7754e904150df5de8d457d50df69ef)): A proveniência disponível está explícita na Entrega 6. Data/duração/notas primárias da sessão não foram recuperadas; continuam [?], sem inventar evidência ou repetir o walkthrough.
>
> \- Kawan

### 9. O participante do walkthrough é adequado para esta iteração, mas não valida o domínio profissional

A equipe registra corretamente que foi utilizado um colega de curso que não elaborou as telas.

Isso atende à finalidade formativa da Entrega 06.

Porém, o colega pode avaliar:

- compreensão de rótulos;
- visibilidade de campos;
- sequência;
- expectativa sobre controles;
- ambiguidade comunicativa.

Ele não pode validar, por si só:

- se operadores reais usam esse vocabulário;
- se a porcentagem faz sentido no trabalho;
- se os dados da carga precisam aparecer dessa forma;
- se o parecer é realmente encaminhado assim;
- se as ferramentas de tratamento correspondem à prática profissional.

A equipe demonstrou consciência dessa limitação no final da seção 4. É importante manter essa distinção nas próximas entregas.


> **✅ Aplicado** ([`8653884`](https://github.com/KawanMark/template-ihc2026/commit/865388421d7754e904150df5de8d457d50df69ef)): Correção 8: preserva o relato e identifica dados ausentes, sem inventar data, duração, notas ou nova sessão. Mantém o limite de validação do colega (item 9).
>
> \- Kawan

### 10. A prancha possui detalhes que começam a se aproximar de média fidelidade

A representação continua com estética de esboço, mas possui muitos detalhes:

- várias ferramentas de tratamento de imagem;
- controles específicos;
- score;
- limiar;
- alternância de camadas;
- marcação ROI;
- comentários;
- campos de parecer;
- exportação PDF.

Isso não é um problema automaticamente.

Porém, em baixa fidelidade, a equipe deve evitar investir energia demais em controles que ainda não tiveram sua necessidade investigada.

O valor da prancha está em testar:

- como o operador examina;
- como compara;
- como registra;
- como comunica.

Não é necessário decidir agora exatamente todos os sliders, filtros e tratamentos que existirão no produto final.


> **✅ Aplicado** ([`3703be7`](https://github.com/KawanMark/template-ihc2026/commit/3703be7b8c315ca947391d21d4e6ade3087b32d9)): Correções 10/11: preserva baixa fidelidade e registra H43 para investigar necessidade e simplificação dos filtros.
>
> \- Kawan

### 11. Algumas ferramentas da prancha precisam continuar rastreadas como hipóteses, não como requisitos

Na lateral esquerda aparecem recursos como:

- exposição;
- penetração;
- negativo;
- super realce;
- brilho/contraste;
- nitidez;
- bordas;
- densidade/cor;
- isolamento de faixa.

Parte desses recursos se inspira nas interfaces concorrentes estudadas, o que é uma boa origem para exploração.

Mas a existência em concorrentes não significa automaticamente que todos devam aparecer na solução.

Nas próximas iterações, a equipe deve investigar quais controles:

- realmente fazem parte do trabalho de P01;
- são necessários para a tarefa;
- podem ser simplificados;
- devem ser agrupados;
- podem ser removidos.


> **✅ Aplicado** ([`3703be7`](https://github.com/KawanMark/template-ihc2026/commit/3703be7b8c315ca947391d21d4e6ade3087b32d9)): Correções 10/11: preserva baixa fidelidade e registra H43 para investigar necessidade e simplificação dos filtros.
>
> \- Kawan

### 12. A equipe corrigiu corretamente o problema de P03 observado na Entrega 05

Este é um ponto importante de continuidade e deve ser preservado.

A Entrega 06 declara explicitamente:

> “P03 permanece stakeholder, sem tela própria.”

Isso está coerente com H42 e com a revisão da Entrega 05.

T07–T09 não foram usados para justificar um aplicativo móvel no protótipo. Em vez disso, a equipe concentrou a interface nas informações que P01 produz e que poderão apoiar os atores posteriores.

Essa decisão torna o escopo mais defensável.


> **ℹ️ Preservado e conferido** ([`0e92077`](https://github.com/KawanMark/template-ihc2026/commit/0e92077)): P03 permanece stakeholder, sem tela móvel e com H42 aberta.
>
> \- Kawan

### 13. A rastreabilidade da Entrega 06 está atualizada e registra o ciclo de revisão

A matriz registra a criação da Mesa de inspeção, os fluxos PF01/PF02, os estados PP01–PP06, o walkthrough e as principais decisões posteriores.

Isso é positivo porque mostra que a interface não surgiu isoladamente.

A equipe também criou prefixos específicos `PF` e `PP`, mantendo a convenção de identificadores organizada.

O cuidado agora é não usar a rastreabilidade para declarar uma cobertura maior do que a interface realmente possui - especialmente em relação a T04–T06.


> **✅ Aplicado** ([`7478605`](https://github.com/KawanMark/template-ihc2026/commit/7478605d754b82ca3ab0ae9c9a31f3ea2aed622b)): Correção 1: PF02 cobre T03 de P01; emitir o PDF não executa T04–T06 de P02. Ajusta a cobertura declarada na entrega e na matriz.
>
> \- Kawan

## Recomendações de melhoria

### 1. Acrescentar uma prancha “depois”

Mantenham `mesa_inspecao.png` como registro da versão testada e acrescentem uma segunda imagem mostrando as alterações decorrentes de OBS-01 a OBS-06.

Isso tornaria o ciclo iterativo imediatamente verificável.


> **ℹ️ Situação da recomendação** ([`2d7474d`](https://github.com/KawanMark/template-ihc2026/commit/2d7474d4370683a99b58355a3f5956a0c657ad3d)): Encaminhada nas correções 4, com o alcance e as pendências explicitados acima.
>
> \- Kawan

### 2. Mostrar visualmente pelo menos os estados essenciais

Não é necessário desenhar uma tela completamente diferente para cada PP.

Uma única prancha pode mostrar miniaturas ou recortes de:

- PP01;
- PP02/PP03;
- PP04;
- PP05;
- PP06.

O importante é tornar visível o que muda de um estado para outro.


> **ℹ️ Situação da recomendação** ([`cb04295`](https://github.com/KawanMark/template-ihc2026/commit/cb042954f1d03d37794e726c18feaf26deaf0485)): Encaminhada nas correções 3, com o alcance e as pendências explicitados acima.
>
> \- Kawan

### 3. Explicitar a fronteira entre P01 e P02

A documentação deveria dizer claramente:

- o que P01 faz na Mesa de inspeção;
- qual artefato/informação sai dessa atividade;
- como essa informação chega a P02;
- se a interação de P02 está ou não dentro do escopo desta versão.

Isso evitará que o protótipo misture parecer técnico e ato formal.


> **ℹ️ Situação da recomendação** ([`7478605`](https://github.com/KawanMark/template-ihc2026/commit/7478605d754b82ca3ab0ae9c9a31f3ea2aed622b), [`55840c5`](https://github.com/KawanMark/template-ihc2026/commit/55840c52ab1eceab76fd5f6b445fe82e517afdf4)): Encaminhada nas correções 1, 2, com o alcance e as pendências explicitados acima.
>
> \- Kawan

### 4. Usar a própria OBS-03 como hipótese para a Entrega 07

A dúvida sobre “94%” é excelente matéria de investigação.

Em vez de apenas melhorar a legenda, a equipe deve investigar se usuários do domínio:

- desejam um número;
- entendem confiança/score;
- preferem indicação qualitativa;
- precisam conhecer limiar;
- relacionam o score a risco de ilícito.

A melhor solução pode não ser “explicar melhor o 94%”; pode ser apresentar a informação de outra forma.


> **ℹ️ Situação da recomendação** ([`5d018c1`](https://github.com/KawanMark/template-ihc2026/commit/5d018c101d9dd9a1dc7563330613d54612d0d59a)): Encaminhada nas correções 7, com o alcance e as pendências explicitados acima.
>
> \- Kawan

### 5. Preservar a baixa fidelidade

Continuem priorizando fluxo, significado e decisão.

Ainda não é hora de transformar a Mesa de inspeção em uma réplica visual detalhada de um produto final.


> **ℹ️ Situação da recomendação** ([`3703be7`](https://github.com/KawanMark/template-ihc2026/commit/3703be7b8c315ca947391d21d4e6ade3087b32d9)): Encaminhada nas correções 10, 11, com o alcance e as pendências explicitados acima.
>
> \- Kawan

## Pontos que devem alimentar as próximas entregas

- A distinção entre parecer técnico de P01 e decisão formal de P02 deve permanecer central.
- OBS-03 deve alimentar a investigação sobre explicabilidade do resultado do modelo.
- OBS-04 deve alimentar terminologia e separação de responsabilidades.
- OBS-01 reforça H11: quais dados da carga precisam acompanhar a imagem.
- OBS-02 deve gerar alternativas reais de comparação, não apenas uma correção automática para “lado a lado”.
- OBS-05 indica necessidade de vínculo claro entre região marcada e comentário.
- OBS-06 deve alimentar prevenção de erro e recuperação.
- A Entrega 07 deve investigar as hipóteses que o walkthrough com colega não consegue validar no domínio profissional.
- A Entrega 08 deverá transformar algumas dessas preocupações em metas verificáveis de usabilidade, sem confundir desempenho do modelo com qualidade da interação.
- As Entregas 09–11 devem preservar a diferença entre conclusão da análise de imagem, comunicação de suspeita e decisão aduaneira.
- P03 deve continuar fora da camada interativa até que H42 receba evidência suficiente.


> **ℹ️ Encaminhamento:** os limites de P01/P02/P03, hipóteses abertas e vínculo com a avaliação foram preservados nos documentos e na matriz. Esta rodada não produz MoLIC, Figma ou avaliações das Entregas 10–14. Na Entrega 7, as pendências online estão no checklist e no README dos instrumentos.
>
> \- Kawan

## Síntese das ações recomendadas

1. **Manter como atendido o requisito de existência de protótipo visual no repositório.**
2. **Manter como atendido o preenchimento das seções do modelo.**
3. **Manter como atendida a realização/documentação básica do walkthrough.**
4. **Corrigir a associação de PF02 com T03–T06, declarando apenas as tarefas realmente cobertas.**
5. **Explicitar se P02 usa a interface ou apenas recebe a saída produzida por P01.**
6. **Adicionar representação visual dos principais estados PP01–PP06 dentro da documentação da Entrega 06.**
7. **Preservar a versão “antes”, mas acrescentar uma versão visual “depois” do walkthrough.**
8. **Propagar visualmente as mudanças de OBS-04, substituindo rótulos que ainda sugerem decisão formal da carga.**
9. **Revisar o termo “Veredito final”.**
10. **Manter score e limiar como hipótese de design e investigar sua interpretação.**
11. **Registrar melhor os metadados da sessão de walkthrough em futuras avaliações formativas.**
12. **Preservar a decisão de não criar interface própria para P03 enquanto H42 estiver aberta.**
13. **Revisar quais controles de tratamento de imagem realmente precisam permanecer nas próximas versões.**

## Parecer geral sobre a Entrega 06

A Entrega 06 atende aos três pilares mais importantes desta atividade: **há protótipo visual, o modelo foi preenchido e existe um walkthrough com alterações derivadas da observação**.

O grupo também demonstra uma evolução importante no processo de IHC: em vez de apenas produzir uma tela “bonita”, documentou problemas de compreensão e mudou decisões a partir deles. OBS-03 e OBS-04 são bons exemplos de como uma prototipação de baixa fidelidade pode revelar problemas conceituais antes da implementação.

A revisão necessária agora é de precisão. A interface mostrada pertence principalmente a P01, mas a documentação afirma cobertura de tarefas de P02 que ainda não estão efetivamente prototipadas. Além disso, a entrega descreve muito bem os estados e as alterações pós-simulação, porém ainda os mostra pouco visualmente dentro de `assets/06_prototipos/`.

O próximo passo não é acrescentar mais funções. É deixar mais clara a relação:

**persona → tarefa → estado da interface → observação do walkthrough → alteração de design**.

Quando essa cadeia estiver explícita, a prototipação cumprirá plenamente seu papel no projeto.

> **Complemento de preservação documental** ([`5d174d2`](https://github.com/KawanMark/template-ihc2026/commit/5d174d29fca861af555406e56d0dd357bb300ad9)): o registro detalhado original continua íntegro na seção histórica da referência da Entrega 11. A abertura aponta para a prancha e os estados revisados; os valores e rótulos históricos não são requisitos atuais.
>
> \- Kawan

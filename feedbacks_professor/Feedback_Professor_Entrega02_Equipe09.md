# Feedback do Professor > Entrega 02 > Equipe 09

> **Status da aplicação (06/10/2026):** esta revisão cobre a análise C02, de Gabriel, e as partes de grupo da entrega: seções 3.1, 4 e 5, checklist e matriz de rastreabilidade. As análises C01 (Kawan) e C03 (Alexandre) ficam com seus autores. Cada comentário abaixo traz uma anotação com o link para o commit correspondente, na branch `aplicar-feedback`. O texto original do professor foi preservado; as anotações aparecem em blocos de citação logo após cada item.
>
> | Item do parecer | Situação | Commit(s) |
> |---|---|---|
> | Correção 1: requisito visual parcial | aplicada em C02; C03 fica com Alexandre | [`fc1936b`](https://github.com/KawanMark/template-ihc2026/commit/fc1936b) |
> | Correção 2: prints ligados aos achados | aplicada em C02; C01 fica com Kawan e C03 com Alexandre | [`0e15205`](https://github.com/KawanMark/template-ihc2026/commit/0e15205) |
> | Correção 3: origem de RC04 | aplicada | [`6fa619a`](https://github.com/KawanMark/template-ihc2026/commit/6fa619a) |
> | Correção 4: RC05, canal e risco da IA | aplicada | [`009030b`](https://github.com/KawanMark/template-ihc2026/commit/009030b) |
> | Correção 5: RC06 como hipótese | aplicada | [`dc04e17`](https://github.com/KawanMark/template-ihc2026/commit/dc04e17) |
> | Correção 6: RC09 | aplicada na seção 5; texto de C03 fica com Alexandre | [`c08610d`](https://github.com/KawanMark/template-ihc2026/commit/c08610d) |
> | Correção 7: RC10 | aplicada na seção 5; texto de C03 fica com Alexandre | [`58f9252`](https://github.com/KawanMark/template-ihc2026/commit/58f9252) |
> | Correção 8: RC11 | aplicada | [`481ba6a`](https://github.com/KawanMark/template-ihc2026/commit/481ba6a) |
> | Correção 9: origem de RC03 | aplicada | [`35b58fe`](https://github.com/KawanMark/template-ihc2026/commit/35b58fe) |
> | Correção 10: classificação das recomendações | aplicada | [`053a335`](https://github.com/KawanMark/template-ihc2026/commit/053a335) |
> | Recomendação 1: qualidade visual de C01 | fica com Kawan | |
> | Recomendações 2 e 3: limitações e documentação normativa | aplicadas | [`fc1936b`](https://github.com/KawanMark/template-ihc2026/commit/fc1936b) |
> | Recomendação 4: impactos na matriz | aplicada | [`2b9632a`](https://github.com/KawanMark/template-ihc2026/commit/2b9632a) |
> | Registro da revisão | aplicado | [`8e99857`](https://github.com/KawanMark/template-ihc2026/commit/8e99857) |
>
> \- Gabriel

## Avaliação geral

A equipe atendeu ao requisito quantitativo mais importante da Entrega 02: há **três integrantes e três análises individualizadas**, com autoria explícita - C01 por Kawan Mark Geronimo da Silva, C02 por Gabriel Albertini Pinheiro e C03 por Alexandre Domiciano Pierri. Portanto, o critério de **pelo menos uma interface corrente analisada por aluno** foi atendido.

A seleção das referências também é coerente com o escopo do projeto: a equipe não procurou apenas “concorrentes do algoritmo”, mas investigou uma ferramenta de apoio à interpretação radiográfica (C01), uma interface profissional já pertencente ao contexto aduaneiro (C02) e outra família de ferramentas de inspeção de imagens (C03). Isso é adequado para um TCC que originalmente não previa interface.

O ponto que mais merece revisão está no **grau de força das conclusões derivadas**. A equipe fez uma análise rica e encontrou padrões úteis, porém algumas recomendações da seção 5 avançam além do que as evidências observadas permitem concluir. Em especial, em alguns pontos uma ausência de recurso no concorrente passa a ser tratada como prova de que o projeto deve implementar esse recurso; em outros, uma convenção normativa do Siscomex é transferida diretamente para uma escala de risco da IA, embora sejam conceitos potencialmente diferentes.

Quanto às evidências visuais, o atendimento é **parcial**. O diretório `assets/02_concorrencia/` contém sete imagens e está organizado de forma coerente. C01 possui capturas efetivamente relacionadas à interface/ferramentas analisadas. C02 possui uma tela pública do Portal Único e uma captura de documentação normativa, mas não a interface operacional do Auditor-Fiscal. C03 contém páginas públicas de produto da Smiths Detection, e não telas reais da estação de trabalho RIW/CargoVision em uso. A própria equipe reconhece essa limitação no checklist, o que é correto. Assim, a documentação visual existe e é útil, mas não atende integralmente ao objetivo de observar estados e decisões reais de interface em todas as três análises.

De modo geral, a Entrega 02 apresenta boa maturidade analítica e mostra evolução em relação às hipóteses da Entrega 01. O trabalho agora precisa distinguir com maior rigor três coisas diferentes: **padrão efetivamente observado**, **inferência plausível a partir do concorrente** e **decisão de design ainda a validar no próprio projeto**.

## Pontos positivos

- O requisito de uma análise por integrante foi cumprido de forma clara e rastreável.
- As três análises têm autores identificados e apresentam recortes complementares, evitando três avaliações praticamente idênticas do mesmo produto.
- C01 é bem alinhada à tarefa central do projeto de IHC: interpretação visual de imagens radiográficas com apoio computacional.
- C02 amplia corretamente a análise para uma interface que faz parte do ecossistema profissional do público-alvo, mesmo não sendo concorrente direto.
- C03 procura compreender convenções visuais já conhecidas por operadores de inspeção, especialmente filtros, pseudo-cor, realce e integração com manifesto.
- A equipe registra limitações das fontes, em vez de fingir acesso a interfaces restritas.
- A análise comparativa da seção 4 usa critérios comuns entre C01, C02 e C03, o que permite realmente comparar as soluções.
- A Entrega 02 produziu evolução concreta da rastreabilidade: H09 foi revista, H15 foi parcialmente corrigida e H24 foi atualizada para reconhecer quatro canais normativos.
- A equipe identificou padrões que podem alimentar o projeto, como centralidade da imagem, comparação visual, linguagem do domínio, linha do tempo de processo, atribuição de responsável e necessidade de não sobrecarregar a imagem.
- O diretório `assets/02_concorrencia/` está organizado com nomes de arquivos consistentes e relacionados diretamente às análises.

## Correções prioritárias

### 1. O requisito visual foi apenas parcialmente atendido para C02 e C03

O diretório `assets/02_concorrencia/` contém:

- três imagens relacionadas à C01;
- duas imagens relacionadas à C02;
- duas imagens relacionadas à C03.

Em C01, as capturas mostram diretamente recursos utilizados na análise - High Density, Similar Cargo e Vehicle Compare. Portanto, existe boa correspondência entre evidência visual e argumento.

Em C02, a captura `c02_siscomex_portal_perfis.png` mostra uma interface real e corrente do Portal Único, mas em nível de entrada/perfil. Já `c02_siscomex_canais_parametrizacao.png` é essencialmente uma captura de documentação normativa. Ela é uma boa evidência para os quatro canais, mas não é uma tela operacional do fluxo do Auditor-Fiscal.

Em C03, `c03_smiths_daisy_plataforma.png` e `c03_smiths_vizual_discriminacao.png` são páginas públicas de produto do fabricante. Elas sustentam que DaiSy e viZual existem e quais capacidades são divulgadas, porém não permitem observar organização da estação de trabalho, posição dos controles, densidade de informação, sequência de uso ou comportamento do operador.

A própria equipe reconhece corretamente essa limitação no checklist. Portanto, não considero esse item simplesmente “não feito”; considero **parcialmente atendido**.

Para melhorar a entrega, a equipe deve procurar, quando legalmente e publicamente disponível, manuais, datasheets ilustrados, vídeos institucionais, materiais de treinamento, artigos ou apresentações técnicas que exibam a estação real. Caso isso realmente não exista publicamente, mantenham a limitação explicitada e evitem transformar especificações funcionais em conclusões sobre layout.

> **🟨 Tratado em parte** ([`fc1936b`](https://github.com/KawanMark/template-ihc2026/commit/fc1936b)): em C02, a tabela de prints diz a natureza de cada captura. `c02_siscomex_portal_perfis.png` é tela real em nível de entrada, e `c02_siscomex_canais_parametrizacao.png` é documentação normativa. Três células da tabela de funcionalidades citavam o print como evidência de funções que ele não mostra e foram corrigidas. A ressalva e a nota do checklist registram o requisito como parcialmente atendido e dizem que C02 e C03 não concluem sobre layout. A busca por manuais, vídeos ou materiais de treinamento que exibam a tela do Auditor-Fiscal não foi feita nesta revisão e fica para a coleta de dados da Entrega 7.
>
> **⏭️ Fora desta revisão**: a busca por material público que mostre a estação RIW em C03 fica com Alexandre.
>
> \- Gabriel

> **➕ Complemento (06/10/2026)** ([`ed78639`](https://github.com/KawanMark/template-ihc2026/commit/ed78639)): a busca por material público que mostre a tela de trabalho do Auditor-Fiscal foi feita e não encontrou manuais, vídeos nem materiais de treinamento. O resultado está nas limitações de C02. Foram localizadas normas da RFB sobre o uso de escâner, que descrevem o processo e os requisitos do software, e não a tela.
>
> \- Gabriel

### 2. Os prints precisam ficar mais fortemente ligados aos achados positivos, negativos e padrões de mercado

A equipe descreve os achados em tabelas e referencia os arquivos do diretório `assets/02_concorrencia/`, o que é positivo. Porém, a comprovação visual ainda depende muito da interpretação do leitor.

Uma melhoria simples seria numerar ou destacar nas capturas os elementos relevantes e depois relacionar cada marcação ao texto. Por exemplo:

- “P1 - comparação simultânea das imagens”;
- “P2 - barra de ferramentas lateral”;
- “N1 - excesso de comandos próximos à imagem”;
- “M1 - padrão de mercado: imagem ocupa área central”.

Não é necessário transformar cada print em um pôster. O objetivo é permitir que o leitor identifique rapidamente **qual parte da tela comprova o ponto discutido**.

Esse aspecto é especialmente importante em uma entrega de análise de concorrência: o argumento deve nascer daquilo que foi observado, e não apenas do texto que acompanha a imagem.

> **🟨 Tratado em parte** ([`0e15205`](https://github.com/KawanMark/template-ihc2026/commit/0e15205)): C02 ganhou versões marcadas das duas capturas (`c02_siscomex_portal_perfis_marcado.png` e `c02_siscomex_canais_parametrizacao_marcado.png`) e uma tabela que liga cada marca (P, N, M) ao ponto que ela comprova. As marcas da página de canais mostram a lista dos quatro canais, os elementos de seleção, o redirecionamento de canal e o Auditor-Fiscal responsável pelo desembaraço.
>
> **⏭️ Fora desta revisão**: as marcações nos prints de C01 ficam com Kawan e as de C03 com Alexandre.
>
> \- Gabriel

> **➕ Complemento (06/10/2026)**: os trechos das marcas P2 e P3 foram conferidos no texto da página oficial da Receita Federal e correspondem ao que a tabela de marcações diz. Não houve mudança de arquivo.
>
> \- Gabriel

### 3. RC04 está atribuída à fonte errada

A RC04 afirma que o fluxo de decisão deve incluir justificativa e trilha de auditoria e a deriva de uma **limitação da C01**, isto é, do fato de a Rapiscan não mostrar publicamente essa dimensão.

A ausência de evidência em C01 não é suficiente para concluir que o projeto precisa dessa funcionalidade.

Entretanto, a própria C02 apresenta evidência muito mais forte: exigência fiscal, atribuição a auditor responsável, processo formal e rastreabilidade. Portanto, a recomendação pode fazer sentido, mas sua origem precisa ser corrigida.

Sugiro que RC04 seja derivada principalmente de C02 e relacionada às hipóteses H17, H18, H19 e H32. A limitação de C01 pode aparecer apenas como contraste.

> **✅ Como foi tratado** ([`6fa619a`](https://github.com/KawanMark/template-ihc2026/commit/6fa619a)): RC04 deriva principalmente de C02 (exigência fiscal com motivo e prazo, distribuição para auditor, linha do tempo) e cita H17, H18, H19 e H32. A limitação de C01 aparece só como contraste. O texto de C02 que dizia "Confirma RC04" agora diz que C02 é a origem principal de RC04 e RC07.
>
> \- Gabriel

### 4. RC05 mistura “canal aduaneiro” com “nível de risco da IA”

A C02 identificou corretamente quatro canais normativos - verde, amarelo, vermelho e cinza - e isso corrige a hipótese H24 da Entrega 01.

Porém, RC05 conclui que **“a escala de risco da fila deve ter quatro estados alinhados aos canais oficiais”**.

Aqui existe um salto conceitual importante.

Os canais do Siscomex representam uma **classificação normativa do processo de despacho e do tipo de conferência**. Já o resultado do modelo de IA representa uma medida, classificação ou evidência de **anomalia radiográfica**. Não está demonstrado que essas duas escalas sejam semanticamente equivalentes.

A equipe deve evitar transformar os quatro canais normativos em quatro níveis de risco algorítmico apenas porque ambos podem ser apresentados com cores.

Uma recomendação mais defensável seria: o projeto deve **preservar e respeitar a semântica oficial dos canais quando essa informação for exibida**, deixando separada a evidência produzida pela IA até que sua relação com a decisão aduaneira seja investigada.

Este é um ponto prioritário porque uma mistura conceitual aqui pode induzir o usuário a interpretar um resultado algorítmico como decisão normativa.

> **✅ Como foi tratado** ([`009030b`](https://github.com/KawanMark/template-ihc2026/commit/009030b)): RC05 pede que a semântica oficial dos quatro canais seja preservada quando o canal for exibido e que ele não represente o resultado do modelo. A relação entre evidência de anomalia e canal virou a lacuna ?08 na matriz, com o que o Manual de Despacho já mostra: os critérios de seleção do canal são fiscais e documentais. As duas linhas de C02 que falavam em "semáforo de risco" e em "estado que falta na nossa fila" foram reescritas.
>
> \- Gabriel

### 5. RC06 transforma uma ausência observada em necessidade confirmada

A C02 não encontrou evidência pública de uma fila priorizada por risco para o fiscal. A equipe interpreta isso como uma “oportunidade clara” e RC06 determina que a tela deve oferecer uma fila ordenada por risco.

A ausência de um recurso no concorrente não demonstra automaticamente que o usuário precisa dele.

Pode ser:

- uma oportunidade real;
- uma função existente, mas não documentada;
- uma atividade realizada em outro sistema;
- uma função desnecessária;
- uma prática proibida ou incompatível com o processo institucional.

Portanto, RC06 ainda deve permanecer como **hipótese de design**, vinculada a H25/H33/H35, até que a investigação do trabalho real demonstre que o usuário precisa decidir “qual contêiner examinar primeiro” e possui autonomia para alterar essa ordem.

A análise de concorrência encontrou um vazio. A próxima etapa deve descobrir se esse vazio é realmente um problema.

> **✅ Como foi tratado** ([`dc04e17`](https://github.com/KawanMark/template-ihc2026/commit/dc04e17)): RC06 é hipótese de design, vinculada a H25, H33 e H35 e condicionada à nova H41 (o usuário decide o que examinar primeiro e tem autonomia para alterar a ordem). A linha "Oportunidade clara" de C02, a linha de dashboard da seção 3.1 e as células de navegação e eficiência da seção 4 listam as outras explicações possíveis para a ausência. Na matriz, H25 e H33 deixaram o estado "oportunidade confirmada".
>
> \- Gabriel

### 6. RC09 extrapola corretamente um problema, mas prescreve cedo demais a solução

C03 mostra que o operador pode utilizar pseudo-cor, realce de bordas, equalização e outras formas de tratamento visual. Isso sustenta uma recomendação importante: **a visualização da IA não deve competir com as codificações visuais já conhecidas pelo operador**.

Entretanto, RC09 determina diretamente “opacidade ajustável e alternância rápida”.

Esses controles são soluções candidatas plausíveis, mas não foram observados como padrão de mercado nas evidências apresentadas.

Sugiro separar:

- **recomendação derivada:** a camada de IA deve poder ser distinguida dos tratamentos radiográficos existentes e não deve ocultar a imagem;
- **hipótese de solução:** testar opacidade ajustável, toggle, comparação lado a lado ou outras alternativas.

Isso prepara melhor a equipe para prototipação sem transformar uma primeira ideia em requisito.

> **🟨 Tratado em parte** ([`c08610d`](https://github.com/KawanMark/template-ihc2026/commit/c08610d)): RC09 separa a recomendação derivada (a camada de IA deve ser distinguível dos tratamentos radiográficos e não ocultar a imagem) da hipótese de solução (opacidade, alternância, lado a lado). A linha de realce e pseudo-cor da seção 3.1 acompanha.
>
> **⏭️ Fora desta revisão**: na análise C03, a linha "Limitação: acúmulo de filtros na tela" ainda prescreve slider e toggle. A reescrita fica com Alexandre.
>
> \- Gabriel

### 7. RC10 contém uma boa conclusão e uma decisão de layout não sustentada

A centralidade da imagem radiográfica é bem sustentada por C01 e C03. Portanto, a recomendação de reservar alta prioridade visual à imagem faz sentido.

Porém, RC10 acrescenta que metadados e ações devem ficar em **“painéis laterais retráteis”**. Essa decisão específica não foi demonstrada pelas evidências.

“Imagem deve permanecer central” é recomendação derivada.

“Painéis laterais retráteis” é uma alternativa de design a experimentar posteriormente.

A equipe está um pouco ansiosa para abrir o Figma - calma, ele não vai fugir.

> **🟨 Tratado em parte** ([`58f9252`](https://github.com/KawanMark/template-ihc2026/commit/58f9252)): RC10 mantém a prioridade visual da imagem, derivada de C01 e C03, e trata a posição de metadados e ações como alternativa de layout a experimentar.
>
> **⏭️ Fora desta revisão**: na análise C03, a linha "Lição de IHC: centralidade na imagem radiográfica" ainda cita painéis laterais retraíveis. A reescrita fica com Alexandre.
>
> \- Gabriel

### 8. RC11 é conceitualmente boa, mas sua justificativa precisa ser corrigida

A recomendação de não transmitir informação crítica apenas por cor é coerente com princípios de acessibilidade e deve ser preservada.

Entretanto, a frase que afirma que C02 e C03 **“dependem exclusivamente de cor”** é mais forte do que as evidências apresentadas.

No caso do Siscomex, os canais possuem nomes textuais e significado normativo, ainda que a cor seja muito importante. Em C03, as páginas de produto demonstram pseudo-cor associada à discriminação de materiais, mas não demonstram que a interface completa dependa exclusivamente dessa codificação.

Portanto, RC11 deve ser apresentada como:

- uma preocupação despertada pela forte presença de codificação cromática nas interfaces analisadas;
- reforçada por princípios de acessibilidade de IHC.

Assim fica claro o que veio da concorrência e o que veio da teoria.

> **✅ Como foi tratado** ([`481ba6a`](https://github.com/KawanMark/template-ihc2026/commit/481ba6a)): RC11 é apresentada como recomendação de acessibilidade (uso de cor, WCAG 2.1, critério 1.4.1), motivada pela presença de codificação cromática em C02 e C03. O texto diz que a dependência exclusiva de cor não está demonstrada. A linha de canal da seção 3.1 e as células de acessibilidade da seção 4 foram ajustadas.
>
> \- Gabriel

### 9. RC03 deveria incorporar C02 e C03, e não somente C01

RC03 recomenda usar linguagem operacional do domínio e evitar métricas técnicas de IA como elemento principal.

A recomendação faz sentido, mas a fundamentação mais forte não é apenas a organização do InSight por tarefas.

C02 fornece evidência explícita do vocabulário profissional brasileiro: canal, parametrização, exigência, desembaraço, dossiê etc. C03 também utiliza terminologia operacional específica da inspeção.

Portanto, RC03 deveria ser marcada como recomendação derivada **de C01 + C02 + C03**, com destaque especial para C02 quando o assunto for terminologia normativa do fiscal.

> **✅ Como foi tratado** ([`35b58fe`](https://github.com/KawanMark/template-ihc2026/commit/35b58fe)): RC03 deriva de C01, C02 e C03, com C02 como referência para a terminologia normativa do fiscal.
>
> \- Gabriel

### 10. É preciso separar com mais rigor “padrão de mercado”, “achado do concorrente” e “oportunidade do projeto”

Na seção 3.1, alguns itens estão muito bem tratados. Por exemplo, dashboard é explicitamente marcado como **não observado**.

Esse cuidado deveria ser aplicado uniformemente.

Sugiro que cada recomendação da seção 5 receba uma classificação simples:

- **PM - padrão observado em mercado**;
- **AP - achado/problema observado**;
- **HD - hipótese de design derivada**;
- **TIHC - recomendação sustentada principalmente pela teoria de IHC**.

Isso evitaria frases como “o concorrente não tem, então nosso sistema deve ter”.

A Entrega 02 é justamente a fase em que o grupo aprende com o mercado. Aprender também significa descobrir o que **ainda não sabemos**.

> **✅ Como foi tratado** ([`053a335`](https://github.com/KawanMark/template-ihc2026/commit/053a335)): cada recomendação da seção 5 traz PM, AP, HD ou TIHC, com legenda. RC06 e RC08 são HD, RC11 é TIHC, e RC09 e RC10 têm duas marcas: uma para o princípio e outra para a solução citada.
>
> \- Gabriel

## Recomendações de melhoria

### 1. Valorizar mais a qualidade visual de C01

C01 possui as evidências mais diretamente observáveis da entrega. A equipe poderia explorar melhor elementos concretos visíveis nos prints - distribuição espacial, comparação lado a lado, ferramentas periféricas, centralidade da imagem e formas de destaque.

Atualmente, parte da análise ainda se apoia fortemente no texto promocional do fabricante.

> **⏭️ Fora desta revisão**: a análise C01 é de Kawan. Explorar melhor os elementos visíveis nos prints do InSight fica com ele.
>
> \- Gabriel

### 2. Manter a boa prática de registrar limitações de acesso

A ressalva de C02 e C03 é adequada e deve ser preservada. Em sistemas governamentais e de segurança, é perfeitamente plausível que telas reais não sejam públicas.

O erro seria inventar a interface que não foi observada. A equipe não fez isso de forma explícita, mas algumas inferências de layout precisam ser moderadas para manter essa coerência.

> **✅ Como foi tratado** ([`fc1936b`](https://github.com/KawanMark/template-ihc2026/commit/fc1936b)): as ressalvas de acesso foram mantidas. Em C02 a ressalva agora diz também o que a análise deixa de concluir por causa dela.
>
> \- Gabriel

### 3. Diferenciar documentação normativa de screenshot de interface

`c02_siscomex_canais_parametrizacao.png`, no diretório `assets/02_concorrencia/`, é uma ótima evidência de domínio e processo, mas não deve ser contabilizada conceitualmente como “tela de interface analisada” no mesmo sentido de uma tela de operação.

Ela sustenta linguagem, estados normativos e regras. Não sustenta usabilidade da tela operacional.

> **✅ Como foi tratado** ([`fc1936b`](https://github.com/KawanMark/template-ihc2026/commit/fc1936b)): a tabela de prints de C02 tem a coluna "Natureza" e classifica `c02_siscomex_canais_parametrizacao.png` como documentação normativa, que sustenta linguagem, estados e regras, e não usabilidade.
>
> \- Gabriel

### 4. Atualizar a matriz de rastreabilidade sem transformar “parcialmente sustentada” em “requisito”

A matriz foi atualizada de forma muito boa, mas alguns impactos já são escritos como componentes definidos - por exemplo, inclusão de painel, score, busca ou alertas.

Quando o estado é “parcialmente sustentada” ou “aberta”, o impacto deveria preferencialmente permanecer como possibilidade a investigar.

> **✅ Como foi tratado** ([`2b9632a`](https://github.com/KawanMark/template-ihc2026/commit/2b9632a)): na matriz, a coluna de impacto de vinte hipóteses abertas ou parcialmente sustentadas passou a descrever possibilidades a investigar. Uma nota na seção 2 registra a regra.
>
> \- Gabriel

## Pontos que devem alimentar as próximas entregas

- **H01:** continuar investigando se Operador de Scanner e Auditor-Fiscal são de fato o mesmo papel ou papéis distintos.
- **H11:** aprofundar quais informações documentais precisam estar visíveis junto da imagem e em que momento.
- **H24:** manter os quatro canais como convenção normativa, sem confundi-los automaticamente com score/risco do modelo de IA.
- **H25/H33/H35:** investigar se existe realmente uma tarefa de priorização de fila e se o usuário possui autoridade para executá-la.
- **H28:** relatório/laudo continua sem evidência suficiente e deve permanecer hipótese.
- **H29:** separar claramente busca por identificador, histórico cronológico e busca por risco; são necessidades distintas.
- **H30:** comparação visual possui boa sustentação de mercado, mas a preferência entre lado a lado e sobreposição ainda deve ser testada.
- **H31:** ROI/destaque visual tem sustentação parcial; score numérico e sua interpretação continuam abertos.
- **H32:** rastreabilidade da decisão é importante no domínio, mas o formato concreto da trilha deve ser investigado.
- **Acessibilidade:** transformar RC11 em requisito de qualidade fundamentado em IHC e posteriormente verificar contraste, redundância visual e interpretação da informação cromática.
- **Protótipos:** testar alternativas em vez de congelar desde já slider, painel retrátil, fila automática ou quatro níveis de “risco IA”.

> **ℹ️ Encaminhamento** ([`009030b`](https://github.com/KawanMark/template-ihc2026/commit/009030b), [`dc04e17`](https://github.com/KawanMark/template-ihc2026/commit/dc04e17), [`2b9632a`](https://github.com/KawanMark/template-ihc2026/commit/2b9632a)): H01 foi tratada na revisão da Entrega 1, com a nova H39. H24 ficou separada do resultado da IA (RC05, ?08). H25, H33 e H35 dependem de H41. H28 a H32 têm o impacto descrito como possibilidade na matriz. A acessibilidade segue por RC11. Os testes de alternativas ficam para as Entregas 6 e 12 a 14.
>
> \- Gabriel

## Síntese das ações recomendadas

1. **Manter como atendido o requisito de uma análise por aluno:** C01, C02 e C03 possuem autoria individual explícita.
2. **Registrar o requisito de prints como parcialmente atendido**, pois C02 e principalmente C03 não possuem todas as telas operacionais reais; no parecer, as evidências do `.zip` correspondem ao diretório `assets/02_concorrencia/`.
3. **Reforçar as capturas com marcações ou chamadas visuais**, ligando diretamente o screenshot ao ponto positivo, negativo ou padrão observado.
4. **Reescrever RC04 com origem principal em C02**, e não na ausência de informação em C01.
5. **Revisar RC05 para não confundir os quatro canais normativos do Siscomex com quatro níveis de risco da IA.**
6. **Rebaixar RC06 para hipótese de design** até validar que priorização de fila é realmente uma tarefa do usuário.
7. **Separar em RC09 e RC10 o princípio aprendido da solução concreta**, deixando opacidade, toggle e painéis retráteis para prototipação e teste.
8. **Ajustar RC11**, apresentando redundância além da cor como recomendação de acessibilidade apoiada pela teoria, motivada - mas não totalmente provada - pelos concorrentes.
9. **Ampliar a origem de RC03 para C01+C02+C03**, porque a linguagem do domínio está especialmente bem evidenciada em C02.
10. **Classificar recomendações como padrão observado, achado, hipótese de design ou princípio de IHC**, aumentando a rastreabilidade entre evidência e decisão.

> **Situação:** as ações 1, 2 e 4 a 10 foram aplicadas em C02, nas seções 3.1, 4 e 5 e na matriz. A ação 3 foi aplicada só nos prints de C02. Ficam com Kawan as marcações e o aprofundamento visual de C01. Ficam com Alexandre as marcações de C03 e as duas linhas de C03 que ainda prescrevem slider e painéis retraíveis.
>
> \- Gabriel

## Parecer geral sobre a Entrega 02

A Entrega 02 cumpre bem sua função principal de tirar o projeto do campo das suposições e colocá-lo em contato com soluções e convenções reais do domínio. A cobertura por aluno foi atendida, as três análises são complementares e a equipe demonstrou capacidade de revisar hipóteses anteriores a partir de novas evidências. O principal ponto de atenção está na passagem entre **“observei isto no mercado”** e **“portanto meu sistema deve fazer aquilo”**: algumas recomendações são diretamente sustentadas, enquanto outras ainda são hipóteses de design apresentadas com força excessiva. Também é necessário reconhecer formalmente que as evidências visuais no diretório `assets/02_concorrencia/` são desiguais: C01 possui material de interface mais representativo, C02 combina interface pública com documentação normativa e C03 utiliza páginas de produto porque as telas operacionais são restritas. Com esses ajustes, a equipe terá uma base muito boa para avançar sem copiar concorrentes e, principalmente, sem transformar ausência de evidência em requisito.

> **Complemento de situação (15/11/2026)** ([`c8f5510`](https://github.com/KawanMark/template-ihc2026/commit/c8f551062b0c55b4a76b1d500bcb95cf72e859bd), [`6f267f6`](https://github.com/KawanMark/template-ihc2026/commit/6f267f6b6a308c5cc4b051139115a5c67c70f10f)): C01/C03 possuem figuras com marcações e alcance explícito. C03 ganhou reproduções operacionais da brochura oficial, sem generalizar sobre a versão corrente. C02 permanece parcial por acesso restrito à tela de trabalho. Recomendações de camadas/layout continuam alternativas de design.
>
> \- Kawan

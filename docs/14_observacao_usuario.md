# Entrega 14 — Observação de usuários

**Data:** 21/11/2026<br>
**Status:** 🟩 concluída — piloto interno, três sessões com participantes proxy externos (`U01`–`U03`) sobre o protótipo `v1.1`, métricas consolidadas, achados `AU01`–`AU05` comparados com a heurística e vídeo demonstrativo publicado.<br>
**Responsáveis:** Kawan Mark Geronimo Da Silva, Gabriel Albertini Pinheiro e Alexandre Domiciano Pierri.

Aplicar o [plano DECIDE](12_planejamento_avaliacao.md) à Mesa de inspeção. Os testes foram conduzidos com três participantes proxy adultos externos à equipe (`U01`, `U02` e `U03`), com justificativa individual de aderência e limitações registradas, após a correção dos bloqueios da [Entrega 13](13_avaliacao_heuristica.md).

## A. Fluxograma do processo

![Processo da observação](../assets/14_testes/fluxograma_avaliacao.svg)

[Fonte SVG editável](../assets/14_testes/fluxograma_avaliacao.svg).

## B. Preparação e execução

### 1. Objetivos e versão

Verificar comparação (MU01), entendimento dos limites da IA (MU02), parecer completo (MU03), tempo de registro (MU04), recuperação (MU05) e facilidade (MU06). O teste avalia a interação, não a validade científica do modelo.

**Versão avaliada:** Protótipo HTML navegável `v1.1` ([`assets/11_figma/prototipo/index.html`](../assets/11_figma/prototipo/index.html), 19 telas/estados), gerado a partir da mesma base de telas da [Entrega 11](11_figma.md) e congelado em 21/11/2026 após incorporar as correções `V01`–`V07` e `V09` da [Entrega 13](13_avaliacao_heuristica.md). Todas as três sessões finais utilizaram exatamente essa mesma versão congelada.

| Tarefa | Verificação técnica antes do piloto (v1.0 → v1.1) | Estado congelado usado nas sessões (v1.1) |
|---|---|---|
| UT01 | Os controles de visualização levam de `F03` a `F04` e `F05`; códigos `S` removidos (`V04`) e contorno duplo aplicado (`V07`). | Retorno livre entre `Sobreposta`, `Sem mapa` e `Lado a lado` com mesma imagem e identificador `CASO-DEMO-0417`. |
| UT02 | `V01` corrigido (`F11b → F07b → F08b` preserva “Sem ressalvas na imagem”); `V03` corrigido (`F11a → F07`); `Restaurar ajustes` (`V05`) e link `Editar` (`V09`) adicionados. | Fluxo completo `F03 → F06 → F07 → F08 → F09 → F12` sem perda de conclusão humana e com conferência na prévia. |
| UT03 | `V02` e `V06` corrigidos: criada variante `F10c_ut03` isolando apenas `Responsável` ausente, com campo clicável direto na interface e aviso de limite visível em 1440×900. | Estado inicial `F10c_ut03` preparado fora da medição; primeira exportação válida aciona falha simulada `F10d` e “Tentar novamente” conclui em `F09` preservando os dados. |

**Verificação técnica complementar no Chromium:** a análise em andamento permite cancelar e voltar à entrada (`F02 → F01`), a falha de análise permite tentar novamente (`F10b → F02`) e a exportação simulada chega à confirmação e ao PDF (`F08 → F09 → F12`). Com os bloqueios `V01`–`V03` corrigidos na `v1.1`, o piloto interno e as três sessões finais foram executados sobre essa versão congelada.

### 2. Participantes e recrutamento

Foram observados **três participantes proxy adultos externos à equipe** (`U01`, `U02` e `U03`), igualando o número de integrantes (3), conforme o enunciado da disciplina. Nenhum integrante da equipe atuou como participante final; os nomes reais e termos assinados ficam arquivados fora do Git, vinculados apenas aos IDs anônimos.

| ID | Perfil (sem nome real) | Critérios que justificam a participação (proxy) | Integrante responsável (moderador) |
|---|---|---|---|
| **U01** | Adulto (28 anos), analista de controle de qualidade industrial | Habituado à inspeção visual de imagens técnicas e ao registro estruturado de não conformidades; aderência direta a `UT01` e `UT02`. | Kawan Mark Geronimo Da Silva |
| **U02** | Adulto (31 anos), analista administrativo / auditoria documental | Leitura e emissão diária de pareceres técnicos e relatórios de conferência; aderência direta a `UT02`, `UT03` e leitura de `F08`/`F12`. | Gabriel Albertini Pinheiro |
| **U03** | Adulto (26 anos), técnico de logística e conferência de cargas | Uso diário de sistemas de manifesto, conferência de unidade de carga e registro de ocorrências; aderência ao vocabulário de `M03`. | Alexandre Domiciano Pierri |

**Limitação explícita do recrutamento:** por restrição de acesso a operadores aduaneiros da RFB/recintos alfandegados no prazo da disciplina, foram utilizados proxies adultos externos com experiência pertinente às tarefas de inspeção visual, leitura de relatórios e logística. Os resultados avaliam exclusivamente a compreensão e a usabilidade da interação no protótipo simulado, sem equivaler à validação com especialistas reais nem à rotina aduaneira oficial.

### 3. Consentimento e privacidade

Usar o [termo preparado](../instrumentos/12_avaliacao/consentimento.md) antes da sessão. Gravação prevista de tela e áudio, sem webcam, somente mediante autorização específica. Se houver recusa à gravação, respeitar a escolha e registrar a limitação da evidência; não produzir vídeo sem consentimento.

Guardar consentimentos e registros brutos em pasta privada da equipe, acessível ao professor quando necessário. Publicar apenas resumos anônimos U01–U03. O vídeo acadêmico terá link restrito ao professor, nunca dados pessoais expostos no Git. Descartar os registros brutos em até 90 dias após a sessão. Usar caso/carga fictícios e responsável fictício no protótipo; fechar notificações e outras janelas.

### 4. Piloto

**Situação:** realizado internamente em 21/11/2026 sobre a versão HTML `v1.1` (`assets/11_figma/prototipo/index.html`), após a aplicação das correções `V01`–`V07` e `V09` da [Entrega 13](13_avaliacao_heuristica.md). O participante interno do piloto não entrou na amostra final.

**Ajustes confirmados no piloto antes de congelar a versão:**
- Alinhamento do identificador do caso para `CASO-DEMO-0417` na instrução de `UT01`.
- Verificação do estado inicial `F10c_ut03` (isolando apenas o campo `Responsável` vazio) para permitir observar a recuperação natural em `UT03` sem recorrer à faixa de simulação.
- Verificação da remoção dos códigos internos `(S01)`–`(S18)` dos rótulos visíveis e do contraste do contorno duplo na região do modelo.
- Duração total do piloto: 22 minutos, dentro da janela planejada de 25–30 minutos. Versão `v1.1` congelada para as três sessões finais.

### 5. Tarefas

| ID | Instrução resumida — ler a versão integral no roteiro | Sucesso / medidas | Ligação |
|---|---|---|---|
| UT01 | Examinar a área indicada, comparar com a imagem sem destaque e explicar o alcance do resultado. | Comparação concluída sem ajuda; distingue indício de prova e de autorização. Tempo, erros, ajudas e facilidade. | T01/T02; O02/O03/O08; M01; F03–F05. |
| UT02 | Registrar a região/observação e preparar parecer para outra pessoa com conclusão e autoria fictícia. | Caso correto, região comentada, conclusão, justificativa e responsável; mediana ≤ 180 s sem ajuda. | T03; consulta de T05/T06; O04–O07/O09; M01/M03; F06–F09/F12. |
| UT03 | Resolver a falta do responsável e eventual falha, preservando o registro ao emitir o parecer. | Bloqueia emissão incompleta; recupera omissão e falha de exportação sem perder dados. | O05/O08; M01/M03; F07/F10C/D/F08/F09. |

O identificador do caso em UT01 foi alinhado para `CASO-DEMO-0417` na Entrega 12 e no roteiro, correspondendo à interface HTML. Antes do piloto, confirmar se a versão congelada do Figma exibe o mesmo identificador e usar a mesma formulação para todos os participantes.

Limite de 5 minutos por tarefa. Estados iniciais são independentes: caso pronto em UT01/UT02; registro sem responsável e primeira exportação válida com falha simulada em UT03. Não depender do sucesso anterior para aplicar a próxima tarefa. O [roteiro](../instrumentos/12_avaliacao/roteiro.md) traz instruções neutras e condições iguais para todos.

### 6. Protocolo do moderador

1. Receber a pessoa, explicar que o produto está sendo avaliado e obter consentimento.
2. Registrar perfil mínimo e condição profissional/proxy; permitir exploração inicial padronizada.
3. Preparar estado inicial, ler a instrução e iniciar o cronômetro.
4. Observar sem ensinar o caminho; separar pedidos de ajuda e intervenções. Não exigir fala contínua durante a medição.
5. Registrar sucesso, erros, ajudas e tempo. Encerrar em desistência ou limite, sem penalizar a pessoa.
6. Perguntar facilidade de 1 a 5 e motivo; aplicar pergunta de compreensão após UT01.
7. Fazer pós-teste, agradecer, salvar registros anonimizados e verificar autorizações antes de compartilhar evidências.

**Materiais:** [perfil/pós-teste](../instrumentos/12_avaliacao/questionarios.md), [planilha de observação](../instrumentos/12_avaliacao/observacoes.csv) e fichas [U01](../instrumentos/14_observacao/u01.md), [U02](../instrumentos/14_observacao/u02.md), [U03](../instrumentos/14_observacao/u03.md).

### 7. Sessão remota e vídeo pedidos na aula

Para a atividade remota pedida pelo professor, abrir uma sala virtual por sessão e testar conexão, compartilhamento, zoom e áudio antes; mostrar apenas a janela do protótipo, silenciar notificações e combinar como interromper. Guardar interrupções técnicas separadamente do desempenho. O vídeo deve ilustrar instrução, uso e resultados, com IDs anônimos e acesso autorizado ao professor.

#### Recomendações da palestra e aplicação no projeto

| Tema e trecho indicado | Como vamos aplicar na Mesa de inspeção |
|---|---|
| Objetivos e formato do teste (7:42–8:42) | Usar UT01–UT03 para ver se a pessoa compara a imagem, prepara o parecer e se recupera de um erro. Fazer sessões moderadas para perguntar o que ela entendeu depois de cada tarefa. |
| Recrutamento (10:01; 34:32) | Priorizar pessoas externas com experiência relacionada às tarefas. Se for necessário usar um perfil aproximado, registrar a experiência que justifica a escolha e a limitação. |
| Preparação e plano B (15:34; 26:25) | Testar o link, a gravação e o compartilhamento no piloto. Ter uma segunda opção de chamada e registrar qualquer interrupção à parte. |
| Chamada, protótipo e anotações (18:51–25:06) | Abrir o Figma em uma chamada com compartilhamento de tela. Usar a ficha para anotar ação, dificuldade e tempo. Gravar somente com autorização. |

Fonte: [palestra de Felipe Melo indicada no Moodle](https://www.youtube.com/watch?v=zjKaHb6erzQ). Síntese baseada no resumo com marcações de tempo fornecido à equipe.

**Divisão prevista:** Kawan conduz U01, Gabriel conduz U02 e Alexandre conduz U03. Em cada sessão, o próximo integrante da sequência anota enquanto o outro confere a gravação autorizada e a preparação da próxima tarefa. A equipe reúne as fichas ao final e escolhe as melhorias que os registros sustentarem.

**Link do vídeo do teste:** [Vídeo demonstrativo do teste de usabilidade — Mesa de inspeção (Entrega 14)](https://www.youtube.com/watch?v=G2-ZTG27CLQ) *(YouTube não listado, acesso verificado sem login em 21/11/2026)*.

## C. Resultados por participante

As três sessões foram realizadas em 21/11/2026 sobre a mesma versão congelada `v1.1` do protótipo HTML (`assets/11_figma/prototipo/index.html`), com participantes proxy adultos externos à equipe e dados detalhados em [`observacoes.csv`](../instrumentos/12_avaliacao/observacoes.csv).

| Participante | Perfil (proxy externo) e condução | UT01 (tempo · sucesso · fac.) | UT02 (tempo · sucesso · fac.) | UT03 (tempo · sucesso · fac.) | Ficha individual |
|---|---|---|---|---|---|
| **U01** | Analista de controle de qualidade (inspeção visual de imagens técnicas) · Kawan | 84 s · Total · 5/5 (0 erros) | 152 s · Total · 4/5 (1 erro nav.) | 71 s · Total · 4/5 (0 erros) | [Ficha U01](../instrumentos/14_observacao/u01.md) |
| **U02** | Analista administrativo/auditoria documental (leitura de pareceres) · Gabriel | 118 s · Total · 4/5 (1 erro interp.) | 188 s · Total · 3/5 (2 erros) | 96 s · Total · 4/5 (1 erro recup.) | [Ficha U02](../instrumentos/14_observacao/u02.md) |
| **U03** | Técnico de logística e conferência de cargas (manifestos/relatórios) · Alexandre | 95 s · Total · 4/5 (0 erros) | 164 s · Total · 4/5 (1 erro nav.) | 82 s · Total · 5/5 (0 erros) | [Ficha U03](../instrumentos/14_observacao/u03.md) |

## D. Consolidação por tarefa

| Tarefa / meta | Taxa de sucesso | Tempo típico (mediana e faixa) | Erros / ajudas | Facilidade / satisfação (mediana) | Meta atendida? | Problemas prioritários |
|---|---|---|---|---|---|---|
| **UT01** / MU01–MU02 | **3/3** total sem ajuda · **3/3** distinguem indício de prova e de liberação | **95 s** (84–118 s) | 1 erro (interpretação) / 0 ajudas | **4/5** (4–5) | **Sim** (MU01 e MU02) | `AU02` (busca inicial por score), `AU05` (zoom em F05) |
| **UT02** / MU03–MU04 | **3/3** total sem ajuda (4 itens corretos no parecer) | **164 s** (152–188 s) | 4 erros (3 nav., 1 preenc.) / 0 ajudas | **4/5** (3–4) | **Sim** (MU03 e MU04; U02 passou 8 s do marco individual de 180 s) | `AU01` (ação de marcar na imagem/painel), `AU03` (destaque de `Editar`) |
| **UT03** / MU05 | **3/3** total (0 emissões incompletas; 3/3 recuperaram preservando dados) | **82 s** (71–96 s) | 1 erro (recuperação) / 0 ajudas | **4/5** (4–5) | **Sim** (MU05) | `AU04` (insegurança na preservação de dados em `F10d`) |

**MU06 (facilidade declarada em UT01 e UT02):** mediana **4/5** em UT01 (`5, 4, 4`) e **4/5** em UT02 (`4, 3, 4`), atendendo ao critério (mediana ≥ 4). Todos os participantes concluíram as tarefas dentro do limite de 5 minutos e sem intervenções do moderador.

## E. Achados e recomendações

| ID | Achado / tarefa | Evidência quantitativa e qualitativa | Impacto | Recomendação / artefato |
|---|---|---|---|---|
| **AU01** | Busca pela ação de marcar fora da barra superior (`UT02`) | **2/3** (`U01`, `U02`) clicaram primeiro na radiografia ou no bloco “Regiões marcadas” antes de achar `Marcar` na barra superior. *U01: “tentei clicar direto na imagem para marcar o ponto”.* | Médio — aumenta tempo inicial de registro em `UT02`. | Incluir botão de atalho `+ Marcar região` dentro do bloco “Regiões marcadas” no painel direito (`F03`–`F05`, Entrega 11). |
| **AU02** | Expectativa inicial por indicador numérico de confiança (`UT01`) | **1/3** (`U02`) procurou um percentual de certeza antes de ler o bloco qualitativo “Indício de atipicidade”; após a leitura, compreendeu corretamente os limites. | Baixo — não impediu sucesso, mas gerou hesitação inicial. | Manter classificação qualitativa (sem score sem calibração, `H31`/`H37`) e destacar o subtítulo explicativo de triagem em `F03`. |
| **AU03** | Baixa saliência da ação de edição no cartão da região (`UT02`) | **1/3** (`U02`) hesitou para editar o comentário antes de notar o link `Editar` no canto do cartão. | Médio — pode levar a excluir e refazer marcações desnecessariamente. | Dar estilo de botão/ação destacada a `Editar` e indicar visualmente que o campo de comentário é editável (`F06`/`F07`). |
| **AU04** | Insegurança sobre preservação dos dados na falha de exportação (`UT03`) | **1/3** (`U02`) clicou em `Voltar ao parecer` em `F10d` para conferir se os textos continuavam salvos antes de tentar novamente. | Baixo a médio — adiciona um passo extra na recuperação. | Reforçar a frase em `F10d` (*“Seus registros foram mantidos. Confira a pasta e clique em Tentar novamente.”*) e reforçar hierarquia visual do botão primário. |
| **AU05** | Tamanho reduzido das radiografias no modo lado a lado (`UT01`/`UT02`) | **1/3** (`U03`) relatou no pós-teste que as imagens em `F05` ficam pequenas para inspecionar detalhes finos sem zoom sincronizado. | Baixo na tarefa simulada; médio em operação real. | Prever zoom e pan sincronizados entre os dois painéis de `F05` na implementação da interface do TCC. |

## F. Comparação com a heurística

| Achado heurístico (Entrega 13) | Situação antes das sessões | Evidência observada com `U01`–`U03` |
|---|---|---|
| `V01` · conclusão trocada após `F11b` | **Corrigido na v1.1** (`F07b`/`F08b`). | Bloqueio eliminado antes das sessões; fluxo de conclusão seguiu sem inversões. |
| `V02` · recuperação em `F10c` presa à faixa roxa | **Corrigido na v1.1** (campos clicáveis + `F10c_ut03`). | **3/3** recuperaram o campo `Responsável` diretamente pela interface em `UT03` (mediana 82 s). |
| `V03` · perda da conclusão em `F11a` | **Corrigido na v1.1** (`F11a → F07`). | Sem perda de dados nas sessões. |
| `V04` · códigos `S01`–`S18` visíveis nos rótulos | **Corrigido na v1.1** (rótulos limpos). | Nenhum participante relatou estranhamento com códigos acadêmicos na tela ou no PDF `F12`. |
| `V05` · botão `Restaurar ajustes` e zoom em `F05` | **Parcial na v1.1** (botão incluído; zoom em `F05` no backlog). | `U03` encontrou `Restaurar ajustes` após procurar no rodapé e corroborou a necessidade de zoom sincronizado em `F05` (`AU05`). |
| `V06`/`V07` · corte em `F10c` e contraste do tracejado | **Corrigidos na v1.1**. | `U02` (em 1440×900) leu normalmente `F10c`; `U01` e `U03` elogiaram a visibilidade do contorno duplo. |
| `V09` · edição do comentário em `F06`/`F07` | **Parcial na v1.1** (link `Editar` adicionado). | `U02` ainda hesitou para perceber o link (`AU03`), indicando necessidade de maior destaque visual. |
| *(Novo na observação)* `AU01`, `AU02`, `AU04` | **Não previstos na inspeção heurística.** | Surgiram apenas na interação observada: clique direto na imagem/painel para marcar (`AU01`), busca por score (`AU02`) e verificação de dados após `F10d` (`AU04`). |

## G. Conclusão e pendências reais

As seis metas de usabilidade (`MU01`–`MU06`) definidas na [Entrega 8](08_engenharia_usabilidade.md) foram atingidas na amostra de três participantes proxy externos sobre a versão `v1.1` da Mesa de inspeção: **3/3** compararam original e mapa sem ajuda e compreenderam os limites do apoio automático (`MU01`/`MU02`), **3/3** emitiram o parecer completo com mediana de **164 s** (`MU03`/`MU04`), **3/3** recuperaram omissão e falha de exportação sem perda de dados (`MU05`) e avaliaram a facilidade com mediana **4/5** (`MU06`).

O ciclo iterativo ficou evidente na prática: a inspeção heurística (Entrega 13) eliminou os bloqueios graves (`V01` e `V02`) e ruídos de linguagem (`V04`) antes do teste, enquanto a observação revelou comportamentos espontâneos que a inspeção não havia antecipado — principalmente a expectativa de iniciar a marcação clicando direto na imagem ou no bloco de regiões (`AU01`). Como prioridades concretas de melhoria para a próxima iteração ficam: (1) atalho `+ Marcar região` no painel direito (`AU01`), (2) destaque visual do botão `Editar` no cartão da região (`AU03`), (3) reforço textual/visual da preservação de dados em `F10d` (`AU04`) e (4) zoom sincronizado em `F05` (`AU05`).

**Limitações registradas:** a amostra tem apenas três participantes proxy (não operadores aduaneiros da RFB/recintos), o ambiente e as falhas são simulados no protótipo HTML `v1.1` e não há integração com backend institucional. Os resultados avaliam exclusivamente a compreensão e a usabilidade da interface da disciplina, sem validar o desempenho científico do modelo do TCC nem a rotina real de despacho. O protótipo no Figma e o vídeo demonstrativo do teste estão acessíveis pelos links verificados neste relatório e na [Entrega 11](11_figma.md).

## Checklist

- [x] Fluxograma, preparação, tarefas e protocolo documentados.
- [x] Três vagas externas e responsabilidades definidas.
- [x] Alternativa de proxies e suas limitações explicitadas previamente.
- [x] Avaliação de interação separada da avaliação técnica do TCC.
- [x] Instrumentos, critérios, anonimização e autorização de gravação preparados.
- [x] Protótipo navegável (`v1.1` HTML) e inspeções concluídos antes da aplicação.
- [x] Três participantes externos (`U01`–`U03`, proxies justificados) consentidos e anonimizados.
- [x] Piloto realizado e alterações registradas.
- [x] Sessões observadas sem ensino do caminho, com métricas por pessoa/tarefa.
- [x] Recomendações da palestra incorporadas ao protocolo a partir do resumo fornecido.
- [x] Vídeo autorizado do teste disponível ao professor. *(Publicado em YouTube não listado e linkado na seção B.7.)*
- [x] Consolidação, comparação com heurística e conclusão sustentadas por dados.
- [x] Achados geraram recomendações e atualização da rastreabilidade.

**Referências:** aula 14, *Teste de Usabilidade com Observação do Usuário*, págs. 4–16; *Plano de Avaliação de Usabilidade com Observação*, págs. 2–6; modelo de consentimento 01; atividade remota no conteúdo do tópico. Cópias locais em `FEI_CC8122_IHC/14 - Tópico 14/`.

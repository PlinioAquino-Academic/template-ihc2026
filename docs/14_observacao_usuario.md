# Entrega 14 — Avaliação de usabilidade por observação de usuários

**Data do relatório:** 18/11/2026.  
**Status:** 🟨 em andamento — resultados de U01 informados por Gabriel e analisados; U02 e consolidação final pendentes.  
**Responsabilidade:** solução consolidada por equipe, com dois participantes finais externos à equipe.

## Objetivo da atividade

Observar participantes realizando tarefas representativas para avaliar eficácia, eficiência, compreensão e satisfação. O objeto é a interação com o protótipo Figma da Entrega 11, e não o desempenho científico do algoritmo ou do SUMO.

**Origem dos registros:** os resultados, o perfil, a concordância, o piloto e as respostas de U01 foram fornecidos por Gabriel e declarados por ele como correspondentes a uma sessão real. Este relatório organiza esse relato; não constitui verificação independente da coleta. Os valores demonstrativos do próprio Figma continuam fictícios e são distintos das medidas de interação informadas pelo moderador.

U01 é um participante aproximado (*proxy*), sem experiência profissional em controle de tráfego. Essa condição limita as conclusões sobre as personas profissionais do projeto. Integrantes da equipe não integram a amostra final.

## A. Fluxograma do processo — equipe

![Fluxograma da avaliação observacional](../assets/14_testes/fluxograma_avaliacao.svg)

O processo compreende: planejamento e definição da versão → recrutamento → consentimento → preparação e piloto → tarefas e observação → pós-teste → análise → recomendações.

A sessão de U01 e o piloto foram informados como realizados. A etapa de U02 e a consolidação final permanecem pendentes. O arquivo SVG deve ser adicionado ou substituído manualmente pelo fluxograma real; este relatório não comprova que o artefato gráfico foi finalizado.

## B. Procedimento de preparação e execução — equipe

### Passo 1 — Objetivos e versão avaliada

**Interface:** Figma da Entrega 11, fluxos M01 e M02.  
**Data informada para a sessão de U01:** 18/11/2026.

- [Arquivo editável](https://www.figma.com/design/YJJhBTujdrsjDY113Iefj4/Sem-t%C3%ADtulo?node-id=4-12).
- [M01 — configuração e execução](https://www.figma.com/proto/YJJhBTujdrsjDY113Iefj4/Sem-t%C3%ADtulo?node-id=4-12&scaling=scale-down-width&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=4%3A12).
- [M02 — histórico e resultados](https://www.figma.com/proto/YJJhBTujdrsjDY113Iefj4/Sem-t%C3%ADtulo?node-id=16-206&scaling=scale-down-width&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=16%3A206).

Na UT03, o estado Executando foi apresentado de forma estável, conforme o ajuste de preparação informado pelo moderador. O resultado dessa tarefa avalia o reconhecimento do estado nessa condição e não demonstra que as transições automáticas originais tenham duração adequada.

Não foi fornecido identificador de revisão histórica do Figma nem um registro de correções HC01–HC07. Não se presume que esses problemas tenham sido corrigidos.

| Meta | Critério previsto | Fonte |
|---|---|---|
| MU01 | 100% preparam a configuração sem ajuda direta. | UT01 |
| MU02 | 100% identificam a ação correta de recuperação. | UT02 |
| MU03 | Mediana de preparação de até 5 minutos. | UT01 |
| MU04 | 100% reconhecem estado e controlador. | UT03 |
| MU05 | 100% identificam registro e condições solicitadas. | UT04 |
| MU06 | Mediana de localização de até 3 minutos. | UT04 |
| MU07 | Mediana de facilidade de pelo menos 4/5. | Pós-tarefa |
| MU08 | 100% compreendem consulta individual e comparação externa. | UT05 e pós-teste |

As metas são referentes à amostra prevista. Resultados de U01 serão apresentados individualmente, sem considerar U02 como sucesso, falha ou zero antes de receber sua sessão.

R2-001 mostra 28 s e R2-002 mostra 36 s de espera média. Esses valores pertencem à demonstração do Figma e não são resultados reais de desempenho do algoritmo.

A exploração da aplicação funcional R3 em 15/11 permanece separada: não foi utilizada para preencher tempos, erros ou satisfação desta sessão padronizada.

### Passo 2 — Participantes

| ID | Perfil e adequação | Responsável | Situação |
|---|---|---|---|
| U01 | Conhecimento básico do conceito de simulação, sem prática com SUMO; familiaridade com tabelas, gráficos de barras e indicadores; conhecimento básico de mobilidade urbana. Proxy com familiaridade parcial com análise, sem experiência profissional em controle de tráfego. | Gabriel Koiama de Rocha Lira — 22.125.067-3. | Sessão e resultados informados como reais pelo moderador. |
| U02 | Perfil a registrar por João. | João Pedro Lopes Santana Villas Bôas — 22.125.065-7. | Pendente. |

A familiaridade de U01 com gráficos fundamenta sua participação como perfil aproximado, sem torná-lo equivalente a um especialista. O relato não detalha seu uso anterior da aplicação ou do Figma; esse fator não será presumido ao interpretar os tempos.

### Passo 3 — Consentimento, ambiente e privacidade

- **Instrumento:** [termo e procedimento de consentimento](../instrumentos/termo_consentimento_modelo.md).
- **Aceite de U01:** concordância voluntária antes da sessão, conforme informação do moderador. A forma documental do aceite não foi especificada no material recebido.
- **Registros utilizados:** tabela de tarefas, descrições das ocorrências e respostas pós-teste fornecidas por Gabriel. Nenhuma gravação foi disponibilizada para esta análise.
- **Identificação pública:** U01 e U02.
- **Ambiente e dispositivo:** o relato identifica a interface Figma, mas não especifica local, equipamento, resolução, escala ou horário da sessão. Esses dados não foram deduzidos da exploração de 15/11.
- **Guarda prevista:** registros sob responsabilidade de Gabriel, separados de dados identificáveis e de eventuais termos de consentimento. A preservação dos arquivos técnicos do TCC não equivale à divulgação dos dados pessoais da avaliação.

### Passo 4 — Teste piloto

**Situação informada:** realizado antes da sessão de U01.  
**Responsável pelo relato:** Gabriel.  
**Data, executor e ambiente específicos do piloto:** não discriminados no registro fornecido.

| Verificação informada | Registro |
|---|---|
| Links M01 e M02 | Abertura correta. |
| UT02 | Configuração com seed ausente preparada. |
| UT03 | Estado Executando apresentado de forma estável para permitir a pergunta. |
| Instrumentação | Cronômetro e planilha conferidos. |
| Instruções | Mantidas padronizadas. |

**Ajuste informado:** apresentar diretamente o quadro Executando durante UT03 para evitar que a transição automática impedisse a observação. Esse procedimento deve ser identificado também na sessão de U02, para permitir comparação entre condições equivalentes.

O piloto não é contado na amostra final. A exploração de 15/11 não foi reclassificada como piloto.

### Passo 5 — Tarefas padronizadas

As instruções abaixo são as da Entrega 12 e do instrumento `roteiro_teste_usabilidade.md`. **O participante recebe apenas o enunciado**, não o critério de sucesso nem os caminhos esperados.

| ID | Instrução apresentada | Critério de sucesso do observador | Métricas | Rastreabilidade |
|---|---|---|---|---|
| UT01 | Prepare um experimento para Regional São Paulo, usando o controlador híbrido, seed 42 e execução sem abrir a janela gráfica do simulador. Confira as condições antes de iniciar. | Chegar ao resumo com cenário R2, controlador híbrido, seed 42 e modo Headless. | Sucesso, tempo até o resumo, erros, ajudas e facilidade. | T01–T03; OBJ02–OBJ03; M01; F01–F03. |
| UT02 | Um colega preparou uma configuração. Ao tentar deixá-la pronta para execução, você encontra um problema. Descubra o que precisa corrigir. | Identificar a seed ausente, recuperar 42 e validar novamente. | Sucesso, tempo, erros, ajudas e facilidade. | T02/T04; OBJ03; M01; F02/F02E/F03. |
| UT03 | O experimento já foi confirmado. Diga em que estado se encontra e qual estratégia está sendo usada. | Identificar o estado mostrado e o controlador. | Acerto, tempo de resposta, ajudas, facilidade e eventual interferência de transição. | T05; OBJ04; M01; F04/F04P/F05. |
| UT04 | Encontre R2-001 e identifique seu cenário, sua estratégia e sua seed. | Abrir R2-001 e informar Regional São Paulo, híbrido e seed 42. | Sucesso, tempo de localização, erros, ajudas e facilidade. | T06; OBJ06; M02; F07/F08. |
| UT05 | Compare o tempo médio de espera de R2-001 e R2-002. Explique quais condições precisam ser conferidas antes de interpretar a diferença. | Identificar 28 s e 36 s nos registros corretos, conferir condições e explicar a reunião externa dos valores. | Sucesso, valores e explicação, tempo, erros, ajudas e facilidade. | T06–T08; OBJ07–OBJ09; M02; F07/F08/F08B/F09/F09B. |
| UT06 | Consulte R2-003. Se encontrar um impedimento, explique o que aconteceu e continue com outro registro. | Reconhecer a indisponibilidade, retornar ao histórico e abrir outro resultado. | Sucesso, tempo, erros, ajudas e facilidade. | T06; OBJ06; M02; F07/F08E/F08. |

**Critérios de classificação e registro:**

- **Sucesso total:** critério cumprido sem orientação sobre a solução.
- **Sucesso parcial:** critério parcialmente cumprido ou conclusão após ajuda direta.
- **Falha:** critério não atingido, resposta incorreta ou abandono.
- **Erro:** ação que afasta o participante do objetivo ou exige correção; registrar o tipo e o contexto.
- **Ajuda direta:** intervenção do moderador indicando como resolver. A simples repetição do enunciado será registrada separadamente.
- **Tempo:** iniciar após a leitura da instrução e encerrar ao atingir o critério ou terminar a tentativa. Em UT01, parar na revisão do resumo; em UT04, medir o tempo de localização até abrir o registro, registrando separadamente o acerto das condições.
- **Facilidade percebida:** 1 = muito difícil; 2 = difícil; 3 = nem fácil nem difícil; 4 = fácil; 5 = muito fácil.
- **Limites:** não impor tempo-limite; comparar os registros com as metas apenas na análise posterior.

### Passo 6 — Condução de U01 — Gabriel

O registro fornecido identifica Gabriel como moderador. Foram informados resultados por tarefa e respostas pós-teste. O procedimento de referência utiliza os [enunciados padronizados](../instrumentos/roteiro_teste_usabilidade.md) e a [planilha de observação](../instrumentos/planilha_observacao_modelo.md).

A classificação distingue erros corrigidos espontaneamente de ajuda direta. Em UT02, houve uma intervenção orientando o participante a examinar os campos obrigatórios; por isso, a conclusão foi classificada como parcial.

Não foram fornecidos horários de início e fim nem fichas originais separadas. Os tempos abaixo são as durações informadas. Em UT04, o tempo exclusivo até abrir o registro não foi separado do restante da tarefa no material recebido.

## C. Resultados — por participante

### U01 — Participante proxy sob responsabilidade de Gabriel

**Data informada:** 18/11/2026.  
**Moderador:** Gabriel Koiama de Rocha Lira — 22.125.067-3.  
**Interface:** Figma da Entrega 11; M01 e M02.  
**Consentimento:** concordância voluntária prévia, conforme relato do moderador.  
**Situação:** seis resultados e respostas pós-teste registrados a partir dos dados fornecidos.

| Tarefa | Grau de sucesso | Erros | Dificuldade ou ocorrência | Ajudas | Tempo | Facilidade | Evidência/observação |
|---|---|---:|---|---:|---|---:|---|
| UT01 | Total | 1 | Escolheu Visual inicialmente e corrigiu para Headless sem ajuda. | 0 | 02:42 | 4/5 | Resumo com R2, híbrido, seed 42 e Headless. |
| UT02 | Parcial | 1 | Procurou o problema nas opções do controlador antes de identificar a seed ausente. | 1 | 01:42 | 3/5 | Após orientação para examinar os campos obrigatórios, recuperou 42 e validou novamente. |
| UT03 | Total | 0 | Nenhuma dificuldade relatada na condição de apresentação estável. | 0 | 00:12 | 5/5 | Identificou Executando e o controlador híbrido. |
| UT04 | Total | 1 | Abriu R2-002 e corrigiu a seleção espontaneamente. | 0 | 01:34 | 4/5 | Abriu R2-001 e identificou cenário, controlador e seed. |
| UT05 | Parcial | 1 | Interpretou inicialmente o menor tempo como melhor desempenho antes de conferir as condições; não completou a explicação da reunião externa durante a tarefa. | 0 | 02:36 | 3/5 | Identificou corretamente 28 s e 36 s; a explicação mais completa surgiu no pós-teste. |
| UT06 | Total | 0 | Nenhuma dificuldade relatada na recuperação. | 0 | 01:15 | 4/5 | Reconheceu o aviso de indisponibilidade, voltou ao histórico e abriu outro resultado. |

#### Detalhamento das ocorrências

- **UT01:** o erro foi corrigido espontaneamente antes da confirmação. A existência de um erro corrigido não impede sucesso total, pois o critério foi atingido sem ajuda direta.
- **UT02:** a configuração inválida foi o estado inicial previsto. O erro contabilizado corresponde à investigação inicial do controlador; a necessidade de ajuda explica a classificação parcial.
- **UT03:** a condição estável permite avaliar identificação, mas limita conclusões sobre percepção de estados durante a execução temporizada original.
- **UT04:** a seleção incorreta foi recuperada sem ajuda. O registro de 01:34 não discrimina separadamente o momento de abertura de R2-001.
- **UT05:** sucesso parcial foi preservado para a execução da tarefa. A resposta posterior mais completa foi registrada separadamente e não altera retroativamente o desempenho observado.
- **UT06:** a recuperação foi concluída. Não foi informada a percepção do participante sobre o status de R2-003 antes da abertura.

#### Pós-teste

**Em qual momento foi mais difícil decidir como prosseguir?**

> Na parte de comparar os resultados. Eu conseguia encontrar os valores, mas fiquei em dúvida sobre quais informações precisava conferir para comparar as simulações corretamente.

**Que informação teria ajudado?**

> Uma explicação mais clara das métricas e uma escala numérica nos gráficos ajudariam a entender melhor os resultados.

**Como reuniria as informações para comparar duas execuções?**

> Eu consultaria cada execução no histórico, anotaria os valores e as condições do experimento e organizaria tudo em uma tabela para comparar depois.

As falas foram transcritas conforme o texto fornecido pelo moderador; não foram confrontadas com gravação.

#### Síntese individual

| Indicador | U01 |
|---|---|
| Sucesso total | 4/6 tarefas — 66,7%. |
| Sucesso parcial | 2/6 tarefas — 33,3%. |
| Falhas | 0/6 tarefas. |
| Erros | 4 ocorrências informadas. |
| Ajudas diretas | 1, em UT02. |
| Facilidade por tarefa | 4, 3, 5, 4, 3 e 4. |
| Mediana das seis notas de U01 | 4/5. |
| Menor facilidade | UT02 e UT05, ambas com 3/5. |

Essas proporções descrevem tarefas de um participante. Não equivalem à proporção de participantes que atende a cada meta na amostra completa. A mediana das seis notas de U01 também não substitui a análise por tarefa com os dois participantes.

### U02 — Participante sob responsabilidade de João Pedro

**Situação:** perfil, consentimento, sessão e resultados ainda não registrados nesta versão.

| Tarefa | Grau de sucesso | Erros | Dificuldades | Ajudas | Tempo | Facilidade | Observação |
|---|---|---:|---|---:|---|---|---|
| UT01 | N/D | N/D | N/D | N/D | N/D | N/D | Pendente. |
| UT02 | N/D | N/D | N/D | N/D | N/D | N/D | Pendente. |
| UT03 | N/D | N/D | N/D | N/D | N/D | N/D | Pendente. |
| UT04 | N/D | N/D | N/D | N/D | N/D | N/D | Pendente. |
| UT05 | N/D | N/D | N/D | N/D | N/D | N/D | Pendente. |
| UT06 | N/D | N/D | N/D | N/D | N/D | N/D | Pendente. |

N/D significa não disponível; não é tratado como zero ou falha.

## D. Consolidação por tarefa — equipe

### Parcial disponível: apenas U01

| Tarefa | Sucesso total observado | Tempo informado de U01 | Erros | Facilidade | Leitura individual |
|---|---|---|---:|---:|---|
| UT01 | 1/1 | 02:42 | 1 | 4/5 | Concluiu sem ajuda, em tempo inferior a 5 minutos. |
| UT02 | 0/1; 1 parcial | 01:42 | 1 | 3/5 | Recuperação concluída com uma ajuda direta. |
| UT03 | 1/1 | 00:12 | 0 | 5/5 | Reconhecimento correto em estado apresentado de forma estável. |
| UT04 | 1/1 | 01:34 | 1 | 4/5 | Registro e condições corretos; tempo exclusivo de localização não discriminado. |
| UT05 | 0/1; 1 parcial | 02:36 | 1 | 3/5 | Valores corretos; explicação incompleta durante a tarefa e mais completa no pós-teste. |
| UT06 | 1/1 | 01:15 | 0 | 4/5 | Recuperação da consulta concluída sem ajuda. |

O denominador 1 representa somente os dados disponíveis de U01. A consolidação final com N = 2 aguarda U02.

### Comparação preliminar com as metas

| Meta | Evidência de U01 | Situação da análise |
|---|---|---|
| MU01 | UT01 total, sem ajuda. | Critério individual demonstrado; amostra completa pendente. |
| MU02 | UT02 parcial, com ajuda direta. | Recuperação realizada, sem demonstração de identificação autônoma. |
| MU03 | UT01 em 02:42. | Tempo individual inferior a 5 min; mediana final depende de U02. |
| MU04 | Estado e controlador corretos. | Demonstrado apenas na condição estável da UT03. |
| MU05 | Registro, cenário, controlador e seed corretos. | Critério individual demonstrado; amostra completa pendente. |
| MU06 | UT04 em 01:34; marco exclusivo de localização não separado. | Precisão da medida de localização limitada; mediana final pendente. |
| MU07 | Mediana individual 4/5; UT02 e UT05 com 3/5. | Apresentar notas por tarefa; análise conjunta depende de U02. |
| MU08 | Explicação incompleta durante UT05; resposta pós-teste descreve consulta, anotações e tabela externa. | Evidências distintas por momento; manter sucesso parcial da tarefa e explicitar a resposta posterior. |

Não se declara atendimento global de MU01–MU08 com a amostra incompleta.

## E. Achados e recomendações — contribuição de U01

| ID | Achado | Evidência informada | Impacto | Recomendação | Artefatos |
|---|---|---|---|---|---|
| AU01 | Escolha inicial de modo incompatível com a tarefa. | UT01: 1 erro, 0 ajudas; correção espontânea antes do resumo. | Exige revisão da escolha, sem impedir a conclusão. | Conferir a clareza da distinção Visual/Headless e preservar a revisão antes de iniciar. | F02/F03; signos de modo; M01. |
| AU02 | Dificuldade para localizar a causa da configuração inválida. | UT02: 1 erro, 1 ajuda, sucesso parcial e facilidade 3/5. | Recuperação dependeu de intervenção. | Reforçar a associação entre a mensagem e o campo seed; verificar o comportamento com outro participante. | F02E; signo de validação; M01. |
| AU03 | Seleção inicial do registro incorreto. | UT04: abriu R2-002 antes de R2-001; corrigiu sem ajuda. | Acrescenta navegação, sem impedir a consulta. | Verificar a diferenciação visual dos identificadores e das condições na lista. Não concluir que um único erro prove uma causa de interface. | F07; M02. |
| AU04 | Comparação exigiu maior compreensão do protocolo experimental. | UT05: sucesso parcial, 1 erro, facilidade 3/5; pós-teste apontou dúvida sobre condições de comparação. | A leitura dos números não garantiu interpretação completa durante a tarefa. | Oferecer orientação contextual sobre condições relevantes e sobre a reunião externa dos dados, preservando os limites do protótipo. | F08/F08B; M02; CI02. |
| AU05 | Participante solicitou explicações de métricas e escala numérica. | Comentário de pós-teste; sem medida isolada do efeito da escala durante a tarefa. | Oportunidade de melhorar interpretação, sem estimar impacto causal com este relato. | Explicar indicadores e completar a escala dos gráficos; verificar o efeito em nova observação. | F08/F08B/F09/F09B; signos de métricas. |

Os achados descrevem um único participante. A recorrência entre pessoas só poderá ser examinada após U02.

## F. Comparação com a avaliação heurística — parcial U01

| Heurística consolidada | Evidência disponível de U01 | Conclusão permitida |
|---|---|---|
| HC01 — status de R2-003 | Reconheceu indisponibilidade depois de abrir e recuperou a consulta. | Recuperação bem-sucedida; não há registro suficiente sobre percepção do status na lista. |
| HC02 — identidade inconsistente | Não foram informadas conclusões alternativas de controlador/modo. | Não exercitado no caminho relatado. |
| HC03 — diagnóstico de falha de processamento | UT02 utilizou validação da seed, não F04E. | Não exercitado; a dificuldade de UT02 não confirma HC03. |
| HC04 — gráficos sem escala | Escala numérica mencionada no pós-teste como ajuda desejada. | Comentário relacionado ao problema, sem demonstração isolada de seu efeito na execução. |
| HC05 — Projeção regional | Nenhuma passagem pela configuração avançada foi descrita. | Não exercitado no relato. |
| HC06 — acesso ao histórico nas alternativas | As alternativas de conclusão correspondentes não foram informadas. | Não exercitado no caminho relatado. |
| HC07 — definição de Throughput | Houve pedido geral por explicação de métricas, sem menção específica ao indicador. | Não confirma especificamente HC07; requer investigação. |

Uma tarefa bem-sucedida não comprova ausência de violação. Ausência de comentário não significa correção do problema.

## G. Conclusão — contribuição de Gabriel

Segundo os resultados informados pelo moderador, U01 concluiu quatro tarefas integralmente e duas parcialmente, sem falhas. Houve quatro erros, uma ajuda direta e mediana individual de facilidade de 4/5.

UT02 e UT05 receberam as menores notas, 3/5. Em UT02, a recuperação exigiu orientação do moderador. Na UT05, o participante identificou os valores, mas apresentou explicação incompleta durante a tarefa; no pós-teste, descreveu uma forma de reunir os dados externamente. Os dois momentos foram mantidos separados na análise.

As prioridades sustentadas por esse relato são melhorar a associação da validação ao campo correspondente, apoiar a interpretação das condições experimentais e avaliar explicações de métricas e escala gráfica.

A análise é limitada a um participante proxy, à apresentação estável da UT03, à falta de separação do tempo de localização em UT04 e ao registro fornecido pelo moderador. A familiaridade prévia, o equipamento e a revisão histórica exata do Figma não foram detalhados. Não são feitas generalizações sobre profissionais de mobilidade nem sobre o desempenho científico do TCC.

**Consolidação final da equipe:** aguarda os dados de U02, a comparação dos resultados por tarefa, a atualização da rastreabilidade e o registro das decisões finais de melhoria.

## Checklist

- [x] Fluxos, objetivos, tarefas e critérios estão documentados.
- [x] A avaliação da interação foi distinguida da avaliação científica do TCC.
- [x] U01 foi identificado como proxy e sua limitação foi registrada.
- [x] Piloto e ajuste da UT03 foram registrados conforme relato do moderador.
- [x] A concordância de U01 foi relatada como obtida antes da sessão.
- [x] Os seis resultados de U01 possuem sucesso, erros, ajudas, tempo e facilidade informados.
- [x] As respostas pós-teste de U01 foram registradas.
- [x] A análise de U01 diferencia desempenho durante a tarefa e resposta posterior.
- [x] Os achados foram relacionados à avaliação heurística sem presumir confirmações.
- [ ] Detalhes documentais do aceite, do piloto, do dispositivo e da revisão do Figma foram completados.
- [ ] O fluxograma SVG real foi conferido no repositório.
- [ ] João registrou perfil, consentimento, sessão e resultados de U02.
- [ ] Os dois participantes finais e a consolidação por tarefa atendem ao enunciado.
- [ ] A conclusão da equipe e a comparação final com MU01–MU08 foram concluídas.
- [ ] A rastreabilidade e os documentos de controle foram atualizados.



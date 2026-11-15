# Entrega 8 — Ciclo de vida e engenharia de usabilidade

**Data:** 15/11/2026  
**Status:** 🟩 concluída  
**Responsabilidade:** 1 solução por equipe

## Objetivo da atividade

Transformar o conhecimento acumulado sobre usuários, tarefas, plataforma e contexto em princípios e **metas de usabilidade verificáveis**, mantendo o caráter iterativo do projeto.

## Delimitação do sistema interativo

Antes das características da plataforma, separe:

| Camada | O que pertence ao projeto | O que será avaliado em IHC |
|---|---|---|
| contribuição técnica do TCC | modelo | desempenho técnico não é substituído pelo teste de IHC |
| camada de interação da disciplina | interface | compreensão, eficácia, eficiência, satisfação, erros, acessibilidade etc. |
| integrações/dados simulados | base de dados anonimizados de pacientes, disponibilizada no [Kaggle](https://www.kaggle.com/datasets/hadighahroudi/ct-kidney-dataset-normal-cyst-tumor-and-stone/data) | se o resultado gerado é compreensível; |

Em um protótipo de disciplina, é aceitável simular processamento ou resultados quando a implementação técnica não estiver integrada, desde que isso seja declarado e a simulação seja suficiente para avaliar a interação.

## 1. Características da plataforma

| Característica | Descrição | Consequência para IHC |
|---|---|---|
| Software | Protótipo Web local do TCC: interface HTML/CSS/JavaScript, API FastAPI/Python e modelo DT-DNN em TensorFlow; exames e pacientes são carregados de arquivos locais, sem integração demonstrada com prontuário institucional. | Avaliar separadamente a compreensão da interface e a resposta do modelo; explicitar ao participante quais dados e funções são de demonstração. |
| Hardware/dispositivos | A interface é acessada em navegador; o servidor local carrega os modelos e processa volumes de imagens. Não há especificação comprovada de GPU, estação clínica ou monitor de diagnóstico; o CSS inclui adaptação para telas menores. | Testar legibilidade das fatias, do mapa e dos textos no dispositivo efetivamente usado; não presumir adequação para interpretação diagnóstica nem desempenho idêntico em outros equipamentos. |
| Capacidades | O protótipo permite buscar e selecionar paciente por nome/CPF ou prontuário, confirmar dados e iniciar análise de tomografia vinculada; apresenta classe prevista, percentual exibido como confiança, comparação animada com GradCAM, laudo sugerido e histórico local. | Verificar se o profissional identifica o exame correto e distingue previsão, confiança, visualização e texto sugerido de uma conclusão clínica; testar a utilidade desses elementos (H01, H03, H06). |
| Restrições | A análise usa imagens previamente associadas ao paciente no conjunto local, checkpoints treinados e um número configurável de fatias; não há envio de exame pela interface nem integração DICOM/PACS demonstrada. O laudo é montado de textos predefinidos por classe. | Não instruir o participante a fazer upload ou inferir que o laudo descreve achados verificados individualmente; declarar as limitações e validar se seleção de paciente representa o fluxo real (H02). |
| Conectividade/latência | A demonstração inicia por padrão em `127.0.0.1:8000`; o navegador consulta a API local e carrega o GIF de resultado por requisições HTTP. Não há suporte offline independente do servidor nem latência de rede institucional medida. | Sinalizar carregamento e falhas de comunicação; medir espera no ambiente do teste sem extrapolar para uso remoto ou institucional. |
| Segurança/privacidade | A API lê cadastro de pacientes de arquivo JSON local e devolve seus dados ao navegador; cada análise grava histórico no JSON e GIF em disco. Não há autenticação, autorização por papel ou proteção de dados demonstrada no protótipo. | Usar somente dados fictícios ou devidamente anonimizados nas avaliações; não expor a aplicação com dados de pacientes reais nem tratar a demonstração como pronta para uso clínico. |
| Volume de dados/histórico | A interface lista pacientes e análises e permite consultar o histórico registrado no JSON; a busca ocorre no navegador e não há paginação ou limite de registros implementado. Volume e necessidade real de histórico não foram validados (H07). | Avaliar se localizar exames anteriores é uma tarefa pertinente; caso confirmado, testar busca, filtros e legibilidade com quantidade representativa antes de especificar paginação. |
| Tempo de processamento | A requisição de análise carrega imagens, executa o modelo e o GradCAM, gera um GIF e só então devolve o resultado; durante a espera o botão é desabilitado e aparece uma mensagem textual. O walkthrough do TCC relata cerca de 9 s em uma demonstração, não um tempo garantido. | Tornar o estado de processamento perceptível, diferenciar erro de espera e avaliar necessidade de cancelamento ou retomada; medir a duração no ambiente do teste sem confundi-la com tempo de decisão clínica. |
| Papéis/permissões | A interface mostra um médico fictício, mas não implementa login nem perfis de acesso; não há confirmação de quem deve selecionar exames, executar análises ou ler resultados na rotina real (H02). | Investigar responsabilidades antes de projetar permissões; no teste, explicar o papel simulado e impedir que a aparência de um perfil médico seja tomada como controle de acesso real. |

## 2. Princípios gerais do projeto

Inclua apenas normas, leis, padrões e princípios realmente relevantes, explicando **como** afetam o projeto. Não transforme esta seção em lista de links.

| Princípio/norma | Aplicabilidade ao contexto | Decisão/requisito decorrente | Fonte |
|---|---|---|---|
| Contexto de uso | O recorte propõe que um nefrologista consulte a classificação de uma tomografia renal; perfil, papéis, fluxo de acesso e ambiente de trabalho ainda precisam ser confirmados (H02, H05). | Investigar com profissionais quem acessa o exame, em que etapa consulta a indicação, quais informações utiliza e sob quais condições trabalha antes de fixar requisitos de interação. | Entregas 1/2/3; [ISO 9241-11](https://www.iso.org/standard/63500.html) |
| Design centrado no ser humano | A interface proposta para apoiar a avaliação de T01 ainda não foi validada com seus possíveis usuários; compreender o contexto não substitui testar as soluções desenhadas. | Envolver profissionais na revisão de fluxos e protótipos, observar a execução de T01 e iterar as telas conforme dificuldades de compreensão, erros e necessidades identificadas. | [ISO 9241-210](https://www.iso.org/standard/52075.html); Entregas 3/5 |
| LGPD e minimização de dados | Tomografias e informações sobre pacientes podem conter dados pessoais sensíveis de saúde; mesmo um protótipo não deve expor dados reais sem base legal e salvaguardas adequadas. | Usar casos fictícios ou anonimizados nos testes; se houver tratamento real, definir base legal aplicável, finalidade, acesso por papel, proteção e retenção com orientação institucional antes da coleta. | [Lei nº 13.709/2018 (LGPD)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm), arts. 5º, II, 6º e 11 |
| Acessibilidade da interface | Profissionais podem ter necessidades distintas de percepção e interação; rótulos, alertas e resultados não devem depender apenas de cor ou da precisão do mouse. | Se a interface for Web, prever contraste, navegação por teclado, foco visível e textos compreensíveis para estados e erros; verificar os critérios pertinentes no protótipo. | [WCAG 2.2 (W3C)](https://www.w3.org/TR/WCAG22/); [ISO 9241-210](https://www.iso.org/standard/52075.html) |
| Segurança de uso e prevenção de erros | Associar a indicação ao exame errado ou interpretar a saída do modelo como diagnóstico final pode afetar a avaliação proposta (H03). | Exibir contexto suficiente para confirmar o exame, diferenciar visual e textualmente indicação automatizada de conclusão clínica e oferecer feedback inequívoco em falhas ou ausência de resultado; avaliar essas interações com usuários. | [IEC 62366-1](https://www.iso.org/standard/63179.html) (engenharia de usabilidade de dispositivos médicos); Entregas 1/3/5 |
| Gestão de riscos relacionados ao uso | Erros não têm a mesma gravidade: uma seleção incorreta de exame ou interpretação indevida da classificação exige atenção distinta de um clique sem consequência clínica. | Identificar cenários de uso potencialmente perigoso, avaliar causas e impactos com profissionais e revisar o protótipo; não considerar uma média baixa de erros como evidência suficiente de segurança. | [ISO 14971](https://www.iso.org/standard/72704.html) (gestão de riscos para dispositivos médicos); [IEC 62366-1](https://www.iso.org/standard/63179.html) |
| Enquadramento regulatório do software médico | Se o sistema deixar de ser protótipo acadêmico e for destinado a uso clínico, sua finalidade pretendida poderá exigir enquadramento como software como dispositivo médico; o enquadramento ainda não foi estabelecido. | Declarar que resultados simulados não servem para decisões clínicas e não alegar validação clínica ou conformidade regulatória; antes de uso real, avaliar classificação e exigências aplicáveis junto à área regulatória. | ANVISA, [RDC nº 657/2022](https://anvisalegis.datalegis.net/action/ActionDatalegis.php?acao=abrirTextoAto&tipo=RDC&numeroAto=00000657&seqAto=000&valorAno=2022&orgao=RDC/DC/ANVISA/MS&codTipo=&desItem=&desItemFim=&cod_menu=1696&cod_modulo=134&pesquisa=true) (software como dispositivo médico) |

## 3. Metas de usabilidade

Usabilidade deve ser discutida **no contexto de uso**. Metas quantitativas devem dizer o que será medido, em qual tarefa, com qual população e qual limite será considerado aceitável.

### 3.1 Metas qualitativas

| Meta | Para quem/tarefa | Evidência desejada | Justificativa |
|---|---|---|---|
| Identificar e confirmar o exame correto antes de consultar a saída do modelo | Médico nefrologista (P01), no acesso ao exame em T01, caso esse fluxo seja confirmado (H02) | Em teste com dados fictícios, indica como verificou a correspondência entre exame e caso; não prossegue quando os dados não coincidem | A síntese da Entrega 5 prioriza localizar o exame correto; meios de acesso e identificadores ainda precisam ser validados (H02). |
| Compreender o que a classificação informa e quais são seus limites | Médico nefrologista (P01), ao consultar a saída do modelo em T01 (H06) | Explica com suas palavras o significado da indicação apresentada e aponta dúvidas ou informações ausentes, sem atribuir ao sistema uma capacidade não mostrada | A classificação de imagens é a contribuição declarada do TCC; forma de apresentação e compreensão pelo profissional ainda não foram verificadas (H01, H06). |
| Distinguir a indicação automatizada de uma conclusão clínica | Médico nefrologista (P01), ao relacionar a saída do modelo à avaliação de T01 (H03) | Em cenário simulado, descreve a indicação como apoio e identifica que a decisão clínica depende de sua avaliação, inclusive diante de divergência ou incerteza | H03 permanece aberta; confundir a saída do modelo com diagnóstico final comprometeria a interpretação pretendida para a interface. |
| Entender a explicação do modelo, se ela estiver disponível e for incluída no protótipo | Médico nefrologista (P01), ao examinar a explicação associada à classificação em T01 (H01, H06) | Descreve o que a explicação mostra, o que não permite concluir e se ela ajuda ou atrapalha a avaliação; observam-se interpretações equivocadas | O TCC prevê análise de interpretabilidade, mas o formato, a disponibilidade e a utilidade de uma explicação na interface ainda precisam ser confirmados. |
| Reconhecer o estado da análise e saber como agir quando não houver resultado | Médico nefrologista (P01), durante o processamento proposto em T01, se essa etapa fizer parte do fluxo (H02) | Em simulação de espera ou falha, relata o estado percebido e o próximo passo possível, sem confundir ausência de resultado com indicação de ausência de patologia | A jornada provisória inclui processamento, mas duração, falhas e necessidade de retorno visual ainda não foram investigadas (H02). |
| Identificar um próximo passo sem delegar a decisão ao modelo | Médico nefrologista (P01), ao encerrar a consulta da saída em T01, em caso hipotético com dúvida (H03) | Explica como consideraria a indicação junto às informações disponíveis e que informação adicional ou avaliação profissional buscaria se necessário | O objetivo proposto nas Entregas 1, 3 e 5 é apoiar a avaliação e decidir como prosseguir; o pós-uso real ainda não foi validado. |

### 3.2 Metas quantitativas

| ID | Dimensão | Métrica | Tarefa/escopo | Meta | Como medir | Justificativa |
|---|---|---|---|---|---|---|
| MU01 | facilidade de Aprendizado | taxa de conclusão de execução sem ajuda | T01 | ≥ 90% | teste observado | A primeira execução do fluxo proposto deve permitir ao profissional localizar o exame e consultar a indicação sem depender de orientação do avaliador; o percentual é um critério inicial de projeto, a revisar após teste piloto com o público-alvo (H02). |
| MU02 | facilidade de Memorização | taxa de conclusão em reexecução sem ajuda após intervalo de tempo | T01 | ≥ 95% | teste observado | A reexecução verifica se o profissional consegue retomar o fluxo sem reaprender a interface; o intervalo entre execuções e o mesmo critério de sucesso de T01 devem ser definidos antes do teste. O limite é provisório, não derivado de dados de usuários. |
| MU03 | eficiência | tempo médio de execução da tarefa | T01 | ≤ 5min | cronometragem no teste de usabilidade | Medir o tempo do recorte de interação de T01 ajuda a detectar obstáculos na localização do exame e na consulta da saída, sem avaliar a rapidez da decisão clínica ou do modelo. Cinco minutos é um limite preliminar, a ajustar após delimitar o início/fim da tarefa e realizar um piloto (H02). |
| MU04 | taxa e gravidade de erros | número médio de erros cometidos por usuário | T01 | ≤ 1 | registrar cada ação errada (clicks em botão errado, campo não preenchido, campo preenchido incorretamente, timeout) | Erros de seleção do exame ou de leitura da indicação podem comprometer o uso da informação como apoio (H03); a média deve ser baixa, e erros críticos devem ser analisados separadamente, mesmo que a média atenda ao limite. O valor é provisório até o piloto definir quais ações contam como erro. |
| MU05 | satisfação positiva do usuário | escala pós-tarefa | T01 | ≥ 85% | questionário após teste de usabilidade | A percepção do profissional complementa as medidas de conclusão, tempo e erros: conseguir executar T01 não garante que a interação pareça clara ou adequada ao trabalho. O limite é preliminar; é preciso definir o instrumento e como sua pontuação será convertida em percentual antes da coleta. |

### 3.3 Priorização das metas (se exigida na disciplina)

Se o professor solicitar porcentagens que somem 100%, trate-as como **peso de prioridade**, não como métrica de usabilidade.

| Meta | Peso de prioridade | Justificativa |
|---|---:|---|
| MU01 | 20% | A primeira execução sem ajuda indica se o profissional consegue iniciar o uso do fluxo proposto de T01; recebe peso igual por ainda não haver evidência com usuários que sustente uma hierarquia entre dimensões. |
| MU02 | 20% | A reexecução sem ajuda verifica se o fluxo pode ser retomado após um intervalo; mantém peso igual provisório porque a frequência de uso e o intervalo relevante ainda não foram confirmados. |
| MU03 | 20% | O tempo de interação ajuda a identificar obstáculos na consulta ao exame e à saída do modelo; recebe o mesmo peso inicial, sem pressupor que rapidez seja mais importante do que compreensão ou prevenção de erros. |
| MU04 | 20% | Monitorar erros é essencial para identificar seleção equivocada de exame ou interpretação incorreta da indicação (H03); o peso igual não dispensa tratar qualquer erro crítico separadamente, independentemente da pontuação agregada. |
| MU05 | 20% | A satisfação capta dificuldades percebidas que conclusão, tempo e erros podem não revelar; recebe peso igual enquanto não há dados de profissionais para justificar outra distribuição. |
| **Total** | **100%** | |

## 4. Como o ciclo será iterado

Explique que artefatos serão revisitados após protótipos e avaliações.

O ciclo de usabilidade seguirá a Engenharia de Usabilidade de Mayhew, com avaliações dos protótipos para verificar o atendimento às metas qualitativas e quantitativas definidas no projeto. Os resultados permitirão identificar problemas de interação e revisar os artefatos afetados, como requisitos, análise de tarefas e protótipos.

## Checklist

- [x] Capacidades e restrições têm impacto de IHC explicitado.
- [x] Está claro o limite entre contribuição técnica do TCC e camada interativa da disciplina.
- [x] Resultados/processamento simulados no protótipo foram explicitados.
- [x] Metas de usabilidade avaliam a interação, não substituem métricas técnicas do TCC.
- [x] Normas/princípios estão contextualizados, não apenas copiados.
- [x] Metas quantitativas são mensuráveis e associadas a tarefas/público.
- [x] Eficácia, eficiência e satisfação são consideradas quando pertinentes.
- [x] Metas poderão ser verificadas nas Entregas 12–14.

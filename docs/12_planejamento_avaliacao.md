# Entrega 12 — Planejamento da avaliação (DECIDE)

**Data:** 11/11/2026<br>
**Status:** 🟩 plano concluído; execução depende do protótipo navegável e dos participantes.<br>
**Responsáveis:** Kawan Mark Geronimo Da Silva, Gabriel Albertini Pinheiro e Alexandre Domiciano Pierri.

Avaliar a **interação da Mesa de inspeção**, conforme MU01–MU06 da [Entrega 8](08_engenharia_usabilidade.md). Não avaliar acurácia, localização de anomalias ou validade científica do modelo. As imagens vêm dos exemplos do TCC; caso, carga, autoria, resultado e falhas são demonstrativos. A espera prevista é de 3 segundos.

## A. DECIDE aplicado

| Etapa | Aplicação |
|---|---|
| **D — Determinar objetivos** | Verificar comparação da imagem, compreensão dos limites da IA, integridade do parecer, recuperação e facilidade percebida. |
| **E — Explorar perguntas** | QA01–QA06 abaixo transformam MU01–MU06 em evidências observáveis. |
| **C — Escolher métodos** | Inspeção heurística individual dos três integrantes (Entrega 13), seguida de observação de três pessoas externas (Entrega 14). Inspeção antecipa problemas; observação registra uso real. |
| **I — Questões práticas** | Um piloto interno e três sessões individuais de 25–30 minutos; computador com mouse/teclado, navegador e tela de referência 1920 × 1080. Kawan conduz U01, Gabriel U02 e Alexandre U03; outro integrante registra. Calendário após publicação e inspeção do protótipo. |
| **D — Questões éticas** | Consentimento antes da sessão, participação voluntária, IDs anônimos, dados fictícios. Gravação de tela e áudio somente com autorização específica; sem webcam. Não publicar consentimentos assinados nem dados pessoais no Git. |
| **E — Avaliar e apresentar** | Registrar sucesso, tempo, erros, ajuda e facilidade por pessoa/tarefa; consolidar contagens, mediana e falas autorizadas. Comparar com as metas sem generalizar uma amostra de três pessoas. |

## B. Perguntas de avaliação

| ID | Pergunta | Método / evidência | Critério esperado |
|---|---|---|---|
| QA01 | A pessoa compara original e mapa sem ajuda? | Observação UT01: sucesso e intervenções; inspeção H3/H6. | MU01: 3/3. |
| QA02 | Entende o que o modelo permite concluir? | Pergunta aberta após UT01; inspeção H2/H10. | MU02: 3/3 distinguem indício de prova e autorização de liberação. |
| QA03 | Emite parecer com caso, região comentada, responsável e conclusão corretos? | Observação UT02 e conferência do documento; H5/H6. | MU03: 3/3, quatro itens presentes. |
| QA04 | Consegue registrar um achado com agilidade? | Tempo de UT02, com caso já aberto. | MU04: mediana ≤ 180 s, sem ajuda; falhas informadas à parte. |
| QA05 | Corrige omissão e falha sem perder registros? | UT03, validação e recuperação; H1/H5/H9. | MU05: nenhuma emissão incompleta; 3/3 recuperam. |
| QA06 | Considera comparação e registro fáceis? | Escala 1–5 após cada tarefa e comentário. | MU06: mediana ≥ 4 em UT01/UT02. |

## C. Escopo e participantes

| Item | Definição |
|---|---|
| Versão | Pranchas F01–F12 da Entrega 11 como base; antes de coletar, registrar URL/node/versão e commit do protótipo navegável nas fichas. Protótipo navegável publicado no Figma (arquivo `9cKfwkCvyasTplQlf90RTC`, fluxo a partir de F01, ver [Entrega 11](11_figma.md)); falta conferir o acesso público ao link. |
| Escopo | M01–M03: entrada, análise, comparação, registro, revisão, parecer, erros e confirmações. Sem despacho, histórico, dashboard ou vistoria física. |
| Inspeção | A01 Kawan; A02 Gabriel; A03 Alexandre. Cada um examina todos os estados, sem discutir achados até terminar. |
| Observação | Três adultos externos à equipe. Prioridade para profissionais ligados à inspeção/logística/análise de imagens. Nenhum foi recrutado ainda. |
| Alternativa de recrutamento | Sem acesso profissional, usar proxies com experiência em análise de imagens/dados ou sistemas de relatórios, justificando a relação individualmente e validando a adequação com o professor antes da coleta. Colega apenas por conveniência não basta. |
| Inclusão/exclusão | Maior de 18 anos, consentimento e familiaridade com computador; não integrar a equipe nem ter elaborado as telas. Registrar experiência pertinente sem coletar nome no relatório. |
| Ambiente e piloto | Preferência por sessões presenciais na mesma estação; remoto só com compartilhamento/gravação autorizada e condições registradas. Piloto interno verifica roteiro, resets, duração e falhas; não conta entre os três usuários. |
| Condição para executar | Figma conectado, tarefas exercitadas, variantes de falha previsíveis e nenhum bloqueio grave da inspeção. Se o protótipo não permitir a ação necessária, corrigir antes do teste. |

## D. Tarefas e critérios prévios

As instruções entregues aos participantes não mencionam controles ou caminhos.

| ID | Cenário neutro | Objetivo da avaliação | Sucesso | Limite |
|---|---|---|---|---|
| UT01 | “Você recebeu o caso DEMO-001. Examine a área indicada e compare essa informação com a imagem sem o destaque. Ao terminar, explique o que o resultado permite concluir.” | T01/T02, O02/O03/O08, M01; MU01/MU02. | Localiza a área, consulta original e retorna à comparação; explica limites sem ajuda. | 5 min. |
| UT02 | “A dúvida sobre a região permanece. Registre a área e sua observação e prepare um parecer de apoio para outra pessoa, com sua conclusão e um responsável fictício.” | T03 e consulta de T05/T06, O04–O07/O09, M01/M03; MU03/MU04. | Parecer corresponde ao caso e contém região comentada, conclusão, justificativa e responsável; consegue relacionar o conteúdo à imagem. | 5 min; meta 3 min. |
| UT03 | “Neste registro preparado falta a identificação do responsável. Tente emitir o parecer e resolva o que impedir sua emissão. Se houver falha, procure concluir preservando o registro.” | O05/O08, M01/M03; MU05. | Emissão incompleta impedida; preenche autoria e recupera uma falha de exportação, sem perder comentário/conclusão. | 5 min. |

UT01 começa com caso pronto; UT02 recebe o mesmo estado inicial pronto para registrar, sem depender de sucesso anterior. UT03 começa com registro completo exceto autoria. O moderador prepara essas condições antes da instrução; a primeira exportação válida de UT03 falha de maneira simulada e a seguinte funciona. Fora da tarefa, o piloto/inspeção percorre F01/F02/F10A/B/F11A/B e a leitura F12.

## E. Instrumentos prontos

- [Consentimento e autorização de gravação](../instrumentos/12_avaliacao/consentimento.md).
- [Roteiro do moderador e tarefas](../instrumentos/12_avaliacao/roteiro.md).
- [Perfil e pós-teste](../instrumentos/12_avaliacao/questionarios.md).
- [Planilha de observação — nove registros vazios](../instrumentos/12_avaliacao/observacoes.csv).
- [Ficha individual de inspeção](../instrumentos/12_avaliacao/ficha_heuristica.md).

## F. Plano de análise

**Sucesso total:** todos os critérios, sem orientação; **parcial:** objetivo parcialmente atingido ou concluído com ajuda; **falha:** não concluiu, desistiu ou excedeu o limite. Consulta à ajuda da interface é permitida e registrada. Falta de ação no protótipo é defeito do protótipo, não erro da pessoa.

Cronometrar do fim da instrução até a conclusão/desistência; incluir espera simulada e registrar interrupções técnicas separadamente. Erro é uma ação com resultado contrário ao objetivo; contar a ocorrência e classificar como navegação, interpretação, preenchimento ou recuperação. Dúvida é pergunta verbal/hesitação confirmada por relato, não silêncio presumido. Registrar pedidos e intervenções; qualquer orientação de caminho conta como ajuda. Abandono encerra a tarefa sem penalidade.

Facilidade: 1 muito difícil, 2 difícil, 3 neutra, 4 fácil, 5 muito fácil. Codificar comentários em comparação, entendimento da IA, registro, recuperação e satisfação, mantendo fala e interpretação separadas. Sucesso é apresentado como `n/3`; falhas não são excluídas. MU04 só é considerada atendida se houver três conclusões sem ajuda e mediana ≤ 180 s. Priorizar por impacto, recorrência e persistência, vinculando achado à tela e à meta. Descrever limitações de proxies e de simulação.

## Checklist

- [x] Seis etapas DECIDE contextualizadas e ligadas às metas.
- [x] Perguntas, métodos, evidências e critérios definidos antes da coleta.
- [x] Avaliação de IHC separada do desempenho técnico do TCC.
- [x] Simulações declaradas; tarefas e estados iniciais definidos.
- [x] Recrutamento, piloto, ambiente, ética e armazenamento planejados.
- [x] Instrumentos preparados para inspeção e observação.
- [x] Procedimento de análise e apresentação definido.

**Referência:** aula 12, *Planejamento da Avaliação de IHC*, págs. 25–38 (DECIDE na pág. 37); aulas 13–14 para inspeção, preparação e observação. Concluir o plano não significa que recrutamento ou sessões já ocorreram.

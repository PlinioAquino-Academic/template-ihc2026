# Entrega 13 — Avaliação de IHC por inspeção heurística

**Data:** 18/11/2026  
**Status:** 🟨 em andamento  
**Responsabilidade:** 1 avaliação completa por integrante, sobre todas as telas/estados relevantes do projeto.

## Objetivo da atividade

Encontrar problemas de usabilidade por inspeção sistemática da interface com as **10 heurísticas de Nielsen**. Cada avaliador trabalha individualmente primeiro; depois a equipe consolida problemas duplicados e prioridades.

> **Parte de violações:** registre somente problemas reais. Não invente uma violação para “preencher” cada heurística. Para provar que todas foram exercitadas, use a **matriz de cobertura H1–H10**. Para heurísticas sem violação, a disciplina solicita um exemplo didático de boa prática.

## 1. Heurísticas adotadas

1. Visibilidade do status do sistema
2. Compatibilidade entre o sistema e o mundo real
3. Controle e liberdade do usuário
4. Consistência e padrões
5. Prevenção de erros
6. Reconhecimento em vez de memorização
7. Flexibilidade e eficiência de uso
8. Estética e design minimalista
9. Ajudar usuários a reconhecer, diagnosticar e recuperar-se de erros
10. Ajuda e documentação

**Referência:** [10 Usability Heuristics for User Interface Design — Nielsen Norman Group](https://www.nngroup.com/articles/ten-usability-heuristics/).

## Cobertura especial para interfaces administrativas e analíticas

Quando existirem, não limite a avaliação às “telas principais”. Inspecione também:

- dashboard em estados normal, vazio e erro;
- filtros sem resultado e filtros combinados;
- relatórios e exportação;
- histórico/listas longas;
- formulários CRUD (criação, edição, exclusão, validação);
- alteração de perfil/permissão;
- confirmações de ações destrutivas;
- processamento/loading/progresso;
- falha e recuperação;
- comparação de resultados;
- mensagens de termos técnicos, métricas e recomendações;
- ajuda/documentação contextual.

Em TCCs técnicos, observe especialmente se a interface comunica o estado do processamento e traduz informações técnicas para o vocabulário do usuário escolhido.

**Aplicação no projeto:** foram considerados configuração, validação, confirmação, processamento, falha, conclusão, histórico, resultados e gráficos. A comparação consiste na consulta individual dos registros e na reunião externa dos valores, conforme o planejamento da Entrega 12. Não foi exigida uma tela de comparação integrada. Administração, permissões, CRUD, exportação e filtros de histórico não fazem parte dos quadros examinados.

## 2. Escopo da inspeção

| Item | Definição |
|---|---|
| Versão avaliada | Protótipo navegável da Entrega 11, consultado em 18/11/2026. Os resultados e o processamento são demonstrativos. As capturas preservam os estados observados nesta inspeção. |
| Arquivo editável | [Figma — arquivo do projeto](https://www.figma.com/design/YJJhBTujdrsjDY113Iefj4/Sem-t%C3%ADtulo?node-id=4-12). |
| Fluxo M01 | [Seleção, configuração e execução](https://www.figma.com/proto/YJJhBTujdrsjDY113Iefj4/Sem-t%C3%ADtulo?node-id=4-12&scaling=scale-down-width&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=4%3A12). |
| Fluxo M02 | [Histórico, resultados e gráficos](https://www.figma.com/proto/YJJhBTujdrsjDY113Iefj4/Sem-t%C3%ADtulo?node-id=16-206&scaling=scale-down-width&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=16%3A206). |
| Telas/estados considerados | F01, F01S, F02, F02A, F02E, F03, F04, F04P, F04E, F05, F06, F07, F08, F08B, F09, F09B e F08E. |
| Cobertura das evidências | Capturas de F01, F02, F02A, F02E, F03, F04, F04E, F05, F07, F08, F08B, F09, F09B e F08E. F01S foi atravessado na navegação; F04P e F06 tiveram também sua estrutura e suas transições consultadas. As combinações duplicadas de controlador e modo não foram verificadas exaustivamente. |
| Dispositivo/viewport | Navegador em computador; capturas em viewport de 1440 × 960 pixels, com quadros de 1190 × 730 pixels. |
| Avaliador A01 | Gabriel Koiama de Rocha Lira — 22.125.067-3. Registro preparado com inspeção assistida por IA; a revisão individual de Gabriel ainda precisa ser confirmada. |
| Avaliador A02 | João Pedro Lopes Santana Villas Bôas — 22.125.065-7. Seção individual ainda não preenchida. |

**Limites:** a inspeção trata da interação do Figma e não avalia a validade do algoritmo, o desempenho do SUMO ou a execução R3 da aplicação funcional. Não houve teste sistemático de teclado, leitor de tela ou responsividade. As observações não constituem certificação de acessibilidade. A participação de Luiza e Flavio na exploração de 15/11 não substitui as inspeções individuais desta entrega.

## 3. Procedimento individual

Cada avaliador deve:

1. percorrer os fluxos/telas ao menos uma vez para familiarização;
2. inspecionar novamente aplicando sistematicamente H1–H10;
3. registrar cada problema com evidência e contexto;
4. atribuir severidade **depois de compreender bem o problema**, justificando a decisão;
5. não discutir achados com os demais antes de terminar a inspeção individual, quando o objetivo for preservar independência.

**Registro da preparação da seção A01:** o protótipo foi percorrido com assistência de IA, foram capturados estados dos dois fluxos e foram consultados textos e transições do arquivo. Os achados abaixo são verificáveis nessas evidências. A autoria de uma inspeção humana independente não foi presumida; Gabriel deverá conferir o registro. A seção A02 permanece sem resultados atribuídos a João.

### Escala de severidade (0–4)

| Grau | Interpretação |
|---:|---|
| 0 | não é considerado problema de usabilidade |
| 1 | problema cosmético; corrigir se houver tempo |
| 2 | problema menor; baixa prioridade |
| 3 | problema maior; alta prioridade |
| 4 | catástrofe de usabilidade; correção imperativa antes de disponibilizar |

Ao justificar, considere **frequência, impacto e persistência** do problema no contexto real de uso. A frequência indicada a seguir descreve a presença da condição na interface; não representa frequência medida com participantes.

---

## Avaliador A01 — Gabriel Koiama de Rocha Lira

**Matrícula:** 22.125.067-3.  
**Data da inspeção assistida:** 18/11/2026.  
**Situação:** registro preparado para revisão individual do integrante.

### 4. Matriz de cobertura das 10 heurísticas

| Heurística | Telas/fluxos examinados | Houve violação? | IDs dos achados | Exemplo de boa prática se não violada |
|---|---|---|---|---|
| H1 | F04/F04P/F05, F07 e F08E; M01/M02 | Sim | V01, V04 | — |
| H2 | F02/F03 e F08/F08B/F09/F09B; M01/M02 | Sim | V03, V05 | — |
| H3 | Retornos de F02A, F03, F04E, F08, F09 e F08E; M01/M02 | Não observada no recorte | — | Voltar à configuração, às métricas e ao histórico oferece saídas explícitas. |
| H4 | Rótulos e ações em F02, F03, F08/F08B e F09/F09B | Não observada no recorte | — | As duas execuções usam a mesma organização das métricas e os mesmos comandos de retorno. |
| H5 | F02E e F03; M01 | Não observada no recorte | — | A seed ausente recebe validação e a execução exige revisão e confirmação. |
| H6 | F03, F04E, F05 e F08/F08B; M01/M02 | Não observada no recorte | — | Cenário, controlador e seed são apresentados no contexto da tarefa. |
| H7 | Escolha de parâmetros e navegação em F02 e F07–F09B | Não observada no recorte | — | Os três registros têm acesso direto ao resultado; as opções principais de configuração estão expostas. |
| H8 | Composição de F01–F09B nos estados capturados | Não observada no recorte | — | Os quadros distinguem título, conteúdo e ações, concentrando a informação na tarefa corrente. |
| H9 | F02E, F04E e F08E; M01/M02 | Sim | V02 | — |
| H10 | Textos de apoio em F02/F02A e métricas de F08/F08B | Sim | V03, associado a H2 | — |

“Não observada” significa que não foi identificado um problema sustentado pelas evidências examinadas; não equivale a garantir ausência de problemas em todas as condições de uso.

### 5. Declaração de violações

| ID | Heurística | Tela/estado | Problema observado | Evidência | Severidade | Justificativa da severidade | Recomendação |
|---|---|---|---|---|---:|---|---|
| V01 | H1 | F04 → F04P → F05 | A inicialização avança automaticamente após 0,75 s e o estado Executando após aproximadamente 1,8 s. A janela curta dificulta ler o estado e o controlador antes da conclusão, especialmente na UT03. | [Captura da inicialização](../assets/13_heuristica/06-processamento.jpg). Transições dos nós Figma `4:398` e `4:448`. | 2 | Frequência: a condição ocorre no caminho temporizado examinado. Impacto: pode prejudicar a leitura e a medida de reconhecimento do estado. Persistência: o estado deixa de estar visível após a transição. A conclusão continua acessível. | Preparar um estado Executando estável para a avaliação, com avanço controlado pelo moderador, ou ampliar sua permanência após um piloto. Declarar que o tempo é simulado. |
| V02 | H9 | F04E | A mensagem informa a interrupção e orienta revisar as condições, mas não apresenta a causa nem identifica uma verificação concreta. O usuário pode voltar à configuração sem saber o que modificar. | [Captura da falha](../assets/13_heuristica/14-falha.jpg), nó `4:548`: “Revise as condições do experimento antes de iniciar outra tentativa.” | 2 | Frequência: ocorre quando este estado de falha é apresentado. Impacto: exige tentativa sem diagnóstico. Persistência: a mensagem permanece genérica ao consultar o aviso. Existe saída para revisão ou encerramento, sem bloqueio total demonstrado. | Modelar uma falha específica e comunicar causa e ação correspondente. Se a causa for desconhecida, informar isso e oferecer tentativa novamente ou consulta a detalhes, sem atribuir o problema à configuração sem evidência. |
| V03 | H2; associada a H10 | F02, F08 e F08B | Seed e os controladores Max Pressure/Actuated aparecem sem explicação suficiente de seu significado. Nos resultados, Throughput aparece sem tradução ou definição contextual. As unidades ajudam, mas não esclarecem integralmente os conceitos para um usuário com menor familiaridade. | [Configuração](../assets/13_heuristica/02-configuracao.jpg) e [resultado](../assets/13_heuristica/09-resultado-a.jpg), nós `4:144` e `16:239`. | 2 | Frequência: os termos aparecem na configuração e na interpretação. Impacto: pode causar escolha ou leitura inadequada para o perfil menos experiente. Persistência: não foi localizada ajuda contextual nesses quadros. O efeito deve ser verificado com o perfil previsto no pré-teste. | Apresentar “Seed — semente aleatória” com explicação da repetibilidade; resumir o propósito de cada controlador; traduzir Throughput e definir o que é contado, a unidade e o intervalo de referência. |
| V04 | H1 | F07 → F08E | O histórico mostra R2-003 sem informar sua indisponibilidade. O usuário precisa abrir o registro para descobrir que não poderá consultar o resultado. | [Histórico](../assets/13_heuristica/08-historico.jpg) e [indisponibilidade](../assets/13_heuristica/13-indisponivel.jpg), nós `16:206` e `16:357`. | 2 | Frequência: ocorre ao consultar o terceiro registro demonstrativo. Impacto: provoca uma navegação sem acesso à informação pretendida. Persistência: ao retornar à lista, a ausência do status continua. Há recuperação por escolha de outro registro. | Indicar “Resultado indisponível” na própria linha de R2-003. Manter acesso ao aviso e ao contexto, com rótulo de ação coerente com o que será apresentado. |
| V05 | H2 | F09 e F09B | O gráfico mostra barra e linhas de grade, mas não apresenta valores na escala. O texto permite ler 28 s ou 36 s; a representação gráfica, isoladamente, não oferece referência quantitativa para interpretar a altura da barra. | [Gráfico R2-001](../assets/13_heuristica/10-grafico-a.jpg) e [gráfico R2-002](../assets/13_heuristica/12-grafico-b.jpg), nós `16:276` e `16:335`. | 2 | Frequência: ocorre nos dois gráficos consultados. Impacto: reduz a interpretação da magnitude e a utilidade do gráfico na comparação. Persistência: as referências não aparecem ao permanecer no quadro. Os valores textuais continuam disponíveis. | Incluir escala numérica, unidade e identificação do registro. Adotar a mesma escala nos dois gráficos para permitir comparação visual coerente. |

**Qualidade do relato:** o problema deve ser observável e localizado. Evite “interface confusa” sem dizer **o que**, **onde**, **quando** e **para quem**.

V03 é um único problema associado a duas heurísticas; não é contado duas vezes no total de problemas.

### 6. Boas práticas — heurísticas não violadas (atividade didática)

| Heurística sem violação | Exemplo no sistema | Evidência | Por que atende |
|---|---|---|---|
| H3 | O resumo permite voltar à configuração antes de confirmar. O resultado indisponível permite retornar ao histórico. | [Confirmação](../assets/13_heuristica/05-confirmacao.jpg) e [indisponibilidade](../assets/13_heuristica/13-indisponivel.jpg). | O usuário encontra caminhos explícitos para rever escolhas ou continuar a consulta. |
| H4 | F08 e F08B mantêm a disposição de contexto, métricas e ações. | [Resultado R2-001](../assets/13_heuristica/09-resultado-a.jpg) e [resultado R2-002](../assets/13_heuristica/11-resultado-b.jpg). | O padrão aprendido em um registro pode ser reutilizado no outro. |
| H5 | A seed ausente recebe orientação para correção; F03 apresenta as condições antes do início. | [Validação](../assets/13_heuristica/04-validacao.jpg) e [confirmação](../assets/13_heuristica/05-confirmacao.jpg). | A interface ajuda a detectar uma configuração incompleta e a revisar escolhas antes de executar. |
| H6 | F03 reúne cenário, controlador, seed e modo. F08 apresenta as condições junto às métricas. | [Confirmação](../assets/13_heuristica/05-confirmacao.jpg) e [resultado](../assets/13_heuristica/09-resultado-a.jpg). | A leitura do quadro corrente fornece o contexto necessário sem exigir lembrar a configuração anterior. |
| H7 | F07 oferece acesso direto a cada um dos três registros. | [Histórico](../assets/13_heuristica/08-historico.jpg). | O conjunto pequeno pode ser consultado sem percorrer sequencialmente todos os resultados. A falta de filtros, isoladamente, não foi tratada como violação. |
| H8 | F08 separa condições experimentais e métricas; F03 destaca a revisão e a confirmação. | [Resultado](../assets/13_heuristica/09-resultado-a.jpg) e [confirmação](../assets/13_heuristica/05-confirmacao.jpg). | A hierarquia visual favorece localizar contexto, valores e ação principal. |

---

## Avaliador A02 — João Pedro Lopes Santana Villas Bôas

**Matrícula:** 22.125.065-7.  
**Data:** {{dd/mm/aaaa}}

### 4. Matriz de cobertura das 10 heurísticas

| Heurística | Telas/fluxos examinados | Houve violação? | IDs dos achados | Exemplo de boa prática se não violada |
|---|---|---|---|---|
| H1 | | | | |
| H2 | | | | |
| H3 | | | | |
| H4 | | | | |
| H5 | | | | |
| H6 | | | | |
| H7 | | | | |
| H8 | | | | |
| H9 | | | | |
| H10 | | | | |

### 5. Declaração de violações

| ID | Heurística | Tela/estado | Problema observado | Evidência | Severidade | Justificativa da severidade | Recomendação |
|---|---|---|---|---|---:|---|---|
| | | | | | | | |

### 6. Boas práticas — heurísticas não violadas (atividade didática)

| Heurística sem violação | Exemplo no sistema | Evidência | Por que atende |
|---|---|---|---|
| | | | |

## 7. Consolidação da equipe

Problemas iguais ou muito semelhantes encontrados por avaliadores diferentes devem ser consolidados, preservando quem os encontrou.

| ID consolidado | Achados individuais | Heurística | Problema | Severidade final | Prioridade | Responsável pela correção |
|---|---|---|---|---:|---|---|
| | | | | | | |

## 8. Síntese e plano de melhoria

### Registro preliminar da seção A01

- **Total:** cinco problemas distintos.
- **Por heurística principal:** H1 = 2; H2 = 2; H9 = 1. H10 está associada a V03.
- **Por severidade:** grau 0 = 0; grau 1 = 0; grau 2 = 5; grau 3 = 0; grau 4 = 0.
- **Bloqueios:** não foi demonstrado impedimento total de conclusão dos fluxos. V01 exige ajuste na preparação da UT03 para que a observação não dependa de uma janela muito curta.
- **Padrões recorrentes:** falta de explicação contextual de termos e de estados excepcionais; gráficos com referências quantitativas incompletas.
- **Melhorias propostas:** preparar o estado da UT03; tornar a falha específica; explicar termos e métricas; sinalizar indisponibilidade no histórico; completar a escala dos gráficos.
- **Verificação posterior:** repetir os caminhos afetados e registrar a versão após qualquer correção. Nenhuma recomendação deste relatório é apresentada como já implementada.

### Percurso e condição observada

1. **Escolher cenário:** caminho disponível e contexto apresentado.
2. **Configurar e revisar:** validação e resumo presentes; explicação de termos precisa melhorar.
3. **Acompanhar a execução:** estados presentes; transições curtas exigem preparação para a avaliação.
4. **Recuperar falha:** retorno disponível; diagnóstico insuficiente.
5. **Consultar histórico:** acesso aos registros disponível; indisponibilidade omitida na lista.
6. **Interpretar resultados e gráficos:** contexto e valores textuais presentes; termos e escala gráfica precisam melhorar.

### Síntese consolidada da equipe

{{preencher após as inspeções individuais}}

## Checklist

- [ ] Cada integrante fez uma inspeção completa e identificada. (A seção A01 foi preparada com assistência de IA e depende de revisão individual; A02 está em branco.)
- [ ] Todas as telas/estados relevantes foram examinados. (Falta confirmar a cobertura individual completa e as combinações alternativas.)
- [x] Estados de histórico, processamento, validação e erros foram considerados na inspeção assistida, quando existentes no recorte.
- [x] A inspeção avaliou a interface/protótipo, não o mérito técnico do algoritmo/modelo.
- [ ] H1–H10 aparecem na matriz de cobertura de cada avaliador. (A matriz A01 está preenchida; A02 aguarda preenchimento.)
- [x] Parte de violações contém apenas problemas observados, sem forçar um problema por heurística.
- [x] Todo problema registrado possui captura/localização e contexto.
- [x] Severidade possui justificativa de frequência, impacto e persistência.
- [x] Cada problema registrado possui recomendação específica.
- [ ] Achados duplicados foram consolidados ao final. (A consolidação aguarda as duas avaliações individuais.)

# Roteiro de teste de usabilidade

**Projeto:** Interface para Configuração, Execução e Análise de Simulações de Controle Semafórico Inteligente.  
**Equipe:** Gabriel Koiama de Rocha Lira e João Pedro Lopes Santana Villas Bôas.  
**Referência:** Entrega 12 — Planejamento DECIDE.  
**Interface deste roteiro:** Figma da Entrega 11.

## 1. Preparação

1. Identificar o participante como U01 ou U02.
2. Registrar data, moderador, dispositivo e versão utilizada.
3. Conferir os links e os estados iniciais das tarefas.
4. Preparar cronômetro e planilha.
5. Apresentar o termo e registrar a concordância.
6. Informar a duração estimada de até 40 minutos.
7. Confirmar que o registro será por anotações, sem gravação.

A aplicação funcional utilizada na exploração de 15/11/2026 deve ser identificada separadamente dos quadros do Figma deste roteiro.

## 2. Abertura padronizada

“Vamos observar como você utiliza a interface para preparar uma simulação e consultar resultados. Queremos identificar dificuldades e oportunidades de melhoria.

Você pode comentar suas dúvidas, pedir uma pausa ou encerrar a participação.

Nesta sessão, o Figma representa o funcionamento da interface. O processamento e os valores apresentados são demonstrativos.

Apresentarei uma tarefa por vez. Tente realizá-la como faria normalmente.”

## 3. Perfil pré-teste

- Você já configurou ou acompanhou uma simulação?
- Você já utilizou tabelas ou gráficos para comparar resultados?
- Você tem familiaridade com mobilidade urbana ou controle de tráfego?

Registrar as respostas na planilha. Quando o perfil for aproximado ao público-alvo, considerar essa condição na análise.

## 4. Tarefas

| ID | Instrução ao participante | Preparação do moderador |
|---|---|---|
| UT01 | Prepare um experimento para Regional São Paulo, usando o controlador híbrido, seed 42 e execução sem abrir a janela gráfica do simulador. Confira as condições antes de iniciar. | Começar no catálogo. Parar o tempo na conferência do resumo. |
| UT02 | Um colega preparou uma configuração. Ao tentar deixá-la pronta para execução, você encontra um problema. Descubra o que precisa corrigir. | Começar na configuração com seed vazia. |
| UT03 | O experimento já foi confirmado. Diga em que estado se encontra e qual estratégia está sendo usada. | Apresentar o quadro Executando. |
| UT04 | Encontre R2-001 e identifique seu cenário, sua estratégia e sua seed. | Começar no histórico e medir a localização até abrir o registro correto. |
| UT05 | Compare o tempo médio de espera de R2-001 e R2-002. Explique quais condições precisam ser conferidas antes de interpretar a diferença. | Começar no histórico. |
| UT06 | Consulte R2-003. Se encontrar um impedimento, explique o que aconteceu e continue com outro registro. | Começar no histórico. |

## 5. Critérios do observador

| Tarefa | Resultado esperado |
|---|---|
| UT01 | Resumo com cenário R2, controlador híbrido, seed 42 e modo Headless. |
| UT02 | Reconhecimento da seed ausente, recuperação do valor 42 e nova validação. |
| UT03 | Identificação correta do estado e do controlador. |
| UT04 | Abertura de R2-001 e identificação de Regional São Paulo, controlador híbrido e seed 42. |
| UT05 | Identificação de 28 s em R2-001 e 36 s em R2-002, consideração do contexto experimental e compreensão da comparação externa. |
| UT06 | Reconhecimento da indisponibilidade e abertura de outro resultado após retornar ao histórico. |

Na UT03, os estados automáticos podem passar rapidamente. Apresentar o quadro Executando diretamente e mantê-lo disponível durante a pergunta, usando o mesmo procedimento para todos. Registrar esse procedimento.

## 6. Durante a tarefa

- Ler o mesmo enunciado para todos.
- Iniciar o cronômetro depois da leitura.
- Observar a tentativa antes de intervir.
- Registrar erros, dúvidas, ajudas e comentários.
- Registrar separadamente a repetição do enunciado.
- Se uma limitação técnica impedir a tarefa, anotar a causa e seu efeito sobre a medição.
- Respeitar pausas e pedidos de encerramento.

## 7. Pós-tarefa

Perguntar “Quão fácil ou difícil foi realizar esta tarefa?”.

| Nota | Resposta |
|---|---|
| 1 | Muito difícil |
| 2 | Difícil |
| 3 | Nem fácil nem difícil |
| 4 | Fácil |
| 5 | Muito fácil |

Depois perguntar “O que mais influenciou sua resposta?”.

## 8. Encerramento

- Em qual momento foi mais difícil decidir como prosseguir?
- Que informação teria ajudado?
- Como você reuniria as informações para comparar duas execuções?

Agradecer a participação e salvar as anotações com o identificador correspondente.

## 9. Limitação da atividade anterior

A exploração de 15/11/2026 ocorreu sem roteiro padronizado, cronômetro ou planilha de observação. Este instrumento foi preparado posteriormente e será utilizado nas sessões padronizadas.

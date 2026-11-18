# Entrega 11 — Protótipo no Figma

**Data:** 18/11/2026  
**Status:** 🟩 concluída  
**Responsabilidade:** 1 protótipo integrado por equipe cobrindo os fluxos MoLIC.

## Objetivo da atividade

Materializar o modelo de interação em um protótipo navegável, preservando a lógica dos objetivos, tópicos, signos, feedbacks, alternativas e recuperações definidos anteriormente.

## Biblioteca de possibilidades para projetos técnicos

O protótipo deve materializar os fluxos definidos nas entregas anteriores. Dependendo do escopo, podem fazer sentido:

1. **Dashboard:** indicadores, alertas, estado, tendências e atalhos para tarefas frequentes.
2. **Configuração/parametrização:** escolhas, presets, validação e explicação de opções técnicas.
3. **Entrada de dados:** upload, conexão, seleção, pré-visualização e validação.
4. **Processamento:** fila, status, progresso, cancelamento, falha e reexecução.
5. **Relatório/resultados:** síntese, métricas, gráficos, explicação, exportação e compartilhamento.
6. **Histórico:** busca, filtros, ordenação, paginação, detalhes e repetição de execução.
7. **Comparação:** antes/depois, modelo A/B, execução A/B, baseline ou períodos.
8. **Explicabilidade:** confiança, fatores, evidências, limitações e correção/contestação.
9. **Administração:** usuários, grupos, perfis, permissões, integrações e políticas.
10. **CRUDs de domínio:** somente quando criar/consultar/editar/excluir representa tarefa real.
11. **Auditoria/logs:** histórico de alterações e eventos em linguagem adequada.
12. **Alertas/ocorrências:** severidade, impacto, ação, responsável e resolução.
13. **Ajuda/documentação:** apoio contextual a tarefas complexas.

### Estados que não podem ser esquecidos

Quando aplicável, considere: vazio/sem dados; carregamento/processamento; sucesso; erro de entrada; erro de processamento; filtro sem resultados; permissão insuficiente; confirmação de ação destrutiva; cancelamento/desfazer/recuperação; dados desatualizados/conflito.

> Esta lista é repertório de design, **não uma exigência de quantidade de telas**. A rastreabilidade deve explicar por que cada tela existe.

## Link do Figma

**Protótipo:** [Entrega 11 — Protótipo navegável da equipe](https://www.figma.com/proto/YJJhBTujdrsjDY113Iefj4/Sem-t%C3%ADtulo?node-id=4-12&scaling=scale-down-width&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=4%3A12&show-proto-sidebar=1)  
**Arquivo editável:** [Entrega 11 — Arquivo de design da equipe](https://www.figma.com/design/YJJhBTujdrsjDY113Iefj4/Sem-t%C3%ADtulo?node-id=4-12)  
**Última verificação de permissão:** 18/11/2026. A abertura do link foi confirmada por Gabriel. A configuração do Figma permite visualização por qualquer pessoa com o link.

**Atalho para o M02:** [Histórico de execuções](https://www.figma.com/proto/YJJhBTujdrsjDY113Iefj4/Sem-t%C3%ADtulo?node-id=16-206&scaling=scale-down-width&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=16%3A206&show-proto-sidebar=1)

## Cobertura MoLIC → Figma

| MoLIC | Objetivo | Fluxo/telas no Figma | Estados de erro/recuperação | Responsável |
|---|---|---|---|---|
| M01 | OBJ01 a OBJ04 — Produzir execuções sob condições comparáveis, preparar a configuração, validar e iniciar a simulação e acompanhar sua execução. | `F01 → F01S → F02 → F03 → F04 → F04P → F05`. A configuração avançada fica em `F02A`. Na conclusão do percurso principal, `F05` permite abrir o histórico, preparar outra execução ou encerrar em `F06`. | Limpar a seed e validar leva a `F02E`, com opção de corrigir o valor. `F03` permite voltar à configuração. O fluxo **M01 · Falha e recuperação** passa por `F04T → F04E` e permite revisar a configuração ou encerrar. | Gabriel Koiama de Rocha Lira — 22.125.067-3 |
| M02 | OBJ05 a OBJ09 — Localizar uma execução, interpretar suas métricas, verificar condições para comparar e reunir informações para uma síntese. | `F07 → F08 → F09` para R2-001 e `F07 → F08B → F09B` para R2-002. Cada gráfico retorna ao respectivo resultado, e os dois resultados permitem voltar ao histórico. | `F07 → F08E → F07` para o registro R2-003, cujo resultado está indisponível. | João Pedro Lopes Santana Villas Bôas — 22.125.065-7, responsável pelo cenário CI02 |

No M01, o Figma simula a validação e o processamento. A integração com o SUMO pertence à interface funcional do TCC. No M02, os registros, valores e gráficos são demonstrativos. O usuário consulta as execuções individualmente e realiza a comparação e a síntese fora do protótipo.

A ação **Abrir histórico** em `F05` conecta o percurso principal do M01 ao M02. O histórico também pode ser aberto diretamente pelo seletor de fluxos do Figma.

## Catálogo de telas/estados

### F01 — Escolha do cenário de tráfego

![F01 — Catálogo com o cenário R2 · Regional São Paulo](https://raw.githubusercontent.com/koiamagabriel/IHCsemaforo/7f8fe1b20a78b04ab3e1c6631e5511ebc207834c/assets/11_figma/f01.svg)

**Objetivo do usuário:** localizar e selecionar a malha viária que será usada na simulação.  
**Signos principais:** catálogo, cenário **R2 · Regional São Paulo**, esquema da malha e ação **Selecionar cenário**.  
**Origem no MoLIC:** M01, cena «Escolha do cenário de tráfego».

### F07 — Histórico de execuções

![F07 — Histórico com registros de simulações](https://raw.githubusercontent.com/koiamagabriel/IHCsemaforo/7f8fe1b20a78b04ab3e1c6631e5511ebc207834c/assets/11_figma/f07.svg)

**Objetivo do usuário:** localizar e escolher uma execução para consultar.  
**Signos principais:** identificação do registro, cenário, controlador, seed e estado da execução.  
**Origem no MoLIC:** M02, cena «Localizar execução no histórico».

### F08 — Resultado individual

![F08 — Condições experimentais e métricas da execução selecionada](https://raw.githubusercontent.com/koiamagabriel/IHCsemaforo/7f8fe1b20a78b04ab3e1c6631e5511ebc207834c/assets/11_figma/f08.svg)

**Objetivo do usuário:** conferir as condições da execução e interpretar as métricas.  
**Signos principais:** registro, cenário, controlador, seed, condição de demanda, métricas e unidades.  
**Origem no MoLIC:** M02, cena «Interpretar o resultado individual».  
**Navegação:** `F08` apresenta R2-001 e `F08B` apresenta R2-002. Em ambos, é possível consultar o gráfico ou voltar ao histórico.

### F09 — Gráfico da execução

![F09 — Gráfico demonstrativo de tempo médio de espera](https://raw.githubusercontent.com/koiamagabriel/IHCsemaforo/7f8fe1b20a78b04ab3e1c6631e5511ebc207834c/assets/11_figma/f09.svg)

**Objetivo do usuário:** examinar a representação gráfica do tempo médio de espera.  
**Signos principais:** identificação do registro, indicador, valor, unidade e gráfico.  
**Origem no MoLIC:** M02, cena «Consultar o gráfico da execução».  
**Navegação:** `F09` e `F09B` retornam às métricas da execução correspondente.

### F08E — Resultado indisponível

![F08E — Aviso de resultado indisponível e retorno ao histórico](https://raw.githubusercontent.com/koiamagabriel/IHCsemaforo/7f8fe1b20a78b04ab3e1c6631e5511ebc207834c/assets/11_figma/f08e.svg)

**Objetivo do usuário:** entender por que a consulta foi interrompida e selecionar outra execução.  
**Signos principais:** registro R2-003, aviso de indisponibilidade e ação **Voltar ao histórico**.  
**Origem no MoLIC:** M02, transição de recuperação após «Recuperar resultado».

## Sistema visual e consistência

| Elemento | Regra adotada | Justificativa |
|---|---|---|
| Tipografia | Usar Inter nos dois fluxos, com tamanhos e pesos distintos para títulos, rótulos, valores e ajuda. | Facilita a leitura das condições experimentais e das métricas. |
| Cores | Usar fundo escuro, ciano nas ações principais e rótulos de texto para estados como conclusão, falha e indisponibilidade. | O significado dos estados pode ser identificado pelo texto. |
| Componentes | Reutilizar os botões principal e secundário e indicar na barra lateral a etapa atual. | Ajuda a reconhecer ações equivalentes durante a configuração e a consulta. |
| Feedback | Mostrar a validação junto aos controles da seed, destacar o andamento da simulação e associar a indisponibilidade à ação de voltar ao histórico. | Ajuda o usuário a identificar o problema e retomar a tarefa. |

## Verificação de acessibilidade básica

Os estados de validação, falha, conclusão e indisponibilidade estão identificados por texto. As capturas do catálogo têm textos alternativos que descrevem seu conteúdo. As métricas apresentam nomes e unidades visíveis, como segundos para espera média e veículos por hora para throughput.

A verificação formal de contraste e a avaliação da navegação por teclado ficam para a inspeção de usabilidade. O protótipo desta entrega foi preparado para apresentação em desktop.

## Checklist

- [x] Link do Figma está acessível.
- [x] Há capturas representativas dos dois fluxos no repositório.
- [x] Os fluxos M01 e M02 estão cobertos.
- [x] Estados de erro, feedback e recuperação foram prototipados.
- [x] A terminologia de cenário, controlador, seed e registro da execução segue a Entrega 9.
- [x] Os dois fluxos reutilizam os botões principal e secundário.
- [x] Os percursos principais são clicáveis do início ao fim.
- [x] As conexões de recuperação retornam à configuração ou ao histórico, conforme o fluxo.
- [x] O histórico e o resultado individual são rastreáveis ao CI02, ao M02 e às tarefas T06–T08.
- [x] Os estados de processamento, conclusão, validação inválida, falha e resultado indisponível foram representados.
- [x] Os resultados demonstrativos identificam as métricas, suas unidades e o registro da execução.
- [x] A documentação distingue a simulação no Figma da integração funcional com o SUMO.

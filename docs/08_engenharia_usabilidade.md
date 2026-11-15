# Entrega 8 — Ciclo de vida e engenharia de usabilidade

**Data:** 14/11/2026  
**Status:** 🟨 em andamento  
**Responsabilidade:** 1 solução por equipe

## Objetivo da atividade

Transformar o conhecimento acumulado sobre usuários, tarefas, plataforma e contexto em princípios e **metas de usabilidade verificáveis**, mantendo o caráter iterativo do projeto.

## Delimitação do sistema interativo

Antes das características da plataforma, separe:

| Camada | O que pertence ao projeto | O que será avaliado em IHC |
|---|---|---|
| contribuição técnica do TCC | modelo | desempenho técnico não é substituído pelo teste de IHC |
| camada de interação da disciplina | interface | compreensão, eficácia, eficiência, satisfação, erros, acessibilidade etc. |
| integrações/dados simulados | {{...}} | {{limites do protótipo}} |

Em um protótipo de disciplina, é aceitável simular processamento ou resultados quando a implementação técnica não estiver integrada, desde que isso seja declarado e a simulação seja suficiente para avaliar a interação.

## 1. Características da plataforma

| Característica | Descrição | Consequência para IHC |
|---|---|---|
| Software | {{...}} | {{...}} |
| Hardware/dispositivos | {{...}} | {{...}} |
| Capacidades | {{listar e explicar}} | {{...}} |
| Restrições | {{listar e explicar}} | {{...}} |
| Conectividade/latência | {{...}} | {{...}} |
| Segurança/privacidade | {{...}} | {{...}} |
| Volume de dados/histórico | {{...}} | {{impacto em busca, filtros, paginação...}} |
| Tempo de processamento | {{...}} | {{feedback, progresso, cancelamento...}} |
| Papéis/permissões | {{...}} | {{administração, prevenção de erros...}} |

## 2. Princípios gerais do projeto

Inclua apenas normas, leis, padrões e princípios realmente relevantes, explicando **como** afetam o projeto. Não transforme esta seção em lista de links.

| Princípio/norma | Aplicabilidade ao contexto | Decisão/requisito decorrente | Fonte |
|---|---|---|---|
| Contexto de uso | {{...}} | {{...}} | Entregas 1/3 |
| LGPD, se aplicável | {{...}} | {{...}} | {{fonte oficial}} |
| Acessibilidade | {{...}} | {{...}} | {{WCAG/norma aplicável}} |
| {{outro}} | {{...}} | {{...}} | {{...}} |

## 3. Metas de usabilidade

Usabilidade deve ser discutida **no contexto de uso**. Metas quantitativas devem dizer o que será medido, em qual tarefa, com qual população e qual limite será considerado aceitável.

### 3.1 Metas qualitativas

| Meta | Para quem/tarefa | Evidência desejada | Justificativa |
|---|---|---|---|
| {{ex.: compreensão clara da diferença entre X e Y}} | {{...}} | {{fala/observação}} | {{...}} |

### 3.2 Metas quantitativas

| ID | Dimensão | Métrica | Tarefa/escopo | Meta | Como medir | Justificativa |
|---|---|---|---|---|---|---|
| MU01 | facilidade de Aprendizado | taxa de conclusão de execução sem ajuda | T01 | ≥ 90% | teste observado | {{...}} |
| MU02 | facilidade de Memorização | taxa de conclusão em reexecução sem ajuda após intervalo de tempo | T01 | ≤ 95% | teste observado | {{...}} |
| MU03 | eficiência | tempo médio de execução da tarefa | T01 | ≤ 5min | cronometragem no teste de usabilidade | {{...}} |
| MU04 | taxa e gravidade de erros | número médio de erros cometidos por usuário | T01 | ≥ 1 | registrar cada ação errada (clicks em botão errado, campo não preenchido, campo preenchido incorretamente, timeout) | {{...}} |
| MU05 | satisfação positiva do usuário | escala pós-tarefa | T01 | ≥ 85% | questionário após teste de usabilidade | {{...}} |

### 3.3 Priorização das metas (se exigida na disciplina)

Se o professor solicitar porcentagens que somem 100%, trate-as como **peso de prioridade**, não como métrica de usabilidade.

| Meta | Peso de prioridade | Justificativa |
|---|---:|---|
| MU01 | 20% | {{...}} |
| MU02 | 20% | {{...}} |
| MU03 | 20% | {{...}} |
| MU04 | 20% | {{...}} |
| MU05 | 20% | {{...}} |
| **Total** | **100%** | |

## 4. Como o ciclo será iterado

Explique que artefatos serão revisitados após protótipos e avaliações.

## Checklist

- [ ] Capacidades e restrições têm impacto de IHC explicitado.
- [ ] Está claro o limite entre contribuição técnica do TCC e camada interativa da disciplina.
- [ ] Resultados/processamento simulados no protótipo foram explicitados.
- [ ] Metas de usabilidade avaliam a interação, não substituem métricas técnicas do TCC.
- [ ] Normas/princípios estão contextualizados, não apenas copiados.
- [ ] Metas quantitativas são mensuráveis e associadas a tarefas/público.
- [ ] Eficácia, eficiência e satisfação são consideradas quando pertinentes.
- [ ] Metas poderão ser verificadas nas Entregas 12–14.

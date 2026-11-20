# Checklist final do projeto de IHC — Equipe 24

**Disciplina:** Interação Humano-Computador (CC8122) — Centro Universitário FEI — 2026/2.  
**Projeto:** Interface para Configuração, Execução e Análise de Simulações de Controle Semafórico Inteligente.  
**Equipe:** Gabriel Koiama de Rocha Lira e João Pedro Lopes Santana Villas Bôas.  
**Escopo:** conferência documental do repositório após a conclusão das Entregas 1–14.

## Como interpretar este checklist

- `[x]` — requisito atendido ou documentado nos artefatos do repositório.
- `[x]` — verificação que ainda precisa ser realizada ou confirmada pela equipe; não representa, por si só, ausência do artefato acadêmico.
- **Não se aplica** — requisito condicional que não faz parte do escopo definido; não exige implementação.

A conclusão documental de uma entrega não comprova que todas as metas de usabilidade foram atingidas, que todas as recomendações foram implementadas ou que as hipóteses H01–H03 foram validadas para especialistas de mobilidade.

## 1. Relação entre TCC e escopo de IHC

- [x] A contribuição técnica do TCC e o escopo de IHC estão distinguidos em `README.md` e nas E1/E8.
- [x] O repositório registra que a interface desktop V0 já fazia parte do planejamento do TCC e que a disciplina aprofundou os requisitos e a modelagem da interação.
- [x] O público prioritário adotado — pesquisadores/analistas de mobilidade — é plausível e está identificado como hipótese H01, ainda não validada diretamente com especialistas.
- [x] Os objetivos humanos (preparar, acompanhar, interpretar e comparar experimentos) estão descritos para além do simples uso de telas.
- [x] O recorte de IHC cobre configuração, execução/acompanhamento e consulta individual de resultados; não exige funcionalidades alheias ao domínio.
- [x] A cadeia problema humano → contribuição computacional → interação → impacto potencial pode ser reconstruída pelas entregas e pela rastreabilidade.
- **Não se aplica:** derivar uma interface do zero para um TCC sem interface previamente prevista.

## 2. Estrutura, autoria e apresentação

- [x] Os 14 arquivos `docs/01_...md` a `docs/14_...md` estão presentes e relacionados no `README.md`.
- [x] As entregas individuais identificam seus responsáveis, com consolidação de equipe onde prevista.
- [x] Existem evidências de personas, HTA/GOMS/CTT, V0, MoLIC, Figma, inspeção heurística e observação de usuários.
- [x] As referências locais dos documentos Markdown foram conferidas estruturalmente, sem vínculos quebrados identificados nos documentos de entrega e apoio examinados.
- [x] `README.md` e `RASTREABILIDADE.md` registram as 14 entregas e preservam as limitações metodológicas da E14.
- [x] Conferir a renderização e a legibilidade dos diagramas e capturas diretamente na interface do GitHub, especialmente o SVG M01 da E10.
- [x] Conferir os dois fluxos públicos do Figma (M01/M02) em janela anônima, sem sessão privilegiada, e confirmar a navegabilidade dos caminhos principais e de recuperação.
- [x] Confirmar a preservação de fontes editáveis dos diagramas quando disponíveis e necessárias à apresentação, além das versões renderizadas.

## 3. Coerência da análise e do projeto de interação

- [x] A E2 identifica concorrentes e referencia decisões de interface sem convertê-las automaticamente em requisitos obrigatórios.
- [x] As proto-personas P01/P02 e os cenários C01/C02 são rastreados às tarefas T01–T08.
- [x] Os cenários de problema da E4 descrevem contexto, objetivos, rupturas e consequências sem depender de telas futuras.
- [x] A E5 contém HTA, GOMS e CTT para ambos os integrantes.
- [x] A E6 documenta a interface V0 real, PF01–PF03, PP01–PP07, evidências visuais e walkthrough formativo; a comparação entre execuções é externa/manual.
- [x] A E7 apresenta I01 e I02 como instrumentos planejados, sem alegar aplicação de questionários ou entrevistas naquela entrega.
- [x] A E8 distingue princípios PG, metas MQ/MU e capacidades existentes de propostas futuras.
- [x] A E9 registra CI01/CI02, OBJ01–OBJ09 e o esquema conceitual de signos.
- [x] A E10 contém M01 e M02 com caminhos, alternativas, rupturas e recuperação.
- [x] Conferir especificamente a notação MoLIC do diagrama M01 em relação ao material da disciplina antes de marcar os dois itens remanescentes da E10.
- [x] A E11 contém o protótipo navegável e a cobertura dos fluxos M01/M02, sem alegar processamento real no Figma.
- [x] A terminologia de cenário, controlador, seed, histórico, registro, resultado e métrica é rastreável entre E9–E14.
- [x] Metas MU01–MU08 são mensuráveis ou possuem ressalvas explícitas quando a medida não foi obtida exatamente.

## 4. Telas, padrões e limites funcionais

- [x] O catálogo, a configuração, a validação, o processamento, a conclusão, o histórico, os resultados e os estados de erro têm relação com tarefas e objetivos.
- [x] As informações experimentais necessárias à interpretação (cenário, controlador, seed e métricas) aparecem como requisitos conceituais e são discutidas nas avaliações.
- [x] As diferenças entre modos Visual/Headless e entre resultados individuais e comparação externa estão documentadas.
- [x] Foram considerados feedback de processamento, validação incorreta, falha, conclusão e resultado indisponível.
- [x] Os problemas de clareza, escala de gráficos, identidade de registros e recuperação foram documentados como achados e recomendações; não se presume sua correção.
- **Não se aplica:** implementar comparação automática lado a lado, dashboards adicionais, filtros avançados, exportação, administração, CRUD ou gestão de permissões sem objetivo rastreado e autorização de escopo.
- [x] A documentação distingue a existência de um protótipo demonstrativo de uma interface funcional de simulação SUMO/TraCI.

## 5. Avaliação heurística — Entrega 13

- [x] Gabriel (A01) e João (A02) registraram suas inspeções dos estados e caminhos definidos no escopo.
- [x] As dez heurísticas de Nielsen foram contempladas nas matrizes individuais.
- [x] Os achados têm localização, evidência, interpretação de severidade e recomendação.
- [x] Os doze achados individuais foram consolidados em sete problemas distintos (HC01–HC07), preservando a origem das observações.
- [x] HC02 e HC06, severidade 3, permanecem priorizados no plano de melhorias.
- [x] O relatório não afirma que propostas da inspeção já tenham sido implementadas no Figma ou na V0.

## 6. Observação de usuários — Entrega 14

- [x] A E12 descreve DECIDE, objetivos, perguntas QA01–QA10, critérios, instrumentos e tarefas padronizadas UT01–UT06.
- [x] A E14 contém registros individuais de U01/Gabriel e U02/João, ambos externos à equipe e classificados como participantes *proxy*.
- [x] Os resultados relatados apresentam seis tarefas por pessoa, com sucesso, tempo, erros, ajudas, facilidade, ocorrências e respostas pós-teste.
- [x] O piloto preparatório e a apresentação estável do estado Executando na UT03 estão registrados como condições metodológicas, sem generalização sobre a transição automática.
- [x] A consolidação registra 8/12 sucessos totais, 4/12 parciais, 9 erros, 3 ajudas e mediana global de facilidade de 4/5.
- [x] MU01–MU08 foram confrontadas com as evidências disponíveis; MU02 não atingiu a autonomia pretendida, e MU06 não tem mediana exata de localização.
- [x] As dificuldades observadas foram consolidadas como AU01–AU06, com o AU07 provisório incorporado ao AU02.
- [x] A comparação com HC01–HC07 distingue achados confirmados, relacionados e não exercitados nas tarefas.
- [x] A conclusão apresenta recomendações concretas, condições de interpretação e limites de generalização de dois participantes *proxy*.
- [x] A equipe informou ter confirmado com o professor que **não é necessária gravação** da interação para esta entrega.
- [x] Confirmar administrativamente que **dois participantes** satisfazem a exigência específica do professor, caso isso ainda não tenha sido confirmado.

## 7. Ética, privacidade e registros

- [x] Os moderadores relataram obter concordância voluntária antes das sessões padronizadas e informar a possibilidade de interrupção.
- [x] O relatório E14 identifica os participantes apenas como U01/U02, sem publicar seus nomes.
- [x] Os códigos EX01/EX02 diferenciam, após atualização dos arquivos pertinentes, a exploração R3 de 15/11 das sessões padronizadas do Figma em 18–19/11.
- [x] A documentação distingue resultados técnicos de simulação e registros pessoais de testes de usabilidade.
- [x] Não há exigência de gravação para as sessões de observação, conforme orientação docente relatada pela equipe.
- [x] Não anexar nomes, contatos, gravações ou fichas brutas identificáveis ao repositório público sem base e autorização pertinentes.

## 8. Comunicação, apresentação e submissão

- [x] O README permite compreender o problema, a solução interativa, a relação com o TCC, as responsabilidades e os resultados documentados.
- [x] A matriz de rastreabilidade relaciona capacidades, objetivos, personas, tarefas, protótipos, métricas e achados até a E14.
- [x] A apresentação dos resultados preserva a diferença entre avaliação de IHC e validação científica do controle semafórico.
- [x] A documentação preserva hipóteses H01–H03 abertas ou parcialmente investigadas, sem afirmar validação estatística.
- [x] Realizar a conferência final da branch `main` após as correções pontuais, a limpeza dos arquivos residuais e a revisão deste checklist.
- [x] Confirmar se a submissão acadêmica exige ação adicional no ambiente da disciplina (link, formulário, prazo ou apresentação), além do commit no GitHub.

## Situação consolidada

**Conteúdo acadêmico:** as Entregas 1–14 estão produzidas e a E14 está consolidada em relatório.  
**Correções de conteúdo previstas para encerramento:** anonimização/identificação separada da exploração anterior, atualização da ressalva de acessibilidade na E11, ajuste de conclusão individual da E14 e atualização das descrições dos assets.  
**Verificações externas remanescentes:** legibilidade/notação M01, acesso ao Figma sem privilégios, comprovantes de consentimento aplicáveis e requisitos específicos de submissão/quantidade de participantes.  
**Melhorias de produto:** HC01–HC07 e AU01–AU06 constituem recomendações documentadas; sua implementação não é requisito presumido para considerar os relatórios acadêmicos concluídos.

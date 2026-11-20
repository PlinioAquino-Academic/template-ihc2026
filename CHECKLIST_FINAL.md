# Checklist final do projeto

Última conferência: 20/11/2026 (branch `entrega12`). Itens desmarcados indicam pendências reais de acesso externo, inspeções individuais dos demais integrantes ou execução dos testes com participantes externos.

## Relação entre TCC e escopo de IHC

- [x] Está claro qual é o **tema/contribuição do TCC** e qual é o **escopo de IHC da disciplina**.
- [x] A equipe registrou se o TCC já previa interface, previa parcialmente ou não previa.
- [x] Se o TCC não previa interface, a equipe explicou como derivou o recorte de IHC a partir da contribuição técnica.
- [x] O usuário escolhido para IHC é plausível e possui relação clara com o valor produzido pelo tema do TCC.
- [x] O objetivo do usuário é descrito como resultado no mundo real, e não como “usar o sistema”.
- [x] A interface da disciplina não é apresentada como obrigação formal do TCC, salvo se isso tiver sido acordado com o orientador.
- [x] O recorte de IHC é pequeno o suficiente para ser modelado, prototipado e avaliado durante a disciplina.
- [x] O projeto consegue explicar a cadeia **problema humano → contribuição computacional → forma de uso → impacto potencial**.

## Estrutura e apresentação

- [x] O README explica problema, público, contexto, contribuição do TCC e recorte de IHC.
- [x] Todos os 14 arquivos de entrega estão linkados e abrem corretamente.
- [x] Não existem links locais quebrados.
- [x] Imagens e diagramas são legíveis no GitHub.
- [x] Arquivos editáveis dos principais diagramas foram preservados quando possível.
- [x] Entregas individuais identificam o autor.
- [ ] As quantidades mínimas por integrante foram atendidas. *(Faltam A02 e A03 na Entrega 13 e as três sessões U01–U03 na Entrega 14.)*
- [ ] Links externos (Figma, Forms, vídeos) foram testados sem autenticação privilegiada. *(Figma retornou HTTP 404 em 20/11/2026; vídeo da Entrega 14 ainda não gravado.)*

## Coerência de IHC

- [x] Público-alvo, personas e participantes de pesquisa/teste são coerentes com o escopo de IHC.
- [x] Cenários de problema descrevem o problema/atividade sem antecipar a solução.
- [x] Tarefas analisadas correspondem a objetivos importantes das personas.
- [x] Modelo conceitual, signos e MoLIC usam terminologia consistente.
- [x] MoLIC contém caminhos principais, alternativas e rupturas relevantes.
- [x] O Figma cobre os fluxos modelados e não cria funcionalidades críticas sem rastreabilidade.
- [x] Metas de usabilidade são verificáveis.
- [x] Em projetos técnicos, resultados do algoritmo/modelo foram traduzidos para linguagem e decisões compreensíveis ao perfil de usuário escolhido.

## Justificativa das telas e padrões

- [x] Cada tela importante possui relação com uma tarefa/objetivo rastreável.
- [x] Dashboard, se existente, apoia uma decisão ou necessidade de acompanhamento concreta. *(Não criado — fora do recorte.)*
- [x] Relatórios apresentam informação necessária para uma tarefa, e não apenas “números porque existem”.
- [x] Histórico, busca, ordenação e filtros possuem volume/uso que justifique sua existência. *(Não criados — fora do recorte.)*
- [x] Telas administrativas existem porque há atividades reais de configuração, governança ou operação. *(Não criadas — fora do recorte.)*
- [x] CRUDs representam entidades e tarefas relevantes; não foram criados apenas para aumentar o número de telas. *(Não criados — fora do recorte.)*
- [x] Gestão de usuários/perfis/permissões, se existente, considera papéis, prevenção de erros e consequências de alterações. *(Não criada — fora do recorte.)*
- [x] Telas de configuração não expõem complexidade técnica desnecessária sem justificativa.
- [x] Estados de carregamento, processamento, vazio, erro, sucesso e recuperação foram considerados quando pertinentes.
- [x] Comparações e visualizações ajudam o usuário a interpretar diferenças e tomar decisões.

## Avaliação

- [ ] Cada avaliador heurístico percorreu todas as telas/estados relevantes. *(A01 Kawan concluída no HTML; faltam A02 Gabriel e A03 Alexandre e confirmação no Figma.)*
- [ ] As 10 heurísticas foram explicitamente verificadas por cada avaliador. *(Concluída por A01; faltam A02 e A03.)*
- [x] Violações têm evidência, localização, severidade justificada e recomendação. *(Preliminares V01–V03 e ficha A01 preenchidas.)*
- [ ] Problemas duplicados entre avaliadores foram consolidados sem apagar a autoria da descoberta. *(Aguarda A02 e A03.)*
- [ ] O número final de usuários observados atende ao exigido pela disciplina. *(Pendente: 3 participantes externos U01–U03.)*
- [ ] Participantes finais representam o público-alvo e não são membros da equipe. *(Pendente de recrutamento e execução.)*
- [x] Se o perfil profissional é difícil de recrutar, qualquer uso de participante aproximado/proxy foi justificado e registrado como limitação. *(Critérios e limitações definidos nas Entregas 12 e 14; justificativa individual de cada proxy pendente do recrutamento.)*
- [x] Tarefas de teste possuem cenário, instrução neutra e critério de sucesso.
- [ ] Tempos, erros, ajudas, sucesso e satisfação foram registrados por usuário/tarefa. *(Planilha e fichas prontas; coleta pendente.)*
- [x] A avaliação mede a **interação com o protótipo**, e não tenta substituir a avaliação técnica/científica do algoritmo ou modelo do TCC.
- [ ] A conclusão identifica padrões, problemas prioritários e mudanças concretas. *(Aguarda coleta da Entrega 14.)*

## Ética e privacidade

- [x] Há consentimento compatível com a atividade realizada.
- [x] O participante sabe que pode interromper a participação.
- [x] Dados pessoais desnecessários não foram coletados/publicados.
- [x] Vídeos/áudios/imagens de participantes só são compartilhados com autorização. *(Regra definida no termo e no protocolo; sem gravações ainda.)*
- [x] Resultados públicos usam IDs anônimos (`U01`, `U02`...).

## Comunicação e INOVA

- [x] A equipe consegue explicar o projeto sem depender apenas de jargão técnico.
- [x] O protótipo demonstra como uma pessoa poderia usar ou se beneficiar da contribuição técnica.
- [x] A apresentação deixa claro o que é resultado real do TCC e o que é hipótese/protótipo da disciplina.
- [x] O potencial de aplicação, mercado ou extensão é apresentado sem afirmar validações que ainda não ocorreram.

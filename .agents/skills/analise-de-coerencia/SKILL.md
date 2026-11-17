---
name: analise-de-coerencia
description: Audita a coerência documental do repositório, gera relatórios HTML com tickets numerados e atualiza seu acompanhamento quando solicitado.
---

# Análise de coerência

Faça uma auditoria documental somente de leitura. Entregue o diagnóstico em HTML e preserve os arquivos analisados para uma etapa posterior de revisão.

## Escopo

- Trate os documentos indicados pelo usuário como foco principal. Quando nenhum documento for indicado, compare todos os documentos do repositório.
- Considere o repositório inteiro como contexto em toda execução. Inventarie todos os arquivos, leia todo texto produzido para o projeto e inspecione arquivos não textuais quando forem citados ou puderem mudar a conclusão. Registre no relatório qualquer categoria excluída e o motivo.
- Descubra a proposta do projeto e a autoridade relativa dos documentos a partir do próprio conteúdo. Use objetivos, decisões explícitas, datas, estados, referências e rastreabilidade. A ordem dos nomes dos arquivos não determina sozinha qual documento deve mudar.
- Use pesquisa na web quando ela ajudar a verificar uma afirmação, fonte ou prática externa. Cite cada fonte externa perto da conclusão que ela sustenta.
- Trabalhe sem entrevista inicial. Investigue o material disponível e avance. Quando a evidência não permitir uma conclusão segura, marque o ticket como `Precisa de revisão` e explique o que falta confirmar.

## Procedimento

1. **Cobrir o repositório.** Faça um inventário completo. Classifique arquivos como fonte textual, apoio, mídia, artefato gerado ou dependência. Leia cada fonte textual produzida para o projeto. A cobertura termina quando todo arquivo estiver lido, inspecionado ou incluído em uma categoria de exclusão justificada.

2. **Mapear o que cada documento afirma.** Extraia propósito, escopo, decisões, fatos, hipóteses, dúvidas, recomendações, público, terminologia e dependências. Anote a seção ou outra localização precisa de cada afirmação relevante. O mapa termina quando toda conclusão potencial pode ser rastreada a passagens concretas.

   Distinga decisões e conteúdo preenchido de instruções, exemplos e campos pendentes do template. Use relatórios anteriores como histórico de auditoria; revalide seus achados nos documentos atuais antes de repeti-los.

3. **Comparar.** Procure contradições, omissões, mudanças silenciosas de escopo, hipóteses tratadas como fatos, requisitos sem origem, recomendações sem apoio, terminologia incompatível e decisões que ignoram o contexto do projeto. Separe desalinhamento real de informação nova compatível e de diferença apenas editorial.

   Abra tickets com evidência e efeito concreto. Para contradições, cite afirmações incompatíveis no mesmo contexto. Para omissões, identifique a exigência ou dependência não atendida e considere o estágio de elaboração do documento. Para recomendações sem apoio, explique qual fundamentação é necessária e por quê. Preferências editoriais só justificam tickets quando prejudicam a compreensão ou violam uma convenção explícita.

4. **Investigar incertezas.** Consulte referências internas e, quando trouxer ganho real, fontes externas. Evidência externa verifica fatos e práticas; decisões explícitas do projeto continuam sendo definidas pelo repositório. Se interpretações razoáveis ainda competirem, mantenha o achado e marque `Precisa de revisão`.

5. **Agrupar e numerar os tickets.** Agrupe ocorrências com a mesma causa e correção conjunta em um ticket, citando todos os documentos afetados. Antes de criar tickets, procure nos relatórios da pasta `analises de coerencia` o maior identificador `AC-###`, inclusive em comentários de tickets retirados. Consulte também `análises de coerência` se essa pasta existir, para preservar históricos anteriores. Comece no número seguinte, ou em `AC-001` se não houver histórico. Cada novo ticket recebe um ID único. Quando um achado anterior persistir ou reaparecer, crie um novo ticket com referência ao ID e relatório anteriores, explicando a situação atual. Preserve os relatórios anteriores durante uma nova auditoria.

6. **Escrever cada ticket.** Inclua gravidade, confiança na conclusão, status de acompanhamento, evidências localizáveis, efeito sobre a coerência e mudança sugerida no documento que fizer mais sentido para a proposta do projeto. Use os critérios abaixo. Para cada recomendação analisada, verifique se é possível relacioná-la a alguma seção, atividade, hipótese ou decisão de um documento de base. Quando a relação não existir, apresente a recomendação como exploratória e sujeita a validação.

7. **Gerar o HTML.** Crie o relatório em `analises de coerencia/DD-MM-YYYY-HH-MM.html`, usando a data, hora e fuso locais. Use hífen entre hora e minuto no nome do arquivo; reserve `HH:MM` para o texto do relatório. Isso evita caracteres problemáticos em links locais e visualizadores. Se o nome já existir, acrescente `-02`, `-03` e assim por diante, sem sobrescrever relatórios. Coloque no começo do documento a assinatura `modelo (nível de raciocínio) no harness`, com os dados reais da execução. Quando algum dado não estiver disponível, escreva `não informado` em seu lugar.

8. **Verificar.** Valide a estrutura do HTML, os tickets e a preservação dos arquivos analisados. Quando houver navegador disponível e permitido, abra o arquivo pelo mecanismo de preview que será entregue ao usuário e confira conteúdo visível e leitura em uma largura estreita. Um parser HTML não comprova renderização nem funcionamento do link. Se a verificação visual estiver indisponível ou bloqueada, registre essa limitação e não declare que o preview foi verificado. Confira a continuidade e a unicidade dos IDs. A execução termina quando o relatório existe, todas as fontes do escopo foram contabilizadas e cada conclusão está sustentada ou marcada para revisão.

## Critérios dos tickets

A gravidade expressa o impacto, independentemente da confiança na conclusão:

- `Alta`: conflito que altera escopo ou público, ou invalida uma atividade ou conclusão central.
- `Média`: inconsistência que prejudica a interpretação ou a rastreabilidade sem invalidar o trabalho central.
- `Baixa`: problema localizado de compreensão ou de cumprimento de uma convenção explícita.

Use `Sustentado` quando a evidência justificar a conclusão e `Precisa de revisão` quando faltar confirmação ou houver interpretações concorrentes. Neste último caso, registre o que falta decidir ou verificar.

## Acompanhamento

Registre o status de cada ticket no próprio HTML, separado da gravidade e da confiança:

- `Pendente`: status inicial; a mudança ainda não foi concluída. Aplicações parciais permanecem pendentes, com nota do que falta.
- `Aplicado`: a correção foi verificada nos documentos ou o usuário informou que a aplicou. Registre a data e a evidência localizável, ou atribua explicitamente a confirmação ao usuário.
- `Descartado`: o usuário decidiu não aplicar a sugestão ou a reavaliação mostrou que ela não procede. Registre data e justificativa, preservando o ticket.

Derive o status da análise dos tickets, recalculando-o a cada atualização:

- `Sem achados`: nenhum ticket.
- `Pendente`: todos os tickets pendentes.
- `Em andamento`: há tickets pendentes e outros aplicados ou descartados.
- `Aplicada`: todos os tickets aplicados.
- `Encerrada`: nenhum ticket pendente e pelo menos um descartado.

Quando o usuário pedir para marcar tickets ou uma análise inteira, atualize o HTML correspondente. Marcar a análise como aplicada equivale a marcar todos os seus tickets como aplicados; pedidos explícitos de marcação valem como confirmação do usuário. Preserve justificativas anteriores e registre mudanças de status com data e motivo, inclusive reaberturas. Relatórios antigos sem status começam com acompanhamento pendente, sem inferir que as sugestões foram aplicadas.

O acompanhamento persiste no arquivo versionado. Uma atualização de status modifica apenas o relatório; a aplicação das correções nos documentos depende de um pedido para realizá-las.

## Conteúdo do relatório

O HTML deve ser autocontido, sem scripts ou folhas de estilo externas. Use HTML semântico, CSS inline, tema claro e escuro conforme o sistema, contraste legível e tabelas responsivas.

Inclua no mínimo:

- assinatura do agente no início;
- data, escopo e status derivado da análise, com contagem de tickets por status;
- conclusão geral;
- cobertura com caminhos relativos dos documentos lidos e materiais inspecionados, materiais inacessíveis e exclusões justificadas por categoria; materiais inacessíveis são limitações, não fontes verificadas;
- pontos que já estão alinhados;
- tickets `AC-###`, organizados para leitura rápida;
- limitações da análise e fontes externas usadas.

Use nomes relativos ao repositório e seções para localizar evidências. Não exponha caminhos absolutos da máquina. Recomendações devem dizer qual documento mudaria e o que mudaria, sem editar o documento.

## Revisão de um relatório existente

Quando o usuário pedir ajustes no HTML, edite apenas o relatório indicado. Preserve os IDs dos tickets mantidos. Ao retirar um ticket, conserve seu identificador em um comentário HTML no formato `<!-- ticket-retirado: AC-### -->`; isso impede que o número seja reutilizado em relatórios futuros.

## Correção de abertura do relatório

Quando o usuário relatar preview em branco, diferencie arquivo vazio ou malformado, falha de resolução do caminho e falha do visualizador. Não atribua a causa ao CSS ou ao nome sem evidência. Se renomear um relatório para compatibilidade, preserve conteúdo, IDs e acompanhamento, atualize referências sob controle da tarefa e entregue o novo link. Não crie uma nova auditoria nem marque tickets como aplicados por corrigir a abertura.

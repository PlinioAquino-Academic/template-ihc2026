// Na conta da equipe, execute criarFormularioReposicao em script.google.com.
// O registro da execução mostra os links de edição e de resposta.
function criarFormularioReposicao() {
  const trava = LockService.getScriptLock();
  trava.waitLock(30000);
  try {
    const propriedades = PropertiesService.getScriptProperties();
    const id = propriedades.getProperty('formularioI01');
    const formulario = id ? FormApp.openById(id) : FormApp.create('Estoque com ML — Rotina de reposição', false);
    if (!id) propriedades.setProperty('formularioI01', formulario.getId());
    if (!propriedades.getProperty('i01Pronto')) {
      if (formulario.isPublished() || formulario.getResponses().length) {
        throw new Error('O rascunho já foi publicado ou recebeu respostas. Confira no editor antes de continuar: ' + formulario.getEditUrl());
      }
      montarI01(formulario);
      propriedades.setProperty('i01Pronto', 'sim');
    }
    if (!propriedades.getProperty('i01Publicado')) {
      formulario.setPublished(true);
      propriedades.setProperty('i01Publicado', 'sim');
    }
    console.log('Edição (equipe): ' + formulario.getEditUrl());
    console.log('Resposta: ' + formulario.getPublishedUrl());
  } finally {
    trava.releaseLock();
  }
}

function montarI01(formulario) {
  const contato = 'victor.merker.bindaa@gmail.com';
  formulario.setDescription([
    'Somos Paulo e Victor, estudantes de IHC da FEI. Queremos entender como as pessoas decidem o que comprar para repor o estoque de um pequeno comércio. O tempo previsto é de 10 a 15 minutos.',
    'Participar é voluntário. Falar de dificuldades pode causar desconforto. Você pode pular as perguntas depois da triagem ou fechar a página antes de enviar. A pesquisa não avalia seu desempenho e não oferece benefício individual garantido.',
    'Não pedimos nome, e-mail, valores financeiros nem dados de clientes. Só a equipe consulta as respostas individuais e as apaga até 90 dias após a avaliação final da disciplina. O relatório apresenta uma síntese sem identificação.',
    'Se quiser poder retirar sua resposta depois de enviar, guarde o código informado na seção de perfil. Dúvidas ou retirada enquanto for possível localizar o registro: ' + contato + '.'
  ].join('\n\n'));
  formulario.setCollectEmail(false).setLimitOneResponsePerUser(false).setPublishingSummary(false)
    .setShuffleQuestions(false).setShowLinkToRespondAgain(false).setAllowResponseEdits(false)
    .setConfirmationMessage('Obrigado por participar! Guarde seu código, caso tenha usado um. Para falar com a equipe ou pedir a retirada da resposta enquanto ela puder ser localizada, escreva para ' + contato + '.');

  // Retoma a construção de um rascunho incompleto sem excluir itens nem duplicá-los.
  const existentes = formulario.getItems();
  let posicao = 0;
  function item(tipo, titulo) {
    const anterior = existentes[posicao++];
    if (!anterior) return formulario['add' + tipo + 'Item']().setTitle(titulo);
    const anteriorDoTipo = anterior['as' + tipo + 'Item']();
    if (anteriorDoTipo.getTitle() && anteriorDoTipo.getTitle() !== titulo) {
      throw new Error('O rascunho contém uma alteração na posição ' + posicao + '. Confira o formulário antes de retomar.');
    }
    return anteriorDoTipo.setTitle(titulo);
  }
  function pagina(titulo) { return item('PageBreak', titulo); }
  function escolha(titulo, opcoes) {
    const pergunta = item('MultipleChoice', titulo).setRequired(false);
    if (opcoes) pergunta.setChoiceValues(opcoes);
    return pergunta;
  }
  function varias(titulo, opcoes) {
    return item('Checkbox', titulo).setChoiceValues(opcoes).showOtherOption(true).setRequired(false);
  }
  function aberta(titulo) { return item('ParagraphText', titulo).setRequired(false); }
  function destinos(pergunta, pares) {
    pergunta.setChoices(pares.map(function(par) { return pergunta.createChoice(par[0], par[1]); }));
  }

  const aceite = escolha('Você leu as informações acima e aceita participar?').setRequired(true);
  const idade = pagina('Idade');
  const maior = escolha('Você tem 18 anos ou mais?').setRequired(true);
  const triagem = pagina('Experiência recente');
  const elegivel = escolha('Q01. Nos últimos três meses, você participou da decisão de comprar produtos para repor o estoque de um pequeno comércio?').setRequired(true);

  const perfil = pagina('Sua participação no comércio').setHelpText('A partir daqui, todas as perguntas são opcionais.');
  item('Text', 'Código para localizar sua resposta (opcional)').setRequired(false)
    .setHelpText('Use o código do convite ou invente um código de oito letras e números, sem dados pessoais. Anote-o. Sem um código, a equipe pode não conseguir localizar sua resposta para retirá-la.');
  escolha('Como está preenchendo?', ['Por conta própria', 'Alguém está lendo as perguntas para mim']);
  varias('Q02. O que você faz quando é preciso repor produtos?', ['Decido o que comprar', 'Reúno informações', 'Confiro o estoque', 'Aprovo o valor da compra']);
  escolha('Q03. Há quanto tempo você participa dessas decisões?', ['Menos de 6 meses', 'De 6 meses a menos de 2 anos', 'De 2 a 5 anos', 'Mais de 5 anos']);
  escolha('Q04. Qual é a sua faixa etária?', ['18 a 29 anos', '30 a 44 anos', '45 a 59 anos', '60 anos ou mais', 'Prefiro não responder']);
  const registros = escolha('Q05. Você mantém ou consulta algum registro de estoque?');

  const fontes = pagina('Seus registros de estoque');
  varias('Q05a. Onde você registra ou consulta o estoque?', ['Caderno ou papel', 'Planilha', 'Sistema de vendas ou estoque', 'Mensagens', 'Plataforma de vendas on-line']);
  const encontrou = escolha('Q11. No último mês, você encontrou alguma diferença entre o que estava registrado e o estoque disponível?');
  const diferenca = pagina('A última diferença');
  aberta('Q11a. O que você fez ao encontrar essa diferença?').setHelpText('Pode descrever em uma frase, sem citar nomes.');

  const aparelhos = pagina('Uso de dispositivos');
  const dispositivo = escolha('Q06. Qual dispositivo você mais usa nessa atividade?');
  const digital = pagina('Uso de ferramentas digitais');
  escolha('Q06a. Quando precisa de internet no trabalho, consegue se conectar?', ['Sempre', 'Na maioria das vezes', 'Poucas vezes', 'Nunca', 'Não preciso de internet', 'Não sei']);
  escolha('Q07. Como você usa as ferramentas digitais de estoque?', ['Sem ajuda', 'Com ajuda só em situações novas', 'Com ajuda frequente', 'Outra pessoa faz essa parte', 'Não uso essas ferramentas']);

  const rotina = pagina('A última reposição');
  escolha('Q08. Com que frequência você decide reposições?', ['Diariamente', 'Algumas vezes por semana', 'Semanalmente', 'Quinzenalmente', 'Mensalmente ou menos', 'Quando surge a necessidade, sem intervalo fixo']).showOtherOption(true);
  aberta('Q09. Pense na última vez em que precisou repor um produto. Que informações usou para decidir?');
  pagina('Sobre essa decisão');
  aberta('Q09a. O prazo do fornecedor ou os recursos disponíveis fizeram diferença nessa decisão? De que maneira?').setHelpText('Se não fizeram diferença, pode dizer isso. Não informe valores financeiros.');
  escolha('Q10. No último mês, quantas vezes precisou parar uma análise de reposição para atender outra demanda?', ['Nenhuma', '1 a 2 vezes', '3 a 5 vezes', '6 vezes ou mais', 'Não fiz essa análise', 'Não lembro']);
  aberta('Q12. Como você registra a decisão para consultar depois, se costuma fazer isso?');
  aberta('Q12a. Depois que os produtos chegam, como verifica se a reposição foi adequada, se faz esse acompanhamento?');
  item('Text', 'Q13. Há 6 unidades de um produto, e 2 delas já estão reservadas. Quantas estão livres para novas vendas?')
    .setRequired(false).setHelpText('Escreva um número ou “não sei”.');
  aberta('Q14. Você lê “Estimativa de venda: 10 unidades nos próximos 7 dias. Os valores reais podem variar”. O que essa frase significa para você?');

  pagina('Sua opinião').setHelpText('Você pode deixar qualquer item em branco.');
  aberta('Q14a. Que outras informações você procuraria antes de decidir uma compra, se procuraria alguma?');
  aberta('Q14b. Quando essa estimativa ajudaria no seu trabalho? Em que situação ela seria pouco útil?');
  const importancia = ['1 — Nada importante', '2 — Pouco importante', '3 — Moderadamente importante', '4 — Importante', '5 — Muito importante', 'Não se aplica'];
  ['Entender de onde vieram os valores', 'Poder corrigir uma decisão', 'Terminar a tarefa rapidamente', 'Consultar decisões anteriores'].forEach(function(aspecto) {
    escolha('Q15. Que importância tem para você: ' + aspecto.toLowerCase() + '?', importancia);
  });
  aberta('Q16a. Ao ler informações de estoque, há algo difícil de entender? Se houver, o quê?');
  varias('Q16. Como você prefere aprender a usar uma ferramenta nova?', ['Ver alguém demonstrar', 'Ler instruções', 'Ver um vídeo', 'Experimentar com exemplos']).setHelpText('Se ainda não sabe, pode escrever “não sei” em Outra ou pular.');
  aberta('Q17. Na rotina de reposição, o que mais gostaria de melhorar, se houver algo?');
  const sair = pagina('Fim da participação').setHelpText('Obrigado pelo interesse. Sua participação termina aqui. Pode fechar esta página sem enviar. Dúvidas: ' + contato + '.');

  destinos(aceite, [['Sim, aceito', idade], ['Não aceito', sair]]);
  destinos(maior, [['Sim', triagem], ['Não', sair], ['Prefiro não informar', sair]]);
  destinos(elegivel, [['Sim', perfil], ['Não', sair], ['Não sei ou prefiro não informar', sair]]);
  destinos(registros, [['Sim', fontes], ['Não mantenho nem consulto registros', aparelhos], ['Não sei', aparelhos], ['Prefiro não responder', aparelhos]]);
  destinos(encontrou, [['Sim', diferenca], ['Não', aparelhos], ['Não sei', aparelhos], ['Prefiro não responder', aparelhos]]);
  destinos(dispositivo, [['Celular', digital], ['Computador ou notebook', digital], ['Tablet', digital], ['Outro dispositivo digital', digital], ['Não uso dispositivo digital nessa atividade', rotina], ['Prefiro não responder', rotina]]);
  // Cada quebra controla a saída da página ANTERIOR quando a pergunta de salto é pulada.
  fontes.setGoToPage(aparelhos);
  diferenca.setGoToPage(aparelhos);
  digital.setGoToPage(rotina);
  sair.setGoToPage(FormApp.PageNavigationType.SUBMIT);
}

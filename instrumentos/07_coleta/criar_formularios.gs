// Entrega 7: consulta dos formulários existentes, sem reproduzir perguntas de I02.
// Não cria instrumentos, não altera respostas nem publica conteúdo.
function consultarInstrumentosEntrega7() {
  const ids = ['1oxMqGPpMAJ3TN2_hBkf4w9bmwdtfrLn6T1TFNv9LkFQ',
               '1_yuRgM6ilwdGepLaH4PZddhkT0oRkj6iZUr1WPa1Ku8'];
  ids.forEach(id => {
    const form = FormApp.openById(id);
    Logger.log(form.getTitle() + ' | EDITAR: ' + form.getEditUrl() +
               ' | RESPONDER: ' + form.getPublishedUrl());
  });
}

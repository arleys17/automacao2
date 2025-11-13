Feature: Enviar mensagem no WhatsApp Web
  Como usuário
  Quero acessar o WhatsApp Web
  Para enviar uma mensagem automaticamente

  Scenario: Enviar mensagem para um contato específico
    Given que estou no WhatsApp Web
    When eu pesquiso pelo contato "Marcio"
    And envio a mensagem "Olá, esta é uma mensagem automática!"
    Then a mensagem deve ser enviada com sucesso

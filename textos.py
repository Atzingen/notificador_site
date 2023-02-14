def gera_lista_notificadores(notifications):
    lista_notificadores = 'Sites com notificadores cadastrados:\n\n'
    for notification in notifications:
        lista_notificadores += f'➡️Identificador: {notification[0]} \n🌐URL: {notification[1]}\n\n'
    return lista_notificadores


help_message = '''*✅Mensagem de Ajuda do Bot Notificador✅*

🤖 Possíveis comandos 🤖:

➡️ /add\_notificador *identificador\-do\-site* **url\-do\-site** Adiciona um notificador ✅

➡️ /list\_notificador Lista os notificadores cadastrados 🌐

➡️ /dell\_notificador *nome do notificador* Deleta notificador ❌

➡️ /dell\_account Deleta sua conta ❌ 🏴‍☠️

➡️ /help Ajuda com os comandos ℹ️

'''

not_registered = '''*❌Você não está registrado no bot❌*'''

add_notificador_incorreto = '''*❌Erro no formato do comando /add\_notificador ❌*

O formato correto deve ser: 

/add\_notificador *identificador\-do\-site* **url\-do\-site**

➡️ A url deve ser um site válido e o identificador deve ser um texto que identifique o site\.
➡️ Ambos não podem conter espaços\.
➡️ Deve existir um espaço simples entre o comando e o primeiro parâmetro e com o segundo\.
'''

usuario_nao_registrado = '''*🤖 Boas Vindas ao Bot Notificador 🤖*
Com este bot você pode receber notificações de sites que você deseja acompanhar e ser avisado quando houver alguma alteração\.

Você Ainda não está registrado no bot ❌
Para se cadastrar, basta adicionar um notificador com o comando:

➡️ /add\_notificador *identificador\-do\-site* **url\-do\-site**

Após cadastrado, você será avisado via mensagem quando o site for alterado\.
Cadastre uma notificação e bom uso \! ✅
'''

dell_notificador_incorreto = '''*❌Formato errado no envio do comando /dell\_notificador ❌*

Por favor utilize o formato:

/dell\_notificador *nome\_do\_notificador*

Use apenas um espaço simples entre o comando e o nome do notificador\.
'''

txt_sem_notificadores = '''*❌Não há notificadores cadastrados❌*

🤖 Para cadastrar um notificador utilize o comando:

/add\_notificador *identificador\-do\-site* **url\-do\-site**

➡️ A url deve ser um site válido e o identificador deve ser um texto que identifique o site\.
➡️ Ambos não podem conter espaços\.
➡️ Deve existir um espaço simples entre o comando e o primeiro parâmetro e com o segundo\.
'''

delete_account_success = '''🏴‍☠️ Sua conta foi apagada 🏴‍☠️
Todos os notificadores cadastrados foram apagados e você não receberá mais mensagens e avisos deste BOT\.

Obrigado por utilizar o BOT Notificador\.

Volte sempre que quiser\.
'''

delete_account_confirm = '''🏴‍☠️ Você solicitou um pedido de apagar a conta 🏴‍☠️

Ao apagar a conta, todos os notificadores cadastrados serão apagados.
Caso deseje realmente apagar a conta, confirme (ou cancele) o pedido no botão abaixo.
'''


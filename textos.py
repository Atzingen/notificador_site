help_message = '''*✅Mensagem de Ajuda do Bot Notificador✅*

🤖 Possíveis comandos 🤖:

➡️ /help Ajuda com os comandos ℹ️
➡️ /list\_notificador Lista os notificadores cadastrados 🌐
➡️ /dell\_notificador *nome do notificador* Deleta um notificador ❌
➡️ /add\_notificador *url\_do\_site* *identificador\_do\_site* Adiciona um notificador ✅
➡️ /dell\_account Deleta sua conta ❌ 🏴‍☠️

'''

add_notificador_incorreto = '''*❌Erro no formato do comando /add\_notificador ❌*

O formato correto deve ser: 

/add\_notificador *url\_do\_site* *identificador\_do\_site*

➡️ A url deve ser um site válido e o identificador deve ser um texto que identifique o site\.
➡️ Ambos não podem conter espaços\.
➡️ Deve existir um espaço simples entre o comando e o primeiro parâmetro e com o segundo\.
'''

dell_notificador_incorreto = '''*❌Formato errado no envio do comando /dell\_notificador ❌*

Por favor utilize o formato:

/dell\_notificador *nome\_do\_notificador*

Use apenas um espaço simples entre o comando e o nome do notificador\.
'''

txt_sem_notificadores = '''*❌Não há notificadores cadastrados❌*

🤖 Para cadastrar um notificador utilize o comando:

/add\_notificador *url\_do\_site* *identificador\_do\_site*

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

def gera_lista_notificadores(notifications):
    lista_notificadores = 'Sites com notificadores cadastrados:\n'
    for notification in notifications:
        lista_notificadores += f'Identificador: {notification[0]} \n URL: {notification[1]}\n\n'
    return lista_notificadores
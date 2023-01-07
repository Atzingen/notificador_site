help_message = '''*Mensagem de Ajuda do Bot Notificador*

\#\# Possíveis comandos:

1\. /help Ajuda com os comandos
2\. /list\_notificador Lista os notificadores cadastrados
3\. /dell\_notificador *nome do notificador* Deleta um notificador

'''

add_notificador_incorreto = '''
\# Erro no formato do comando /add\_notificador

O formato correto deve ser: 

/add\_notificador *url\_do\_site* *identificador\_do\_site*

\- A url deve ser um site válido e o identificador deve ser um texto que identifique o site\.
\- Ambos não podem conter espaços\.
\- Deve existir um espaço simples entre o comando e o primeiro parâmetro e com o segundo\.
'''

dell_notificador_incorreto = '''*Formato errado no envio do comando /dell\_notificador*

Por favor utilize o formato:

/dell\_notificador *nome do notificador*

Use apenas um espaço simples entre o comando e o nome do notificador\.
'''

def gera_lista_notificadores(notifications):
    lista_notificadores = 'Sites com notificadores cadastrados:\n'
    for notification in notifications:
        lista_notificadores += f'Identificador: {notification[0]} \n URL: {notification[1]}\n\n'
    return lista_notificadores
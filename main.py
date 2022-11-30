import os
import asyncio
import hashlib
import requests
from dotenv import load_dotenv
import logging
import telegram
from telegram.ext import CommandHandler, CallbackContext, Updater
from telegram import Update

load_dotenv() 
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

BOT_TOKEN = os.getenv('BOT_TOKEN')
TEST_USER_ID = os.getenv('TEST_USER_ID')

site_url = 'http://www.finep.gov.br/chamadas-publicas/chamadapublica/702'

def get_site(site: str) -> str:
    '''
    Get site content and return its text as a string
    ''' 
    result = requests.get(site)
    return result.text

def calc_hash(text: str) -> str:
    '''
    Calculate hash of text
    '''
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def send_msg(msg: str, bot: telegram.Bot):
    bot.send_message(text=msg, chat_id=int(TEST_USER_ID))

# async def send_msg(msg):
#     bot = telegram.Bot(BOT_TOKEN)
#     async with bot:
#         await bot.send_message(text='Hi John!', chat_id=int(TEST_USER_ID))

# site = get_site(site_url)
# hash_text = calc_hash(site)

# bot = telegram.Bot(BOT_TOKEN)
# send_msg(hash_text)


def add_notificador(update: Update, context: CallbackContext):
    text = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def help_bot(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, 
    text='''Olá, eu sou o bot do notificador de atualizações em um site que você aguarda notícias. 
    Para adicionar uma nova notificação, digite:
    /add_notificador url_do_site identificador_do_site
    Onde a url deve ser um site válido e o identificador deve ser um texto que identifique o site.
    ''')

def dell_notificador(update: Update, context: CallbackContext):
    text = update.message.text
    notificadores = text.split(' ')
    if len(notificadores) > 1:
        notificador = notificadores[1]
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Notificador {notificador} deletado com sucesso!")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Não foi possível deletar o notificador.")

def list_notificador(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Lista de notificações:")

add_notificador_handler = CommandHandler('add_notificador', add_notificador)
help_bot_handler = CommandHandler('help', help_bot)
dell_notificador_handler = CommandHandler('dell_notificador', dell_notificador)
list_notificador_handler = CommandHandler('list_notificador', list_notificador)

updater = Updater(token=BOT_TOKEN, use_context=True)

dispatcher = updater.dispatcher
dispatcher.add_handler(add_notificador_handler)
dispatcher.add_handler(help_bot_handler)
dispatcher.add_handler(dell_notificador_handler)
dispatcher.add_handler(list_notificador_handler)

updater.start_polling()

# asyncio.run(send_msg(hash_text))
import os
from functools import partial
import logging
from dotenv import load_dotenv
import logging
from telegram.ext import CommandHandler, ApplicationBuilder, CallbackQueryHandler

from bot_functions import *

load_dotenv() 
logging.basicConfig(level=logging.INFO,
                    filename='bot.log',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

BOT_TOKEN = os.getenv('BOT_TOKEN')
TEST_USER_ID = os.getenv('TEST_USER_ID')

add_notificador_handler = CommandHandler('add_notificador', add_notificador)
help_bot_handler = CommandHandler('help', help_bot)
dell_notificador_handler = CommandHandler('dell_notificador', dell_notificador)
list_notificador_handler = CommandHandler('list_notificador', list_notificador)
dell_account_handler = CommandHandler('dell_account', dell_account)
button_handler = CallbackQueryHandler(button)

application = ApplicationBuilder().token(BOT_TOKEN).build()

application.add_handler(button_handler)
application.add_handler(help_bot_handler)
application.add_handler(add_notificador_handler)
application.add_handler(list_notificador_handler)
application.add_handler(dell_notificador_handler)
application.add_handler(dell_account_handler)

job_queue = application.job_queue
job_queue.run_repeating(buscador.check_updates_all,
                        interval=30, 
                        first=0)

application.run_polling()

import os
from functools import partial
import logging
from dotenv import load_dotenv
import logging
from telegram.ext import CommandHandler, ApplicationBuilder, \
     CallbackQueryHandler, MessageHandler, filters

os.makedirs('logs', exist_ok=True)

load_dotenv() 
logging.basicConfig(level=logging.INFO,
                    filename='logs/bot.log',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

from bot_functions import *
from db_manager import *

try:
    create_table()
except Exception as e:
    logging.warning(e)

BOT_TOKEN = os.getenv('BOT_TOKEN')
TEST_USER_ID = os.getenv('TEST_USER_ID')

logging.info('Bot started')

add_notificador_handler = CommandHandler('add_notificador', add_notificador)
help_bot_handler = CommandHandler('help', help_bot)
dell_notificador_handler = CommandHandler('dell_notificador', dell_notificador)
list_notificador_handler = CommandHandler('list_notificador', list_notificador)
dell_account_handler = CommandHandler('dell_account', dell_account)
button_handler = CallbackQueryHandler(button)
regular_text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, regular_text)

application = ApplicationBuilder().token(BOT_TOKEN).build()

application.add_handler(button_handler)
application.add_handler(help_bot_handler)
application.add_handler(add_notificador_handler)
application.add_handler(list_notificador_handler)
application.add_handler(dell_notificador_handler)
application.add_handler(dell_account_handler)
application.add_handler(regular_text_handler)
application.add_error_handler(error_function)

job_queue = application.job_queue
job_queue.run_repeating(buscador.check_updates_all,
                        interval=6000, 
                        first=10)

application.run_polling()

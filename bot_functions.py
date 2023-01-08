import logging
import telegram
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

import db_manager, buscador
import textos

def check_registered(func):
    async def wrapper(update: Update, context: CallbackContext):
        if not db_manager.check_user_exists(update.effective_chat.id):
            print("Usuário não registrado")
            return await context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=textos.usuario_nao_registrado,
                                     parse_mode=telegram.constants.ParseMode.MARKDOWN_V2)
        return await func(update, context)
    return wrapper

async def help_bot(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                             text=textos.help_message,
                             parse_mode=telegram.constants.ParseMode.MARKDOWN_V2)
 
async def add_notificador(update: Update, context: CallbackContext):
    text = update.message.text
    try:
        _, identificador_do_site, url_do_site = text.split(' ')
        site_text = buscador.get_site(url_do_site)
        hash_site = buscador.calc_hash(site_text)
        db_manager.insert_notification(user_id=update.effective_chat.id, 
                                       site_name=identificador_do_site, 
                                       site_url=url_do_site, 
                                       site_hash=hash_site)
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=f"Notificador {identificador_do_site} adicionado com sucesso!")	
    except Exception as e:
        logging.debug(text)
        logging.debug(e)
        await context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text=textos.add_notificador_incorreto,
                                 parse_mode=telegram.constants.ParseMode.MARKDOWN_V2)

@check_registered   
async def dell_notificador(update: Update, context: CallbackContext):
    text = update.message.text
    notificadores = text.split(' ')
    if len(notificadores) > 1:
        notificador = notificadores[1]
        db_manager.delete_notification(update.effective_chat.id, notificador)
        await context.bot.send_message(chat_id=update.effective_chat.id, 
                                       text=f"Notificador {notificador} deletado com sucesso!")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, 
                                       text=textos.dell_notificador_incorreto,
                                       parse_mode=telegram.constants.ParseMode.MARKDOWN_V2)

@check_registered   
async def dell_account(update: Update, context: CallbackContext):
    buttons = [
        [InlineKeyboardButton("✅ Sim", callback_data="Sim"),
         InlineKeyboardButton("❌ Não", callback_data="Não")],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   reply_markup=reply_markup,
                                   text=textos.delete_account_confirm)

@check_registered   
async def list_notificador(update: Update, context: CallbackContext):
    notifications = db_manager.get_notifications_list(update.effective_chat.id)
    txt_notificadores = textos.gera_lista_notificadores(notifications)
    if txt_notificadores:
        await context.bot.send_message(chat_id=update.effective_chat.id, 
                                    text=txt_notificadores)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, 
                                    text=textos.txt_sem_notificadores,
                                    parse_mode=telegram.constants.ParseMode.MARKDOWN_V2)

async def button(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data
    if data == "Sim":
        db_manager.delete_user(update.effective_chat.id)
        await context.bot.send_message(chat_id=update.effective_chat.id, 
                                       text=textos.delete_account_success,
                                       parse_mode=telegram.constants.ParseMode.MARKDOWN_V2)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, 
                                       text=f"You clicked button {data}.")
import re
import requests
import hashlib
import logging
from telegram.ext import CallbackContext

import db_manager

logging.basicConfig(level=logging.INFO,
                    filename='bot.log',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def formaturl(url: str):
    '''
    Add http:// or https to url if it doesn't have it
    '''
    if not re.match('(?:http|ftp|https)://', url):
        return 'http://{}'.format(url)
    return url

def get_site(site: str) -> str:
    '''
    Get site content and return its text as a string
    ''' 
    result = requests.get(formaturl(site))
    return result.text

def calc_hash(text: str) -> str:
    '''
    Calculate hash of text
    '''
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def verify_site(site: str, hash_site: str) -> bool:
    '''
    Verify if site has changed
    '''
    site_text = get_site(site)
    hash_site_text = calc_hash(site_text)
    return hash_site_text == hash_site

async def check_updates_all(context: CallbackContext):
    logging.debug('check_updates_all Chamado')
    base = db_manager.get_all_sites()
    notify = []
    for user_id, site_name, site_url, hash_site in base:
        if not verify_site(site_url, hash_site):
            logging.debug(f'O site {site_name} foi alterado! - id = {user_id}')
            notify.append((user_id, site_url))
            db_manager.delete_notification(user_id, site_name)
            await context.bot.send_message(chat_id=int(user_id), 
                          text=f'🤖 Boa Notícia 🤖 \n\n➡️ O site {site_name} foi alterado!\n\nAcesse {site_url} para conferir!')
    logging.debug(notify)
    
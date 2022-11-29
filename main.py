
import os
import asyncio
import telegram
import requests
import hashlib
from dotenv import load_dotenv
import logging

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

def send_msg(msg: str):
    bot = telegram.Bot(BOT_TOKEN)
    bot.send_message(text='Hi John!', chat_id=int(TEST_USER_ID))

# async def send_msg(msg):
#     bot = telegram.Bot(BOT_TOKEN)
#     async with bot:
#         await bot.send_message(text='Hi John!', chat_id=int(TEST_USER_ID))

site = get_site(site_url)
hash_text = calc_hash(site)

send_msg(hash_text)

# asyncio.run(send_msg(hash_text))
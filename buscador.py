import requests
import hashlib

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
import buscador

def test_foo_bar():
   assert True

def test_foo_bar2():
   assert True

def test_formaturl():

    txt_formated = buscador.formaturl('www.google.com')
    assert txt_formated == 'https://www.google.com' or \
           txt_formated == 'http://www.google.com'

    txt_formated = buscador.formaturl('http://www.google.com')
    assert txt_formated == 'https://www.google.com' or \
           txt_formated == 'http://www.google.com'

def test_get_site():
    sites = ['www.google.com', 
             'http://www.google.com', 
             'https://www.google.com',
             'terra.com.br',
             'http://terra.com.br',
             'https://terra.com.br',
             'youtube.com']
    for site in sites:
        txt_site = buscador.get_site(site)
        assert len(txt_site) > 500
    
def test_calc_hash():
    txt1 = 'teste'
    txt2 = 'teste2'
    txt3 = 'teste3'

    hash1 = buscador.calc_hash(txt1)
    hash2 = buscador.calc_hash(txt2)
    hash3 = buscador.calc_hash(txt3)

    assert hash1 == hash1
    assert hash2 == hash2
    assert hash3 == hash3
    assert hash1 != hash2
    assert hash1 != hash3
    assert hash2 != hash3

def test_verify_site():
    site = 'https://codewithrockstar.com/code'
    site_text = buscador.get_site(site)
    hash_site_text = buscador.calc_hash(site_text)
    assert buscador.verify_site(site, hash_site_text)
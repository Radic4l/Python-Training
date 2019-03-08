# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

# Url cible
url = 'http://localhost/mediawiki/index.php'
balises = ['h1','h2','h3','h4','h5','h6','div','button','span','a','ul','li','input','form']

# Configurations du dictionnaire de proxy
http_proxy = 'http://'
https_proxy = 'https://'
ftp_proxy = 'ftp://'
proxyDict = {'http': http_proxy, 'https': https_proxy, 'ftp': ftp_proxy}

reponse = requests.get(url) # Ajouter proxies=proxyDict en second parametre si besoins
content = reponse.content
# print(content)

parser = BeautifulSoup(content, 'html.parser')
soup = parser.body
# print(body.prettify())
# print(body)

def get_id(parameters):
    for params in parameters:
        list_id = []
        for param in soup.find_all(params):
            id = param.get('id')
            if id != None:
                list_id.append(id)
            else:
                pass
        if len(list_id) == 0:
            pass
        else:
            print('\nLes IDs des balises {0} sont :'.format(params))
            print(list_id)

def get_class(parameters):
    for params in parameters:
        list_class = []
        for param in soup.find_all(params):
            _class = param.get('class')
            if _class != None:
                list_class.append(_class)
            else:
                pass
        if len(list_class) == 0:
            pass
        else:
            print('\nLes classes des balises {0} sont :'.format(params))
            print(list_class)


print('\n--------------------------------IDs-------------------------------------\n')
get_id(balises)
print('\n------------------------------CLASSES-----------------------------------\n')
get_class(balises)
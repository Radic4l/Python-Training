# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

# Url cible
url = ''
balises = ['h1','h2','h3','h4','h5','h6','div','button','span','a','ul','li','input','form']

# Configurations du dictionnaire de proxy
http_proxy = ''
https_proxy = ''
ftp_proxy = ''
proxyDict = {'http': http_proxy, 'https': https_proxy, 'ftp': ftp_proxy}

reponse = requests.get(url, proxies=proxyDict) # Ajouter proxies=proxyDict en second parametre si besoins
content = reponse.content
# print(content)

parser = BeautifulSoup(content, 'html.parser')
soup = parser.body
datas_text = 'D:/utilisateurs/adujardin/Documents/Python-Training/web-scraping/datas.txt'
f = open(datas_text, 'w')
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
            # f.write('ID list \n{0}'.format(list_id))

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
            # f.write('Class list \n{0}'.format(list_class))

def get_values(parameters):
    for params in parameters:
        list_values = []
        for param in soup.find_all(params):
            value = param.get('value')
            if value != None:
                list_values.append(value)
            else:
                pass
        if len(list_values) == 0:
            pass
        else:
            print('\nLes Values des balises {0} sont :'.format(params))
            print(list_values)
            # f.write('Value list \n{0}'.format(list_values))

def get_types(parameters):
    for params in parameters:
        list_types = []
        for param in soup.find_all(params):
            type = param.get('type')
            if type != None:
                list_types.append(type)
            else:
                pass
        if len(list_types) == 0:
            pass
        else:
            print('\nLes Types des balises {0} sont :'.format(params))
            print(list_types)
            # f.write('Types list \n{0}'.format(list_types))

print('\n--------------------------------IDs-------------------------------------\n')
get_id(balises)
print('\n------------------------------CLASSES-----------------------------------\n')
get_class(balises)
print('\n-------------------------------VALUES-----------------------------------\n')
get_values(balises)
print('\n--------------------------------Types-----------------------------------\n')
get_types(balises)
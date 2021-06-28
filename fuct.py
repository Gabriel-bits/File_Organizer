import os
import json

try:
    with open('config.json', 'r') as f:
        config = json.load(f)
except FileNotFoundError:
    pass

def load_dic():
    if os.path.exists('config.json'):
        with open('config.json', 'r') as f:
            config = json.load(f)
    return config

def verif():
    if os.path.exists('config.json'):
        return config['direct']
    else:
        return "Escolha seu diretorio aqui !"

def load_names():
    with open('config.json', 'r') as f:
        config = json.load(f)
    config.update({"Images-":'Images-'})
    config.update({"Videos-":'Videos-'})
    config.update({"Audios-":"Audios-"})
    config.update({"Codigo-":"Codigo-"})
    config.update({"Textos-":"Textos-"})
    config.update({"Pdf-":"Pdf-"})
    config.update({"Word documents-":"Word documents-"})
    config.update({"Spreadsheets-":"Spreadsheets-"})
    config.update({"Presentation files-":"Presentation files-"})
    config.update({"Executaveis-":"Executaveis-"})
    config = config
    return config


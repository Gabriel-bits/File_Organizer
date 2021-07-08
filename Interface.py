import PySimpleGUI as sg
import json
import os
from fuct import *

#Ler arquivo, se tiver o arquivo nao vai abrir nada e so executar

sg.SetGlobalIcon('favicon.ico')

try:
    with open('config.json', 'r') as f:
        config = json.load(f)
        print(config['direct'] + ' lendo')
    nome_dict = config['direct']


except FileNotFoundError:

    config = {
    'direct':None,
    'direct_inic':None, 
    'stado':1,
    'Codigo-':"Codigo-", 
    'Textos-':"Textos-", 
    'Pdf-': "Pdf-", 
    'Audios-':"Audios-", 
    'Images-':"Images-", 
    'Videos-':"Videos-", 
    'Zip-':"Compactados-",
    'Word documents-':"Word documents-", 
    'Spreadsheets-':"Spreadsheets-", 
    'Presentation files-':"Presentation files-", 
    'Executaveis-':"Executaveis-"
    }

print(config['stado'])

if config['stado'] == 1:

    def Apresent():
        sg.theme('Dark Blue2')
        layout = [
            [sg.Text('◄ Ola, seja bem vindo ►\r\rNesse app voce pode organizar uma pasta apenas escolhendo \ro diretorio da pasta ', size=(0,4))],
            [sg.Text()],
            [sg.Button('Avançar', bind_return_key=True), sg.Button('Cancelar')],
        ]
        return sg.Window('Inicio', layout=layout, finalize=True)

    def tela1():
        sg.theme('Dark Blue2')
        layout2 = [
            [sg.Text('Aponte um diretorio pra começar a organizar \ros arquivos.\r',size=(0, 2))],
            [sg.T()],
            [sg.Text('Diretorio:')],
            [sg.Input(default_text=verif() , key='direct'), sg.FolderBrowse()],
            [sg.Button('Ok', bind_return_key=True), sg.Button('Cancelar')]
        ]
        return sg.Window('Organizar', layout=layout2, finalize=True)          

    def tela2():
        sg.theme('Dark Blue2')
        if os.path.exists('config.json'):
            load_names()
        layout3 = [
            [sg.Text('◄ Finalização ►')],
            [sg.Text('Nome das pastas (fazer mudanças e extramamente opcional):')],
            [sg.Input(default_text=config["Images-"], size=(20, 0), k='-nome1-')],
            [sg.Input(default_text=config["Videos-"], size=(20, 0), k='-nome2-')],
            [sg.Input(default_text=config["Audios-"], size=(20, 0), k='-nome3-')],
            [sg.Input(default_text=config["Codigo-"], size=(20, 0), k='-nome4-')],
            [sg.Input(default_text=config["Textos-"], size=(20, 0), k='-nome5-')],
            [sg.Input(default_text=config["Pdf-"], size=(20, 0), k='-nome6-')],
            [sg.Input(default_text=config["Word documents-"], size=(20, 0), k='-nome7-')],
            [sg.Input(default_text=config["Spreadsheets-"], size=(20, 0), k='-nome8-')],
            [sg.Input(default_text=config["Presentation files-"], size=(20, 0), k='-nome9-')],
            [sg.Input(default_text=config["Executaveis-"], size=(20, 0), k='-nome10-')],
            [sg.Input(default_text=config["Zip-"], size=(20, 0), k='-nome11-')],
            [sg.T()],
            [sg.T('◄( ALERTA )►')],
            [sg.Text('Essas janelas não serar reproduzidas nas priximas inicializações, a não ser que seja inicializado pelo seguinte () execultavel na pasta desse script', size=(34, 5))],
            [sg.Button('voltar'), sg.Button('finalizar')]
        ]

        return sg.Window('Nome das pastas', layout=layout3, finalize=True )

    #Açoes em nas janelas:

    janela1, janela2, janela3 = Apresent(), None, None 
    loop = True
    while loop:

        window, event, values = sg.read_all_windows()
        
        #Eventos na janela 1 =============================:

        if window == janela1 and event == sg.WIN_CLOSED:
            loop = False

        elif window == janela1 and event == 'Cancelar':
            loop = False

        elif window == janela1 and event == 'Avançar':
            janela1.Close()
            janela2 = tela1()

        if window == janela2 and event == sg.WIN_CLOSED:
            loop = False

        if window == janela2 and event == 'Ok':
            janela2.hide()
            janela3 = tela2()
        
            config.update({'stado':2})
            config.update({'direct':values['direct'].replace("/", "\\")})

            with open('config.json', 'w') as f:
                json.dump(config ,f)
                print(config['direct'] + ' salvo')

        elif window == janela2 and event == 'Cancelar':
            loop = False

        #Eventos na janela 2 =============================:

        elif window == janela3 and event == sg.WIN_CLOSED:
            loop = False

        elif window == janela3 and 'checks' == True:
            print('1')

        elif window == janela3 and event == 'voltar':
            janela3.hide()
            janela2.un_hide()

        elif window == janela3 and event == 'finalizar':
            sg.popup('hora de organizar', title='Ultima etapa', auto_close=True, auto_close_duration=5, icon='ima.ico', keep_on_top=True)

            config.update({"Images-":values['-nome1-']})
            config.update({"Videos-":values['-nome2-']})
            config.update({"Audios-":values['-nome3-']})
            config.update({"Codigo-":values['-nome4-']})
            config.update({"Textos-":values['-nome5-']})
            config.update({"Pdf-":values['-nome6-']})
            config.update({"Word documents-":values['-nome7-']})
            config.update({"Spreadsheets-":values['-nome8-']})
            config.update({"Presentation files-":values['-nome9-']})
            config.update({"Executaveis-":values['-nome10-']})
            config.update({"Zip-":values['-nome11-']})

            with open('config.json', 'w') as f:
                json.dump(config ,f)

            print(values['-nome1-'])
            print(values['-nome2-'])
            print(values['-nome3-'])
            print(values['-nome4-'])
            print(values['-nome5-'])
            print(values['-nome6-'])
            print(values['-nome7-'])
            print(values['-nome8-'])
            print(values['-nome9-'])
            print(values['-nome10-'])
            print(values['-nome11-'])
            janela2.Close()
            janela3.Close()
            loop = False



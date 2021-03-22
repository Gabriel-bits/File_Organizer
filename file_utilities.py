import shutil
import os
import json
import PySimpleGUI as sg

def extension_type(event):
    return event.src_path[event.src_path.rindex('.') + 1:]


def is_text_file(event):
    if extension_type(event) == 'txt':
        return True
    return False


def is_pdf_file(event):
    if extension_type(event) == 'pdf':
        return True
    return False


def is_rar_file(event):
    if extension_type(event) in ('zip', '7z', 'rar', 'RAR', 'ZIP'):
        return True
    return False


def is_mp3_file(event):
    if extension_type(event) in ('mp3', 'm4a', 'MP3'):
        return True
    return False


def is_image_file(event):
    if extension_type(event) in ('png', 'jpg', 'bmp', 'gif', 'raw', 'jpeg', 'JPEG', 'PNG'):
        return True
    return False


def is_video_file(event):
    if extension_type(event) in ('mov', 'mp4', 'avi', 'flv', 'MP4'):
        return True
    return False


def is_doc_file(event):
    if extension_type(event) in ('doc', 'docx', 'DOCX'):
        return True
    return False


def is_spreadsheet_file(event):
    if extension_type(event) in ('xls', 'xlsx'):
        return True
    return False


def is_presentation_file(event):
    if extension_type(event) in ('ppt', 'pptx'):
        return True
    return False


def is_code_file(event):
    if extension_type(event) in ('py', 'htm', 'jar', 'js', 'php', 'html', 'sql', 'css'):
        return True
    return False


def is_executable_file(event):
    if extension_type(event) in ('exe', 'msi', 'EXE', 'MSI'):
        return True
    return False


with open('config.json', 'r') as f:
    f = json.load(f)
    Arquivo_lido = f['direct']

def make_folder(foldername):
    os.chdir(Arquivo_lido.replace("/", "\\"))
    if os.path.exists(foldername) == True:
        print('Pasta ja existe, pulando etapa')
        return os.getcwd() + os.sep + str(foldername)
    else:
        os.mkdir(str(foldername))
        return os.getcwd() + os.sep + str(foldername)


def move_to_new_corresponding_folder(event, path_to_new_folder):
    try:
        shutil.move(event.src_path, path_to_new_folder)
        print('Movendo arquivo ')
            # sg.popup_animated('378.gif',message='load' , time_between_frames=3)

    except:
        print('O arquivo já existe na pasta de destino')
        pass

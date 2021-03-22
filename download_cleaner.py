import os
import Interface
import logging
import time
import json

import file_utilities
from file_utilities import *
from watchdog.events import FileSystemEventHandler, LoggingEventHandler
from watchdog.observers import Observer


with open('config.json', 'r') as f:
    config = json.load(f)

class Handler(FileSystemEventHandler):
    @staticmethod
    def on_created(event):
        pass

    @staticmethod
    def on_modified(event):
        try:
            if os.path.isdir(event.src_path):
                return

            if is_code_file(event) == True:
                path_to_folder = make_folder(config["Codigo-"])
                move_to_new_corresponding_folder(event, path_to_folder)
                return
            elif is_text_file(event) == True:
                path_to_folder = make_folder(config["Textos-"])
                move_to_new_corresponding_folder(event, path_to_folder)
                return
            elif is_pdf_file(event) == True:
                path_to_folder = make_folder(config["Pdf-"])
                move_to_new_corresponding_folder(event, path_to_folder)
                return
            elif is_mp3_file(event) == True:
                path_to_folder = make_folder(config["Audios-"])
                move_to_new_corresponding_folder(event, path_to_folder)
                return
            elif is_image_file(event) == True:
                path_to_folder = make_folder(config["Images-"])
                move_to_new_corresponding_folder(event, path_to_folder)
                return
            elif is_video_file(event) == True:
                path_to_folder = make_folder(config["Videos-"])
                move_to_new_corresponding_folder(event, path_to_folder)
                return
            elif is_doc_file(event) == True:
                path_to_folder = make_folder(config["Word documents-"])
                move_to_new_corresponding_folder(event, path_to_folder)
                return
            elif is_spreadsheet_file(event) == True:
                path_to_folder = make_folder(config["Spreadsheets-"])
                move_to_new_corresponding_folder(event, path_to_folder)
                return
            elif is_presentation_file(event) == True:
                path_to_folder = make_folder(config["Presentation files-"])
                move_to_new_corresponding_folder(event, path_to_folder)
                return
            elif is_executable_file(event) == True:
                path_to_folder = make_folder(config["Executaveis-"])
                move_to_new_corresponding_folder(event, path_to_folder)
                return
            elif is_rar_file(event) == True:
                path_to_folder = make_folder(config["Zip-"])
                move_to_new_corresponding_folder(event, path_to_folder)
                return
        except ValueError:
            print('Arquivo sem extenção')
            return


    @staticmethod
    def on_deleted(event):
        pass

    @staticmethod
    def on_moved(event):
        pass

with open('config.json', 'r') as f:
    arq_direc = json.load(f)
    Arquivo_lido = arq_direc['direct']

file_change_handler = Handler()
observer = Observer()
os.chdir(Arquivo_lido.replace("/", "\\"))
print(os.getcwd())
observer.schedule(file_change_handler, os.getcwd(), recursive=False,)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()

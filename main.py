import shutil


if __name__ == "__main__":
    import json, os, time
    import PySimpleGUI as pg
    import shutil

    #'C:/Users/Narutinn/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/download_cleaner.py'

    into_file_system = [
        "A:", "B:", "C:", "D:", "E:", "F:", "G:", "H:", "I:", "J:", "K:", "L:", "M:", "N:", "O:", "P:", "Q:", "R:", "S:", "T:", "U:", "V:", "W:", "X:", "Y:", "V:"
    ]


    for roots, directs, files in os.walk("/Users/"):
        roots = roots.replace("/", "\\")
        print(roots)
        if "\Start Menu\Programs\Startup" in roots:
            for into_ in into_file_system:
                print(into_)
                try:
                       
                    if os.path.exists(f"{into_}{roots}") == True:
                        dir_startup = f"{into_}{roots}\\"
                        dir_startup = dir_startup.replace("\\", "/")
                        # copy_lnk = shutil.copyfile(src="download_cleaner.py - Atalho.lnk", dst=dir_startup)
                        arq_athl = "download_cleaner.py - Atalho.lnk"
                        # shutil.move(src=copy_lnk, dst=dir_startup)
                        time.sleep(9)
                        os.system(f'Copy-Item "{arq_athl}" {dir_startup} -Force')
                        break
                        
                except:
                    break
    
    # if os.path.exists("/AppData/Microsoft/Windows/Start Menu/Programs/Startup/download_cleaner.py/"):
    #     print('1')     


    #.\Users\Narutinn\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
    #.\download_cleaner.py - Atalho.lnk
    #os.system(f"-root -Copy-Item -Path {arq_athl} -Destination {dir_startup} -Force")

    # try:

    #     with open('config.json', 'r') as f:
    #         config = json.load(f)

    #     config.update({'stado':1})
    #     with open('config.json', 'w') as f:
    #         json.dump(config ,f)
            
    # except FileNotFoundError:
    #     pass    
    # os.startfile("./download_cleaner.py", "open")

if __name__ == "__main__":
    import json, os
    import PySimpleGUI as pg

#'C:/Users/Narutinn/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/download_cleaner.py'


    for root, directs, files in os.walk("/Users/") :
        for direct in directs:
            if direct == "Programs/":
                print(direct)

    # if os.path.exists("/AppData/Microsoft/Windows/Start Menu/Programs/Startup/download_cleaner.py/"):
    #     print('1')     


    
    # try:

    #     with open('config.json', 'r') as f:
    #         config = json.load(f)

    #     config.update({'stado':1})
    #     with open('config.json', 'w') as f:
    #         json.dump(config ,f)
            
    # except FileNotFoundError:
    #     pass    
    # os.startfile("./download_cleaner.py", "open")

    

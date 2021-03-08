import os

def show(dir_path: str):
    with os.scandir(dir_path) as scan:
        for entry in scan:
            #if entry.is_dir():
            if entry.is_file():
                print(entry)
            

show("/Users/Асер/Documents/pp2/")
import os

def walk(dir_path: str):
    for entry in os.walk(dir_path):
        print(entry)
    

walk("/Users/Асер/Documents/pp2/")
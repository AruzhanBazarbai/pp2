import os

def get(dir_path: str):
    subfolders=[f.path for f in os.scandir(dir_path) if f.is_dir()]
    print(subfolders)

get("/Users/Асер/Documents/pp2/")
import os
import fnmatch

dir_path="/Users/Асер/Documents/pp2/tsis5/"

with os.scandir(dir_path) as entry:
    for item in entry:
        if item.is_file():
            if fnmatch.fnmatch(item.name,"*.py"):
                print(f"----------------{item.name}")
                file=open(item)
                text=file.read()
                print(text)
                file.close()
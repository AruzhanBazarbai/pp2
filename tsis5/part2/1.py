import os
import os.path
import time
import shutil
from pathlib import Path

dir_path=os.getcwd()

def main_Menu():
    print("0. Input '0' - Back")
    print("1. Input '1' - Show dir_path")
    print("2. Input '2' - Exit")

def dir_Menu():
    print("0. Input '0' - Back")
    print("1. Input '1' - Content")
    
#dir Menu
def dir_content():
    list_dir=os.listdir(dir_path)
    for i in list_dir:
        print(i)
    
def dir_choices():
    print("0. Input '0' - Back")
    print("1. Input '1' - Rename directory")
    print("2. Input '2' - Print number of files")
    print("3. Input '3' - Print number of directories")
    print("4. Input '4' - List content of the directory")
    print("5. Input '5' - Add file to this directory")
    print("6. Input '6' - Add new directory to this directory")


def dir_rename():
    #print(f"Current working directory is:{dir_path}")
    try:
        src=input("Enter the name of directory:     ")
        dst=input("Rename directory to:             ")
        os.rename(src,dst)
        print('Directory renamed successfully!')
    except FileNotFoundError:
        print('Directory not found')


def dir_print_numberF():
    cnt=0
    with os.scandir(dir_path) as items:
        for item in items:
            if item.is_file():
                cnt+=1
    print(f"Number of files in this directory is {cnt}")
    
def dir_print_numberD():
    cnt=0
    with os.scandir(dir_path) as items:
        for item in items:
            if item.is_dir():
                cnt+=1
    print(f"Number of directories in this directory is {cnt}")

def dir_add_file():
    print("Enter the name of new file:   ")
    name=str(input())
    with open(name,"w") as f:
        print("File created succesfully!")
        f.close()

def dir_add_dir():
    name=str(input("Enter the name of new directory:   "))
    os.mkdir(name)
    print("Directory created succesfully!")


#main choices
def choices():
    print("0. Input '0' - Back")
    print("1. Input '1' - Work with dir")
    print("2. Input '2' - Work with file")

#file Menu   
def file_choices():
    print("0. Input '0' - Back")
    print("1. Input '1' - Delete file")
    print("2. Input '2' - Rename file")
    print("3. Input '3' - Add content to this file")
    print("4. Input '4' - Rewrite content of this file")
    print("5. Input '5' - Return to the parent directory")

def file_delete():
    try:
        f=input("Enter the name of file:    ")
        os.remove(f)
        print("File deleted succesfully!")
    except FileNotFoundError:
        print("File not found!")

def file_rename():
    try:
        src=input("Enter the name of file:    ")
        dst=input("Rename the file to:    ")
        os.rename(src,dst)
        print("File renamed succesfully!")
    except FileNotFoundError:
        print("File not found!")

def file_add():
    try:
        src=input("Enter the name of file:    ")
        with open(src,"a") as f:
            f.write(str(input("Write to file:    ")))
            f.close()
        print("Data added to file succesfully!")
    except FileNotFoundError:
        print("File not found!")

def file_rewrite():
    try:
        src=input("Enter the name of file:    ")
        with open(src,"w") as f:
            f.write(str(input("Write to file:    ")))
            f.close()
        print("Data rewrited to file succesfully!")
    except FileNotFoundError:
        print("File not found!")

def file_return_to_parent():
    try:
        f=str(input("Enter the full path:   "))
        p=Path(f).parent
        print(p)
    except FileNotFoundError:
        print("File not found!")



#----------------------------------------------------------------
print("Hello world! Hello user!")

while True:
    main_Menu()

    fir_choise=int(input("Input:    "))

    if fir_choise==1:
        print(dir_path)
        choices()

        third_choise=int(input("Input:     "))
            #dir_content()

        if third_choise==1:
            dir_choices()
            fourth_choise=int(input("Input:     "))

            if fourth_choise==1:
                dir_rename()
            elif fourth_choise==2:
                dir_print_numberF()
            elif fourth_choise==3:
                dir_print_numberD()
            elif fourth_choise==4:
                dir_content()
            elif fourth_choise==5:
                dir_add_file()
            elif fourth_choise==6:
                dir_add_dir()
            else:
                continue


        elif third_choise==2:
            file_choices()
            any_choise=int(input("Input:     "))

            if any_choise==1:
                file_delete()
            elif any_choise==2:
                file_rename()
            elif any_choise==3:
                file_add()
            elif any_choise==4:
                file_rewrite()
            elif any_choise==5:
                file_return_to_parent()
            else:
                continue

        else:
            continue

    elif fir_choise==0:
        continue

    else:
        exit()

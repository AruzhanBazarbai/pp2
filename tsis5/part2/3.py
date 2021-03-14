import os
import os.path
import time 
import shutil

def Menu():
    print("0. Input '0' - back")
    print("1. Input '1' - work with dir")

def DirMenuChoices():
    print("0. Input '0' - back")
    print("1. Content")

def ContentOfDir():
    content = os.listdir(curDir)
    for i in content:
        print(i)



print("FileMan v1.0")
while(True):
    curDir = os.getcwd()
    Menu()
    print(curDir)
    Fchoice = int(input("Input:  "))

    if Fchoice == 1:
        DirMenuChoices()
        Schoice = int(input("Input:  "))
        if Schoice == 1:
            ContentOfDir()



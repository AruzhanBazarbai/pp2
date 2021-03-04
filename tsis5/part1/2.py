# Write a Python program to read first n lines of a file
from itertools import islice

def fread(fnames,n):
    with open(fnames) as myfile:
        for line in islice(myfile,n):
            print(line)

fread("test.txt",2)

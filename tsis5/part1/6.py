#Write a Python program to read a file line by line store it into a variable
def f_read(fname):
    with open(fname,"r") as f:
        lines=f.readlines()
        print(lines)

f_read("test.txt")
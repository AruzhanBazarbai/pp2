#Write a Python program to read a file line by line and store it into a list
def f_read(fname):
    with open(fname) as f:
        lines=f.readlines()
    print(lines)

f_read("test.txt")
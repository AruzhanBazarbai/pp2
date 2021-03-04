#Write a Python program to get the file size of a plain file
def f_size(fname):
    import os
    statinfo=os.stat(fname)
    return statinfo.st_size

print(f_size("test.txt"))
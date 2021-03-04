# Write a Python program to read last n lines of a file.
def f_read(fname,n):
    with open(fname) as f:
        text=f.readlines()
        x=len(text)
        for i in range(n):
            print(text[x-n+i],end='')
        
f_read("test.txt",3)
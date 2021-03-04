# Write a Python program to read a file line by line store it into an array
def f_read(fname):
    a=[]
    with open(fname,"r") as f:
        for x in f:
            a.append(x)

        print(a)
        

f_read("test.txt")
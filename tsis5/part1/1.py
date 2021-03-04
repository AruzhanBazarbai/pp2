# Write a Python program to read an entire text file.
def f_read(fname):
    text=open(fname)
    print(text.read())

f_read('test.txt')
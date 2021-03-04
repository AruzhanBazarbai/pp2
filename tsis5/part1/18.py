#Write a Python program that takes a text file as input and returns the number of words of a given text file
def f(fname):
    with open(fname) as file:
        text=file.read()
        text.replace(","," ")
    return len(text.split(' '))

print(f("test.txt"))
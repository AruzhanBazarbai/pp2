#Write a Python program to count the number of lines in a text file
def strings_size(fname):
    with open(fname) as f:
        lines=f.readlines()
    for num,value in enumerate(lines):
        pass
    return(num+1)
print(strings_size("test.txt"))



'''
def strings_size(fname): 
    with open(fname,"r") as f:
        words=f.read().split()
    print(len(words))

strings_size("test.txt")
'''
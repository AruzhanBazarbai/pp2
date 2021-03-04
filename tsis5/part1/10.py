 #Write a Python program to count the frequency of words in a file
def strings_size(fname):
    a={}
    with open(fname) as f:
        lines=f.readlines()
    for line in lines:
        x=line.split()
        for y in x:
            if y not in a:
                a[y]=1
            else:
                a[y]+=1
    for key,value in a.items():
        print(f'number of {key} is {value}')
    
print(strings_size("test.txt"))

'''
from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("test.txt"))
'''
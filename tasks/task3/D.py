
c=dict()
f=open("input.txt","r",encoding="utf-8")
text=f.read().split()


for word in text:
    if word not in c:
        c[word]=1
    else:
        c[word]+=1


c=sorted((key,value) for key,value in c.items())
c=dict(c)

for key,value in c.items():
    if value%2==0:
        print(key)


'''
from collections import Counter

def read(fname):
    with open(fname) as f:
        return Counter(f.read().split())

print(read("input.txt"))
'''


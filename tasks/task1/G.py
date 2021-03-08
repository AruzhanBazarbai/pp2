
n=int(input())
s1=set()
s2=set()

for i in range(n):
    x=input()
    for j in x:
        s1.add(j)
    
    if len(s2)!=0:
        s2=s2.intersection(s1)
        s1.clear()
    else:
        s2=s1

if len(s2)==0:
    print("NO COMMON CHARACTERS")
else:
    s2=sorted(s2,key=str)
    for x in s2:
        print(x,end=" ")

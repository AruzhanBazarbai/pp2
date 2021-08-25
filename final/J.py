#done
import math
list1=[]
a,b=map(int,input().split())

while a<=b:
    if a==2 or a==3:
        list1.append(a)
    elif a>3:
        k=True
        for i in range(2,int(math.sqrt(a))+1):
            if a%i==0:
                k=False
                break
        if k:
            list1.append(a)
    a+=1

list1=sorted(list1)
list1=reversed(list1)
print(*list1)

#done

l,r=map(int,input().split())
a=[]

for i in range(l,r+1):
    if i%7==1 or i%7==5 or i%7==2:
        a.append(i)
        

print(*a)
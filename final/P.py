#done
n=int(input())
a,b=[],[]
k=0
for i in range(n):
    c=k
    while c<n+i:
        b.append(c)
        c+=1
    a.append(b)
    b=[]
    k+=1
# print(a)
for x in a:
    print(*x,sep=' ')
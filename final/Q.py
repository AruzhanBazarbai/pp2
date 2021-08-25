#done
n,m=map(int,input().split())
a,b=[],[]
for i in range(n):
    for j in range(m):
        if i<n//2:
            if j<m//2:
                b.append(1)
            else:
                b.append(0)
        else:
            if j<m//2:
                b.append(2)
            else:
                b.append(3)
    a.append(b)
    b=[]
for x in a:
    print(*x)
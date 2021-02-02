#Задача №1433. Кролики
n,m=map(int,input().split())

if m<n:
    print(1)
else:
    c=m//n
    d=m%n
    if d==0:
        print(c)
    else:
        print(c+1)
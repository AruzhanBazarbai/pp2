#Задача №258. Шоколадка
n=int(input())
m=int(input())
k=int(input())

z=False

for x in range(1,m+1):
    if x*n==k:
        print("YES")
        z=True
        break

if z==False:
    for x in range(1,n+1):
        if x*m==k:
            print("YES")
            z=True
            break

if z==False:
    print("NO")

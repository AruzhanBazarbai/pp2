#Задача №3515. Шоколадка
n=int(input())
m=int(input())
k=int(input())

a=0

for x in range(1,n+1):
    if x*m==k:
        a=1
        break

for x in range(1,m+1):
    if x*n==k:
        a=1
        break

if a==0: 
    print("NO")
else: 
    print("YES")
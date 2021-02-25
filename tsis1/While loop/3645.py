#Задача №3645. Точная степень двойки
n=int(input())
i=0
x=0

while x<n:
    x=2**i
    i+=1

if x==n:
    print("YES")
else:
    print("NO")
    
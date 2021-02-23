#Задача №3529. Ряд - 2
a=int(input())
b=int(input())

if a<b:
    for i in range(a,b+1):
        print(i,end=' ')
else:
    for i in range(a-b+1):
        print(a-i,end=' ')
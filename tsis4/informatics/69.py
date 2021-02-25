#Задача №69. Переставить элементы в обратном порядке
n=int(input())
a=list(map(int,input().split()))
b=a[::-1]

for x in b:
    print(x,end=' ')
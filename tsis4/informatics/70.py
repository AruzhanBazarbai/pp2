#Задача №70. Переставить соседние элементы
n=int(input())
a=list(map(int,input().split()))

for i in range(0,len(a)-1,2):
    print(a[i+1],a[i],end=' ')

if len(a)%2!=0:
    print(a[len(a)-1])
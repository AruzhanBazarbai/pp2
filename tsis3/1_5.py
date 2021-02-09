#Задача №3853. Большой сдвиг
a=list(map(int,input().split()))
x=int(input())

if x>=0:
    for i in range(len(a)):
        z=(len(a)-x+i)%len(a)
        print(a[z],end=' ')
    
elif x<0:
    x=len(a)+x
    for i in range(len(a)):
        z=(len(a)-x+i)%len(a)
        print(a[z],end=' ')





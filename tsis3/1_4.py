#Задача №3850. Сжатие списка

a=list(map(int,input().split()))
b=[]

for i in range(len(a)):
    if a[i]!=0:
        b.append(a[i])

for j in range(len(b),len(a)):
    b.append(0)

for i in range(len(b)):
    print(b[i],end=' ')
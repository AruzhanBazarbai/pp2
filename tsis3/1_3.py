#Задача №3840. Переставить в обратном порядке
a=list(map(int,input().split()))

for i in range(len(a)):
    print(a[len(a)-i-1])
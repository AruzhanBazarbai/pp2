#Задача №3750. Количество совпадающих
a=list(map(int,input().split()))
b=list(map(int,input().split()))
set1=set(a)
set2=set(b)

x=list(set1.intersection(set2))

print(len(x))
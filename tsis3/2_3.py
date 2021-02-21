#Задача №3751. Пересечение множеств
a=list(map(int,input().split()))
b=list(map(int,input().split()))
set1=set(a)
set2=set(b)

print(*sorted(set1 & set2, key=int))
#print(*sorted(set(input().split()) & set(input().split()), key=int))



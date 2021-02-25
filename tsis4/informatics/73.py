#Задача №73. Количество различных элементов в монотонном массиве
n=int(input())
a=list(map(int,input().split()))
s=set(a)
print(len(s))
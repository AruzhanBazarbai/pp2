#Задача №294. Максимум из трех
a=int(input())
b=int(input())
c=int(input())

maxi=-1e9

if maxi<a:
    maxi=a
if maxi<b:
    maxi=b
if maxi<c:
    maxi=c

print(maxi)
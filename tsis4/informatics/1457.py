#Задача №1457. Двойной переворот
n,a,b,c,d=map(int,input().split())

list1=[]
for x in range(n+1):
    list1.append(x)

list1[a:b+1]=list1[b:a-1:-1]
list1[c:d+1]=list1[d:c-1:-1]
print(*list1[1:])
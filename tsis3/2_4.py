#Задача №3753. Кубики
n,m=input().split()
n=int(n)
m=int(m)

anya=set()
bori=set()

for i in range(n):
    anya.add(int(input()))

for i in range(m):
    bori.add(int(input()))

print(len(anya&bori))
print(*sorted(anya&bori,key=int))
print(len(anya-bori))
print(*sorted(anya-bori))
print(len(bori-anya))
print(*sorted(bori-anya))


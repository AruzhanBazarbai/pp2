#Задача №3460. МКАД
v=int(input())
t=int(input())

s=v*t%109
res=(s+109)%109
print(res)
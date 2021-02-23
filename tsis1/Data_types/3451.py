#Задача №3451. Корень степени 10.
n=179**10
n=str(n)
res=""
for i in range(4):
    res+=n
res=int(res)
y=1/10
x=res**y
print(x)


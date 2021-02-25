#Задача №3643. Минимальный простой делитель
n=int(input())
p=1
k=0
while p*p<=n:
    p+=1
    if n%p==0:
        z=1
        for i in range(2,p):
            if p%i==0:
                z=0
                break
    if n%p==0 and z==1:
        k=1
        break
    
if k==0:
    print(n)
else:
    print(p)

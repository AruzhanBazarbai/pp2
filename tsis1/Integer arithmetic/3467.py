#Задача №3467. Парты
def f(a):
    if a%2==0:
        return a//2
    else:
        return (a+1)//2

a=int(input())
b=int(input())
c=int(input())

cnt=0

cnt+=f(a)
cnt+=f(b)
cnt+=f(c)

print(cnt)
#Задача №1466. Сумма от 1 до N
n=input()
n=int(n)

if n>0:
    sum=(1+n)*n//2
    print(sum)
else:
    sum=-1*((1+abs(n))*abs(n)//2)+1
    print(sum)

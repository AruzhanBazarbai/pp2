#Задача №1475. k-я секунда суток
n=input()
n=int(n)

h=n//3600
n=n%3600
m=n//60
n=n%60
s=n

print("It is",h,"hours",m,"minutes.")

#Задача №3531. Сумма квадратов
n=int(input())

cnt=0

for i in range(1,n+1):
    cnt+=i*i

print(cnt)
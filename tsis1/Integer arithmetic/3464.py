#Задача №3464. Сумма цифр
n=int(input())
cnt=0
while n>0:
    cnt+=n%10
    n//=10
print(cnt)
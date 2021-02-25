#Задача №1456. Шеренга
n=int(input())
a=list(map(int,input().split()))
x=int(input())
cnt1=0
cnt2=0

for i in range(len(a)):
    if x<=a[i]:
        cnt1+=1

print(cnt1+1)

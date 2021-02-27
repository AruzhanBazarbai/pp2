#Задача №1461. Шарики
a=list(map(int,input().split()))
cnt,i,b,res=1,0,0,0

while i<len(a):
    if i+1<len(a) and a[i]==a[i+1]:
        cnt+=1
        i+=1
        continue
    if cnt>=3:
        res+=cnt
        del a[i-cnt+1:i+1]
        cnt=1
        i=0
    else:
        cnt=1
        i+=1
print(res)


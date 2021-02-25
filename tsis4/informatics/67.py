#Задача №67. Есть ли два элемента с одинаковыми знаками
n=int(input())
a=list(map(int,input().split()))
k=0
for i in range(len(a)-1):
    if a[i]>0 and a[i+1]>0:
        print("YES")
        k=1
        break
    elif a[i]<0 and a[i+1]<0:
        print("YES")
        k=1
        break
        
if k==0:
    print("NO")
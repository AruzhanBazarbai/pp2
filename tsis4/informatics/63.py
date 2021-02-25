#Задача №63. A[0], A[2], A[4], ...
n=int(input())
a=list(map(int,input().split()))

for i in range(len(a)):
    if i%2==0:
        print(a[i],end=' ')
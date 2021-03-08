
n=int(input())
a=set(map(int,input().split()))
a=list(a)
for i in range(1,len(a)+1):
    print(i,a[i-1])


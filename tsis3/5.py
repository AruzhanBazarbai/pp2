a=list(map(int,input().split()))
x=int(input())

if x>0:
    for i in range(x-1,len(a)+x-1):
        z=(abs(len(a)-i))%len(a)
        print(a[z],end=' ')
    
elif x<0:
    x*=-1
    for i in range(x,len(a)+x):
        z=(len(a)+i)%len(a)
        print(a[z],end=' ')





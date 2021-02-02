k,n=map(int,input().split())
d=n%k
if d==0:
    print(n//k,k)
else:
    print(n//k+1,n%k)

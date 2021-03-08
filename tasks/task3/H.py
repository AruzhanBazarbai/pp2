
n,k=map(int,input().split())
z=False

for i in range(n):
    a,b,c=map(int,input().split())
    d=a+b+c
    if d/3>=k:
        z=True
        break
if z:
    print("YES")
else:
    print("NO")
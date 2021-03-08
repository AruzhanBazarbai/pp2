#contest-16914
#done
n=int(input())
m=int(input())
k=int(input())
z=False
for x in range(1,n+1):
    if x*m==k:
        z=True
        break

for x in range(1,m+1):
    if n*x==k:
        z=True
        break
if z:
    print("YES")
else:
    print("NO")

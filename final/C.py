#done
a=list(map(int,input().split()))
b=[]
for x in a:
    if x!=0:
        b.append(x)

while len(b)<len(a):
    b.append(0)
print(*b)
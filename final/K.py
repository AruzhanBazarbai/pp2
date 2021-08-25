#done
def f(n):
    i=2
    j=0
    if n==1:
        return True
    while i<n:
        i=2
        i**=j
        j+=1
    if i==n:
        return True
    return False

a=list(map(int,input().split()))
b=set()
for x in a:
    if f(x):
        b.add(x)
print(*sorted(b,key=int))

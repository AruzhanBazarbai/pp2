#done
a=[]
def f(l,r):
    if l>r:
        return l
    a.append(l)
    return f(l+2,r)




l,r=map(int,input().split())
if l%2==0:
    l+=1

f(l,r)
print(*a)


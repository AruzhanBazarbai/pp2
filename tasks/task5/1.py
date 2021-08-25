#done
list1=list(map(int,input().split()))
n=int(input())
list_g=[]
for i in range(n):
    list2=[]
    list2=list(map(int,input().split()))
    for x in list2:
        list_g.append(x)

set1=set()

for x in list1:
    k=True
    for y in list_g:
        if x==y:
            k=False
            break
    if k:
        set1.add(x)
# print(*sorted(set1,key=int))
a=sorted(set1,key=int,reverse=True)
# print(*reversed(a))
print(*a)

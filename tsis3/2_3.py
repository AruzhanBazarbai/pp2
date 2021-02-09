a=list(map(int,input().split()))
b=list(map(int,input().split()))
set1=set(a)
set2=set(b)
list2=list(set1.intersection(set2))

for i in range(len(list2)):
    print(list2[i],end=' ')


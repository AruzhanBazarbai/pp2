#done
n=int(input())
a=list(map(int,input().split()))
maxi=-1e9
for i in a:
    if maxi<i:
        maxi=i
b=[]
for i in a:
    if i==maxi:
        b.append(1)
    else:
        b.append(0)
print(*b)
#done
n,m=map(int,input().split())
maxi=-1e9
index=0
for i in range(n):
    a=list(map(int,input().split()))
    cnt=0
    for j in a:
        cnt+=j
    if maxi<cnt:
        maxi=cnt
        index=i+1
print(index)
#done

def f(l,r,walls):
    maxi=-1
    cnt=0
    for i in range(l,r+1):
        if  maxi<walls[i]:
            maxi=walls[i]
            cnt+=1
    print(cnt)



n=int(input())
walls=list(map(int,input().split()))
m=int(input())

for i in range(m):
    l,r=map(int,input().split())
    f(l,r,walls)

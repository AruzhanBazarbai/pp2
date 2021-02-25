n,a,b,c,d=map(int,input().split())

list1=[]
for i in range(1,n+1):
    list1.append(i)
print(list1)
for i in range(a-1):
    print(list1[i],end=' ')
print(*list1[a-1:b-1:-1])
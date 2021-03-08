#done

n=int(input())
a=[]
for i in range(n):
    b,c,d=input().split()
    a.append([b,c,d])


for i in range(len(a)):
    for j in range(len(a[i])):
        if len(a[i][j])<2:
            a[i][j]='0'+a[i][j]


a=sorted(a,key=str)


for i in range(len(a)):
    for j in range(len(a[i])):
        print(int(a[i][j]),end=' ')
    print(sep="/n")

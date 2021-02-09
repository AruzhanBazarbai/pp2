a=list(map(int,input().split()))

mini=1e9

for i in range(len(a)):
    if a[i]>0:
        if mini>a[i]:
            mini=a[i]

print(mini)
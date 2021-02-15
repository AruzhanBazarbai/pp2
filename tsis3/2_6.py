while True:
    a=list(input().split())
    res=dict()

    for i in range(len(a)):
        x=res[a[i]]
        res[a[i]]=x+1

for key in res:
    print(key,res[key])

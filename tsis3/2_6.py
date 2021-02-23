a=list(map(int,input().split()))

mp={}

for i in range(len(a)):
    if a[i] not in mp:
        mp[a[i]]=1
    else:
        mp[a[i]]+=1

for key in mp:
    print(mp[key])
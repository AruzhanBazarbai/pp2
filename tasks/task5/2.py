#done
a=list(map(str,input().split()))
cnt=0
for x in a:
    if len(x)%2==0:
        cnt+=1

print(cnt)
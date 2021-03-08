

n=int(input())
a=list(map(int,input().split()))
k=int(input())

cnt1,cnt2="",""
if k==0:
    print(0)
    exit()
    
for i in range(k):
    cnt1+=str(a[i])

for i in range(k,len(a)):
    cnt2+=str(a[i])

cnt1=int(cnt1)
cnt2=int(cnt2)
print(cnt1*cnt2)
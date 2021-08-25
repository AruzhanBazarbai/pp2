#done
s=input()
a=["MON","TUE","WED","THU","FRI","SAT","SUN"]
cnt=0
for i in range(len(a)):
    if s==a[i]:
        cnt=i
if cnt==6:
    print(7)
else:
    print(len(a)-cnt-1)
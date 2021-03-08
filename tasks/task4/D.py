

s=input()
x,y=map(int,input().split())
x1,y1=0,0
k=0
if x==x1 and y==y1:
    k=1
for i in s:
    if i=='R':
        x1+=1
        if x1==x and y1==y:
            k=1
            break
    elif i=='L':
        x1-=1
        if x1==x and y1==y:
            k=1
            break
    elif i=='U':
        y1+=1
        if x1==x and y1==y:
            k=1
            break
    elif i=='D':
        y1-=1
        if x1==x and y1==y:
            k=1
            break

if k:
    print("Passed")
else:
    print("Missed")
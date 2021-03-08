
n=int(input())
x=list(input().split())
m=int(input())
y=list(input().split())

s1=set(x)
s2=set(y)

a,b=[],[]

for i in x:
    cnt=len(s2)
    s2.add(i)
    if len(s2)!=cnt:
        a.append(i)
for i in y:
    cnt=len(s1)
    s1.add(i)
    if len(s1)!=cnt:
        b.append(i)

print("Missed students:")
for i in a:
    print("-",i)
print("Not in the group:")
for i in b:
    print("-",i)


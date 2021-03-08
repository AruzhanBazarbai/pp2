
n=int(input())
a=list(map(int,input().split()))
s1=""
for x in a:
    s1+=str(x)

a.sort()
s2=""

for x in a:
    s2+=str(x)


if s1==s2:
    print("Interesting")
else:
    print("Not interesting")
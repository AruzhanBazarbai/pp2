#done
s1=input()
s2=input()
res1,res2='',''
for x in s1:
    if x!=' ':
        res1+=x

for x in s2:
    if x!=' ':
        res2+=x
print(res2==res1)
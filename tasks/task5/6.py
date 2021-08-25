#done
a=list(map(int,input().split()))
d={}
for x in a:
    if x not in d:
        d[x]=0
    d[x]+=1
s=set()
for value in d.values():
    s.add(value)
# print(len(s),len(d))
if len(s)==len(d):
    print('Perfect')
else:
    print('Not perfect')
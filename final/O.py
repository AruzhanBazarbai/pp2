#done
s=list(input().split())
res=[]
for x in s:
    if x.islower():
        x=x.upper()
    res.append(x)
d={}
for x in res:
    if x not in d:
        d[x]=0
    d[x]+=1

words=sorted((key,value) for key,value in d.items())
# print(len(d))
words=dict(words)
maxi=0
for key,value in words.items():
    if value>maxi:
        maxi=value
for key,value in words.items():
    if value==maxi:
        print(key)


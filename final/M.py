#done
s=input()
d={}
for x in s:
    if x not in d:
        d[x]=0
    d[x]+=1

words=sorted((key,value) for key,value in d.items())
print(len(d))
words=dict(words)
for key,value in words.items():
    print(key,value)
import re
s=input()
k=input()
res=""
a={}
for i in range(len(s)):
    print(i)
    res+=s[i]
    print(res,"---------")
    x=re.search(r"k",res)
    if x:
        start_index=x.start()
        end_index=x.end()
        res=""
        res+=s[i]
        a[start_index]=end_index

for key,value in a.items():
    print(key,value)
    
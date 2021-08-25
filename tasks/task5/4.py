#done
import re
a=input()
x=re.findall(r'(\w+@[a-z0-9]+\.[a-z]{2,4}).(\w+@[a-z0-9]+\.[a-z]{2,4}).?(\w+@[a-z0-9]+\.[a-z]{2,4})?.?(\w+@[a-z0-9]+\.[a-z]{2,4})?',a)
a=[]
for i in x:
    for j in i:
        if j!='':
            a.append(j)
a=sorted(a)
nn,dn,sn=[],[],[]
for x in a:
    m=re.match(r'(\w+)@([a-z0-9]+)\.([a-z0-9]+)',x)
    nn.append(m[1])
    dn.append(m[2])
    sn.append(m[3])
# print(a)
print('nicknames:')
print(*nn)
print('domain name:')
print(*dn)
print('suffix:')
print(*sn)

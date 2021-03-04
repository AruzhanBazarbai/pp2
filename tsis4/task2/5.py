#Re.start() & Re.end()
import re
s=input()
k=input()
res=re.compile(k)
x=res.search(s)

if not x:
    print("(-1, -1)")
while x:
    print("({0}, {1})".format(x.start(),x.end()-1))
    x=res.search(s,x.start()+1)
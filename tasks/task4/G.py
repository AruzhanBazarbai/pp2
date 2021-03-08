
import re
txt=input()
t=input()
s=input()
f=input()

txt=txt.replace(t,s)
#print(txt)

x=re.findall(f,txt)
if x:
    print(len(x))


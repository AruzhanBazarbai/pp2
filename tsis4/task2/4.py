#re.findall()
import re
s=input()
x=re.findall(r"[^aeiouAEIOU]([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])",s)
if x:
    for i in x:
        print(i)
else:
    print(-1)
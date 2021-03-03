#Group(), Groups() & Groupdict()

import re
s=input()
x=re.search(r"([0-9a-zA-Z])\1+",s)

if x:
    print(x.group(1))
else:
    print(-1)
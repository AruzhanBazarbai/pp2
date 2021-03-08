
import re
s=input()
x=re.match("^\w+$",s)
if x:
    print("Found a match!")
else:
    print("Not matched!")
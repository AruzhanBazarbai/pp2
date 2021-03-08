#contestpp2
import re
s=input()

x=re.search("[A-Z][a-z]+",s)
if x:
    print("Found a match!")
else:
    print("Not matched!")

#Validating phone numbers
import re
n=int(input())

for i in range(n):
    s=input()
    x=re.match("^[789]\d{9}$",s)
    if x:
        print("YES")
    else:
        print("NO")
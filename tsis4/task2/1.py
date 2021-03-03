#Detect Floating Point Number
import re

n=int(input())

for i in range(n):
    s=input()
    x=re.match(r"^[+-]?[0-9]*\.[0-9]+$",s)

    if x:
        print("True")
    else:
        print("False")


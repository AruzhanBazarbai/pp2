#done
import re

def f(s):
    x=re.match("^[a-z]+@[a-z]+\.[a-z]+$",s)
    if x:
        print("Yes")
    else:
        print("No")

s=input()
f(s)

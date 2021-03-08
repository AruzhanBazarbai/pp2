#Write a Python function that checks whether a passed string is palindrome or not.

def f(s):
    res=""
    for x in s:
        res=x+res
    if res==s:
        return True
    else:
        return False 



s=input()
if f(s):
    print("YES")
else:
    print("NO")
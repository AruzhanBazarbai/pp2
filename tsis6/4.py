#Write a Python program to reverse a string.

s=input()
s=reversed(s)

res=""
for x in s:
    res+=x
print(res)
#Validating and Parsing Email Addresses
import re

n=int(input())

for i in range(n):
    name,email=input().split()
    x=re.match("^<[a-zA-Z]([a-zA-Z0-9.\-_]+)@([a-zA-Z]+)\.([a-zA-Z]{1,4})>$",email)
    if x:
        print(name,email)
'''
name,email=input().split()
x=re.match("^<[a-zA-Z]([a-zA-Z0-9.\-_]+)@([a-zA-Z]+)\.([a-zA-Z]{1,4})>$",email)
if x:
    print(name,email)
'''

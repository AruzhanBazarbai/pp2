#Write a Python function that takes a number as a parameter and check the number is prime or not
from math import sqrt
def is_prime(n):
    if n==1: 
        return False
    elif n==2 or n==3:
        return False
    else:
        for i in range(2,int(sqrt(n))+1):
            if n%i==0:
                return False
    return True

n=int(input())

if is_prime(n):
    print("YES")
else:
    print("NO")

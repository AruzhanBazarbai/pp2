#Write a Python function to calculate the factorial of a number (a non-negative integer). 
# The function accepts the number as an argument. 

def fact(n):
    cnt=1
    while n>0:
        cnt*=n
        n-=1
    return cnt

n=int(input())
print(fact(n))
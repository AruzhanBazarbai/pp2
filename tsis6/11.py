#Write a Python function to check whether a number is perfect or not.

def f(n):
    cnt=0
    for i in range(1,n):
        if n%i==0:
            cnt+=i

    if cnt==n:
        return True
    return False

n=int(input())

if f(n):
    print("YES")
else:
    print("NO")

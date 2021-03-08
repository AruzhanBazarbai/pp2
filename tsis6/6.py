#Write a Python function to check whether a number is in a given range.

def f(n,a,b):
    if n in range(a,b):
        print(f"{n} is in range {a} and {b}")
    else:
        print(f"{n} is outside of the range {a} and {b}")

n,a,b=map(int,input().split())
f(n,a,b)

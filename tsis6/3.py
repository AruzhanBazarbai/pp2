#Write a Python function to multiply all the numbers in a list

def f(a):
    cnt=1
    for x in a:
        cnt*=x
    return cnt

a=list(map(int,input().split()))
print(f(a))
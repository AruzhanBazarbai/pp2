#Write a Python program to access a function inside a function

def f(x):
    return lambda a: a*x

res=f(10)
print(res(3))
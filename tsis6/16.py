#Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included). 

def f(n):
    a=[]
    for i in range(1,n+1):
        a.append(i**2)
    print(a)

f(30)
#Write a Python program to execute a string containing Python code. 

code1='print("hello world")'
code2='''
def f(x,y):
    return x*y
print(f(2,3))
'''
exec(code1)
exec(code2)
#Write a Python function that takes a list and returns a new list with unique elements of the first list

def f(my_list):
    s=set(my_list)
    s=list(s)
    return s

a=list(map(int,input().split()))

print(f(a))

'''
def f(my_list):
    x=[]
    for a in my_list:
        if a not in x:
            x.append(a)

    return x

print(f(a))
'''
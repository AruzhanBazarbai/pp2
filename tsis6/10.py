#Write a Python program to print the even numbers from a given list

def f(my_list):
    x=[]

    for a in my_list:
        if a%2==0:
            x.append(a)

    return x

a=list(map(int,input().split()))
print(f(a))

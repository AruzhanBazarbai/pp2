#Write a Python function to find the Max of three numbers.

def max_of_two(x,y):
    if x>y:
        return x
    return y

def max_of_three(a,b,c):
    return max_of_two(a,max_of_two(b,c))

a,b,c=map(int,input().split())
print(max_of_three(a,b,c))
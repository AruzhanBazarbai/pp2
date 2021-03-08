# Write a Python function to sum all the numbers in a list

def sumF(a):
    cnt=0
    for x in a:
        cnt+=x
    return cnt

a=list(map(int,input().split()))
print(sumF(a))
#b=sum(a)
#print(b)

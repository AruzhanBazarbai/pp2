n=int(input())
syn=dict()

for i in range(n):
    x,y=input().split()
    syn[x]=y

s=input()

for key in syn:
    #print(key)
    if syn[key]==s:
        print(key)
        break
    elif key==s:
        print(syn[key])
        break

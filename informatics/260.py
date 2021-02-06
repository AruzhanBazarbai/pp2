a=int(input())
b=int(input())
b*=-1

if a==0:
    print("INF")
elif b%a==0:
    print(b//a)
else:
    print("NO")
#else:
#    print("INF")

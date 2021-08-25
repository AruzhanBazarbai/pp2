#done
x=input()
y=input()

x=sorted(x,key=str)
y=sorted(y,key=str)

if x==y:
    print("YES")
else:
    print("NO")
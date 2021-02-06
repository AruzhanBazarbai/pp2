#Задача №298. Король

x1=int(input())
x2=int(input())
y1=int(input())
y2=int(input())

if abs(x1-y1)==1 and abs(x2-y2)==1:
    print("YES")
elif x1==y1 and abs(x2-y2)==1:
    print("YES")
elif x2==y2 and abs(x1-y1)==1:
    print("YES")
else:
    print("NO")
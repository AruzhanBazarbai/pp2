#done
a,b=map(int,input().split())
c,d=map(int,input().split())
x=a+d
y=b+c

if x>y:
    print("Barsenal")
    print(x,y)
elif y>x:
    print("Arselona")
    print(x,y)
elif x==y:
    if b==d:
        print("Friendship")
        print(x,y)
    elif d>c:
        print("Barsenal")
        print(x,y)
    elif b>a:
        print("Arselona")
        print(x,y)
    elif c>d:
        print("Arselona")
        print(x,y)
    elif a>b:
        print("Barsenal")
        print(x,y)
        




       

       
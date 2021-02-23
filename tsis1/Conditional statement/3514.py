#Задача №3514. Шахматная доска
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())

if x1%2==0:
    if x2%2==0:
        if y1%2==0 and y2%2==0:
            print("YES")
        elif y1%2!=0 and y2%2!=0:
            print("YES")
        else:
            print("NO")
    else:
        if y1%2!=0 and y2%2==0:
            print("YES")
        elif y1%2==0 and y2%2!=0:
            print("YES")
        else:
            print("NO")
else:
    if x2%2!=0:
        if y1%2==0 and y2%2==0:
            print("YES")
        elif y1%2!=0 and y2%2!=0:
            print("YES")
        else:
            print("NO")
    else:
        if y1%2!=0 and y2%2==0:
            print("YES")
        elif y1%2==0 and y2%2!=0:
            print("YES")
        else:
            print("NO")



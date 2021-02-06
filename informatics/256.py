#Задача №256. Ферзь

x1=int(input())
x2=int(input())
y1=int(input())
y2=int(input())

if abs(x1-y1)==abs(x2-y2) or x1==y1 or x2==y2:
    print("YES")
else:
    print("NO")
#Задача №3792. Принадлежит ли точка квадрату - 1
import math

def IsPointInSquare(x,y):
    return abs(x)>=0 and abs(x)<=1 and abs(y)>=0 and abs(y)<=1


x=float(input())
y=float(input())

if IsPointInSquare(x,y):
    print("YES")
else:
    print("NO")

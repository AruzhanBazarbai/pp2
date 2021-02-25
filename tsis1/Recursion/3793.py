#Задача №3793. Принадлежит ли точка квадрату - 2
import math

def IsPointInSquare(x,y):
    return abs(y)<=1-abs(x)

x=float(input())
y=float(input())

if IsPointInSquare(x,y):
    print("YES")
else:
    print("NO")

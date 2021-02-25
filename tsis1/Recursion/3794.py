#Задача №3794. Принадлежит ли точка кругу
import math
def IsPointInCircle(x, y, a, b, r):
    return math.sqrt((x-a)*(x-a)+(y-b)*(y-b))<=r

x=float(input())
y=float(input())
a=float(input())
b=float(input())
r=float(input())

if IsPointInCircle(x,y,a,b,r):
    print("YES")
else:
    print("NO")


#Задача №3447. Дзета-функция.
import math
res=0

for x in range(1,11):
    res+=1/x**2

print(math.sqrt(res*6))
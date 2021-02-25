#Задача №3735. Делаем срезы
s=input()
print(s[2])
print(s[len(s)-2])
print(s[:5])
print(s[:len(s)-2])
print(s[:len(s):2])
print(s[1:len(s):2])
print(s[::-1])
y=s[::-1]
print(y[::2])
print(len(s))
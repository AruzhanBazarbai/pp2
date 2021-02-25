#Задача №3737. Две половинки
s=input()
a=len(s)//2
b=len(s)%2
res=s[len(s)-a:]+s[:a+b]
print(res)

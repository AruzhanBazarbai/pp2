#Задача №3118. Две половинки
s=input()
#print(s)

d=len(s)//2
res=""

for i in range(len(s)-d,len(s)):
    res+=s[i]

for i in range(0,len(s)-d):
    res+=s[i]

print(res)
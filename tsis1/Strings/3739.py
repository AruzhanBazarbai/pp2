#Задача №3739. Первое и последнее вхождение
s=input()
i=s.find('f')
j=s.rfind('f')

if i==-1 and j==-1:
    exit()
elif i==j:
    print(i)
else:
    print(i,j)
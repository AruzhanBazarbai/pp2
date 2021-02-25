#Задача №3610. Округление по российским правилам
a=float(input())
b=int(a)
c=float((a*10-b*10)/10)

if c==0.5:
    print(b+1)
else:
    print(round(a))

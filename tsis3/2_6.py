#Задача №3764. Частотный анализ
myFile=open("input.txt","r",encoding='cp1252')

words=dict()

for i in myFile.read().split():
    if i in words:
        words[i]+=1
    else:
        words[i]=0

myFile.close()

words=sorted((-value,key) for key,value in words.items())
print(*(_[1] for _ in words),sep="\n")
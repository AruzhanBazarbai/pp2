#Задача №3530. Ряд - 3
n=int(input())
res="1"
while n>0:
    res+='0'
    n-=1
mini=""

for i in range(len(res)-1):
    mini+=res[i]

mini=int(mini)
maxi=int(res)-1

if mini>0 and mini<9:
    mini=0

while maxi>mini:
    print(maxi,end=' ')
    maxi-=2
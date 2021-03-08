#done
s=str(input())
d={}

for x in s:
    if x not in d:
        d[x]=1
    else:
        d[x]+=1
k=True

if len(s)%2==0:
    for value in d.values():
        if value%2!=0:
            k=False
            break

    
else:
    z=True
    for value in d.values():
        if value%2!=0 and k and z:
            z=False
        elif value%2!=0 and k and z==False:
            k=False
            break
        
if k:
    print("ZA WARUDO TOKI WO TOMARE")
else:
    print("JOJO")




import json
s=input()
#f=open("input.json","r")
#s=f.read()
text=json.loads(s)
nm=""
mx=1e9

for i in text["Subscriptions"]:
    name=i['name']
    #print(name)
    price=int(i['price'])
    #print(price)
    discount=int(i['discount'])
    #print(discount)
    cnt=int(price*(100-discount)/100)
    if mx>cnt:
        mx=cnt
        nm=name

print("Name:",nm)
print("Price:",mx)

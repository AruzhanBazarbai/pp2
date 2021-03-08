
def f(x,n):
    y=ord(x)+n
    if y>90:
        y=y%90+64
     
    return chr(y)


n=int(input())
s=input()
res=""

for x in s:
    x=f(x,n)
    res+=x

print(res)


#done
d={}
k=True
while k:
    try:
        x,y=input().split()
    except Exception as e:
        k=False

    # print(x,y)
    y=int(y)
    if x not in d:
        d[x]=y
    else:
        if d[x]<y:
            d[x]=y


# f=open('input.txt','r')
# text=f.readlines()

# for i in text:
#     res1,res2='',''
#     for x in i:
#         if ord(x)>=ord('A') and ord(x)<=ord('Z'):
#             res1=x
#         elif x in '1234567890':
#             res2+=x
#     # print(res1,res2)
#     res2=int(res2)
#     if res1 not in d:
#         d[res1]=res2
#     else:
#         if d[res1]<res2:
#             d[res1]=res2

words=sorted((key,value) for key,value in d.items())
# print(len(d))
words=dict(words)
for key,value in words.items():
    print(key,value)
        # print(x)

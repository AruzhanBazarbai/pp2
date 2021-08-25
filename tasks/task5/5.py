#done
n=int(input())
dic={}
for i in range(n):
    s,x=input().split()
    # print(s,x)
    x=int(x)
    if s not in dic:
        dic[s]=[]
    dic[s].append(x)
    
# print(dic)
dic_2={}
for key in dic.keys():
    # print(key,dic[key])
    cnt=0
    for x in dic[key]:
        cnt+=x
    l=len(dic[key])
    res=cnt/l
    dic_2[key]=res
# print(dic_2)
# for key,value in dic_2.items():
    # print(f'{key}: {value:.3f}')
gen=sorted((-value,key) for key,value in dic_2.items())
# print(gen)
for x in gen:
    y=abs(x[0])
    print(f'{x[1]}: {y:.3f}')
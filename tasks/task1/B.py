#done
d={}
n=int(input())
my_set=set()
for i in range(n):
    s=input()
    my_set.add(s)
    
for x in my_set:
    a,b=x.split()
    if a not in d:
        d[a]=1
    else:
        d[a]+=1
my_list=list(d.keys())
my_list=sorted(my_list,key=str)

for key in my_list:
    if d[key]>=3:
        print(key,"+1")
    else:
        print(key,"NO BONUS")
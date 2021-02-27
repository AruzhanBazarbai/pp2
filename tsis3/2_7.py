#Задача №3771. Родословная: подсчет уровней
def height(man):
    if man not in p_tree:
        return 0
    else:
        return 1+height(p_tree[man])

n=int(input())

p_tree={}
for i in range(n-1):
    child,parent=input().split()
    p_tree[child]=parent

heights={}

for man in set(p_tree.values()).union(set(p_tree.keys())):
    heights[man]=height(man)

for x,y in sorted(heights.items()):
    print(x,y)


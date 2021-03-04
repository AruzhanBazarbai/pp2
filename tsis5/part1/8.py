# Write a python program to find the longest words.
def longest_word(fname): 
    with open(fname,"r") as f:
        words=f.read().split()
    max_len=len(max(words,key=len))

    return [word for word in words if len(word)==max_len]


print(longest_word("test.txt"))
'''
def f_read(fname):
    res=""
    res_size=0
    a=[]
    with open(fname,"r") as f:
        for x in f:
            a.append(x.split())
        for item in a:
          #print(len(*item),*item)
          n=len(*item)
          if n>res_size:
            res_size=n
            res=item
    print(*res)
        
f_read("test.txt")
'''
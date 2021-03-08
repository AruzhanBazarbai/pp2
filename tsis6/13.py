# Write a Python function that prints out the first n rows of Pascal's triangle

def f(n):
    trow=[1]
    y=[0]
    for i in range(max(n,0)):
        print(trow)
        trow=[l+r for l,r in zip(trow+y,y+trow)]
        
   
    #return n>=1
f(6)

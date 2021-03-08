#Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

def f(s):
    res=""
    text=s.split('-')
    text=sorted(text,key=str)
    for word in text:
        res+=word+'-'
    print(res[:len(res)-1])

f("green-red-yellow-black-white")

"""
items=[n for n in input().split('-')]
items.sort()
print('-'.join(items))
"""
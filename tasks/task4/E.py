
'''
def f(text):
    words=text.split()
    max_size=len(max(words,key=len))
    return [word for word in words if len(word)==max_size]

text=input()
s=f(text)

print(*s)
print(len(*s))

'''

def f(text):
    words=text.split()
    word=max(words,key=len)
    return word

text=input()
s=f(text)

print(s)
print(len(s))








#Write a Python program to write a list to a file
def f(fname):
    a=["aaa","bbb","ccc","ddddd"]
    x=open(fname,"w")
    for item in a:
      x.write(item)
    print(x)

f("text.txt")

'''
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('abc.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('abc.txt')
print(content.read())
'''
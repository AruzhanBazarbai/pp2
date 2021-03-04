#Write a Python program to assess if a file is closed or not
f=open("test.txt","r")
print(f.closed)
f.close()
print(f.closed)
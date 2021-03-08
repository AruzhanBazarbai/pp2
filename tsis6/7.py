#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def f(s):
    cnt1,cnt2=0,0
    for x in s:
        if x.isupper():
            cnt1+=1
        elif x.islower():
            cnt2+=1
    return cnt1,cnt2

s=input()
cnt1,cnt2=(f(s))
print("No. of Upper case characters :",cnt1)
print("No. of Lower case Characters :",cnt2)

#Write a Python function to check whether a string is a pangram or not

def f(s):
    text=s.split()
    my_set=set()
    for word in text:
        for letter in word:
            if letter.isupper():
                letter=letter.lower()
            my_set.add(letter)

    if len(my_set)==26:
        print("YES")
    else:
        print("NO")

s="The quick brown fox jumps over the lazy dog"
f(s)


import re
text=input()
word=input()

x=re.search(word,text)

if x:
    print(f"First time {word} occured in position: {x.start()}")
else:
    print("Not found")
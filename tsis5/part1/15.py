#Write a Python program to read a random line from a file. 
import random

def random_string(fname):
      lines=open(fname).read().splitlines()
      return random.choice(lines)

print(random_string("test.txt"))
# Write a Python program to read a random line from a file.

import random

file=open('file1.txt','r')

R=file.readline()

r=random.choice(R)

print(r)
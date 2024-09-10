# Write a Python program to read a file line by line and store it into a list 

fl=open('Data.txt','r')

lines=[]

for line in fl:
    lines.append(line)

print(lines)
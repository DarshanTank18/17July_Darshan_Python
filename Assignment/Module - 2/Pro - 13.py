# Write a Python program to count the number of characters (character frequency) in a string 
a = input("Enter any string : ")
b = {}

for i in a :
    if i in b:
        b[i] = b[i]+1
    else :
        b[i] = 1
print(b)
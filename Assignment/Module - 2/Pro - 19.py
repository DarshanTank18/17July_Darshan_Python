# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. 
a = input("enter string:")
count = 0
for i in a:
    count += 1
    b = a[:2] + a[-2:]
print("old string:",a)
print("new string:",b)
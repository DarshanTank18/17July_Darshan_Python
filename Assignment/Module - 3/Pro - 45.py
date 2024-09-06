# Write a Python program to find the highest 3 values in a dictionary

A={'A':10, 'B':20, 'C':30, 'D':40, 'E':50}

B=[]

for i in A.values():
    B.append(i)

B.sort()

print("Highest 3 Value in B:",B[-3:])
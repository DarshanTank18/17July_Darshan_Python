# Write a Python function that takes two lists and returns true if they have at least one common member.

a = [1,2,3,4,5,6]
b = [1]

Common=[]

for i in a:
    for j in b:
        if i is j:
            Common.append(i)

if len(Common)>0:
    print("True")
else:
    print("False")
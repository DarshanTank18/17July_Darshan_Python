# Write a Python program to remove duplicates from a list.

list = []
listt = []

A = int(input("Enter the number of elements you want to add to the list: "))

for i in range(A):
    num = int(input("Enter any number: "))
    list.append(num)

for i in list:
    if i not in listt:
        listt.append(i)

print("Before removing duplicates, the list is:", list)
print("After removing duplicates, the list is:", listt)

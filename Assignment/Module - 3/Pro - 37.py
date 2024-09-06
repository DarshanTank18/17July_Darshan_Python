# Write a Python script to print a dictionary where the keys are numbers between 1 and 15.

number = {}

for num in range(1, 16):
    number[num] = num ** 2

print(number)
# Write python program that swap two number with temp variable and without temp variable.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Before swapping: a =", a, ", b =", b)

temp = a
a = b
b = temp

print("After swapping with temp variable: a =", a, ", b =", b)
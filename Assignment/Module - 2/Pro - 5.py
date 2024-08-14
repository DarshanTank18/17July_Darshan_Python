# Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number", number, "is even.")
else:
    print("The number", number, "is odd.")

# Write a python program to sum of the first n positive integers.
n = int(input("Enter number : "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    sum_n = (n * (n + 1)) // 2
    print("The sum of the first", n, "positive integers is:", sum_n)

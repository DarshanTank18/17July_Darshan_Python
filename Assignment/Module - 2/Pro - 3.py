# Write a Python program to get the Fibonacci series of given range.
number = int(input("Enter number : "))
n1 = 1
n2 = 2
count = 0
if number <= 0 :
    print("please enter positive number")
else :
    print("The fibonacci number is ")
    while count < number :
        print(n1)
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        count+=1
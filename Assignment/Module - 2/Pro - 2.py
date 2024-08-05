#Write a Python program to get the Factorial number of given number.
num = int(input("Enter number = "))

Fact = 1
if num < 0 :
    print("Factorial to available")

elif num == 0 :
    print("Number is zero")

else :
    for i in range(1,num + 1) :
        Fact = Fact * i
    print("The factorial of",num,"is",Fact)
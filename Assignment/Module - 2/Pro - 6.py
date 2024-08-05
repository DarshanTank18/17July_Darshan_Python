# Write python program that swap two number with temp variable and without temp variable.
num1 = int( input("Enter First number: "))
num2 = int( input("Enter second number: ")) 
 
temp = num1
num1 = num2
num2 = temp
   
print ("Num1 after swapping: ",num1)  
print ("Num2 after swapping: ",num2) 
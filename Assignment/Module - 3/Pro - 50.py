# Write a Python function to check whether a number is perfect or not.

A=int(input("Enter Any Number : "))

X=0

for i in range(1,A):
    if A%i ==0:
        X+=i

if X==A:
    print("Yes... This Number is Perfect",A)
else:
    print("No.... This Number is Not Perfect",A)
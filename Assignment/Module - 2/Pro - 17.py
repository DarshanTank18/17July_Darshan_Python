# Write a Python program to get a single string from two given strings,separated by a space and swap the first two characters of each string.
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if len(str1) < 2 or len(str2) < 2 :
    print("Both strings must have at least two characters.")

else :
    new1 = str2[:2] + str1[2:]
    new2 = str1[:2] + str2[2:]
    
    Both = new1 + " " + new2

print("Result : ",Both)


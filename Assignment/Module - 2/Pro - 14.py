# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
str1 = input("Enter first string : ")
str2 = input("Enter second string : ")

if len(str1) >= 2 and len(str2) >= 2 :
    swap1 = str2[:2] + str1[2:]
    swap2 = str1[:2] + str2[2:]

    comb = swap1 + " " + swap2
    print(comb)
else:
    print("Both strings must have at least two characters.")
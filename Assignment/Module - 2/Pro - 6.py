# Write a Python program to test whether a passed letter is a vowel or not. 
letter = input("Enter a letter: ")

vowels = ['a','e','i','o','u','A','E','I','O','U']

if letter in vowels:
    print("The letter", letter, "is a vowel.")
else:
    print("The letter", letter, "is not a vowel.")

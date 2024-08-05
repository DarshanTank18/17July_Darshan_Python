# Write a Python program to test whether a passed letter is a vowel or not. 
character = input("Enter character : ")
vowel = ['a','e','i','o','u','A','E','I','o','u']
if character in vowel :
    print("The name",character,"is vowel")
else :
    print("The name ",character," is not vowel")
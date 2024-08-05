# Write a Python program to count the occurrences of each word in a given sentence 
word = input("Enter paragraph : ")
a = {}
b = word.split()

for i in b :
    if i in a :
        a[i] += 1
    else :
        a[i] = 1
print(a)
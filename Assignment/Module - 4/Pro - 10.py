# Write a Python program to count the frequency of words in a file. 

file = open("data.txt","r")
data = file.readline()

count = 0
enter = input("Enter character frequency find : ")

for i in data :
    if i == enter :
        count += len(i)

print(count)
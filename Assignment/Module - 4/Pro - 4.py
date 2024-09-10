# Write a Python program to read first n lines of a file.
fl = open('Data.txt','a')
fl = open('Data.txt','r')

n = int(input("How many lines Are you Read: "))

for i in range(n):
    print(fl.readline())
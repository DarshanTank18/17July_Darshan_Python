# Write a Python program to unzip a list of tuples into individual lists. 

A = [("d","a","r","s","h","a","n"),(1,2,3,4,5,6),("Hello","Rajkot")]

count = 1
for i in A:
    print(f'List {count} : {list(i)}')
    count += 1
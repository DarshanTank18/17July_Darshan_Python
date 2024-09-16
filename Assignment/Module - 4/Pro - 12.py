# Write a Python program to copy the contents of a file to another file.
f1=open('Data.txt','a')
f2=open('demo.txt','r')

for contents in f2:
    f1.write(contents)
print("Done.. please check Data file...")
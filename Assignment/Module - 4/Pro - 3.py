# Write a Python program to append text to a file and display the text.

fl=open('Data.txt','a')
fl.write("\nit's me darshan :)")

read=open('Data.txt','r')
print(read.read())
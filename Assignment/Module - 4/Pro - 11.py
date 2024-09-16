# Write a Python program to write a list to a file. 

list=['Darshan','Dipesh','Dharam','Meet','Tirth','Dax']


fl=open('Data.txt','w')

for i in list:
    fl.write(f"{i}\n")
print("Done..!")
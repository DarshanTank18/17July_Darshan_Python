"""x = input("Enter value : ")
myset = x.split()
my_set = set(myset)
print("The entered value is : ",my_set)"""

stdata = set()

n = int(input("Enter number of element : "))

for i in range(n) :
    x = input("Enter value : ")
    stdata.add(x)
print(stdata)
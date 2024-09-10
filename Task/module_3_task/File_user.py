fl = open("test.txt","x")

inp = ("Enter number : ")
for i in range(inp):
    id = input("Enter id : ")
    name = input("Enter name : ")
    fl.write(name)
    
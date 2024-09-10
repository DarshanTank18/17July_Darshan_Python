file = open("test1.txt","w")
i=1
x = int(input("Enter number : "))
for i in range(x):
    a = int(input("Enter your table : "))
    for i in range(11):
        abc = f"{a} * {i} = {a * i}\n"
        print(abc)
        file.write(abc)

file.close()

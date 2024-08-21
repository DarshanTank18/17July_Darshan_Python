open("test.txt","a")
i=1
x = int(input("Enter number : "))
for i in range(x):
    a = int(input("Enter your table : "))
    for i in range(10):
        print(a,"*",i,"=",a*i)
        i+= 1
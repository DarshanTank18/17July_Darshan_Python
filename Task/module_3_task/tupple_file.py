file = open("demo1.txt","a")

t = []

a = int(input("Enter number : "))

for i in range(a):
    t.append(input("Enter eliments : "))
print(t)
t = tuple(t)
print(type(t))
file.write(f"list : {t}")
file.close()
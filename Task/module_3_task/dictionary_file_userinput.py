file = open("demo1.txt","a")

d = {}

n = int(input("Enter number : "))
for i in range(n):
    k = input("Keys : ")
    v = input("values : ")

    d.update({k:v})
file.write(f"Dictionary : {d} \n")

for file in 'a':
    print("ok")
else:
    print("no")
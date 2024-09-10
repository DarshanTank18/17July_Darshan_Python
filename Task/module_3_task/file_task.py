# fl= open("demo.txt","w")

# fl.write("abd")
# fl.close()
# ===================================
# file = open("demo2.txt","a")

# name = input("Enter name : ")

# file.write(name)
# file.close()

file = open("demo2.txt","a")
nma = input("Enter name : ")
snm = input("Enter snm : ")

file.write(f"name : {nma}\n")
file.write(f"snm : {snm}")
file.close()
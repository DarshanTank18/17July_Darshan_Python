def getdata() :
    id = input("Enter id : ")
    name = input("Enter name : ")
    city = input("Enter city : ")

    print("id : ",id)
    print("name : ",name)
    print("city : ",city)

a = int(input("How many student : "))

for i in range(a) :
    getdata()
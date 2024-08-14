def abc() :
    id = input("ID : ")
    name = input("Name : ")
    return id,name

def bc() :
    a = abc()
    print("Id : ",a[0])
    print("Name : ",a[1])

bc()
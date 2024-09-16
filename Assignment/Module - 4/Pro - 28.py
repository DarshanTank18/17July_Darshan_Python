# What is used to check whether an object o is an instance of class A?

class a:
    pass
obj = a()

if isinstance(obj, a):
    print("obj is instance of class")
else :
    print("obj is not instance of class")
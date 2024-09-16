# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle 

class Rectangle():
    def Rectangle_data(self):
        length = int(input("Enter length of Rectangle : "))
        width = int(input("Enter width of Rectangle : "))

        rec = length * width

        print("Rectangle is :",rec)

r = Rectangle()
r.Rectangle_data()
# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle 

class Circle():
    def Circle_data(self):
        Radius = float(input("Enter Radius of circle : "))

        cir = 3.14*Radius*Radius

        print("Circle is =",cir)

c = Circle()
c.Circle_data()
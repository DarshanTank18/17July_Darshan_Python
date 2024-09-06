# Write a Python program to calculate surface volume and area of a cylinder

import math

R = int(input("Enter redious : "))
H = int(input("Enter height : "))

Volume = 3.14 * R ** 2 * H

surface_area = 2 * 3.14 * R * (R + H)

print(f"Volume of the cylinder is: {Volume}")
print(f"Surface area of the cylinder is: {surface_area}")
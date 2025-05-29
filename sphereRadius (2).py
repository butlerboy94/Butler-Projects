""" Write a program that takes the radius of a sphere (a floating-point number)
as input and then outputs the spheres diameter, circumference, surface area, and volume)"""
# formula for diameter 2*r
# formula for cirumference 2*pi*r
# formula for surface area 4*pi*r**2
# formula for volume (4/3)*pi*r**3
# pi is input as math.pi

# import math
# import fractions from Fraction

import math
from fractions import Fraction

# create variables for fraction, diameter, circumference, surface area, and volume

fraction1 = Fraction(4,3)
radius = float(input("What is the radies of the sphere? "))
sphere_Diameter = (radius * 2)
sphere_Circumference = (2 * math.pi * radius)
sphere_SurfaceArea = (4 * math.pi * radius**2)
sphere_Volume = (fraction1 * math.pi * radius**3)

# output diameter, circumference, surface area, and volume

print("The Diamater is:", sphere_Diameter )
print("The Circumference is:", sphere_Circumference)
print("The Surface Area is:", sphere_SurfaceArea)
print("The Volume is:", sphere_Volume)

# find area and circumfernce of the circle

import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * pow(radius,2)
circumference = 2 * math.pi * radius

print(f"The area of the circle is {round(area,3)}")
print(f"The circumference of of the circle is {round(circumference,3)}")



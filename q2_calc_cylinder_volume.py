# q2_calc_cylinder_volume.py
# calculate volume of cylinder

# get input
radius = float(input("Enter radius of cylinder(cm):"))
length = float(input("Enter length of cylinder(cm):"))

# calculate volume of cylinder
from math import *
area = radius * radius * pi
volume = area * length

# output result
print("Volume of cylinder is", volume)

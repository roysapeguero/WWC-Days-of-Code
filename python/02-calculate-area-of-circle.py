# Today's Challenge:
# Create a program to calculate the area of a circle given its radius.

from math import pi

def area_of_circle(radius):
  circle_area = pi * pow(radius, 2)
  print(circle_area)

area_of_circle(20)

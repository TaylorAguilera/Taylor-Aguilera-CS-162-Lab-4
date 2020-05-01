#Taylor Aguilera CS 162 Lab #4 4/30/2020
import math
class GeometricShape:
   def __init__(self):
       self.color = "green"
       self.filled = True
   def get_color(self):
       return self.color
   def set_color(self, new_color):
       self.color = new_color
   def is_filled(self):
       return self.filled
   def set_filled(self, filled):
       self.filled = filled
   def __str__(self):
       return "color: " + self.color + " and filled " + str(self.filled)
class Circle(GeometricShape):
   def __init__(self, radius, color = "green", filled = True):
       self.radius = radius
       self.color = color
       self.filled = filled
   def get_radius(self):
       return self.radius
   def set_radius(self, new_radius):
       self.radius = new_radius
   def get_area(self):
       return round(math.pi * self.radius ** 2, 2)
   def get_circumferece(self):
       return round(2 * math.pi * self.radius, 2)
   def get_diameter(self):
       return round(2 * self.radius, 2)
   def __str__(self):
       return "Circle with : radius = " + str(self.radius) + " " + super().__str__()
r1 = int(input("Enter the radius:\t"))
color = input("Enter color:\t")
filled = int(input("Enter 1/0 for filled (1: true, 0:false):\t"))
if(filled == 0):
   c1 = Circle(r1, color, False)
else:
   c1 = Circle(r1, color, True)
print("The diameter is : " + str(c1.get_diameter()))
print("The circumference is: " + str(c1.get_circumferece()))
print("The area is : " + str(c1.get_area()))
print("The circle is : " + c1.__str__())
r2 = int(input("Enter the radius:\t"))
c2 = Circle(r1)
print("The diameter is : " + str(c2.get_diameter()))
print("The circumference is: " + str(c2.get_circumferece()))
print("The area is : " + str(c2.get_area()))
print("The circle is : " + c2.__str__())
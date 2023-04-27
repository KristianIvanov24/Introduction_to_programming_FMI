import math


class Shape:
    def area(self):
        pass

      
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height

      
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return 0.5 * self.base * self.height

      
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2

      
shapes = [Rectangle(5, 10), Triangle(3, 6), Circle(7)]
for shape in shapes:
    print(shape.area())

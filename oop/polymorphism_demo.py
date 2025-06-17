import math 
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")     


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
  
    def area(self, width, height):
        return f'THe area of the Rectangle is: {width * height}'
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self, radius):
        return f'The area of the Circle is: {math.pi * radius * radius}'
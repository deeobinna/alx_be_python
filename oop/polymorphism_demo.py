import math 
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")     


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.height = length
  
    def area(self, width, height):
        return f'THe area of the Rectangle is: {self.width * self.length}'
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self, radius):
        return f'The area of the Circle is: {math.pi * self.radius ** 2}'
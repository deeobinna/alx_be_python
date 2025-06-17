
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")     


class Rectangle(Shape):
    def __init__(self, length, width ):
        self.width = width
        self.height = length

    
    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self, radius):
        import math 
        return math.pi * self.radius ** 2
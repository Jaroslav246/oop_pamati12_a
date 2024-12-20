class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math * (self.radius ** 2)

    def perimeter(self):
        return 2 * math * (self.radius)
    
shapes = [
    Rectangle(5, 10),
    Circle(7)
]

for shape in shapes:
  print(f"Shape: {type(shape).__name__}")
  print(f"Area: {shape.area():.2}")
  print(f"Perimeter: {shape.perimeter():.2}")
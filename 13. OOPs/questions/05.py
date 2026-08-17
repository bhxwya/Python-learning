class Shape:
    def draw(self):
        return "Drawing a Shape"

class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"
    
class Rectangle(Shape):
    def draw(self):
        return "Drawing a Rectangle"
    
shape = Shape()

circle = Circle()

rectangle = Rectangle()

# print(shape.draw())

# print(circle.draw())

# print(rectangle.draw())

shapes = [shape, circle, rectangle]
for shape in shapes:
    print(shape.draw())
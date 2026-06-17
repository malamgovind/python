class Rectangle:

    def area(self):
        print("Rectangle area")

class Circle:

    def area(self):
        print("Circle area")


shapes = [Rectangle(), Circle()]

for shape in shapes:
    shape.area()
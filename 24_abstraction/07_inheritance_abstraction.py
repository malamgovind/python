from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def area(self):
        print("Circle Area")

circle = Circle()

circle.area()
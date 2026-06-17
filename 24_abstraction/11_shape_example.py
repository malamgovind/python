from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):

    def draw(self):
        print("Drawing Rectangle")

obj = Rectangle()

obj.draw()
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def move(self):
        pass


class Bike(Vehicle):

    def move(self):
        print("Bike Moving")

bike = Bike()

bike.move()
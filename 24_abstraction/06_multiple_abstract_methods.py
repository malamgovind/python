from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car Started")

    def stop(self):
        print("Car Stopped")

car = Car()
car.start()
car.stop()

# car.start()
#     │
#     ▼
# car variable
#     │
#     ▼
# Car Object
#     │
#     ▼
# Car Class
#     │
#     ▼
# start()
#     │
#     ▼
# self = Car Object
#     │
#     ▼
# print("Car Started")
#     │
#     ▼
# Function End
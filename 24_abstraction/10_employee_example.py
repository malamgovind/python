from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def work(self):
        pass


class Developer(Employee):

    def work(self):
        print("Writing Code")

dev = Developer()

dev.work()
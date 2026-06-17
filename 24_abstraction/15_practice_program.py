from abc import ABC, abstractmethod

class Person(ABC):

    @abstractmethod
    def info(self):
        pass


class Student(Person):

    def info(self):
        print("Student Information")

student = Student()

student.info()
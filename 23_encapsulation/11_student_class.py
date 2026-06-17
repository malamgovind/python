class Student:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

student = Student("govind")

print(student.get_name())
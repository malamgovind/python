class Student:

    def __init__(self):
        self.__name = "malam"

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

student = Student()
student.set_name("govind")
print(student.get_name())    
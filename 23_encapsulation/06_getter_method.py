class Student:

    def __init__(self):
        self.__name = "govind"

    def get_name(self):
        return self.__name
    
student = Student()
print(student.get_name())
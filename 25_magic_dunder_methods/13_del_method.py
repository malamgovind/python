class Student:

    def __del__(self):
        print("Object Deleted")

student = Student()

del student
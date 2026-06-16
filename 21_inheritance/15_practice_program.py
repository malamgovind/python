class Person:

    def show(self):
        print("Person")


class Student(Person):
    pass

student = Student()

student.show()
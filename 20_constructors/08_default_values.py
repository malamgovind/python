class Student:

    def __init__(self, name="defualt"):
        self.name = name

student1 = Student()
student2 = Student("govind")

print(student1.name)
print(student2.name)
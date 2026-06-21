import copy 

class Student:

    def __init__(self, name):
        self.name = name

s1 = Student("govind")

s2 = copy.copy(s1)

s2.name = "malam"

print(s1.name)
print(s2.name)
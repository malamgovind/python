class Person:

    def __init__(self):
        self.__age = 25

    def get_age(self):
        return self.__age
    
age = Person()

print(age.get_age())
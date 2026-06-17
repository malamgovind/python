class Animal:

    def sound(self):
        print("animal sound")

class Cat(Animal):
    
    def sound(self):
        print("meavvv")

class Dog(Animal):
    
    def sound(self):
        print("bhavvvv")

animals = [Cat(), Dog()]

for animal in animals:
    animal.sound()
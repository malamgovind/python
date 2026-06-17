class Dog:

    def sound(self):
        print("bhavv")

class Cat:

    def sound(self):
        print("meyavvv")

class Cow:

    def sound(self):
        print("baaa")

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()
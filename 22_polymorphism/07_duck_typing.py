class Cat:

    def sound(self):
        print("meyavvv")

class Dog:

    def sound(self):
        print("bhauuu")

def make_sound(animal):
    animal.sound()

make_sound(Cat())
make_sound(Dog())
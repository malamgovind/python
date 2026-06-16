# issubclass(Child, Parent)
# Child class Parent ની subclass છે કે નહીં


class Animal:
    pass

class Dog(Animal):
    pass

print(issubclass(Dog, Animal))
class Grandfather:

    def house(self):
        print("Grandfather house")

class Parent(Grandfather):
    pass

class Child(Parent):
    pass

obj = Child()
obj.house()
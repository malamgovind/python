# Child Class
# Parent ના Method ને
# Replace કરે

# =

# Method Overriding

class Parent:

    def show(self):
        print("Parent Method")


class Child(Parent):

    def show(self):
        print("Child Method")

obj = Child()

obj.show()
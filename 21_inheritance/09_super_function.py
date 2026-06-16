# super()

# Parent Class ના Methods
# અને Constructor Call કરવા ઉપયોગી છે.

class Parent:

    def __init__(self):
        print("parent constructor")

    def govind(self):
        print("parent constructor")

class Child(Parent):

    def __init__(self):
        super().__init__()
        super().govind()
        print("child constructor")

child = Child()
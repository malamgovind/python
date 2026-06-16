# Child()
# ↓
# Child Constructor ?
# ↓
# No
# ↓
# Parent Constructor

class Parent:

    def __init__(self):
        print("Parent Constructor")


class Child(Parent):
    pass

child = Child()
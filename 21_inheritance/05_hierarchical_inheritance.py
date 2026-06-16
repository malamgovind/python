#         Parent
#         /   \
#        /     \
#    Child1   Child2

class Parent:

    def home(self):
        print("Parent Home")


class Child1(Parent):
    pass


class Child2(Parent):
    pass

c1 = Child1()
c2 = Child2()

c1.home()
c2.home()
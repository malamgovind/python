class Father:

    def money(self):
        print("father's money")

class Mother:

    def case(self):
        print("mother's case")

class Child(Father, Mother):
    pass

obj = Child()
obj.money()
obj.case()
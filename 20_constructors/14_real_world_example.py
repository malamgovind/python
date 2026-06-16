class Mobile:

    def __init__(self, brand,  ram):
        self.brand = brand
        self.ram = ram

mobile = Mobile("samasung", "12gb")
print(mobile.brand)
print(mobile.ram)
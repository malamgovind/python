class Mobile:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

mobile = Mobile("samansung", 500000)
print(mobile.brand)
print(mobile.price)
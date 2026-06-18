class Product:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

product = Product("Laptop")

print(product)
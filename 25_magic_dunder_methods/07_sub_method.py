class Number:

    def __init__(self, value):
        self.value = value

    def __sub__(self, other):
        return self.value - other.value

n1 = Number(50)
n2 = Number(20)

print(n1 - n2)
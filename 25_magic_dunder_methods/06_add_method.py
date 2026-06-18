# n1 + n2
# ↓
# n1.__add__(n2)
# ↓
# 30

class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)

print(n1 + n2)
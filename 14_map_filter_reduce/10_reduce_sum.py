from functools import reduce

number = [10, 20, 30]

result = reduce(lambda a, b: a + b, number)

print(result)

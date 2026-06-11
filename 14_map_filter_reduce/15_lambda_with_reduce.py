from functools import reduce

numbers = [5, 5, 5]

result = reduce(lambda a, b: a + b, numbers)

print(result)
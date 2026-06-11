from functools import reduce

number = [1, 2, 3, 4, 5]

result = reduce(lambda a, b: a * b, number)

print(result)

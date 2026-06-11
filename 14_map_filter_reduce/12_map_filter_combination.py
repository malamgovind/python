number = [1, 2, 3, 4, 5]

even = filter(lambda x: x % 2 == 0, number)
square = map(lambda x: x ** 2, even)

print(list(square))
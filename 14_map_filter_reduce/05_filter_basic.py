number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = filter(lambda x: x % 2 != 0, number)

print(list(result))
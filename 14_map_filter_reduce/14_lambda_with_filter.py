numbers = [10, 15, 20, 25]

result = filter(lambda x: x % 5 == 0, numbers)

print(list(result))
number = [1, 2, 3, 4, 5]

result = list(filter(lambda x: x % 2 == 0 , number))

print(result)
print(type(result))
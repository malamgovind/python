def calculate(func, value):
    return func(value)

result = calculate(lambda x: x * 10, 5)

print(result)
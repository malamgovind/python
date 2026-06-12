def number():
    yield 10
    yield 20

for num in number():
    print(num)
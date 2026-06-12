def square_generator(limit):

    for i in range(1, limit + 1):
        yield i ** 2

for value in square_generator(5):
    print(value)
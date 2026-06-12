def even_number(limit):
    for i in range(1, limit + 1, 2):
        yield i

for number in even_number(10):
    print(number)
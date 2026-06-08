# generate function with yield 
# problem : write a generator function that yields even numbers up to a specified limit.

def even_numbers(limit):
    for num in range(1, limit + 1):
        yield num * 2

print(even_numbers(10))

def even_generator(limit):
    for num in range(2, limit + 1, 2):
        yield num

for even in even_generator(10):
    print(even)
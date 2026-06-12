def my_generator():
    yield 1

gen = my_generator()

print(next(gen))
# print(next(gen))
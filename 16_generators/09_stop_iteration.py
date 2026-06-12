def number():
    yield 1
    yield 2
    yield 3

gen = number()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
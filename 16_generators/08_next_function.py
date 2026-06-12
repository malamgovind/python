def number():
    yield 1
    yield 2
    yield 3

print(next(number()))
print(next(number()))
print(next(number()))

gen = number()
print(next(gen))
print(next(gen))
print(next(gen))
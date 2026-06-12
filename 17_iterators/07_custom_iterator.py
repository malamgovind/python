class Count:

    def __iter__(self):
        return self

    def __next__(self):
        return 1

obj = Count()

iterator = iter(obj)

print(next(iterator))
print(next(iterator))
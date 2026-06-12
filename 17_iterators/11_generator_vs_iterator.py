class Numbers:

    def __iter__(self):
        return self

    def __next__(self):
        return 1
    
number = Numbers()

def numbers():
    yield 1

print(next(number))
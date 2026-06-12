class NumberIterator:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.num <= 5:
            value = self.num
            self.num += 1
            return value

        raise StopIteration

obj = NumberIterator()

for item in obj:
    print(item)
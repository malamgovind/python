class Counter:

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

counter = Counter()
# print(next(counter))
for item in counter:
    print(item)


#     Object Created

# num = 1
#  │
#  ▼
# return 1

# num = 2
#  │
#  ▼
# return 2

# num = 3
#  │
#  ▼
# return 3

# num = 4
#  │
#  ▼
# return 4

# num = 5
#  │
#  ▼
# return 5

# num = 6
#  │
#  ▼
# StopIteration
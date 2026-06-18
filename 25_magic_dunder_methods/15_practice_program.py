class Book:

    def __init__(self, pages):
        self.pages = pages

    def __len__(self):
        return self.pages

book = Book(250)

print(len(book))
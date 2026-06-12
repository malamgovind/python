class infinite:
    def __iter__(self):
        return self
    
    def __next__(self):
        return 10
    
obj = infinite()

print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
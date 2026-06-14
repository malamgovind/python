def decorator(func):
    def wrapper(*args, **kwargs):
        print("before")
        result = func(*args, **kwargs)
        print("after")
        return result
    return wrapper
def add(a, b):
    return a + b

print(add(10, 20))


#  add(10, 20)
#      │
#      ▼
#  wrapper(10, 20)
#      │
#      ▼
#  result = func(10, 20)
#      │
#      ▼
#  add(10, 20)
#      │
#      ▼
#  30
#      │
#      ▼
#  result = 30
#      │
#      ▼
#  return 30
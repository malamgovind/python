def decorator(fanc):
    def wrapper():
        print("before function")

        fanc()

        print("after function")

    return wrapper

def greet():
    print("govind")

greet = decorator(greet)

greet()


#  greet()
#    │
#    ▼
#  wrapper()
#    │
#    ├── print("Before Function")
#    │
#    ├── func()
#    │      │
#    │      ▼
#    │   original greet()
#    │      │
#    │      ▼
#    │   print("Hello")
#    │
#    └── print("After Function")

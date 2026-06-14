def decorator(fanc):
    def wrapper():
        print("before function")

        fanc()

        print("after function")

    return wrapper

@decorator
def greet():
    print("govind")


greet()

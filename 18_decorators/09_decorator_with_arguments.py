def decorator(func):
    
    def wrapper(name):
        print("welcome")
        func(name)

    return wrapper
@decorator
def demo(name):
    print(name)
demo("govind")
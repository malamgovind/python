def logger(func):

    def wrapper():
        print("Function Started")

        func()

        print("Function Ended")

    return wrapper

@logger
def display():
    print("Running")

display()
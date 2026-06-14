# task problem : Function call પહેલાં અને પછી message print કરો.

def monitor(func):

    def wrapper():

        print("Program Started")

        func()

        print("Program Finished")

    return wrapper


@monitor
def task():
    print("Task Running")

task()
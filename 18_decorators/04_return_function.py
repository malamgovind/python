def outer():
    
    def inner():
        print("hello govind")

    return inner

fanc = outer()

fanc()
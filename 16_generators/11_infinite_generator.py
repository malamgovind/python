def infinite():

    num = 1

    while True:
        yield num
        num += 1

gen = infinite()


for i in range(5):
    print(next(gen))
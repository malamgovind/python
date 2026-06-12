def generator():

    value = yield

    print(value)
gen = generator()
# print(next(gen))
next(gen)
gen.send("hello")
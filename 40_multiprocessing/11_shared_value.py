from multiprocessing import Process,Value

def increment(value):

    value.value += 1

number = Value("i",0)

p = Process(
    target=increment,
    args=(number,)
)

p.start()

p.join()

print(number.value)
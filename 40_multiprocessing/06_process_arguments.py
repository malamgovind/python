from multiprocessing import Process

def add(a,b):
    print(a+b)

p = Process(
    target=add,
    args=(10,20)
)

p.start()

p.join()
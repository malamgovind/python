import threading

def add(a, b):
    print(a + b)

t = threading.Thread(
    target=add,
    args=(10, 20)
)

t.start()

t.join()
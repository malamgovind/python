import threading

def message():

    print("Hello Python")

t = threading.Thread(
    target=message
)

t.start()

t.join()
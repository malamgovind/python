import threading

lock = threading.Lock()

def task():

    with lock:
        print("Resource Locked")

t = threading.Thread(target=task)

t.start()

t.join()
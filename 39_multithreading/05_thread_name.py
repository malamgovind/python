import threading

def task():
    print(threading.current_thread().name)

t = threading.Thread(target=task, name="Worker")

t.start()

t.join()
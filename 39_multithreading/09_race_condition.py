import threading

counter = 0

lock = threading.Lock()

def increment():

    global counter

    with lock:
        counter += 1

threads = []

for i in range(100):

    t = threading.Thread(
        target=increment
    )

    threads.append(t)

    t.start()

for t in threads:
    t.join()

print(counter)
from multiprocessing import Process,Queue

def task(q):
    q.put("Hello")

q = Queue()

p = Process(
    target=task,
    args=(q,)
)

p.start()

print(q.get())

p.join()
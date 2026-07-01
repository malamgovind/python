from multiprocessing import Process

def task():
    print("Hello Process")

p = Process(target=task)

p.start()

p.join()
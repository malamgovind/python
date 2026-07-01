from multiprocessing import Process,current_process

def task():
    print(current_process().name)

p = Process(target=task,name="Worker Process")

p.start()

p.join()
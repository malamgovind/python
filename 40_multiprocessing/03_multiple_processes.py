from multiprocessing import Process

def task(name):
    print(name)

p1 = Process(target=task,args=("Process 1",))
p2 = Process(target=task,args=("Process 2",))

p1.start()
p2.start()

p1.join()
p2.join()
from multiprocessing import Process

def message():
    print("Hello Python")

p=Process(target=message)

p.start()

p.join()
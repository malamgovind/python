from multiprocessing import Process
import time

def work():
    time.sleep(2)
    print("Work Finished")

p = Process(target=work)

p.start()

p.join()

print("Main Process Finished")
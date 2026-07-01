import threading
import time

def work():
    time.sleep(2)
    print("Work Finished")

t = threading.Thread(target=work)

t.start()

t.join()

print("Main Thread Finished")
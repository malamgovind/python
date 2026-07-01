import threading
import time

def background():
    while True:
        print("Running...")
        time.sleep(1)

t = threading.Thread(
    target=background,
    daemon=True
)

t.start()

time.sleep(3)

print("Main Program End")
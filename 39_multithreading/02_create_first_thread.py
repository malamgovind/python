import threading

def show():
    print("Hello Thread")

thread = threading.Thread(target=show)

thread.start()

thread.join()

# Thread Object
# ↓
# start()
# ↓
# Function Executes
# ↓
# join()
# ↓
# Finish
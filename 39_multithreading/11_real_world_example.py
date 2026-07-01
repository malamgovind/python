import threading
import time

def download(file):

    print(file, "Downloading")

    time.sleep(2)

    print(file, "Completed")

files = [
    "image.jpg",
    "video.mp4"
]

threads = []

for file in files:

    t = threading.Thread(
        target=download,
        args=(file,)
    )

    threads.append(t)

    t.start()

for t in threads:
    t.join()

print("All Downloads Finished")
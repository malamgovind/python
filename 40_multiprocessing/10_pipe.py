from multiprocessing import Pipe,Process

def sender(conn):

    conn.send("Hello")

    conn.close()

parent,child = Pipe()

p = Process(
    target=sender,
    args=(child,)
)

p.start()

print(parent.recv())

p.join()
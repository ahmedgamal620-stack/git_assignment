import threading

sem = threading.Semaphore(2)

def task():
    with sem:
        print("Accessing resource")

for _ in range(5):
    threading.Thread(target=task).start()

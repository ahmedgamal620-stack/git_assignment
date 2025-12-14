import threading

def task():
    print("Thread is running")

t = threading.Thread(target=task)
t.start()
t.join()

#this is comment
# threading example

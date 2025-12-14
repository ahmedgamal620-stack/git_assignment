import threading

lock1 = threading.Lock()
lock2 = threading.Lock()

def task1():
    with lock1:
        with lock2:
            print("Task 1")

def task2():
    with lock2:
        with lock1:
            print("Task 2")

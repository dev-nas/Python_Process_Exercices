from multiprocessing import Process, Value, Lock
from time import sleep

def my_func(n, plus, lock):
    while n.value < 100:
        sleep(0.01)
        # entre acquire et release, 
        # aucun autre processus ne peut accéder à n
        lock.acquire()
        print(f"p{plus} lock")
        n.value += plus
        print(f"n = {n.value}")
        # lock.release()

# déverouille le verrou toutes les 0.1s sur une 1s
def check_lock(lock):
    for i in range(100):
        sleep(0.1)
        print(f"p3 release n°{i}")
        lock.release()

n = Value('i', 0)
lock = Lock()
# lock = None
p1 = Process(target = my_func, args = (n, 1, lock))
p2 = Process(target = my_func, args = (n, 2, lock))
p3 = Process(target=check_lock, args = (lock,))
p1.start();p2.start();p3.start()
p1.join();p2.join();p3.join()
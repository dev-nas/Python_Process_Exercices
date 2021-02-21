from multiprocessing import Lock, RLock

# fonction a qui peut utiliser fonction b
def a(lock, param=False):
    # lock.acquire()
    # print("something....")
    # if param:
    #     b(lock)
    # lock.release()
    # Lock.__enter__ procède au acquire()
    # Lock.__exit__ procède au release()
    # Rlock est réentrant
    with lock:
        print("something")
        if param:
            b(lock)

# fonction b qui peut être utilisée en standalone ou dans
def b(lock):
    # lock.acquire()
    # print("something else ...")
    # lock.release()
    with lock:
        print("something else")

if __name__ == "__main__":
    # avec un lock: a(lock, True va bloquer)
    # avec un rlock: le rlock peut être acquis plusieurs fois par le
    # même processus. il doit être libéré autant de fois
    lock = Lock()
    rlock = RLock()
    a(rlock, True)
    
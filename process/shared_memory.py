import os
from multiprocessing import Process, Value, Array

# résultats avec ou sans mémoire partagée

def worker(n, a):
    print(f"child pid: {os.getpid()}")
    #n.value += 5
    n += 5
    a[4] = 6

print(f"parent pid: {os.getpid()}")

#n = Value('i', 5)
#a = Array('i', [1, 2, 3, 4, 5])
n = 5
a = [1, 2, 3, 4, 5]
# print(f"n = {n.value}", f", a[4] = {a[4]}")
print(f"n = {n}", f", a[4] = {a[4]}")

p = Process(target = worker, args = (n, a))
p.start()
p.join()

print(f"child exits: {p.exitcode}")
# print(f"n = {n.value}", f", a[4] = {a[4]}")
print(f"n = {n}", f", a[4] = {a[4]}")
print(list(a))
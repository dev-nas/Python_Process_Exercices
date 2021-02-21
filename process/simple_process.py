import os
from multiprocessing import Process
from time import sleep

# fonction destinée à être exécutée par un 
# processus (ou thread) ==> un WORKER
def my_func(n):
    print(f"child pid: {os.getpid()}")
    for i in range(n):
        print(i)
        if i == 2:
            3/0
        sleep(1)

print(f"parent pid: {os.getpid()}")

# création d'un processus qui va exécuter my_func(5)
p = Process(target = my_func, args = (5,))
# démarrage du processus
p.start()
# attendre par défaut la fin du processus
# p.join()

# join non bloquant : 
# on checke toutes les secondes si le
# process a terminé
# au bout de 2 tentatives on termine le
# process depuis le parent
for i in range(3):
    print(f"tentative {i + 1}")
    p.join(timeout=1)
# savoir si le processus est toujours en cours d'exécution
if p.is_alive():
    print("process trop lent!")
    # "kill" le processus
    p.terminate()

print(f"child exits {p.exitcode}")
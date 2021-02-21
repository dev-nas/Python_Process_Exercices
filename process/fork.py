import os, sys
from time import sleep

# le processus qu'on lancé avec "python3 fork.py"
# demande un fork
# l'état du processus parent s'arrête à l'évaluation 
# de l'expression "os.fork()"
# l'exécution reprend dans les deux processus au moment
# de l'affectation de la valeur de retour du fork
pid = os.fork()

if pid != 0:
    print(f"parent: child PID {pid}")
else:
    print(f"child: own PID: {os.getpid()}")
    sleep(3)
    sys.exit(0)

while True:
    print("waiting for children")
    try:
        # os.waitpid par défaut bloque l'exécution du process
        # de PID pid tant que ce process n'a pas terminé
        pid, status = os.waitpid(pid, 0)
        print(pid, status)
    except OSError as oe:
        print(oe)
        break
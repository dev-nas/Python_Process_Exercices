import signal, os, time, sys
from multiprocessing import Process

def my_handler(signum, stack_frame):
    print(f"I have encountered the signal {signum}")
    time.sleep(3)
    raise SystemExit('parent exit')
    # sys.exit("parent exit")

def trigger_signal(pid, signum):
    time.sleep(3)
    print(f"trigger signal {signum} in pid: {pid}")
    # appel système à kill -10 pid
    os.kill(pid, signum)
    sys.exit("child exit")

# on associe la réception d'un signal SIGUSR1 à l'exécution de my_handler
#signal.signal(signal.SIGUSR1, my_handler)
# on désactive SIGINT (Ctrl C) patr SIG_IGN (IGNORE)
#signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGINT, my_handler)

p = Process(target=trigger_signal, args=(os.getpid(), signal.SIGUSR1))
p.start()

print("waiting for signal SIGUSR1 to terminate")
signal.pause()
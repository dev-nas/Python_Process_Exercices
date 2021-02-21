from multiprocessing import Process, Queue, current_process
import queue, time

# worker de traitement de tâches
def do_job(to_do, jobs_done):
    # cuurent_process renvoie() dess information sur le processus courant
    p_name = current_process().name
    print(f"{p_name} waiting for queue to get elem")
    while True:
        try:
            # Queue.get est bloquant par défaut
            task = to_do.get(False)
            time.sleep(0.001)
        except queue.Empty:
            print(f"{p_name}: empty queue !")
            break
        else:
            # on renvoie dans jobs_done les résultats de traitement
            jobs_done.put(f"{task} done by {p_name}")


to_do, jobs_done = Queue(), Queue()
processes = []
# ajout d'éléments dans la queue to_do
for i in range(10):
    to_do.put(f"Task no {i}")

for w in range(4):
    # on lance 4 workers pour traiter les 10 tâches de jobs
    p = Process(target=do_job, args=(to_do, jobs_done))
    processes.append(p)
    p.start()

for p in processes:
    p.join()

# tant que la queue job_done n'est pas vide
while not jobs_done.empty():
    print(jobs_done.get())
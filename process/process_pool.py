import time
from multiprocessing import Pool, current_process

# worker pour un countdown
def countdown(n):
    while n > 0:
        n -= 1
    return f"{current_process().name} finished!"

COUNT = 100000000
start = time.time()

with Pool(processes=4) as pool:
    # apply est bloquant, apply_async non
    r_apply = pool.apply_async(countdown, [COUNT/4])
    # idem entre map et map_async
    r_map = pool.map_async(countdown,[COUNT/4, COUNT/4, COUNT/4])
    pool.close()
    pool.join()

# apply et map renvoie directment les retour du worker
# les version async renvoie un objet: on utilisera
# leur méthode get()
# print(r_apply, r_map)
print(r_apply.get(), r_map.get())
end = time.time()
print(f"{end-start} s")
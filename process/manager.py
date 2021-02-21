from multiprocessing import Process, Manager


def worker(dct, lst):
    dct['key'] = 'value'
    lst.reverse()

# beaucoup plus pratique que Value et Array
with Manager() as manager:
    dico = manager.dict()
    liste = manager.list(range(10))
    
    p = Process(target=worker, args=(dico, liste))
    p.start()
    p.join()
    
    print(dico, liste)
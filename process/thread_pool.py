import requests, time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor, Future, as_completed

def load(url, urls):
    with requests.Session() as s:
        r = s.get(url)
        if r.status_code == 200:
            urls.append(r)

def load(url):
    with requests.Session() as s:
        try:
            r = s.get(url)
            if r.status_code == 200:
                return r
        except Exception as e:
            return e

URLS = [
    "https://dawan.fr",
    "https://python.org",
    "http://www.fffffffff.fr",
    "https://www.google.fr",
    "https://docs.gitlab.com"
]

if __name__ == "__main__":
    start = time.time()
    with ThreadPoolExecutor(max_workers = 5) as pool:
        # dictionnaire en intension
        # submit lance un worker sur un des threads du pool
        # les objets retournés par submit sont des concurrent.futures.Future
        # ces objets possèdent des méthodes bloquantes pour attendre un resultat
        futures = {
            pool.submit(load, url): url for url in URLS
        }
        results = []
        # as_completed attend le temps minimum de complétion des futures
        for future in as_completed(futures):
            results.append(future.result())
        print(results)
    print(time.time() - start)
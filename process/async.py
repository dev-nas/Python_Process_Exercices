import requests, time
import asyncio

async def load(url):
    with requests.Session() as s:
        try:
            r = s.get(url)
            if r.status_code == 200:
                return r
        except Exception as e:
            return e

# le main est l'appel asynchrone en paramètre de asyncio.run()
async def main():
    # on se donne une liste de tâches asynchrones
    # ici load(url) n'exécute pas la fonction
    # load(url) retourne l'objet coroutine lié à la fonction load
    tasks = [
        asyncio.create_task(load(url)) for url in URLS
    ]
    # attente du retour des appels asynchrone
    # attente ==> await
    r = await asyncio.gather(*tasks)
    
    # as_completed renvoie un otérateur sur les appels asynchrones
    # dans l'ordre des lancements
    # r = asyncio.as_completed(tasks)
    # for cor in r:
    #     print(await cor)

URLS = [
    "https://dawan.fr",
    "https://python.org",
    "http://www.fffffffff.fr",
    "https://www.google.fr",
    "https://docs.gitlab.com"
]

if __name__ == "__main__":
    start = time.time()
    # appel à une coroutine principale
    asyncio.run(main())
    print(time.time() - start)
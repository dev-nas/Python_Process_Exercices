import requests
from concurrent.futures import ThreadPoolExecutor
from itertools import count

class GoRestApiClient:
    _url = None
    _token = None
    
    def __init__(self, token="f272e67cd0429faafae6fba2a892b9464b60fe6fe03621db530f667a62f86cd2", url="https://gorest.co.in/public-api/"):
        self._url = url
        self._token = token
        
    def _call(self, method, endpoint, query_string="", data={}, headers={}):
        ret, location = {}, self._url + endpoint
        try:
            # la fonction getattr(obj, attr) retourne l'attribut ou la méthode attr de l'objet obj 
            call = getattr(requests, method.lower())
            r = call(location, data=data, headers=headers)
            if r.status_code in (200, 201):
                ret = r.json()
        except (HTTPError, RequestException) as e:
            raise ValueError("NOK")
        finally:
            return ret
    
    def get_user(self, id):
        r = self._call("GET", f"users/{id}")
        return r["data"]
    
    def create_user(self, data):
        r = self._call("POST", "users", data=data, headers={"Authorization": f"Bearer {self._token}"})
        return r
    
    # worker potentiel
    def get_user_page(self, page_id):
        return self._call("GET", f"users?page={page_id}")
    
    def get_all_users(self):
        data = []
        # au lieu de renseigner un nombre max d'exécutions
        # on utilise un itérateur infini
        # for i in range(1, 74):
        for i in count(start=1):
            r = self._call("GET", f"users?page={i}")
            if not r["data"]:
                return data
            data += r["data"]
    
    # def get_all_users_thread(self, workers=5):
    #     with ThreadPoolExecutor(max_workers=workers) as pool:
    #         data, eom = [], 0
    #         for i in count():
    #             # récupérer les pages de 5 en 5 (1-6, 6-11, 11-16...)
    #             futs = []
    #             start, end = i * workers + 1, (i + 1) * workers + 1
    #             for j in range(start, end):
    #                  futs.append(pool.submit(self.get_user_page, j))
    #             for f in as_completed(futs):
    #                 # gérer l'arrêt du programme si l'une des pages retournées n'a
    #                 # plus de données
    #                 if not f.result()["data"]:
    #                     eom = 1
    #                 data += f.result()["data"]
    #             print(f"fetched page {start} to {end}")
    #             if eom:
    #                 return data
    
    def get_all_users_thread(self, workers=10):
        with ThreadPoolExecutor(max_workers=workers) as pool:
            data = []
            for i in count():
                # récupérer les pages de 5 en 5 (1-6, 6-11, 11-16...)
                start, end = i * workers + 1, (i + 1) * workers + 1
                # TreadPoolExecutor répartit les exécution du worker sur les threads
                # disponibles du pool et renvoie les résultats dans l'ordre des paramètres
                r = pool.map(self.get_user_page, list(range(start, end)))
                for response in r:
                    if not response["data"]:
                        return data
                    data += response["data"]
                print(f"fetched page {start} to {end}")


if __name__ == "__main__":
    api = GoRestApiClient()
    print(api.get_all_users_thread())
    # print(api.create_user({"name": "bla", "email": "a@a.fr", "status": "Active", "gender": "Female"}))
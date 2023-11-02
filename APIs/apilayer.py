import requests

API_KEY = ""

class APILayer:
    def __init__(self) -> None:
        self.headers = {"apikey": API_KEY}

    def parse(self, filepath):
        url = requests.post(filepath)
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            result = response.json()
            return result
        else:
            return {"Error:": response.status_code}
 
 
import requests
import os 
from FileStores.amazons3 import AmazonS3
from urllib.parse import quote 

class APILayer:
    def __init__(self):
        self.headers = {"apikey": os.environ.get('APILAYER_API_KEY')}

    def parse(self, filepath):
        s3_client = AmazonS3()
        print('uploading file')
        url = s3_client.upload_file(filepath)
        print('fileuploaded')
        url = quote(url, safe='')
        url = f"https://api.apilayer.com/resume_parser/url?url={url}"
        print(url)
        payload = {}
        headers= {
        "apikey": os.environ.get('APILAYER_API_KEY')
        }
        response = requests.request("GET", url, headers=headers, data = payload)

        if response.status_code == 200:
            result = response.json()
            return result
        else:
            print(response)
            print(response.json())
            return {"Error:": response.status_code}
 
 
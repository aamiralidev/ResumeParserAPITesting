import requests

api_key = ''
api_url = 'https://api.superparser.com/parse'

headers = {
    'X-API-Key': api_key
}

class SuperParser:
    def parse(self, filepath): 

        files = {
            'file_name': (filepath.split('/')[-1], open(filepath, 'rb').read())
        }
        response = requests.post(api_url, headers=headers, data=files)
        if response.status_code == 200:
            response_data = response.json()
            return response_data
        else:
            return {'Error': response.status_code}

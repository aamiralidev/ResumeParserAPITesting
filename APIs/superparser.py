import requests
import os

api_url = 'https://api.superparser.com/parse'
headers = {
    'X-API-Key': os.environ.get('SUPER_PARSER_API_KEY')
}

class SuperParser:
    def parse(self, filepath): 

        files = {
            'file_name': open(filepath, 'rb').read()
        }
        response = requests.post(api_url, headers=headers, data=files)
        if response.status_code == 200:
            response_data = response.json()
            return response_data
        else:
            print(response)
            print(response.json())
            return {'Error': response.status_code}

import requests
import os
import base64


class Hirize:
    def parse(self, filepath): 
        
        api_url = f'https://connect.hirize.hr/api/public/parser'
        
        with open(filepath, 'rb') as f:
            base64str = base64.b64encode(f.read()).decode('UTF-8')
            files = {
                'file_name': filepath,
                'payload': base64str
            }
            url = f'{api_url}?api_key={os.environ.get("HIRIZE_API_KEY")}'
            response = requests.post(url, data=files)
            if response.status_code == 201:
                return response.json()['data']['result']
            else:
                return {'Error': response.status_code}

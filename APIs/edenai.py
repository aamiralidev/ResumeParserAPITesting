import json
import requests
import os 

class EdenAIResumeParser:
    def parse(self, filepath):
        headers = {'Authorization': f'Bearer {os.environ.get("EDEN_AI_RESUME_PARSING_API_KEY")}'}
        
        url = "https://api.edenai.run/v2/ocr/resume_parser"
        data={'providers': "HireAbility", 'language': 'en'}
        files = {'file': open(filepath, 'rb')}
        
        response = requests.post(url, data=data, files=files, headers=headers)
        
        if response.status_code == 200:
            return response.json()['HireAbility']['extracted_data']
        else:
            return {'Error': response.status_code}
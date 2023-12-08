import base64
import requests #this module will need to be installed
import json
import os.path
import datetime
import os



class SOVREN:
    def parse(self, filepath): 
 
        with open(filepath, 'rb') as f:
            base64str = base64.b64encode(f.read()).decode('UTF-8')
            
            epochSeconds = os.path.getmtime(filepath)
            lastModifiedDate = datetime.datetime.fromtimestamp(epochSeconds).strftime("%Y-%m-%d") 

            url = "https://rest.resumeparsing.com/v10/parser/resume"
            payload = {
                'DocumentAsBase64String': base64str,
                'DocumentLastModified': lastModifiedDate
            }
 
            headers = {
            'accept': "application/json",
            'content-type': "application/json",
            'sovren-accountid': os.environ.get('SOVREN_ACCOUNT_ID'),
            'sovren-servicekey': os.environ.get('SOVREN_API_KEY'),
            }
            
            #make the request, NOTE: the payload must be serialized to a json string
            response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

            responseJson = json.loads(response.content)
            
            #grab the ResumeData
            resumeData = responseJson['Value']['ResumeData']
            
            return resumeData
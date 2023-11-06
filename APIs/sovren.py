import base64
import requests #this module will need to be installed
import json
import os.path
import datetime

SOVREN_ACCOUNT_ID = None
SOVREN_API_KEY = None



class SOVREN:
    def parse(self, filepath): 

        base64str = ''
        filePath = 'resume.docx'
 
        #open the file, encode the bytes to base64, then decode that to a UTF-8 string
        with open(filePath, 'rb') as f:
            base64str = base64.b64encode(f.read()).decode('UTF-8')
            
            epochSeconds = os.path.getmtime(filePath)
            lastModifiedDate = datetime.datetime.fromtimestamp(epochSeconds).strftime("%Y-%m-%d") 
 
            #use https://eu-rest.resumeparsing.com/v10/parser/resume if your account is in the EU data center or
            #use https://au-rest.resumeparsing.com/v10/parser/resume if your account is in the AU data center
            url = "https://rest.resumeparsing.com/v10/parser/resume"
            payload = {
            'DocumentAsBase64String': base64str,
            'DocumentLastModified': lastModifiedDate
            #other options here (see https://sovren.com/technical-specs/latest/rest-api/resume-parser/api/)
            }
 
            headers = {
            'accept': "application/json",
            'content-type': "application/json",
            'sovren-accountid': SOVREN_ACCOUNT_ID,
            'sovren-servicekey': SOVREN_API_KEY,
            }
            
            #make the request, NOTE: the payload must be serialized to a json string
            response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
            responseJson = json.loads(response.content)
            
            #grab the ResumeData
            resumeData = responseJson['Value']['ResumeData']
            
            return resumeData
            #access the ResumeData properties with simple JSON syntax:
            # print(resumeData['ContactInformation']['CandidateName']['FormattedName'])
            #for response properties and types, see https://sovren.com/technical-specs/latest/rest-api/resume-parser/api/
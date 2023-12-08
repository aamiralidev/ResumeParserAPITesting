from hrflow import Hrflow
import os 

class HrFlow:
    
    def __init__(self):
        self.client = Hrflow(api_secret=os.environ.get('HRFLOW_API_KEY'), api_user=os.environ.get('HRFLOW_API_USER_EMAIL'))

    def parse(self, filepath):

        with open(filepath, "rb") as f:
            file = f.read()

        response = self.client.profile.parsing.add_file(
                    source_key=os.environ.get('HRFLOW_SOURCE_KEY'),
                    profile_file=file,
                    sync_parsing=1, # This is to invoke real time parsing
                    tags=[{"name": "application_reference", "value": os.environ.get('HRFLOW_APPLICATION_REFERENCE')}], # Attach an application tag to the profile to be parsed
                )
        if response.status_code == 200:
            return response['data']['profile']
        else:
            return {'Error': response.status_code}
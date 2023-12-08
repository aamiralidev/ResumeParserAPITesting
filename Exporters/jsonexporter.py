import json

class JsonExporter:
    
    @staticmethod
    def export(filepath, resume):
        print(type(resume))
        with open(filepath, 'w') as f:
            json.dump(resume, f)


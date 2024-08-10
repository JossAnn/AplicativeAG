import json
import os

def destroy():
    array = []
    
    jsonsDirPath = 'jsons'
    if not os.path.exists(jsonsDirPath):
        os.makedirs(jsonsDirPath)
    jsonFilePath = os.path.join(jsonsDirPath, "GeneJson.json")
    
    with open('jsons/GeneJson.json', 'w') as file:
        json.dump(array, file, indent=4)
        json.dumps(array, indent=4)
        
destroy()
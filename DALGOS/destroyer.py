import json


def destructor():
    array = []
    with open('jsons/GeneJson.json', 'w') as file:
        json.dump(array, file, indent=4)
        json.dumps(array, indent=4)
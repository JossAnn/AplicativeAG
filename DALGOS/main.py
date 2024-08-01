import json
from params import ventanaParametral

def main():
    ventanaParametral()
    jsonParamsPath = "jsons\\params.json"
    with open(jsonParamsPath, "r") as json_file:
        params = json.load(json_file)
    """
    {
        "entering": 200,
        "tsAboard": 90,
        "tsBodega": 20,
        "tsCopoya": 20,
        "tsJobo": 20,
        "tsSAgustin": 20,
        "tsSuchiapa": 20,
        "initialPopu": 20,
        "maxiPopu": 50,
        "mutationIndiProba": 10,
        "mutationGenProba": 50,
        "generationNumber": 30
    }
    #"""
    print(params)

if __name__ == "__main__":
    main()
    

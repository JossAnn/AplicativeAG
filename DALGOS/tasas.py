import json
import random
import os


def dropsAndUps():
    jsonParamsPath = "jsons\\params.json"
    with open(jsonParamsPath, "r") as json_file:
        params = json.load(json_file)
    
    #pa que se reinicien siempre
    toAboard, toBodega, toCopoya, toJobo, toSAgustin, toSuchiapa = 0, 0, 0, 0, 0, 0
    upsAboard, upsBodega, upsCopoya, upsJobo, upsSAgustin, upsSuchiapa = 0, 0, 0, 0, 0, 0

    #carga las variables que wa ocupar para sacar pa donde se va la gente
    entering = params["entering"]
    tsAborad = params["tsAboard"]
    tsBodega = params["tsBodega"]
    tsCopoya = params["tsCopoya"]
    tsJobo = params["tsJobo"]
    tsSAgustin = params["tsSAgustin"]
    tsSuchiapa = params["tsSuchiapa"]
    
    for _ in range(entering):
        rdmGeneral = random.randint(0, 100)
        if rdmGeneral <= tsAborad:
            toAboard += 1
    
    #normalizar las tasas para las bajadas
    tsTotal = tsBodega + tsCopoya + tsJobo + tsSAgustin + tsSuchiapa
    normTsBodega = (tsBodega / tsTotal) * toAboard
    normTsCopoya = (tsCopoya / tsTotal) * toAboard
    normTsJobo = (tsJobo / tsTotal) * toAboard
    normTsSAgustin = (tsSAgustin / tsTotal) * toAboard
    normTsSuchiapa = (tsSuchiapa / tsTotal) * toAboard
    
    #pa no afectar el Abordaje inicial
    upsAboard = toAboard
    
    for _ in range(toAboard):
        rdmSel = random.randint(0, toAboard)
        #aqui se calculan los Drops
        if rdmSel <= normTsBodega:
            toBodega += 1
        elif rdmSel <= normTsBodega + normTsCopoya:
            toCopoya += 1
        elif rdmSel <= normTsBodega + normTsCopoya + normTsJobo:
            toJobo += 1
        elif rdmSel <= normTsBodega + normTsCopoya + normTsJobo + normTsSAgustin:
            toSAgustin += 1
        elif rdmSel <= normTsBodega + normTsCopoya + normTsJobo + normTsSAgustin + normTsSuchiapa:
            toSuchiapa += 1
            
    #print(toAboard)
    #print(toBodega, toCopoya, toJobo, toSAgustin, toSuchiapa)
    #summ = normTsBodega + normTsCopoya + normTsJobo + normTsSAgustin + normTsSuchiapa
    
    #aqui se calculan los Ups
    upsAboard -= toBodega
    upsBodega = int((tsBodega / 100) * upsAboard)
    upsAboard -= toCopoya
    upsCopoya = int((tsCopoya / 100) * upsAboard)
    upsAboard -= toJobo
    upsJobo = int((tsJobo / 100) * upsAboard)
    upsAboard -= toSAgustin
    upsSAgustin = int((tsSAgustin / 100) * upsAboard)
    upsAboard -= toSuchiapa
    upsSuchiapa = int((tsSuchiapa / 100) * upsAboard)
    #NOTA: No se si tendre problemas con todas las autoasignaciones de upsAboard
    
    dropsandups = {
        #los que suben
        "toAboard": toAboard,
        
        # Drops (los que bajan)
        "toBodega": toBodega,
        "toCopoya": toCopoya,
        "toJobo": toJobo,
        "toSAgustin": toSAgustin,
        "toSuchiapa": toSuchiapa,
        
        # Ups (los que suben)
        "upsBodega": upsBodega,
        "upsCopoya": upsCopoya,
        "upsJobo": upsJobo,
        "upsSAgustin": upsSAgustin,
        "upsSuchiapa": upsSuchiapa,
        }
    
    os.makedirs('jsons', exist_ok=True)
    with open('jsons/dropsandups.json', 'w') as json_file:
        json.dump(dropsandups, json_file, indent=4)
    json.dumps(dropsandups, indent=4)
    
    return dropsandups
import json
import random
import os


def dropsAndUps():
    dropZ, upsZ = 0, 0
    upsA, upsG, upsL, upsP, upsS      = 0, 0, 0, 0, 0
    dropB, dropC, dropD, dropE, dropF = 0, 0, 0, 0, 0
    dropH, dropI, dropJ, dropK, dropM = 0, 0, 0, 0, 0
    dropN, dropO, dropQ, dropR, dropT = 0, 0, 0, 0, 0
    
    jsonParamsPath = "jsons\\params.json"
    with open(jsonParamsPath, "r") as json_file:
        params = json.load(json_file)
    
    #carga las variables que wa ocupar para sacar pa donde se va la gente
    entering = params["entering"]
    tsAborad = params["tsAboard"]
    tsBodega = params["tsBodega"]
    tsCopoya = params["tsCopoya"]
    tsJobo   = params["tsJobo"]
    tsSAgustin = params["tsSAgustin"]
    tsSuchiapa = params["tsSuchiapa"]
    
    for _ in range(entering):
        rdmGeneral = random.randint(0, 100)
        if rdmGeneral <= tsAborad:
            upsA += 1
    
    #normalizar las tasas para las bajadas
    tsTotal = tsBodega + tsCopoya + tsJobo + tsSAgustin + tsSuchiapa
    normTsBodega    = (tsBodega   / tsTotal) * upsA
    normTsCopoya    = (tsCopoya   / tsTotal) * upsA
    normTsJobo      = (tsJobo     / tsTotal) * upsA
    normTsSAgustin  = (tsSAgustin / tsTotal) * upsA
    normTsSuchiapa  = (tsSuchiapa / tsTotal) * upsA
    #Normalizacion de las subidas de cada parada en funcion de las bajadas (un truquito)
    normUpsBodega   = int((tsBodega   / tsTotal) * normTsBodega)
    normUpsCopoya   = int((tsCopoya   / tsTotal) * normTsCopoya)
    normUpsJobo     = int((tsJobo     / tsTotal) * normTsJobo)
    normUpsSAgustin = int((tsSAgustin / tsTotal) * normTsSAgustin)
    normUpsSuchiapa = int((tsSuchiapa / tsTotal) * normTsSuchiapa)
    #Rangos para ahorrar lineas
    rangoBodega     = normUpsBodega
    rangoCopoya     = rangoBodega   + normUpsCopoya
    rangoJobo       = rangoCopoya   + normUpsJobo
    rangoSAgustin   = rangoJobo     + normUpsSAgustin
    rangoSuchiapa   = rangoSAgustin + normUpsSuchiapa
    #Rangos de tuxtla
    rangoNBodega    = normTsBodega
    rangoNCopoya    = rangoNBodega   + normTsCopoya
    rangoNJobo      = rangoNCopoya   + normTsJobo
    rangoNSAgustin  = rangoNJobo     + normTsSAgustin
    rangoNSuchiapa  = rangoNSAgustin + normTsSuchiapa
    
    ############################################################################################################################
    # TUXTLA
    upsARemains = upsA
    for _ in range(upsA):
        rdmSel = random.randint(0, upsA)
        if rdmSel <= rangoNBodega:
            dropB += 1
        elif rdmSel <= rangoNCopoya:
            dropC += 1
        elif rdmSel <= rangoNJobo:
            dropD += 1
        elif rdmSel <= rangoNSAgustin:
            dropE += 1
        elif rdmSel <= rangoNSuchiapa:
            dropF += 1
    tuxtla = [upsA, dropZ, dropB, dropC, dropD, dropE, dropF]
    
    ############################################################################################################################
    # BODEGA AURRERA
    upsARemains -= dropB
    upsG = int((tsBodega / 100) * upsARemains)
    for _ in range(upsG):
        rdmBod = random.randint(0, upsG)
        if rdmBod <= rangoBodega:
            dropH += 1
        elif rdmBod <= rangoCopoya:
            dropI += 1
        elif rdmBod <= rangoJobo:
            dropJ += 1
        else:
            dropK += 1
    bodegaAurrera = [upsG, dropZ, dropZ, dropH, dropI, dropJ, dropK]
    
    ############################################################################################################################
    # COPOYA
    upsARemains -= dropC
    upsL = int((tsCopoya / 100) * upsARemains)
    for _ in range(upsL):
        rdmCop = random.randint(0, upsL)
        if rdmCop <= rangoCopoya/2:
            dropM += 1
        elif rdmCop <= rangoJobo/1.5:
            dropN += 1
        else:
            dropO += 1
    copoya = [upsL, dropZ, dropZ, dropZ, dropM, dropN, dropO]
    
    ############################################################################################################################
    # EL JOBO
    upsARemains -= dropD
    upsP = int((tsJobo / 100) * upsARemains)
    for _ in range(upsP):
        rdmJob = random.randint(0, upsP)
        if rdmJob <= rangoJobo/3:
            dropQ += 1
        else:
            dropR += 1
    jobo = [upsP, dropZ, dropZ, dropZ, dropZ, dropQ, dropR]
    
    ############################################################################################################################
    # SAN AGUSTIN
    upsARemains -= dropE
    upsS = int((tsSAgustin / 100) * upsARemains)
    for _ in range(upsS):
        rdmSAg = random.randint(0, upsS)
        if rdmSAg <= rangoSAgustin:
            dropT += 1
    sAgustin = [upsS, dropZ, dropZ, dropZ, dropZ, dropZ, dropT]
    
    ############################################################################################################################
    # SUCHIAPA
    suchiapa = [upsZ, dropZ, dropZ, dropZ, dropZ, dropZ, dropZ]
    
    allUps = upsA + upsG + upsL + upsP + upsS + upsZ
    dropCH = dropC + dropH
    dropDIM = dropD + dropI + dropM
    dropEJNQ = dropE + dropJ + dropN + dropQ
    dropFKORT = dropF + dropK + dropO + dropR + dropT
    allDrops = dropZ + dropB + dropCH + dropDIM + dropEJNQ + dropFKORT
    totalUps = [upsA, upsG, upsL, upsP, upsS, upsZ, allUps]
    totalDrops = [dropZ, dropB, dropCH, dropDIM, dropEJNQ, dropFKORT, allDrops]

    dropsandups = {
        "tuxtla": tuxtla,
        "bodega": bodegaAurrera,
        "copoya": copoya,
        "jobo": jobo,
        "sAgustin": sAgustin,
        "suchiapa": suchiapa,
        "ups": totalUps,
        "drops": totalDrops,
    }
    
    os.makedirs('jsons', exist_ok=True)
    with open('jsons/dropsandups.json', 'w') as json_file:
        json.dump(dropsandups, json_file, indent=4)
    json.dumps(dropsandups, indent=4)
    
    return dropsandups

import json
import random

def dalgos():
    with open('jsons/dropsandups.json', 'r') as file:
        data = json.load(file)
        
    #varA, varB, varC, varD = 0, 0, 0, 0
        
    ups = data["ups"]
    drops = data["drops"]
    
    #calcular picos de pasajeros
    tuxtlaLimitRange = (ups[0] - drops[0])#Habria un problema si drops es mayor a cero
    #limites de generacion de numeros aleatoreos
    #Entre 6 paradas para reducir el rango de valores que se pueden generar
    tuxLR = int(tuxtlaLimitRange / 6)
    
    with open('jsons/params.json', 'r') as file:
        dota = json.load(file)
    initialPopu = dota["initialPopu"]
    
    #Generacion de individuos generacion inicial
    individual, population = [], []
    
    for _ in range(initialPopu):
        
        varA = random.randint(0, tuxLR)
        varB = random.randint(0, tuxLR)
        varC = random.randint(0, tuxLR)
        varD = random.randint(0, tuxLR)
        #colets = varA + varB + varC + varD
        #sits = varA*16 + varB*17 + varC*18 + varD*19
        individual = [varA, varB, varC, varD]
        population.append(individual)
    
    
    #print(tuxtlaLimitRange, bodegaLimitRange, copoyaLimitRange, joboLimitRange, sAgustLimitRange, suchLimitRange)
    #print(tuxLR)
    #print(cNumbers, sits, tuxtlaLimitRange)
    #print(population)
    return population


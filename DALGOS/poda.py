import json

def poda(population):
    jsonParamsPath = "jsons\\params.json"
    with open(jsonParamsPath, "r") as jsonfile:
        params = json.load(jsonfile)
    maxiPopu = params["maxiPopu"]  #(es el numero maximo permitido)

    cutPopulation = []

    for individual in population:
        varA, varB, varC, varD = individual
        if (varA >=0 and varB >= 0 and varC >=0 and varD >= 0):#No podemos tener colectivos negativos
            cutPopulation.append(individual)
        if len(cutPopulation) >= maxiPopu:#Detener la seleccion cuando se llega a la poblacion maxima
            break

    return cutPopulation

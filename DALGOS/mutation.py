import random
import json

def mutation(population):
    mutedPopulation = []
    jsonParamsPath = "jsons/params.json"
    with open(jsonParamsPath, "r") as json_file:
        params = json.load(json_file)
    
    indi = params["mutationIndiProba"]  # probabilidad que tiene cada individuo de mutar (0-100)
    gen = params["mutationGenProba"]    # probabilidad de mutar que tiene cada gen del individuo (0-100)
    
    for individual in population:
        if random.randint(1, 100) <= indi:#El individuo muta?
            proxiMuted = individual[:]
            for i in range(len(proxiMuted)):
                if random.randint(1, 100) <= gen: #este gen muta?
                    mutaMasMenos = random.choice([-1, 1])#Puede mutar pa arriba o pa abajo 1, pero no cero
                    proxiMuted[i] += mutaMasMenos
            mutedPopulation.append(proxiMuted)
        else:
            mutedPopulation.append(individual)# cuando no muta se mantiene igual
    
    return mutedPopulation

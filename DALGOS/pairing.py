import random
import json

def pairAndCross(population):
    with open('jsons/params.json', 'r') as file:
        data = json.load(file)
    umbralCruza = data["umbralCruza"]
    
    crossedPopulation = population[:]  # Incluye los padres en la nueva población

    for i in range(len(population)):
        for j in range(i + 1, len(population)):
            if random.random() <= umbralCruza:# es como el umbral Pc del primer algoritmo genetico
                indiParent1 = population[i]
                indiParent2 = population[j]
                
                countPuntosCruza = random.randint(1, len(indiParent1) - 1) #cantidad de puntos de cruza
                puntosCruza = sorted(random.sample(range(1, len(indiParent1)), countPuntosCruza))
                
                #hijos 
                indiSon1, indiSon2 = indiParent1[:], indiParent2[:]
                
                # segmentar los padres para ruzarlos
                for index, point in enumerate(puntosCruza):
                    if index % 2 == 0:#solo si el index es par se hace el cruce para que no queden iguales al padre
                        indiSon1[point:], indiSon2[point:] = indiSon2[point:], indiSon1[point:]
                
                # Agregar hijos a la población cruzada
                crossedPopulation.append(indiSon1)
                crossedPopulation.append(indiSon2)
    return crossedPopulation

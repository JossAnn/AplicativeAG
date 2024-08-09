import json
import os

def fitness(population):
    with open('jsons/dropsandups.json', 'r') as file:
        data = json.load(file)
    ups = data["ups"]
    results, pop = [], []
    
    for individual in population:
        varA, varB, varC, varD = individual
        sits = varA * 16 + varB * 17 + varC * 18 + varD * 19
        
        difference = abs(sits - ups[0])  # diferencia absoluta
        results.append((individual, sits, difference))
    
    # Ordenar los individuos considerando el criterio personalizado
    results.sort(key=lambda x: (x[1] < ups[0], x[2]))

    for result in results:
        individual, sits, difference = result
        pop.append(individual)  # población ordenada de mejor a peor en función del fitness
    
    # Guardar los valores rescatados de cada generación en un JSON
    jsonsDirPath = 'jsons'
    if not os.path.exists(jsonsDirPath):
        os.makedirs(jsonsDirPath)
    jsonFilePath = os.path.join(jsonsDirPath, "GeneJson.json")

    # Leer contenido existente del archivo
    if os.path.exists(jsonFilePath):
        with open(jsonFilePath, 'r') as jsonFile:
            try:
                data = json.load(jsonFile)
                if not isinstance(data, list):
                    data = [data]
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    # Agregar nuevos datos a la lista existente
    data.append(pop[0])

    # Guardar la lista actualizada en el archivo JSON
    with open(jsonFilePath, 'w') as jsonFileIs:
        json.dump(data, jsonFileIs, indent=4)
        
    return pop

"""
def fitness(population):
    with open('jsons/dropsandups.json', 'r') as file:
        data = json.load(file)
    ups = data["ups"]
    results, pop = [], []
    
    for individual in population:
        varA, varB, varC, varD = individual
        sits = varA * 16 + varB * 17 + varC * 18 + varD * 19
        
        difference = abs(sits - ups[0])#diferencia absoluta
        results.append((individual, sits, difference))
    
    # Pa ordenar los individuos 
    results.sort(key=lambda x: x[2])
    #doblar = lambda x: x * 2
    #print(doblar(3))  # Imprime 6

    for result in results:
        individual, sits, difference = result 
        pop.append(individual)#poblacion ordenada de mejor a peor en funcion del fitness
    
    
    
    
    
    
    # Guardar los valores rescatados de cada generación en un JSON
    jsonsDirPath = 'jsons'
    if not os.path.exists(jsonsDirPath):
        os.makedirs(jsonsDirPath)
    jsonFilePath = os.path.join(jsonsDirPath, "GeneJson.json")

    # Leer contenido existente del archivo
    if os.path.exists(jsonFilePath):
        with open(jsonFilePath, 'r') as jsonFile:
            try:
                data = json.load(jsonFile)
                if not isinstance(data, list):
                    data = [data]
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    # Agregar nuevos datos a la lista existente
    data.append(pop[0])

    # Guardar la lista actualizada en el archivo JSON
    with open(jsonFilePath, 'w') as jsonFileIs:
        json.dump(data, jsonFileIs, indent=4)
        
        
        
    return pop
"""
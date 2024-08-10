import json
import os
import matplotlib.pyplot as plt
import pandas as pd


pathResults = "RESULTS"

def table():
    with open('jsons/dropsandups.json', 'r') as file:
        data = json.load(file)
        
    #Asi pq no se puede generar en automatico con las posiciones que ocupo
    df_correct = pd.DataFrame([
        [data["ups"][0], data["drops"][0], data["tuxtla"][1], data["tuxtla"][2], data["tuxtla"][3], data["tuxtla"][4], data["tuxtla"][5], data["tuxtla"][6]],
        [data["ups"][1], data["drops"][1], data["bodega"][1], data["bodega"][2], data["bodega"][3], data["bodega"][4], data["bodega"][5], data["bodega"][6]],
        [data["ups"][2], data["drops"][2], data["copoya"][1], data["copoya"][2], data["copoya"][3], data["copoya"][4], data["copoya"][5], data["copoya"][6]],
        [data["ups"][3], data["drops"][3], data["jobo"][1], data["jobo"][2], data["jobo"][3], data["jobo"][4], data["jobo"][5], data["jobo"][6]],
        [data["ups"][4], data["drops"][4], data["sAgustin"][1], data["sAgustin"][2], data["sAgustin"][3], data["sAgustin"][4], data["sAgustin"][5], data["sAgustin"][6]],
        [data["ups"][5], data["drops"][5], data["suchiapa"][1], data["suchiapa"][2], data["suchiapa"][3], data["suchiapa"][4], data["suchiapa"][5], data["suchiapa"][6]],
        [data["ups"][6], data["drops"][6], '', '', '', '', '', '']
    ], columns=["Suben", "Bajan", "Tuxtla", "Bodega", "Copoya", "Jobo", "San Agustin", "Suchiapa"],
        index=["Tuxtla", "Bodega", "Copoya", "Jobo", "San Agustin", "Suchiapa", "Total"])

    # Graficar la tabla
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.axis('off')

    renderTable = ax.table(cellText=df_correct.values, 
                            colLabels=df_correct.columns, 
                            rowLabels=df_correct.index, 
                            cellLoc='center', 
                            loc='center')

    renderTable.auto_set_font_size(False)
    renderTable.set_fontsize(12)
    renderTable.scale(1.0, 2.0)

    for (i, j), cell in renderTable.get_celld().items():
        cell.set_edgecolor('black')
        cell.set_linewidth(1.5)

    plt.title("Datos de Subidas y Bajadas", fontsize=16)
    pathRes = os.path.join(pathResults, 'TablaDistribucion.png')
    plt.savefig(pathRes)
    plt.close()


def evoGraphic():
    with open('jsons/GeneJson.json', 'r') as file:
        data = json.load(file)
    sums = [sum(arr) for arr in data]

    # Renderizar grafica
    plt.figure(figsize=(10, 6))
    plt.plot(sums, marker='o', linestyle='-')
    plt.xlabel('Generaciones')
    plt.ylabel('Colectivos usados')
    plt.grid(True)
    plt.title("Evolucion del error", fontsize=16)
    pathRes = os.path.join(pathResults, 'EvoError.png')
    plt.savefig(pathRes)
    plt.close()
    
    
def finalTable():
    def fitness(population, ups):
        results, pop = [], []
        for individual in population:
            varA, varB, varC, varD = individual
            sits = varA * 16 + varB * 17 + varC * 18 + varD * 19
            difference = abs(sits - ups[0])
            results.append((individual, sits, difference))
        results.sort(key=lambda x: (x[1] < ups[0], x[2]))
        for result in results:
            individual, sits, difference = result 
            pop.append(individual)
        return results
    with open('jsons/GeneJson.json', 'r') as file:
        population = json.load(file)
    with open('jsons/dropsandups.json', 'r') as file:
        data = json.load(file)
    ups = data["ups"]

    #Esta funcion fitness es ligeramente diferente la del algoritmo en si
    #pero tiene su razon de ser ya que en este caso se envian a los individuos
    #acoplados a sus asientos y a su diferencia por eso no se usa la otra
    #que forma parte del algoritmo
    results = fitness(population, ups)
    bestIndi, bestSits, bestDifference = results[0]
    neededColets = sum(bestIndi)

    renderTable = pd.DataFrame({
        "Colectivos\nde 16": [bestIndi[0]],
        "Colectivos\nde 17": [bestIndi[1]],
        "Colectivos\nde 18": [bestIndi[2]],
        "Colectivos\nde 19": [bestIndi[3]],
        "Asientos\nCubiertos": [bestSits],
        "Asientos\nNecesitados": [ups[0]],
        "Asientos\nSobrantes": [bestDifference],
        "Colectivos\nUsados": [neededColets]
    })

    fig, ax = plt.subplots(figsize=(10, 4))  

    ax.axis('off')
    ax.axis('tight')

    # Renderizar Tabla
    table = ax.table(cellText=renderTable.values, colLabels=renderTable.columns, cellLoc='center', loc='center')

    table.auto_set_font_size(False)
    table.set_fontsize(12) 
    for key, cell in table.get_celld().items():
        cell.set_height(0.2)
        cell.set_width(0.15)

    plt.title("Tabla mejor Individuo", fontsize=16)
    pathRes = os.path.join(pathResults, 'MejorIndividuo.png')
    plt.savefig(pathRes)
    plt.close()

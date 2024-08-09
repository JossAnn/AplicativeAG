import json
import matplotlib.pyplot as plt
import pandas as pd

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

    table_correct = ax.table(cellText=df_correct.values, 
                            colLabels=df_correct.columns, 
                            rowLabels=df_correct.index, 
                            cellLoc='center', 
                            loc='center')

    table_correct.auto_set_font_size(False)
    table_correct.set_fontsize(12)
    table_correct.scale(1.0, 2.0)

    for (i, j), cell in table_correct.get_celld().items():
        cell.set_edgecolor('black')
        cell.set_linewidth(1.5)

    plt.title("Datos de Subidas y Bajadas", fontsize=16)
    plt.show()


def evoGraphic():
    with open('jsons/GeneJson.json', 'r') as file:
        data = json.load(file)

    # Calcular la suma de los valores de cada arreglo
    sums = [sum(arr) for arr in data]

    # Crear la gráfica
    plt.figure(figsize=(10, 6))
    plt.plot(sums, marker='o', linestyle='-')
    plt.title('Suma de valores de cada arreglo')
    plt.xlabel('Índice del arreglo')
    plt.ylabel('Suma de valores')
    plt.grid(True)
    plt.show()
    
    
def finalTable():
    def fitness(population, ups):
        results, pop = [], []
        
        for individual in population:
            varA, varB, varC, varD = individual
            sits = varA * 16 + varB * 17 + varC * 18 + varD * 19
            
            difference = abs(sits - ups[0])  # Diferencia absoluta
            results.append((individual, sits, difference))
        
        # Ordenar los individuos con el criterio personalizado
        #results.sort(key=lambda x: (x[1] < ups[0], x[2]))#este sirve para descartar a los que son menores al requerido
        results.sort(key=lambda x: x[2])

        for result in results:
            individual, sits, difference = result 
            pop.append(individual)
        
        return results

    # Cargar los datos del archivo GeneJson.json
    with open('jsons/GeneJson.json', 'r') as file:
        population = json.load(file)

    # Cargar los datos del archivo dropsandups.json
    with open('jsons/dropsandups.json', 'r') as file:
        data = json.load(file)
    ups = data["ups"]

    # Aplicar la función fitness
    results = fitness(population, ups)

    # Obtener el mejor individuo
    best_individual, best_sits, best_difference = results[0]

    # Calcular la suma de todas las posiciones del arreglo del mejor individuo
    colectivos_necesarios = sum(best_individual)

    # Crear un DataFrame para el mejor individuo
    table_data = pd.DataFrame({
        "VarA": [best_individual[0]],
        "VarB": [best_individual[1]],
        "VarC": [best_individual[2]],
        "VarD": [best_individual[3]],
        "Sits": [best_sits],
        "Difference": [best_difference],
        "Colectivos Necesarios": [colectivos_necesarios]
    })

    # Visualizar la tabla usando matplotlib
    fig, ax = plt.subplots(figsize=(10, 2))  # Tamaño de la figura ajustado

    # Ocultar los ejes
    ax.axis('off')
    ax.axis('tight')

    # Crear la tabla
    ax.table(cellText=table_data.values, colLabels=table_data.columns, cellLoc='center', loc='center')

    # Mostrar la tabla
    plt.title('Mejor Individuo')
    plt.show()
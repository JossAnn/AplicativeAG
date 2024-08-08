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

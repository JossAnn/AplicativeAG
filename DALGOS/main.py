from params import ventanaParametral
from tasas import dropsAndUps
from dalgos import dalgos
from graphics import table, evoGraphic, finalTable
from evaluation import fitness
from pairing import pairAndCross
from mutation import mutation
from poda import poda
from destroyer import destroy
import json
import os
from tqdm import tqdm

def main():
    ventanaParametral()
    """ 
    Ejemplo de parametros que se reciben
    {
        "entering": 200,            gente que llego a terminal
        "tsAboard": 80,             tasa de abordamiento en la terminal
        "tsBodega": 20,             tasa de gente que baja en bodega
        "tsCopoya": 20,             tasa de gente que baja en copoya
        "tsJobo": 20,               tasa de gente que baja en el jobo
        "tsSAgustin": 20,           tasa de gente que baja en el san agustin
        "tsSuchiapa": 20,           tasa de gente que baja en suchiapa
        "initialPopu": 20,          poblacion inicial
        "maxiPopu": 50,             poblacion maxima
        "mutationIndiProba": 10,    probabilidad de mutacion del individuo
        "mutationGenProba": 50,     probabilidad de mutacion del gen del individuo que muta
        "generationNumber": 30      numero de generaciones
    }
    Hay datos que se envian y que no se les da a conocer al usuario, sirven para la evolucion.
    #"""
    
    jsonParamsPath = "jsons\\params.json"
    with open(jsonParamsPath, "r") as json_file:
        params = json.load(json_file)
    generationNumber = params["generationNumber"]
    
    dropsAndUps()
    """ 
    Ejemplo de DropsAndUps que se recibe
    {
        "tuxtla":   [180251,    0,      36296,  35987,  35923,  36094,  35951 ],
        "bodega":   [28791,     0,      0,      7121,   7121,   7243,   7306  ],
        "copoya":   [21593,     0,      0,      0,      7191,   7273,   7129  ],
        "jobo":     [14409,     0,      0,      0,      0,      7183,   7226  ],
        "sAgustin": [7190,      0,      0,      0,      0,      0,      7190  ],
        "suchiapa": [0,         0,      0,      0,      0,      0,      0     ],
        "ups":      [180251,    28791,  21593,  14409,  7190,   0,      252234],
        "drops":    [0,         36296,  43108,  50235,  57793,  64802,  252234]
    }
    
    Notese que las posiciones 0 de tuxtla a suchiapa contienen totales.
    Estos no seran impresos en la tabla a execpcion de los de tuxtla, ya que seran
    usados de otra manera
    #"""

    population = dalgos()
    fitness(population)#despues de esto inicia el ciclo
    """ 
    Ejemplo de lo que devuelve dalgos:
    [
        [21, 8, 10, 16], [8, 15, 18, 17], [15, 12, 13, 14], [26, 14, 27, 23], 
        [23, 9, 22, 13], [6, 28, 8, 7],   [14, 22, 12, 21], [7, 13, 9, 18], 
        [24, 6, 26, 1],  [15, 23, 23, 4], [30, 1, 14, 3],   [29, 21, 17, 7], 
        [4, 14, 15, 0],  [16, 11, 1, 14], [22, 14, 16, 28], [12, 13, 1, 15], 
        [7, 21, 20, 5],  [12, 8, 22, 4],  [27, 23, 12, 3],  [25, 18, 21, 10],
    ]Aqui estan desordenados
    Ejemplo de lo que devuelve fitness:
    [
        [14, 13, 5, 1],  [1, 15, 22, 0],   [22, 14, 4, 1],   [17, 16, 1, 8], 
        [0, 16, 17, 9],  [3, 25, 14, 3],   [15, 26, 0, 7],   [18, 20, 8, 4], 
        [6, 12, 9, 21],  [14, 16, 7, 16],  [3, 14, 18, 19],  [16, 23, 21, 2], 
        [24, 11, 5, 25], [27, 26, 18, 0],  [25, 20, 12, 13], [15, 27, 4, 24], 
        [4, 23, 16, 26], [12, 20, 20, 27], [14, 13, 30, 29], [24, 17, 26, 30]
    ]Aqui estan ordenados en funcion del mejor al peor fitness
    """
    
    
    
    
    i=1
    with tqdm(total=generationNumber, desc="Progreso de generaciones") as pbar:
        while i <= generationNumber:
            population = population
            population = poda(fitness(mutation(pairAndCross(population))))
            
            pbar.update(1)
            i += 1
    
    pathResults = "RESULTS"
    if not os.path.exists(pathResults):
        os.makedirs(pathResults)

    
    table()
    """
    Forma para graficar la tabla:
    |      Suben      |Bajan |Tuxtla   |Bodega   |Copoya   |Jobo     |San Agustin|Suchiapa |
    |-----------+-----+------+---------+---------+---------+---------+-----------+---------|
    |Tuxtla     | ups0|drops0|tuxtla1  |tuxtla2  |tuxtla3  |tuxtla4  |tuxtla5    |tuxtla6  |
    |Bodega     | ups1|drops1|bodega1  |bodega2  |bodega3  |bodega4  |bodega5    |bodega6  |
    |Copoya     | ups2|drops2|copoya1  |copoya2  |copoya3  |copoya4  |copoya5    |copoya6  |
    |Jobo       | ups3|drops3|jobo1    |jobo2    |jobo3    |jobo4    |jobo5      |jobo6    |
    |San Agustin| ups4|drops4|sAgustin1|sAgustin2|sAgustin3|sAgustin4|sAgustin5  |sAgustin6|
    |Suchiapa   | ups5|drops5|suchiapa1|suchiapa2|suchiapa3|suchiapa4|suchiapa5  |suchiapa6|
    |Total      | ups6|drops6|  vacio  |  vacio  |  vacio  |  vacio  |   vacio   |  vacio  |
    
    NOTA: Tecnicamente, los que bajan pueden ser las sumas de todas las celdas 1,2,3,4,5,6 de cada
          una de las columnas, pero era mejor poner las sumas en un solo arreglo, ahora llamado "drops".
    """
    
    evoGraphic()
    finalTable()
    
    destroy()
    
if __name__ == "__main__":
    main()
    

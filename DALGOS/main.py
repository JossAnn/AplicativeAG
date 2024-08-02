import json
import random
from params import ventanaParametral
from tasas import dropsAndUps

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
    #"""
    print(dropsAndUps())
    """ 
    Ejemplo de DropsAndUps que se recibe
    {
        "toAboard": 177,            gente que abordo en la terminal
        "toBodega": 41,             gente que baja en bodega
        "toCopoya": 34,             gente que baja en suchiapa
        "toJobo": 30,               gente que baja en el jobo
        "toSAgustin": 40,           gente que baja en el san agustin
        "toSuchiapa": 32,           gente que baja en suchiapa
        "upsBodega": 27,            gente que sube en bodega
        "upsCopoya": 20,            gente que sube en copoya
        "upsJobo": 14,              gente que sube en el jobo
        "upsSAgustin": 6,           gente que sube en el san agustin
        "upsSuchiapa": 0            gente que sube en suchiapa (siempre debe ser cero, 
                                    si veo que todo va bien lo quitare, estoy probando)
    }
    #"""

if __name__ == "__main__":
    main()
    

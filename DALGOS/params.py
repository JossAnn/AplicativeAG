import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json

def submit(paramsWindow, entries):
    try:
        params = {
            "entering": int(entries['entering'].get()),
            "tsAboard": int(entries['tsAboard'].get()),
            "tsTuxtla": int(entries['tsTuxtla'].get()),
            "tsBodega": int(entries['tsBodega'].get()),
            "tsCopoya": int(entries['tsCopoya'].get()),
            "tsJobo":   int(entries['tsJobo'].get()),
            "tsSAgustin": int(entries['tsSAgustin'].get()),
            "tsSuchiapa": int(entries['tsSuchiapa'].get()),
            
            #Variables del AG (ocultas para el usuario)
            "initialPopu": int(entries['initialPopu'].get()),
            "umbralCruza": float(entries['umbralCruza'].get()),
            "maxiPopu": int(entries['maxiPopu'].get()),
            "mutationIndiProba": int(entries['mutationIndiProba'].get()),
            "mutationGenProba": int(entries['mutationGenProba'].get()),
            "generationNumber": int(entries['generationNumber'].get()),
        }
        
        # Validar los datos
        if params["entering"] <= 0:
            raise ValueError("El numero de personas que llegan a la terminal debe ser mayor a cero")
        if params["tsAboard"] <= 0:
            raise ValueError("La tasa de personas que abordaran debe ser mayor a cero")
        if params["tsBodega"] <= 0:
            raise ValueError("La tasa de personas que bajan en Bodega Aurrera debe ser mayor a cero")
        if params["tsCopoya"] <= 0:
            raise ValueError("La tasa de personas que bajan en Copoya debe ser mayor a cero")
        if params["tsJobo"] <= 0:
            raise ValueError("La tasa de personas que bajan en El Jobo debe ser mayor a cero")
        if params["tsSAgustin"] <= 0:
            raise ValueError("La tasa de personas que bajan en San Agustin debe ser mayor a cero")
        if params["tsSuchiapa"] <= 0:
            raise ValueError("La tasa de personas que bajan en Suchiapa debe ser mayor a cero")
        
        total_ts = params["tsBodega"] + params["tsCopoya"] + params["tsJobo"] + params["tsSAgustin"] + params["tsSuchiapa"]
        if total_ts > 100:
            raise ValueError("Se excede la tasa total de todas las personas que bajan en cada parada")
        if total_ts < 100:
            raise ValueError("No se alcanza la tasa total de todas las personas que bajan en cada parada")
    
        # guardar el JSON
        os.makedirs('jsons', exist_ok=True)
        with open('jsons/params.json', 'w') as file:
            json.dump(params, file, indent=4)
        json.dumps(params, indent=4)
        paramsWindow.destroy()
        
        
    except ValueError as e:
        messagebox.showerror("Error de validación", str(e))

def ventanaParametral():
    squaredParams = tk.Tk()
    squaredParams.title("Parametrizacion")
    
    entries = {}
    
    # TERMINAL
    tk.Label(squaredParams, text="Personas que llegan a la terminal").grid(row=0, column=0)
    entries['entering'] = tk.Entry(squaredParams)
    entries['entering'].grid(row=0, column=1)
    # ABORDAMIENTO
    tk.Label(squaredParams, text="Tasa de personas que abordaran").grid(row=1, column=0)
    entries['tsAboard'] = tk.Entry(squaredParams)
    entries['tsAboard'].grid(row=1, column=1)
    # BODEGA
    tk.Label(squaredParams, text="Tasa de movimiento en Bodega").grid(row=2, column=0)
    entries['tsBodega'] = tk.Entry(squaredParams)
    entries['tsBodega'].grid(row=2, column=1)
    # COPOYA
    tk.Label(squaredParams, text="Tasa de movimiento en Copoya").grid(row=4, column=0)
    entries['tsCopoya'] = tk.Entry(squaredParams)
    entries['tsCopoya'].grid(row=4, column=1)
    # EL JOBO
    tk.Label(squaredParams, text="Tasa de movimiento en El Jobo").grid(row=5, column=0)
    entries['tsJobo'] = tk.Entry(squaredParams)
    entries['tsJobo'].grid(row=5, column=1)
    # sAN AGUSTIN
    tk.Label(squaredParams, text="Tasa de movimiento en San Agustin").grid(row=6, column=0)
    entries['tsSAgustin'] = tk.Entry(squaredParams)
    entries['tsSAgustin'].grid(row=6, column=1)
    # SUCHIAPA
    tk.Label(squaredParams, text="Tasa de movimiento en Suchiapa").grid(row=7, column=0)
    entries['tsSuchiapa'] = tk.Entry(squaredParams)
    entries['tsSuchiapa'].grid(row=7, column=1)
    #ENTRADAS OCULTAS
    entries['tsTuxtla'] = tk.Entry(squaredParams)
    entries['initialPopu'] = tk.Entry(squaredParams)
    entries['umbralCruza'] = tk.Entry(squaredParams)
    entries['maxiPopu'] = tk.Entry(squaredParams)
    entries['mutationIndiProba'] = tk.Entry(squaredParams)
    entries['mutationGenProba'] = tk.Entry(squaredParams)
    entries['generationNumber'] = tk.Entry(squaredParams)
    
    # Valores predeterminados para la wea de las combis
    entries['entering'].insert(0, "200")
    entries['tsAboard'].insert(0, "90")
    entries['tsBodega'].insert(0, "20")
    entries['tsCopoya'].insert(0, "20")
    entries['tsJobo'].insert(0, "20")
    entries['tsSAgustin'].insert(0, "20")
    entries['tsSuchiapa'].insert(0, "20")
    #NOTA!!! entre tsTuxtla, tsBodega, tsCopoya, tsJobo, tsSAgustin, tsSuchiapa deben sumar 100
    
    #valores predeterminados de entradas ocultas
    entries['tsTuxtla'].insert(0, "0")
    entries['initialPopu'].insert(0, "1000")
    entries['umbralCruza'].insert(0, "0.5")
    entries['maxiPopu'].insert(0, "1000")
    entries['mutationIndiProba'].insert(0, "50")
    entries['mutationGenProba'].insert(0, "50")
    entries['generationNumber'].insert(0, "100")
    
    sendBtn = tk.Button(squaredParams, text="Submit", command=lambda: submit(squaredParams, entries))
    sendBtn.grid(row=9, column=0, columnspan=2)
    
    squaredParams.mainloop()


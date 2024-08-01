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
            "tsBodega": int(entries['tsBodega'].get()),
            "tsCopoya": int(entries['tsCopoya'].get()),
            "tsJobo":   int(entries['tsJobo'].get()),
            "tsSAgustin": int(entries['tsSAgustin'].get()),
            "tsSuchiapa": int(entries['tsSuchiapa'].get()),
            
            
            "initialPopu": 20,
            "maxiPopu": 50,
            "mutationIndiProba": 10,
            "mutationGenProba": 50,
            "generationNumber": 30,
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
        with open('jsons/params.json', 'w') as json_file:
            json.dump(params, json_file, indent=4)
        json.dumps(params, indent=4)
        paramsWindow.destroy()
        
        
    except ValueError as e:
        messagebox.showerror("Error de validación", str(e))

def ventanaParametral():
    squaredParams = tk.Tk()
    squaredParams.title("Parametrizacion")
    
    entries = {}
    
    # A     float
    tk.Label(squaredParams, text="Personas que llegan a la terminal").grid(row=0, column=0)
    entries['entering'] = tk.Entry(squaredParams)
    entries['entering'].grid(row=0, column=1)
    # B     float
    tk.Label(squaredParams, text="Tasa de personas que abordaran").grid(row=1, column=0)
    entries['tsAboard'] = tk.Entry(squaredParams)
    entries['tsAboard'].grid(row=1, column=1)
    # tsBodega        float
    tk.Label(squaredParams, text="Tasa de gente que baja en Bodega").grid(row=2, column=0)
    entries['tsBodega'] = tk.Entry(squaredParams)
    entries['tsBodega'].grid(row=2, column=1)
    # Poblacion inicial     int
    tk.Label(squaredParams, text="Tasa de gente que baja en Copoya").grid(row=4, column=0)
    entries['tsCopoya'] = tk.Entry(squaredParams)
    entries['tsCopoya'].grid(row=4, column=1)
    # Poblacion maxima      int
    tk.Label(squaredParams, text="Tasa de gente que baja en El Jobo").grid(row=5, column=0)
    entries['tsJobo'] = tk.Entry(squaredParams)
    entries['tsJobo'].grid(row=5, column=1)
    # Probabilidad de mutacion DEL INDIVIDUO        float
    tk.Label(squaredParams, text="Tasa de gente que baja en San Agustin").grid(row=6, column=0)
    entries['tsSAgustin'] = tk.Entry(squaredParams)
    entries['tsSAgustin'].grid(row=6, column=1)
    # Probabilidad de mutaciOn DEL GEN (cada bit de la cadena de bits del individuo)        float
    tk.Label(squaredParams, text="Tasa de gente que baja en Suchiapa").grid(row=7, column=0)
    entries['tsSuchiapa'] = tk.Entry(squaredParams)
    entries['tsSuchiapa'].grid(row=7, column=1)
    
    # Valores predeterminados para la wea de las combis
    entries['entering'].insert(0, "200")
    entries['tsAboard'].insert(0, "90")
    entries['tsBodega'].insert(0, "20")
    entries['tsCopoya'].insert(0, "20")
    entries['tsJobo'].insert(0, "20")
    entries['tsSAgustin'].insert(0, "20")
    entries['tsSuchiapa'].insert(0, "20")
    
    
    submit_button = tk.Button(squaredParams, text="Submit", command=lambda: submit(squaredParams, entries))
    submit_button.grid(row=9, column=0, columnspan=2)
    
    squaredParams.mainloop()


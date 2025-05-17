"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    import csv
    from pathlib import Path

    ruta = Path(__file__).parent.parent / 'files' / 'input' / 'data.csv'

    suma = 0
    with open(ruta, newline='', encoding='utf-8') as csvfile:
        lector = csv.reader(csvfile)
        for fila in lector:
            a = fila[0].split()
            suma += int(a[1])
            
        return suma 

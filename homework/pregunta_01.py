"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    import csv
    suma = 0
    with open(r'C:\Users\tomas\semestre2025-1\fundamentosAnalitica\LAB-01-python-basico-tvargasl\files\input\data.csv', newline='', encoding='utf-8') as csvfile:
        lector = csv.reader(csvfile)
        for fila in lector:
            a = fila[0].split()
            suma += int(a[1])

    return suma
    

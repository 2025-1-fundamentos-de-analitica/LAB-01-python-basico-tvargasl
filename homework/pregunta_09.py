"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    import csv
    with open(r'C:\Users\tomas\semestre2025-1\fundamentosAnalitica\LAB-01-python-basico-tvargasl\files\input\data.csv', newline='', encoding='utf-8') as csvfile:
        lector = csv.reader(csvfile)
        diccionario = {"aaa":0, "bbb":0, "ccc":0, "ddd":0, "eee":0,
                       "fff":0, "ggg":0, "hhh":0, "iii":0, "jjj":0, }
        for fila in lector:
            for i in range(1, len(fila)):
                if len(fila[i]) > 6:
                    codigo = fila[i].split()[1]
                    partes = codigo.split(":")
                    cadena = partes[0]
                    diccionario[cadena] += 1
                elif len(fila[i]) >= 5:
                    partes = fila[i].split(":")
                    cadena = partes[0]
                    diccionario[cadena] += 1

        return(diccionario)

print(pregunta_09())    
"""
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

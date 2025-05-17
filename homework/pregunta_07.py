"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    import csv
    with open('C:/Users/tomas/semestre2025-1/fundamentosAnalitica/LAB-01-python-basico-tvargasl/files/input/data.csv', newline='', encoding='utf-8') as csvfile:
        lector = csv.reader(csvfile)
        diccionario = {"0":[], "1":[], "2":[], "3":[], "4":[], "5":[], "6":[], "7":[], "8":[], "9":[], }
        for fila in lector:
            a = fila[0].split()
            letra = a[0]
            numero = a[1]
            diccionario[numero].append(letra)

        return([(0, diccionario["0"]),
                (1, diccionario["1"]),
                (2, diccionario["2"]),
                (3, diccionario["3"]),
                (4, diccionario["4"]),
                (5, diccionario["5"]),
                (6, diccionario["6"]),
                (7, diccionario["7"]),
                (8, diccionario["8"]),
                (9, diccionario["9"])])



"""
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """

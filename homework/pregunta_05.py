"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    import csv
    with open('C:/Users/tomas/semestre2025-1/fundamentosAnalitica/LAB-01-python-basico-tvargasl/files/input/data.csv', newline='', encoding='utf-8') as csvfile:
        lector = csv.reader(csvfile)
        diccionario = {"A":[0, 100000], "B":[0, 100000], "C":[0, 100000], "D":[0, 100000], "E":[0, 100000]}
        for fila in lector:
            a = fila[0].split()
            letra = a[0]
            numero = int(a[1])
            if numero > diccionario[letra][0]:
                diccionario[letra][0] = numero
            if numero < diccionario[letra][1]:
                diccionario[letra][1] = numero

        return([('A', diccionario["A"][0], diccionario["A"][1]),
                ('B', diccionario["B"][0], diccionario["B"][1]),
                ('C', diccionario["C"][0], diccionario["C"][1]),
                ('D', diccionario["D"][0], diccionario["D"][1]),
                ('E', diccionario["E"][0], diccionario["E"][1])])
"""
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

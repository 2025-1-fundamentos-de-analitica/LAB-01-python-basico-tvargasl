"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    import csv
    with open('C:/Users/tomas/semestre2025-1/fundamentosAnalitica/LAB-01-python-basico-tvargasl/files/input/data.csv', newline='', encoding='utf-8') as csvfile:
        lector = csv.reader(csvfile)
        lista = []
        for fila in lector:
            a = fila[0].split()
            letra = a[0]
            contador1 = 1
            contador2 = 0
            for i in range(1, len(fila)):
                if len(fila[i]) != 5 and len(fila[i]) !=6:
                    if len(fila[i]) == 1:
                        contador1+= 1
                    else:
                        contador1 +=1
                        contador2 +=1
                else:
                    contador2+=1
            lista.append((letra, contador1, contador2))

        return lista
    



"""
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """

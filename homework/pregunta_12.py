"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    import csv
    with open('C:/Users/tomas/semestre2025-1/fundamentosAnalitica/LAB-01-python-basico-tvargasl/files/input/data.csv', newline='', encoding='utf-8') as csvfile:
        lector = csv.reader(csvfile)
        diccionario = {"A":0, "B":0, "C":0, "D":0, "E":0}
        for fila in lector:
            a = fila[0].split()
            letra = a[0]
            for i in range(1, len(fila)):
                if len(fila[i]) > 6:
                    codigo = fila[i].split()[1]
                    partes = codigo.split(":")
                    numero = int(partes[1])
                    diccionario[letra] += numero
                elif len(fila[i]) >= 5:
                    partes = fila[i].split(":")
                    numero = int(partes[1])
                    diccionario[letra] += numero

        return(diccionario)


"""
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

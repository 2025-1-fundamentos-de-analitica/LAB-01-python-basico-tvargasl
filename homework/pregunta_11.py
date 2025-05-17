"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    import csv
    from pathlib import Path
    ruta = Path(__file__).parent.parent / 'files' / 'input' / 'data.csv'
    with open(ruta, newline='', encoding='utf-8') as csvfile:
        lector = csv.reader(csvfile)
        diccionario = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0}
        for fila in lector:
            a = fila[0].split()
            numero = int(a[1])
            primera = a[3]
            diccionario[primera] += numero
            for i in range(1, len(fila)):
                if len(fila[i]) == 1:
                    diccionario[fila[i]] += numero
                else:
                    letra = fila[i].split()[0]
                    diccionario[letra] += numero
                    break


        return(diccionario)


"""
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """

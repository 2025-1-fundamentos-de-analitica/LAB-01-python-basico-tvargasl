"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    import csv
    from pathlib import Path
    ruta = Path(__file__).parent.parent / 'files' / 'input' / 'data.csv'
    with open(ruta, newline='', encoding='utf-8') as csvfile:
        lector = csv.reader(csvfile)
        diccionario = {"0":[], "1":[], "2":[], "3":[], "4":[], "5":[], "6":[], "7":[], "8":[], "9":[], }
        for fila in lector:
            a = fila[0].split()
            letra = a[0]
            numero = a[1]
            if letra not in diccionario[numero]:
                diccionario[numero].append(letra)

        return([(0, sorted(diccionario["0"])),
                (1, sorted(diccionario["1"])),
                (2, sorted(diccionario["2"])),
                (3, sorted(diccionario["3"])),
                (4, sorted(diccionario["4"])),
                (5, sorted(diccionario["5"])),
                (6, sorted(diccionario["6"])),
                (7, sorted(diccionario["7"])),
                (8, sorted(diccionario["8"])),
                (9, sorted(diccionario["9"]))])

"""
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """

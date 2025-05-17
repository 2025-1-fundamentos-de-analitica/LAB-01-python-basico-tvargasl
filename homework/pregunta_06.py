"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    def evaluar(diccionario, cadena):
        partes = cadena.split(":")
        codigo = partes[0]
        numero = int(partes[1])

        if numero < diccionario[codigo][1]:
            diccionario[codigo][1] = numero
        if numero > diccionario[codigo][0]:
            diccionario[codigo][0] = numero
        
    
    import csv
    with open(r'C:\Users\tomas\semestre2025-1\fundamentosAnalitica\LAB-01-python-basico-tvargasl\files\input\data.csv', newline='', encoding='utf-8') as csvfile:
        lector = csv.reader(csvfile)
        diccionario = {"aaa":[0, 100000], "bbb":[0, 100000], "ccc":[0, 100000], "ddd":[0, 100000], "eee":[0, 100000],
                       "fff":[0, 100000], "ggg":[0, 100000], "hhh":[0, 100000], "iii":[0, 100000], "jjj":[0, 100000], }
        for fila in lector:
            for i in range(1, len(fila)):
                if len(fila[i]) > 6:
                    codigo = fila[i].split()[1]
                    evaluar(diccionario, codigo)
                elif len(fila[i]) >= 5:
                    evaluar(diccionario, fila[i])

        return([('aaa', diccionario["aaa"][1], diccionario["aaa"][0]),
                ('bbb', diccionario["bbb"][1], diccionario["bbb"][0]),
                ('ccc', diccionario["ccc"][1], diccionario["ccc"][0]),
                ('ddd', diccionario["ddd"][1], diccionario["ddd"][0]),
                ('eee', diccionario["eee"][1], diccionario["eee"][0]),
                ('fff', diccionario["fff"][1], diccionario["fff"][0]),
                ('ggg', diccionario["ggg"][1], diccionario["ggg"][0]),
                ('hhh', diccionario["hhh"][1], diccionario["hhh"][0]),
                ('iii', diccionario["iii"][1], diccionario["iii"][0]),
                ('jjj', diccionario["jjj"][1], diccionario["jjj"][0])])
"""
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

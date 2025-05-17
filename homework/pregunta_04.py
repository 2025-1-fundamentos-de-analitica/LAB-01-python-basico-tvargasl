"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    import csv
    from pathlib import Path
    ruta = Path(__file__).parent.parent / 'files' / 'input' / 'data.csv'
    with open(ruta, newline='', encoding='utf-8') as csvfile:
        lector = csv.reader(csvfile)
        diccionario = {"01":0, "02":0, "03":0, "04":0, "05":0 , "06":0, "07":0, "08":0, "09":0, "10":0, "11":0, "12":0, }
        for fila in lector:
            a = fila[0].split()
            fecha = a[2]
            mes = fecha.split("-")[1]
            diccionario[mes] = diccionario[mes] + 1
    
    return [('01', diccionario["01"]), ('02', diccionario["02"]), ('03', diccionario["03"]), ('04', diccionario["04"]), 
                   ('05', diccionario["05"]), ('06', diccionario["06"]), ('07', diccionario["07"]), ('08', diccionario["08"]), 
                   ('09', diccionario["09"]), ('10', diccionario["10"]), ('11', diccionario["11"]), ('12', diccionario["12"])]

"""
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """

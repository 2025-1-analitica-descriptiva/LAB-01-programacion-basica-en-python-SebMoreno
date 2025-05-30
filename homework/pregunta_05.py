"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open('files/input/data.csv', 'r') as file:
        data = {}
        for line in file:
            line = line.split("\t")
            letter = line[0]
            value = int(line[1])
            data.setdefault(letter, [0, float('inf')])
            data[letter][0] = max(value, data[letter][0])
            data[letter][1] = min(value, data[letter][1])
        return sorted((k, ma, mi) for k, (ma, mi) in data.items())

import os
import csv
from typing import ChainMap, final
from pprint import pprint

ruta_completa = '/home/alan/Desktop/programacion/curso_21_22/csv/'

# def leer_csv_normal():
#     with open(ruta_completa + 'archivos.csv') as csv_in:
#         filas = csv_in.readlines()
#         for f in filas:
#             print((f[:-1]).split(','))


#leer_csv_normal()

def leer_con_csv():
    campos = []
    filas = []

    csv_in = open(ruta_completa + 'archivos.csv')
    lector = csv.reader(csv_in)
    campos = next(lector)
    #print(campos)

    for f in lector:
        filas.append(f)
    
    csv_in.close()
    return(campos,filas)

# c,f = leer_con_csv()
# pprint(c)
# pprint(f)

def leer_with():
    filas = []
    campos = []
    with open(ruta_completa + 'archivos.csv') as csv_in:
        lector = csv.reader(csv_in)
        campos = next(lector)
        for f in lector:
            filas.append(f)

    return campos, filas


# c,f = leer_with()
# pprint(c)
# pprint(f)

def leer_dict():
    csv_in = open(ruta_completa + 'archivos.csv')
    lector_dict = csv.DictReader(csv_in)

    list_dict = list(lector_dict)

    csv_in.close
    return list_dict

pprint(leer_dict())


import os
import csv
from pprint import pprint

os.system('clear')

ruta = '/home/alan/Desktop/programacion/curso_21_22/csv/'


# 1- Leer el archivo (como diccionario)
def leer_archivo():
    csv_in = open(ruta + 'titanic.csv') 
    lector_dic = csv.DictReader(csv_in)
    lista_dict = list(lector_dic)
    csv_in.close()
    return lista_dict
    
# 2- Contar (0=muerto, 1=vivo)
def leer_contar_valores():
    survivors = 0
    deads = 0
    for person in leer_archivo():
        if person['Survived'] == '1':
            survivors += 1
        else:
            deads += 1
    return(f'survivors: {survivors}', f'and deads: {deads}')

# 3- Devolver resultado

pprint(leer_contar_valores())
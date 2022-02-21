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

# 2- leer archivos y guardar 20-30 años sobrevividos
def leer_guardar():
    datos_dicii = []
    for person in leer_archivo():
        datos = {}
        if '20' >= person['Age'] <= '30':
            datos['Name'] = person['Name'] #+ str('name')
            datos['Sex'] = person['Sex']
            datos['Pclass'] = person['Pclass']
            datos_dicii.append(datos)
    return datos_dicii

# 3- crear csv y pasar datos
def crea_pasa():    
    with open(ruta + 'datos_pasados.csv', 'w') as salida:
        escritor = csv.writer(salida)
        escritor.writerow(leer_guardar()[0].keys())
        for select in leer_guardar():
            escritor.writerow(select.values())

pprint(leer_guardar())
crea_pasa()
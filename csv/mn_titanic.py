import os
import csv
os.system('clear')

ruta = '/home/alan/Desktop/programacion/curso_21_22/csv/'

# 1- Leer el archivo (como diccionario)
def leer_archivo():
    csv_in = open(ruta + 'titanic.csv') 
    lector_dic = csv.DictReader(csv_in)
    lista_dict = list(lector_dic)
    csv_in.close()
    return lista_dict

# 2- Determinar hombre
def survivior_male_sex():
    male_l = 0
    male_d = 0
    for person in leer_archivo():
        if person['Survived'] == '1' and person['Sex'] == 'male':
            male_l += 1
        if person['Survived'] == '0' and person['Sex'] == 'male':            
            male_d += 1
    return(f'Male survivors: {male_l}', f'and deads: {male_d}')

# 3 - Determinar Mujeres
def survivior_female_sex():
    female_l = 0
    female_d = 0
    for person in leer_archivo():
        if person['Survived'] == '1' and person['Sex'] == 'female':
            female_l += 1
        if person['Survived'] == '0' and person['Sex'] == 'female':
            female_d += 1
    return(f'Female survivors: {female_l}', f'and deads: {female_d}')

print(survivior_female_sex(),survivior_male_sex())
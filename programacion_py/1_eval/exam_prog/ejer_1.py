# Ejercicio 1 de Alan Sweere Segovia
"""
1.	Escriba una función que devuelva una lista con todas aquellas palabras que no contienen la letra 'e', a partir del archivo 'palabras.txt' que puede obtenerse de aquí https://acortar.link/5qNeNj

"""
ruta_entrada = '/home/alan/Documentos/GitHub/curso_21_22/programacion_py/1_eval/exam_prog/palabras.txt.TXT'

def devuelve_lista():
    # leer el archivo
    with open(ruta_entrada) as txt_in:
        lista = txt_in.readlines()
        
        lista_sin_e = [] # Aquí acumulamos de palabraas sin 'e'

        for palabra in lista:
            if not 'e' in palabra: # Obviamos elementos con 'e'
                lista_sin_e.append(palabra) # Los añadimos a la lista sin 'e'
        return lista_sin_e # Devolvemos resultado

        # for l in lista:
        #     if l.find('e'):
        #           lista_con_e.append(l)

import pprint

pprint.pprint(devuelve_lista())

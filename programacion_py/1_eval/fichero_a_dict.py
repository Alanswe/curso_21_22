import os
from pprint import pprint
os.system('clear')

ruta = '/home/alan/Desktop/programacion/curso_21_22/viernes/programacion/python/nombres_dir.txt'
dic_salida = {}
clave = 0

#Leer archivo
with open(ruta) as archivo:
    for l in archivo:
        #Procesar fil a fila
        fila = l[:-1:].split(',')
        #Recorrer lista y rellenar dict
        for nombre in fila:
            dic_salida[clave] = nombre
            clave += 1

#pprint(dic_salida)


def modo2():
    clave = 0
    texto = open(ruta,'r').readlines()
    for archivo in texto:
        dic_salida[clave] = archivo[:-1:]
        clave += 1
    
    return dic_salida


pprint(modo2())
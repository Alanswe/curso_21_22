import os
from settings import RUTA_BASE,CODIGO,MI_CARPETA

#                                1 buscar la carpeta y categorizar .py
list_carpeta = []
archivo_salida = 'listdir.txt'
RUTA_SALIDA = RUTA_BASE + CODIGO + MI_CARPETA
miebros = 5
fila = ''

carpeta = 'RUTA_BASE + CODIGO'
carpeta = os.scandir()                               #Escanea la carpeta y muestra los archivos 
for f in carpeta:
        if f.name.endswith('.py'):
                list_carpeta.append(f.name[:-3:])    #-3 para no mostrar los .py ultimos

#                                2 sacar nombres de carpeta de 5 en 5 en una lista
for x in range(0, len(list_carpeta),miebros):
        temp = list_carpeta[x: x + miebros]
        fila += ','.join(temp) + '\n'

#                                 3 crear y escribir
nuevo = open(RUTA_SALIDA + '/nombres_dir.txt', 'w') #con W se borra el contenido del archivo antes de escribir
nuevo.write(fila[:-1:])
nuevo.close()

#                                'extra' version con lineas de una en una (sustituye el punto 2 y 3)
#nuevo = open(RUTA_SALIDA + '/nombres_dir.txt', 'w')
# for x in range(0, len(list_carpeta),miebros):
#         temp = list_carpeta[x: x + miebros]
#         fila = ','.join(temp) + '\n'
#nuevo.write(fila)
#nuevo.close()
#                                   Open es la funcion que abre los archivos
#                                   Tiene que ser de la misma carpeta y con el vscode solo esa carpeta abierta sin ningun padre
from pprint import pprint
archivo = 'listas.py'
listas = open(archivo) #            Listas sería el manejador del archivo
#                                   Por defecto es lectura escritura
#                                   la siguiente sería donde guardamos el 
# lineas = listas.readlines()
# pprint(lineas)
# for l in lineas:
#     pprint(l)

#listas.close()

for linea in listas:
    pprint(linea)
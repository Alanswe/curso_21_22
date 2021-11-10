import os
from settings import RUTA_BASE,CODIGO,MI_CARPETA

def bucar():
        list_carpeta = []
        carpeta = 'RUTA_BASE + CODIGO'
        carpeta = os.scandir()
        for f in carpeta:
                if f.name.endswith('.py'):
                        list_carpeta.append(f.name[:-3:])
        return list_carpeta

def agrupar(list_carpeta, miembros):
        fila = ''
        for x in range(0, len(list_carpeta),miembros):
                temp = list_carpeta[x: x + miembros]
                fila += ','.join(temp) + '\n'
        return fila[:-1:]

def escribir(cadena,list_carpeta):
        RUTA_SALIDA = RUTA_BASE + CODIGO + MI_CARPETA
        nuevo = open(RUTA_SALIDA + '/nombres_dir.txt', 'w')
        nuevo.write(cadena)
        nuevo.close()

x = bucar()
i = agrupar(x,5)

# def agrupa_escribe():
#         nuevo = open(RUTA_SALIDA + '/nombres_dir.txt', 'w')
#         for x in range(0, len(list_carpeta),miebros):
#                 temp = list_carpeta[x: x + miebros]
#                 fila = ','.join(temp) + '\n'
#         nuevo.write(fila)
#         nuevo.close()
# Programa que pida al ususario los sigueintes datos:
# - Nombre
# - Apellido
# - Fecha de naciemiento
# - Teléfono
# Los datos se guardan en un diccionario

# def Introduce():
#     import pprint
#     dicci = {}
    
#     for x in range(100):
#         input('Nota: Para salir del bucle introduzca (exit) Introduzca ENTER para comenzar: ')
#         nombre = input('Introduzca su nombre: ')
#         if nombre == str('exit'):
#             pprint.pprint(dicci)
#             break
#         else:
#             dicci['Nombre'] = nombre

#         apellido = input('Introduzca sus apellidos: ')
#         if apellido == str('exit'):
#             pprint.pprint(dicci)
#             break
#         else:
#             dicci['Apellido'] = apellido

#         f_nacimiento = input('Introduzca su fecha de naciemeitno, (xx/xx/xx): ')
#         if f_nacimiento == str('exit'):
#             pprint.pprint(dicci)
#             break
#         else:
#             dicci['Fecha_nacimiento'] = f_nacimiento

#         telf = input('Introduzca su Teléfono: ')
#         if telf == str('exit'):
#             pprint.pprint(dicci)
#             break
#         else:
#             dicci['Teléfono'] = telf

#         if input('¿Quiere ver el diccionario, y o n?:  ') == str('y'):
#             pprint.pprint(dicci)
#             print('Ususario registrado con éxito')
#         else:
#             print('Ususario registrado con éxito')

# Introduce()



#crear lista de datos que meta en diccionario
from pprint import pprint
import os
import csv

def pedir_personas():
    seguir = True
    lista_personas = []
    while seguir:
        nombre = input('Introduzca su nombre: ')
        apellido = input('Introduzca sus apellidos: ')
        f_nacimiento = input('Introduzca su fecha de naciemeitno, (xx/xx/xx): ')
        telf = input('Introduzca su Teléfono: ')
        dicci = {'Nombre': nombre, 'Apellido': apellido, 'Fecha_nacimiento': f_nacimiento, 'Teléfono': telf}
        
        lista_personas.append(dicci)

        respuesta = input('¿Desea conotinuar? s/n: ')
        if respuesta.upper() == 'N':
            seguir = False
        os.system('clear')
    return lista_personas

pprint(pedir_personas())

def guardar_csv(contenido,destino):       
    with open(destino, 'w',newline= '') as f: 
        escritor = csv.DictWriter(f,fieldnames=list(contenido[0].keys()))
        escritor.writeheader()
        escritor.writerows(contenido)

cont = pedir_personas
ruta = '/home/alan/Desktop/programacion/curso_21_22/ejercicio_1.csv'

guardar_csv(cont,ruta)
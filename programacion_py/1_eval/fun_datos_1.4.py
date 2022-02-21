# Hacer una función que le pida al usuario datos: DNI, nombre,...etc.
# Tal cual se pide, realiza los imputs que se determinen en orden y recibiendo cualquier resultado.
# Podría hacer un bucle de veces por cada usuario que quiera meter

def Introduce():
    import pprint
    dicci = {}

    nombre = input('Introduzca su nombre: ')
    dicci['Nombre'] = nombre
    apellido = input('Introduzca sus apellidos: ')
    dicci['Apellido'] = apellido
    dni = input('Introduzca su DNI: ')
    dicci['Dni'] = dni
    edad = input('Introduzca su edad: ')
    dicci['Edad'] = edad
    sexo = input('Introduzca su sexo: ')
    dicci['Sexo'] = sexo
    if input('¿Quiere ver el diccionario, y o n?:  ') == str('y'):
        pprint.pprint(dicci)
        print('Ususario registrado con éxito')
    else:
        print('Ususario registrado con éxito')

Introduce()
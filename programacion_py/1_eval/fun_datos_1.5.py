# Hacer una función que le pida al usuario datos: DNI, nombre,...etc.
# Tal cual se pide, realiza los imputs que se determinen en orden y recibiendo cualquier resultado.
# Con una palabra pare el bucle
def Introduce():
    import pprint
    dicci = {}
    
    for x in range(3):
        input('Nota: Para salir del bucle introduzca (exit) Introduzca cualquier tecla para comenzar: ')
        nombre = input('Introduzca su nombre: ')
        if nombre == str('exit'):
            pprint.pprint(dicci)
            break
        else: pass
        dicci['Nombre'] = nombre
        apellido = input('Introduzca sus apellidos: ')
        if apellido == str('exit'):
            pprint.pprint(dicci)
            break
        else: pass
        dicci['Apellido'] = apellido
        dni = input('Introduzca su DNI: ')
        if dni == str('exit'):
            pprint.pprint(dicci)
            break
        else: pass
        dicci['Dni'] = dni
        edad = input('Introduzca su edad: ')
        if edad == str('exit'):
            pprint.pprint(dicci)
            break
        else: pass
        dicci['Edad'] = edad
        sexo = input('Introduzca su sexo: ')
        if sexo == str('exit'):
            pprint.pprint(dicci)
            break
        else: pass
        dicci['Sexo'] = sexo
        if input('¿Quiere ver el diccionario, y o n?:  ') == str('y'):
            pprint.pprint(dicci)
            print('Ususario registrado con éxito')
        else:
            print('Ususario registrado con éxito')

Introduce()
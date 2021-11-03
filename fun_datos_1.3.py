# Hacer una función que le pida al usuario datos: DNI, nombre,...etc.
# Tal cual se pide, realiza los imputs que se determinen en orden y recibiendo cualquier resultado.
def Introduce():
    datos = 0
    Nombre = input('Introduzca su nombre: ')
    Apellido = input('Introduzca sus apellidos: ')
    Dni = input('Introduzca su DNI: ')
    Edad = input('Introduzca su edad: ')
    Sexo = input('Introduzca su sexo: ')
    Pregun = input('¿Quiere ver el diccionario, y o n?:  ')
    import pprint
    for i in range(5):
        dicci = {}
        Nombre
        dicci['Nombre'] = Nombre
        datos += 1
        if datos == 1:
            Apellido
            dicci['Apellido'] = Apellido
            datos += 1
        if datos == 2:
            Dni
            dicci['Dni'] = Dni
            datos += 1
        if datos == 3:
            Edad
            dicci['Edad'] = Edad
            datos += 1
        if datos == 4:
            Sexo
            dicci['Sexo'] = Sexo
            datos += 1
        if datos == 5:
            if Pregun == str('y'):
                pprint.pprint(dicci)
                print('Ususario registrado con éxito')
            else:
                print('Ususario registrado con éxito')

Introduce()
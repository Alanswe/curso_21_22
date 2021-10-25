# Para crear unafunción 

# def primera(mensaje, ususario, tema):  #son obligatorios
#     return mensaje + ususario + tema

# v1 = primera('Hola', ' Mundo', ' DAM')
# print(v1)

# def segunda():
#     v1 = 'Hello'
#     v2 = 'World'

#     return v1,v2

# a1,a2 = segunda()
# print('a1: ', a1)
# print('a2: ', a2)

def tercera(uno=1):                  #funciones con argumentos opcionales, cuando le damos un valor por defecto
    return uno

print(tercera())

#print()     #La funcion print permite una cantidad ilimitada de parametros
#funcion_larga(a,b, *args, **kwargs)               #*args una lista de valores separado por comas (tupla)
funcion_larga(1,2,3,4, name= 'teo', hora='17')                  #**kwargs son paramertros con nombre (Diccionario)
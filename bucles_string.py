
# for i in range(len(cadena)):
#     print(cadena[i].upper())

# #print(cadena[9])

# print('prueba abajo')

# for x in cadena:
#     print(x.upper())

# print('solcución abajo')
cadena = 'Hola caracola'
salida = ''
inversa = ''

for x in cadena:
    #if x == ' ':
    #    break  #si x es igual a ' '(espacio), para y la haca hasta ahí incluso las siguiemntes si tienen el espacio.
    salida += x.upper()
    inversa = x.upper() + inversa
print(salida)
print(inversa)
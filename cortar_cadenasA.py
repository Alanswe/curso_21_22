cadena = 'uno, dos, tres, cuatro, cinco'
cadena2 = []

# if cadena.find(','):
#     cadena[:3]
#     cadena2.append(cadena[:3])

# for x in range(0,3):
#     cadena2.append(cadena.find(',')(cadena[:3]))

# for x in range(len(cadena)):
#       cadena.find(',')
#       cadena[0:3]
#       cadena2.append(x)

for x in range(len(cadena)):
    if cadena.find(','):
        i = cadena[0:3]
        cadena2.append(i)
    else:
        break
print(cadena2)

# for x in range(len(cadena)):
#     if cadena.find(','):
#         i = cadena[0:3]
#         cadena2.append(i)
#     else:
#         break
# print(cadena2)


#resultado esperado ['uno', 'dos'...]
# lista = cadena.split(',')
# print(lista)

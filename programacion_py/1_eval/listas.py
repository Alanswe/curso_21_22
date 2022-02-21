#lista = [0,1,2,3,4,5,6,7,8,9]
# lista2 = ['Pepe', 'Alan', 'juan']

# nueva_lista = lista + lista2
# print(nueva_lista)

#for x in lista:
#   print(x)

# for x in range(len(lista2)):
#    print(lista2[x])

# print(lista2)

# for x in lista2:
#     if type(x) == lista:
#         print(x)
#para que imprima solo las clases str u la que se necesite sustituyendo esta

# ceros = [0] * 5
# print(ceros)
#vale para cualquier otro tipo como por ejemplo 'Hola'


#print(lista[::-1]) # [::-1] slice



# v1 = [1,2,3,4]
# v2 = [6,7,8,9]
# total = 0

# for x in range(len(v1)):
#     total += v1[x] * v2[x] #+= sumaria el 0 al resultado del primer valor (0) y así 4 veces (las veces del len)
# print(total)

origen = [0,1,2,3,4,5,'Jose', 'Alan', 'Fernando']
numeros = []
alumnos = []

for x in origen:
    if type(x) == str:
        alumnos.append(x)
    else:
        numeros.append(x)

print(origen)
print(alumnos)
print(numeros)
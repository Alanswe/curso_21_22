lista1 = [0,1,2,3,4,5,6,7,8,9]
lista2 = [0,1,2,3,4,5,6,7,8,9]
iguales = False

if len(lista1) == len(lista2):
    for x in range(len(lista1)):
        if lista1[x] == lista2[x]:
            iguales = True
        else:
            iguales = False
            break
            
            
if iguales:
    print('Estas listas son iguales')
else:
    print('Estas listas no son iguales')

#-----------------------------------------------------------------------------------------------------

lista1 = [0,1,2,3,4,5,6,7,8,9]
lista2 = [0,1,2,3,4,5,6,7,8,9]

if lista1 == lista2:
    print('Estas listas son iguales')
else:
    print('Estas listas no son iguales')

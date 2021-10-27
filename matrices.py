# pureba de 
# lista = [1,2,3,4,'A']
# lista2 = [5,6,7,8,'B']
# lista3 = [9,10,11,12,'C']
# lista4 = [13,14,15,16,'D']
         

# for i in range(20):
#     x = [lista,lista2,lista3,lista4] 
#     print(x)

import pprint
cols = 15
filas = 15
matriz = []

for i in range(filas):
    fila = []
    for j in range(cols):
        fila.append('X')
    matriz.append(fila)

pprint.pprint(matriz)
matriz1 = [[3,5,3], 
            [9,8,3],
            [4,3,6]]


matriz2 = [[3,5,3], 
            [9,8,3],
            [4,3,6]]

resultado = [[0,0,0],
            [0,0,0],
            [0,0,0]]

for i in range(len(matriz1)):
    for j in range(len(matriz2[0])):   #range(len(matriz2[o]) para la longitud de la pimera columna de matriz dos, cada pimero de linea
        for k in range(len(matriz2)):
            resultado[i][j] += matriz1[i][k] * matriz2[k][j]

from pprint import pprint
pprint(resultado)
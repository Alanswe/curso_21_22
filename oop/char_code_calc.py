"""
Dada una cadena de texto, convertir cada letra a su código ASCII.
Con esto creamos un número total_1.
Cambiar todos los números '7' por '1' y a ese número total_2
"""

"""
Mono:
1 - Se recibe un str
2 - Se pasa a ASCII con ord o chr con nombre total_1
3 - cambiar los numeros 7 a 1 con nombre total_2
4 - total 3 = total_1 - total_2
"""

def code(dato):
    total_0 = []
    total_1 = []
    total_2 = []
    for i in dato:
        for s in i.split(','):
            total_0.append(str(s))
    total_1.append(ord(total_0[0]))
    total_1.append(ord(total_0[1]))
    total_1.append(ord(total_0[2]))

    # 3
    # for e in total_1:
    #     total_2.append(e)
    
    numero_2 = ''.join(total_1).replace('7','1')
    # me falta el totoal 2
    numero_1 = ''.join(total_1)
    # 4
    return int(numero_1) - int(numero_2)

print(code('abc'))
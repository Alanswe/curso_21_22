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
    # total_1 = []
    # total_1_n1 = []
    # total_1_n2 = []
    # total_1_n3 = []
    # for i in dato:
    #     total_1_n1.pop(dato[0])
    #     total_1_n2.pop(dato[1])
    #     total_1_n3.pop(dato[2])
    total_1 = []
    for i in dato:
        for s in i.split(','):
            total_1.append(int(s))

    print(total_1_n3)

code('abc')
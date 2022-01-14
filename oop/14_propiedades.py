# Decorador para comprobar si los parámetros son enteros

def comprueba_enteros(funcion):
    #     def envoltura(a,b):
    def envoltura(*args):
        for i in args:
            if not type(i) is int:
                raise Exception('Parámetros no enteros')
        return funcion(*args)
    return envoltura

@comprueba_enteros
def suma(*args):
    return sum(args)

# Multiplicación de numeros enteros
@comprueba_enteros
def multiplicacion(a,b):
    return a*b

# con_enteros = comprueba_enteros(multiplicacion)
# print(con_enteros(3,2))

con_enteros = multiplicacion(3,2)
#sin_enteros = multiplicacion(3,'a')                # Lanzará el raise

sum_con_enteros = suma(1,2,3,4)
#sum_sin_enteros = suma(1,2,3,'b')                   # Lanzará el raise

print(con_enteros)
#print(sin_enteros)

print(sum_con_enteros)
#print(sum_sin_enteros)
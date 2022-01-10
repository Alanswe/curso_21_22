def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def calcular(operacion, a, b):
    return operacion(a,b)

print(calcular(sumar,1,4))

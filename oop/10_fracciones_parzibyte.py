# https://parzibyte.me/blog/2021/04/17/fracciones-python/
# Ejemplo de parzibyte retocado

class Fraccion():
    def __init__(self, numerador, denominador):
        self.numerador = int(numerador)
        self.denominador = int(denominador)

    def __str__(self):
        return str(self.numerador) + "/" + str(self.denominador)

    def maximo_comun_divisor(self, a, b):
        temporal = 0
        while b != 0:
            temporal = b
            b = a % b
            a = temporal
        return a

    def minimo_comun_multiplo(self, a, b):
        return (a * b) / self.maximo_comun_divisor(a, b)

    # Operaciones ---------------------------------------------------------------------

    def suma(self, otra: 'Fraccion') -> 'Fraccion':
        mcm = self.minimo_comun_multiplo(self.denominador, otra.denominador)
        diferencia_self = mcm/self.denominador
        diferencia_otra = mcm/otra.denominador
        numerador_resultado = (diferencia_self*self.numerador) + \
            (diferencia_otra*otra.numerador)
        return Fraccion(numerador_resultado, mcm)

    def resta(self, otra: 'Fraccion') -> 'Fraccion':
        mcm = self.minimo_comun_multiplo(self.denominador, otra.denominador)
        diferencia_self = mcm/self.denominador
        diferencia_otra = mcm/otra.denominador
        numerador_resultado = (diferencia_self*self.numerador) - \
            (diferencia_otra*otra.numerador)
        return Fraccion(numerador_resultado, mcm)

    def producto(self, otra: 'Fraccion') -> 'Fraccion':
        return Fraccion(self.numerador*otra.numerador, self.denominador*otra.denominador)

    def cociente(self, otra: 'Fraccion') -> 'Fraccion':
        return Fraccion(self.numerador*otra.denominador, self.denominador*otra.numerador)

# Pruebas -----------------------------------------------------------------------------

f = Fraccion(5, 6)
f2 = Fraccion(7, 24)
print(f"{f} + {f2} = {f.suma(f2)}")
print(f"{f} - {f2} = {f.resta(f2)}")
print(f"{f} * {f2} = {f.producto(f2)}")
print(f"{f} / {f2} = {f.cociente(f2)}")
"""
1 - Crear una clase Rectángulo, con atributos base y altura.
2 - Crear también el constructor de la clase 
2_1 - y los métodos necesarios para calcular el área y el perímetro.
3 - Crear las pruebas unitarias necesarias para asegurar que funciona correctamente.

"""
# 1
class Rectangulo():
    base = 0
    altura = 0
    # 2
    def __init__(self, base, altura) -> None:
       self.base = base
       self.altura = altura        

    # 2_1
    def calc_area(self,base,altura):
        return base * altura

    def calc_perimetro(self,base,altura):
        return 2*base + 2*altura

    
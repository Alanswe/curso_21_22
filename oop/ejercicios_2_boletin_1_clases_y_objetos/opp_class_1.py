"""
1 - Crear una clase Rectángulo, con atributos base y altura.
2 - Crear también el constructor de la clase 
2_1 - y los métodos necesarios para calcular el área y el perímetro.
3 - Crear las pruebas unitarias necesarias para asegurar que funciona correctamente.

"""
# 1
class Rectangulo():
    # 2
    def __init__(self, base=0, altura=0) -> None:
       self.base = base
       self.altura = altura        

    # 2_1
    def calc_area(self):
        return self.base * self.altura

    def calc_perimetro(self):
        return 2*self.base + 2*self.altura
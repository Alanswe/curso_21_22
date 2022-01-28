"""
1 - Crear una clase Coche, a través de la cual se pueda conocer el color del coche, la marca, el modelo, el número de puertas y la matrícula.

2 - Crear el constructor del coche, así como los métodos que considere necesarios.

3 - Crear las pruebas unitarias necesarias para comprobar que se pueden establecer y consultar los valores de los atributos.

"""
# 1

class Coche():
    def __init__(self,marca='',modelo='',n_puertas=0,matricula='') -> None:
        self.__marca = marca
        self.__modelo = modelo
        self.__n_puertas = n_puertas
        self.__matricula = matricula
    # 2
    # 3
    @property
    def marca(self):
        return self.__marca
    
    @property
    def modelo(self):
        return self.__modelo

    @property
    def n_puertas(self):
        return self.__n_puertas

    @property
    def matricula(self):
        return self.__matricula

    # Setters
    @marca.setter
    def set_marca(self, new_marca):
        self.__marca = new_marca
    
    @modelo.setter
    def set_modelo(self, new_modelo):
        self.__modelo = new_modelo

    @n_puertas.setter
    def set_n_puertas(self,new_n_puertas):
        self.__n_puertas = new_n_puertas

    @matricula.setter
    def set_martricula(self, new_matricula):
        self.__matricula = new_matricula
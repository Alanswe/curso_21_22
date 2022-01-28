"""
1 - Crear una clase Tiempo, con atributos hora, minuto y segundo, 
1 - 1 - que pueda ser instanciada indicando: los tresb atributos, sólo la hora y minuto, o sólo la hora.
2 - Crear además los métodos necesarios para modificar la hora en cualquier momento de forma manual.
3 - Mantenga la integridad de los datos en todo momento definiendo las variables como privadas.
4 - Crear las pruebas unitarias para asegurar el correcto funcionamiento de la clase.
"""
# 1 y 3
class Tiempo():
    def __init__(self,hora=0,minuto=0,segundo=0) -> None:
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo
    # 2
    @property
    def hora(self):
        return self.__hora
    @property
    def minuto(self):
        return self.__minuto
    @property
    def segundo(self):
        return self.__segundo
    # Setters
    @hora.setter
    def set_hora(self,new_hora):
        self.__hora = new_hora

    @minuto.setter
    def set_minuto(self,new_minuto):
        self.__minuto = new_minuto

    @segundo.setter
    def set_segundo(self,new_segundo):
        self.__segundo = new_segundo
    
    # Instancias 1 - 1 -
    @property
    def get_all(self):
        return f'{self.hora}:{self.minuto}:{self.segundo}'

    @property
    def get_hora_minuto(self):
        return self.hora,self.minuto
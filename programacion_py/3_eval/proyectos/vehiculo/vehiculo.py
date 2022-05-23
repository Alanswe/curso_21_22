
class Vehiculo():
    color = 'Blanco' # Atrubuto de clase (no de init)

    def __init__(self,nombre='',velocidad_max=0,kilometraje=0) -> None:
        self.nombre = nombre
        self.velocidad_max = velocidad_max
        self.kilometraje = kilometraje
        self.capacidad = 1

    def __str__(self) -> str:
        return f'Nombre: {self.nombre}\nV-Max: {self.velocidad_max}\nKlm: {self.kilometraje}'
    
    def cal_tarifa(self):
        return self.capacidad * 100

    def get_padre(self):
        for padre in self.__class__.__bases__:
            return padre.__name__

class Buss(Vehiculo):
    cargo_mantenimiento = 10 
    # Para poder modificarlo con facilidad en el futuro

    def set_capacidad(self, new_capacidad=50):
        self.capacidad = new_capacidad

    def __str__(self) -> str:
        return super().__str__() + f'Capacidad: {self.capacidad}\n color: {self.color}'
    
    def cal_tarifa(self):
        Buss.set_capacidad(self) # llamo a el metodo para determinar el valor de buss
        tarifa_inicial = super().cal_tarifa()
        aumento = tarifa_inicial * (self.cargo_mantenimiento / 100)
        return tarifa_inicial + aumento

# Agregado para el ejercicio 8

class Buss_escolar(Buss):
    def get_padre_del_padre(self):
        for padre in self.__class__.__bases__:
            for abuelo in padre.__bases__:
             return abuelo.__name__

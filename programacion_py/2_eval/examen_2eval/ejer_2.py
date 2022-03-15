
class Cuenta():
    titular = None

    def __init__(self, titular, numero,saldo=0) -> None:
        self.titular = titular
        self.__saldo = saldo
        if len(str(numero)) == 20:
            self.numero = numero
        else:
            raise Exception('Número no valido')
        self.interes = 0
        self.titulares = []

    def get_titular(self):
        return self.titular

    def get_saldo(self): # Solo lectura
        return self.__saldo

    def get_titulares(self):
        list_titu = []
        for p in self.titulares:
            list_titu.append(f'{p.nombre} {p.apellido1} {p.apellido2}')
        return list_titu

    # Los setters

    def set_titulares(self, titulares):
        self.titulares = titulares

    def ingresar(self, ingreso):
        if ingreso <0:
            raise Exception('Error: Valor introducido negativo')
        else:
            self.__saldo = self.__saldo + ingreso 

    def retirar(self, retiro):
        if retiro <0 or retiro > self.__saldo:
            raise Exception('Error: Valor introducido erroneo')
        else:
            self.__saldo = self.__saldo - retiro

    # str

    def __str__(self) -> str:
        return f'Titular: {self.titular}, Número de cuenta: {self.numero}, Saldo: {self.__saldo}, Interés: {self.interes}'
        
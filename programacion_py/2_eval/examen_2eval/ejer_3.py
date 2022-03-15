import ejer_2

class Cuentajoven(ejer_2.Cuenta):

    def __init__(self, titular, numero, edad, saldo=0) -> None:
        super().__init__(titular, numero, saldo)
        self.edad = edad
        self.__bonificacion = 10
        self.__saldo = saldo

    def get_bonificacion(self):
        return f'{self.__bonificacion}€'

    def esTitularValido(self):
        if self.edad > 18: 
            return False 
        else:
            return True

    def set_interes(self):
        if self.esTitularValido() == True :
            if self.__saldo > 5000:
                self.interes = 5
            else:
                self.interes = 1
        else:
            raise Exception('Oferta de interes solo valida para cuentas Joven')

    def ingresar(self, ingreso):
        if self.esTitularValido() == True :
            if ingreso >= 1000:
                return super().ingresar(ingreso+10)
            else:
                return super().ingresar(ingreso)
        else:
            raise Exception('Titular no cumple con requisutos de cuenta joven')

    def retirar(self, retiro):
        if self.esTitularValido() == True :
            mitad_s = self.get_saldo()//2
            if retiro < mitad_s:
                return super().retirar(retiro)
            else:
                raise Exception('No se puede retirar más de la mitad del saldo de una vez')
        else:
            raise Exception('Titular no cumple con requisutos de cuenta joven')

class Nif:
    dicci_letra = {0 : 'T',1 : 'R',2 : 'W',3 : 'A',4 : 'G',5 : 'M',6 : 'Y',7 : 'F',8 : 'P',9 : 'D',
        10: 'X',11: 'B',12: 'N',13: 'J',14: 'Z',15: 'S',16: 'Q',17: 'V',18: 'H',19: 'L',20: 'C',21: 'K',22: 'E'}

    def __init__(self, numero=0, letra=' ') -> None:
        self.__numero = numero
        if numero:
            self.__letra = self.__calcula_letra()
        else:
            self.__letra = ' '

    # Getters
    @property
    def numero(self):
        return self.__numero
    
    @property
    def letra(self):
        return self.__letra

    # Set
    @numero.setter
    def numero(self, numero):
        self.__numero = numero
        self.__letra = self.__calcula_letra()

    def __calcula_letra(self):
        resto = self.__numero % 23
        return self.dicci_letra[resto]

    def __str__(self) -> str:
        return f'{self.__numero}-{self.__letra}' 
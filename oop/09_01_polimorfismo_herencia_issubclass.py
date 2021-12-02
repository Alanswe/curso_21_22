class Pajaro():
    def __str__(self) -> str:
        return 'Pájaro'    
    def cantar(self):
        print('Los pájaros tienen cantos diferentes')

class Gorrion(Pajaro):
    def __str__(self) -> str:
        return 'Gorrión'
    def cantar(self, con_padre=False):
        if con_padre:
            super().cantar()
        print('Gorrión pio, pio')

class Gallo(Pajaro):
    def __str__(self) -> str:
        return 'Gallo'    
    def cantar(self,con_padre=False):
        if con_padre:
            super().cantar()
        print('Gallo kikirikíiii')

class CoroPajaros():
    def __init__(self, lista_pajaros) -> None:
        self.coro = lista_pajaros
    
    def cantar(self):
        for p in self.coro:
            if issubclass(p.__class__ ,Pajaro):
                print(f'Este es un pájaro llamado: {p}')
            else:
                print(f'¡Error! Esto NO es un pájaro: {p}')

lista_pajaros = [Gallo(),'p',1, Gorrion(), 'l']
c = CoroPajaros(lista_pajaros)
c.cantar()


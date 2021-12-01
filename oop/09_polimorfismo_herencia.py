
class Pajaro():
    def cantar(self):
        print('Los pájaros tienen cantos diferentes')

class Gorrion(Pajaro):
    def cantar(self, con_padre=False):
        if con_padre:
            super().cantar()
        print('Gorrion pio, pio...')

class Gallo(Pajaro):
    def cantar(self, con_padre=False):
        if con_padre:
            super().cantar()
        print('Gallo kikirikííí...')

# class Gallo(Pajaro):
#     def cantar(self):
#         super().cantar()
#         print('Gallo kikirikííí...')
lista_pajaros = [Gorrion(),Gallo()]

class CoroPajaros():
    def __init__(self, lista_pajaros) -> None:
        self.coro = lista_pajaros
    def cantar(self):
        # Pajaro.cantar(self)
        titulo = True
        for p in self.coro:
            p.cantar(titulo)
            titulo = False

        # for p in range(len(self.coro)):
        #     if p == 0:
        #         self.coro[p].cantar(True)
        #     else:
        #         self.coro[p].cantar()


# gorri = Gorrion()
# gorri.cantar()

# gallo = Gallo()
# gallo.cantar()



c = CoroPajaros(lista_pajaros)
c.cantar()
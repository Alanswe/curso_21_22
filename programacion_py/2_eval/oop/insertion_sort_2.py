
class Insort():

    def __init__(self, lista_des) -> None:
        self.lista_des = lista_des
        self.lista_ord = []

    def ordena(self):
            lista = list(self.lista_des)
            num_lista = range(len(lista))
            lista_ordenada = []

            for i in num_lista:
                    lista_ordenada.append(lista.pop(lista[max]))

            self.lista_ord = lista_ordenada


    def __str__(self) -> str:
        return f'Desordenada: {self.lista_des}\nOrdenada:    {self.lista_ord}'

# ------------------------------------------------                    
prueba = Insort([4,3,2,10,12,1,5,6])
print(prueba.lista_des)
print(prueba.lista_des)
prueba.__str__()


class Spain():
    def __str__(self) -> str:
        return 'Spain'

    def capital(self):
        print('La capital es Madrid')

    def idioma(self):
        print('El idioma es Castellano')

class Portugal():
    def __str__(self) -> str:
        return 'Portugal'

    def capital(self):
        print('La capital es Lisboa')

    def idioma(self):
        print('El idioma es Portugués')

class Italia():
    def __str__(self) -> str:
        return 'Italia'

    def capital(self):
        print('La capital es Roma')

    def idioma(self):
        print('El idioma es Italiano')

class Aduana():
    def pasar(self, pais, destino):
        print(f'Ahora estoy en {pais} y voy a {destino}')
        pais.capital()
        pais.idioma()
        print(f'En {destino} será:')
        destino.capital()
        destino.idioma()
        print('----------------------------')

        


esp = Spain()
por = Portugal()
ita = Italia()
paises = [esp, por, ita]

# for p in paises:
#     p.capital()
#     p.idioma()

aduana = Aduana()

aduana.pasar(esp,ita)
aduana.pasar(por,esp)
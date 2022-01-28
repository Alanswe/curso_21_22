from pprint import pprint
from random import randint, randrange
class Juego():

    def __init__(self) -> None:
        pass

    def play(self):
        puntos_jugador_1 = 0
        puntos_jugador_2 = 0
        jugador = 1
        partida = []
        meta = 100
        for tirada in range(meta):
                dado_1 = randint(1, 6)
                dado_2 = randint(1, 6)
                if puntos_jugador_1 < meta:
                        puntos_jugador_1 += dado_1
                        jugador = 1
                else:
                        jugador = 1
                        partida.append(f'¡¡El jugador {jugador} HA GANADO!!')
                        break
                if puntos_jugador_2 < meta:
                        puntos_jugador_2 += dado_2
                        jugador = 2
                else:
                        jugador = 2
                        partida.append(f'¡¡El jugador {jugador} HA GANADO!!')
                        break
                partida.append(f'Jugador: {jugador-1} Tirada: {tirada} Puntos: {puntos_jugador_1}')
                partida.append(f'Jugador: {jugador} Tirada: {tirada} Puntos: {puntos_jugador_2}')
                partida.append('--------------------')
        return partida

ejemplo = Juego()

pprint(ejemplo.play())


"""
While True:
    if puntos1 >= LIMITE_PUNTOS:
        uno gana
    randint(1,CARAS_DE_DADO)

"""
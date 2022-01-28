"""
Hacer un programa para simular un juego de tablero sencillo:
        - Habrá dos jugadores.
        - Por turnos, cada uno tira un dado y se van sumando sus puntuaciones.
        - El primero que llegue a 100 puntos gana.
El programa debe simular las tiradas de los dados e imprimir el resultado de cada tirada.
Ejemplo: Jugador: 1 Tirada: 17 Puntos: 45
Cuando gane uno de los jugadores debe imprimir: ¡¡El jugador X HA GANADO!!
"""
# -----------------
""" MONO
1 - Crear base de clase sin variables
2 - función bucle suma a cada jugador el numero de dado - Jugador: 1 Tirada: 17 Puntos: 45
3 - Cuando la suma de los jugadores llege a 100, se para y se imprime ¡¡El jugador X HA GANADO!!
4 - Return de la partida entera + el resultado final
"""
from pprint import pprint
from random import randrange
class Juego():

    def __init__(self) -> None:
        pass

    def play(self):
        puntos_jugador_1 = 0
        puntos_jugador_2 = 0
        jugador = 1
        partida = []
        for tirada in range(100):
                dado_1 = randrange(1, 6)
                dado_2 = randrange(1, 6)
                if puntos_jugador_1 < 100:
                        puntos_jugador_1 += dado_1
                        jugador = 1
                else:
                        jugador = 1
                        partida.append(f'¡¡El jugador {jugador} HA GANADO!!')
                        break
                if puntos_jugador_2 < 100:
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

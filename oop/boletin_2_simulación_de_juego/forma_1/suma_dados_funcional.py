#Programa en versión funcional (sin clases)
"""
Hacer un programa para simular un juego de tablero sencillo:
    - Habrá dos jugadores.
    - Por turnos, cada uno tira un dado y se van sumando sus puntuaciones.
    - El primero que llegue a 100 puntos gana.
El programa debe simular las tiradas de los dados e imprimir el resultado de cada tirada.
Ejemplo: Jugador: 1 Tirada: 17 Puntos: 45
Cuando gane uno de los jugadores debe imprimir: ¡¡El jugador X HA GANADO!!
"""
#-------------------------------
""" MONO
1 - Definir varibles
2 - Cada bucle suma a cada jugador el numero de dado - Jugador: 1 Tirada: 17 Puntos: 45
3 - Cuando la suma de los jugadores llege a 100, se para y se imprime ¡¡El jugador X HA GANADO!!
"""
from random import randrange
def juego():
    puntos_jugador_1 = 0
    puntos_jugador_2 = 0
    jugador = 1
    for tirada in range(100):
        dado_1 = randrange(1,6)
        dado_2 = randrange(1,6)
        if puntos_jugador_1 < 100:
            puntos_jugador_1 += dado_1
            jugador = 1
        else:
            jugador = 1
            print(f'¡¡El jugador {jugador} HA GANADO!!')
            break

        if puntos_jugador_2 < 100:
            puntos_jugador_2 += dado_2
            jugador = 2
        else:
            jugador = 2
            print(f'¡¡El jugador {jugador} HA GANADO!!')
            break
        print(f'Jugador: {jugador-1} Tirada: {tirada} Puntos: {puntos_jugador_1}\nJugador: {jugador} Tirada: {tirada} Puntos: {puntos_jugador_2}\n--------')

# Prueba de funcionamiento
juego()
"""Hacer un programa para simular un juego de tablero sencillo:
        - Habrá dos jugadores.
        - Por turnos, cada uno tira un dado y se van sumando sus puntuaciones.
        - El primero que llegue a 100 puntos gana.
       
El programa debe simular las tiradas de los dados e imprimir el resultado de cada tirada.
Ejemplo: Jugador: 1 Tirada: 17 Puntos: 45

Cuando gane uno de los jugadores debe imprimir: ¡¡El jugador X HA GANADO!!

Se debe entregar:
        - Programa en versión funcional (sin clases)
        - Programa en versión orientada a objetos (usando clases)
NOTA: ES necesario demostrar que el programa funciona, con pruebas unitarias (recomendado) o de alguna otra forma."""

from random import randrange
objetivo = randrange(100)
veces = 0

for i in range(10):
    veces +=1
    intento = int(input('Introduce un número: '))
    if objetivo > intento:
        print('Es mayor... ;)')
    elif objetivo < intento:
        print('Es menor... ;)')
    else:
        print(f'¡Acertaste! :)\nEl número de intentos fueron {i}')
        break
if veces > 9:
    print(f'¡Has perdido! :(\nEl número era {objetivo}')
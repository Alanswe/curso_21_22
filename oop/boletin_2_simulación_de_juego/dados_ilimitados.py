from random import randint

LIMITE_PUNTOS = 100
NUM_JUGADORES = 2
CARAS_DE_DADO = 6

class Jugador():
    def __init__(self) -> None:
        self._puntos = 0
        self._nombre = ''

    @property
    def puntos(self):
        return self._puntos
    
    @puntos.setter
    def puntos(self, ptos):
        self._puntos += ptos

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nom):
        self._nombre = nom

class Partida():
    def __init__(self) -> None:
        self._jugadores = []
        self._crea_lista_jugadores()

    def _crea_lista_jugadores(self):
        for j in range(NUM_JUGADORES):
            jug = Jugador()
            jug.nombre = f'Jugador_{j}'
            self._jugadores.append(jug)

    def jugar(self):
        while True:
            for jugador in self._jugadores:
                dado = randint(1,CARAS_DE_DADO)
                jugador.puntos = dado
                if jugador.puntos >= LIMITE_PUNTOS:
                    return f'Ganador: {jugador.nombre}'

p = Partida()
print(p.jugar)
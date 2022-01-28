from ast import While
from multiprocessing import set_forkserver_preload
from pickle import TRUE
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
        return self.nombre
    
    @puntos.setter
    def nombre(self, nom):
        self._nombre = nom









"""
While True:
    if puntos1 >= LIMITE_PUNTOS:
        uno gana
    randint(1,CARAS_DE_DADO)

"""
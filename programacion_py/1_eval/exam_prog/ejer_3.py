# Ejercicio 3 de Alan Sweere Segovia
"""
3.	Escriba una función que solicite al usuario una lista de personas (del ejercicio anterior). Cuando termine de introducirlas las imprimirá todas por pantalla.
"""

from ejer_2 import lista_personas
import os

os.system('clear')

def solicita_pers(): 
    num_p = len(lista_personas)
    for p in range(num_p): # Solicita una lista de personas al ejercicio 2
        print(lista_personas[p].datos()) # Las imprime todas en pantalla

solicita_pers()

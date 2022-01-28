from random import randrange

puntos_jugador_1 = 0
puntos_jugador_2 = 0
resultados = {}
for tirada in range(100):
    dado = randrange(1,6)
    if resultados.get(dado) == None:
        resultados[dado] = 1
    else:
        resultados[dado] += 1 
print(resultados)

# Siempore tenemos que probar si funbciona el rango entre 1 y 6 desde los extremos es decir 
# aquí no sacaria nun ca el 6 ya que entiende de 1 a 5, para solucionarlo seria (1,7)
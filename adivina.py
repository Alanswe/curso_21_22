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
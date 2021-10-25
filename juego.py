from adivina_finc import adivina


num_oculto = 5
for i in range(1,90,1):
    num_introducido = int(input('Escribe un número: '))
    print(num_introducido)
    if num_introducido == num_oculto:
        print(f'¡Acertaste! :) El numero de intentos fueron {i}')
        break
    elif num_introducido < num_oculto:
        print('Es mayor...')
    elif num_introducido > num_oculto:
        print('Es menor...')
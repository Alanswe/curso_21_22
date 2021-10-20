num_oculto = 5

for i in range(1,10):
    num_introducido = int(input('Di un numero: '))
    print(num_introducido)
    if num_introducido == num_oculto:
        print(f'Acertaste y el numero de intentos fueron {i}')
        break
    elif num_introducido < num_oculto:
        print('Es mayor')
        print(f'Fallaste, te quedan {i} intentos')
    elif num_introducido > num_oculto:
        print('Es menor')
        print(f'Fallaste, te quedan {i} intentos')
               
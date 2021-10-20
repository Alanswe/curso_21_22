num_oculto = 5
for i in range(1,90,1):
    num_introducido = int(input('di un numero: '))
    print(num_introducido)
    if num_introducido == num_oculto:
        print(f'Acertaste y el numero de intentos fueron {i}')
        break
    elif num_introducido < num_oculto:
        print('Es mayor')
    elif num_introducido > num_oculto:
        print('Es menor')
               

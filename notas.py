# si es <5 suspenso
# entre 5 y 8 notable
# más de 8 sobresaliente
nota = 7.5
if nota >=0 and nota <=10:
    if nota < 5:
        print('Suspenso')
    elif nota < 8:
        print('Aprobado')
    else:
        print('Sobresaliente')
else:
    print('Valor incorrecto')
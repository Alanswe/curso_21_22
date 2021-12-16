def sumar(arg):
    # total = 0
    # for val in arg:
    #     total += val
    # return total
    
    total = 0
    lista = arg.split(',')
    if arg == '': #cadena vacía
        return 0
    if arg == str: # cadena
        return 0

    for e in lista:
        if not e.isdigit():
            return 0
        
        if not isinstance(e, int) and not isinstance(e, float): # para la prueba 2(b)
            return "Error: Carácter no numérico"
        
        if not isinstance(e, complex): #para los elementos complejos
            return 0

    for val in lista:
        total += val
    return total

#-----------------------------------------------------
    # A - si no se pasan argumentos devuelve 0
def test_1():
    return sumar('')

    # B - probar que puede sumar eneros o floats
def test_2():
    return sumar('1,3')

    # C - si se pasa cadenas devuelve 0
def test_3():
    return sumar('a,c')

    # D - datos complejos devuelve 0
def test_4():
    return sumar('6j')

    # E - caracteres no nomericos devuelve cero
def test_5():
    return sumar('c')
# Son funciones que adminten fucciones como parametros y 
# devuelven funciones


def mi_decorador(funcion_a_decorar):
    def envoltorio(*args,**kwargs):
        print('-------------Empiezo a decorar')
        c = funcion_a_decorar(*args,**kwargs)
        print(c)
        print('-------------Fin de la decoración')
    return envoltorio


def dercorador_suma(funcion_que_suma):
    def identificador(*args):
        if args != list:
            crea_list = []
            crea_list.append(args)
            return funcion_que_suma(crea_list)
        else:
            return funcion_que_suma(*args)
    return identificador



def saludar():
    print('Hola mundo')

resp_saludo = mi_decorador(saludar)
#resp_saludo()

@mi_decorador
def saludar_decorado():
    print('Hola mundo con decoro')

#saludar_decorado()

# @mi_decorador
# def sumar(a,b):
#     return a + b

# sumar(3,3)

@dercorador_suma
def sumar(*args):
    return sum(args)

sumar(3,3,3,3)

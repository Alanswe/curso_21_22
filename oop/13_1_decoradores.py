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
        if type(args) != list:
            list_num = []
            for element in range(len(args)+1):
                list_num.append(element)
            list_num_new = list(list_num)
            return sum(list_num_new)
        else:
            return funcion_que_suma(args)
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


print(sumar([1,2,3,4]))

print(sumar(1,2,3,4))
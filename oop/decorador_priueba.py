def dercorador_suma(funcion_que_suma):
    def identificador(*args):
        while type(args) != list == True:
            list_num = []
            for element in range(len(args)+1):
                list_num.append(element)
            list_num_new = list(list_num)
            return sum(list_num_new)
        else:
            return funcion_que_suma(args)
    return identificador

@dercorador_suma
def sumar(*args):
    return sum(args)

print(sumar(1,2,3,4))
print(type([1,2,3,4]))
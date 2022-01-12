# def sumar(*args):
#     print(args)
#     print(type(args))
#     for i in args:
#         print(i)

def sumar(*args):
    lista_num = []
    # for i in args:
    #     if type(i) == int:
    #         for i in range(len(args)+1):
    #             lista_num.append(i)
    #         lista_num = list(lista_num)
    for i in args:
        if type(i) == str:
            for s in i.split(','):
                lista_num.append(int(s))
    return lista_num

print(sumar('1,2,3,4'))

# print(sumar(1,2,3,4))

# print(sumar([1,2,3,4]))
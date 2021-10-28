# Estos serian ejemplos para practicar con funciones
def doble(numero):
    if type(numero) in [int,float,complex]:  
        return numero * 2 
    else:
        return None



# def doble(numero):
#     if type(numero) == int:  
#         return numero * 2
#     elif type(numero) == float:
#         return numero * 2
#     elif type(numero) == complex:
#         return numero * 2  
#     else:
#         return None

print(doble(4))
print(doble(4.55475))
print(doble('sgfjeswf'))
print(doble(4+8j))

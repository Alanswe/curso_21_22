# reve1 = x.upper() + reve1
# reve = 


# def palabra(texto):
#     if len(texto) != len(texto):
#         return False
#     else:
#         for x in range(len(texto)):
#             if x == x in reve1:
#                 return True
#             else:
#                 return False

#print(palabra('tenet'))
#print(reve1)

#espx = cadena.replace(' ','')
#acenx = cadena.replace('á','a')
def limpiar(cadena):
    aux = cadena
    aux = aux.lower()
    aux = aux.replace(' ','')
    aux = aux.replace('á','a')
    aux = aux.replace('é','e')
    aux = aux.replace('í', 'i')
    aux = aux.replace('ó', 'o')

def palindromo(cadena):
    aux = limpiar(cadena)
    return aux == aux[::-1]

print(palindromo('Ana ana'))
print(palindromo('hola'))
print(palindromo('Sometamos o matemos'))
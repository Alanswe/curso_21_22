from pprint import pprint

variable = [('campo1','valor1'), 
            ('campo2','valor2'),
            ('campo3','valor3')]  #           key, value

#                                           Crea un diccionario del elemento seleccionado
dic = dict(variable)                          
#pprint(dic)
#                                           Para añadir al diccionario
# dic['key4'] = ['value4']               
# pprint(dic)

#                                           Iterar sobre diccionario

for k in dic:
    print(k,dic[k])
#     print(dic[k]) 

# for k,v in dic.items():
#     print(k,v) 
#     print(f'keys: {k} values: {v}') # f formatea y sustit (r es raw, imprime {k} y {v} también)

#-------------------                         Para obtener las keys or values
# claves = dic.keys()  
# valores = dic.values()
# pprint(claves)
# pprint(valores)


# for k in claves:
#     pprint(k)

#                                             Borrar elemento

# del(dic['key4'])
# pprint(dic)

#                                             Limpiar diccionario
# dic.clear()
# print(dic)

#                                             Extraer elementos

#elem = dic.pop('campo3')        #El Key
elem = dic.popitem()             #Es FILO (pila) quitsris el último en entrar
print(elem)
print(dic)
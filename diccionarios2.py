from pprint import pprint

variable = [('campo1','valor1'), 
            ('campo2','valor2'),
            ('campo3','valor3')]  #key, value

dic = dict(variable) #Crea un diccionario del elemento seleccionado
pprint(dic)

# for k in dic:
#     print(dic[k]) 


# for k,v in dic.items():
#     print(k,v) 

#------------------------
claves = dic.keys()
valores = dic.values()
pprint(claves)
pprint(valores)


for k in claves:
    pprint(k)
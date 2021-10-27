t = (1,2,3,4,5,6,7,8) #Las tuplas se representan con () y las listas con []
#t[2] = 0 #Nos da error al ser inmutables
# w = list(t)
# w[2] = 0 #convertir una tupla a lista y cambiarla
#print(w)
print(t)
t1 = (0,5,7)
t2 = t + t1
print(t2)
#las tuplas spon mas rapidas que las listas, al ser inmutables se pueden utilizar como indices (campo valor)
for elem in t:
    print(elem)
import random as rd
def genera_equipos(alumnos):
    personas = alumnos.copy()            #Para crear una copia de la lista original y usar después, debido al borrado
    rd.shuffle(personas)
    equipos = []
    num_equipos = len(personas) // 2
    for i in range(num_equipos):
        eq = []                          #Crea una lista de equipo para añadirla a la final
        eq.append(personas.pop)          #POP para no repetir persona, va eliminado los selecionados
        eq.append(personas.pop)
        equipos.append(eq)
    if len(personas) > 0:
        equipos[num_equipos - 1].append(personas.pop())    #Para añadirlo al equipo del final
    return equipos

alumnos = ['Pepe', 'juan', 'manolo', 'Pepe2', 'juan2', 'manolo2', 'pedro', 'tomas']
x = genera_equipos(alumnos)
print(x)

alumnos = [1,1,2,3,4,5,6,7,8]
for i in range(5):
    x = genera_equipos(alumnos)
    print(x)
    

#crea con una lista de 9 nombres, equipos de 2 personas 
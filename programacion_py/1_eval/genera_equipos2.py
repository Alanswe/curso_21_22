import random

def genera_equipos(alumnos, mienbros=2):
    random.shuffle(alumnos)
    equipos = []

    for i in range(0, len(alumnos),mienbros):
        equipos.append((alumnos[i: i + mienbros]))
    return equipos

alumnos_1 = ['Lucía', 'Fernando', 'Alan', 'Jose', 'María', 'Pepe', 'Pedro', 'Tomás']

print(genera_equipos(alumnos_1,3))

#------------------------------------------------

gente = [1,1,2,3,4,5,6,7,8]
for i in range(5): # Esto hace 5 veces equipos de 2 (2 está predefido)
    x = genera_equipos(gente) # (gente,3) crearia equipos de 3
    print(x)
    
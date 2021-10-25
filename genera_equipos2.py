import random

def genera_equipos(alumnos, mienbros=2):
    random.shuffle(alumnos)
    equipos =  []

    for x in range(0, len(alumnos),mienbros):
        equipos.append((alumnos[i: i + mienbros]))
    return equipos

gente = [1,1,2,3,4,5,6,7,8]
for i in range(5):
    x = genera_equipos(gente) # (gente,3) crearia equipos de 3
    print(x)
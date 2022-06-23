# Crea con una lista de 9 nombres, equipos de 2 personas 
import random as rd
def genera_equipos(alumnos):
    personas = alumnos.copy()            # Para crear una copia de la lista original y usar después, debido al borrado
    rd.shuffle(personas)
    equipos = []
    num_equipos = len(personas) // 2
    for i in range(num_equipos):
        eq = []                          # Crea una lista de equipo para añadirla a la final
        segundo_contador = 1
        if i == 0:
            eq.append(personas[i])          # POP para no repetir persona, va eliminado los selecionados
            eq.append(personas[i+segundo_contador])   # Se repite para hacer grupos de 2 en este caso        
        else:
            eq.append(personas[i+segundo_contador]) 
            eq.append(personas[i+segundo_contador+1]) 
        equipos.append(eq)
        segundo_contador +=1 # El contador sirve para que no se repita el último número en el bucle
    if len(personas) > 0:
        equipos[num_equipos - 1].append(personas.pop())    # Para añadirlo al equipo del final
    return equipos

alumnos = ['Pepe', 'juan', 'manolo', 'Pepe2', 'juan2', 'manolo2', 'pedro', 'tomas', 'Lucía']
x = genera_equipos(alumnos)
print(x)    

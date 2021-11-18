import csv

ruta = '/home/alan/Desktop/programacion/curso_21_22/csv/'

def csv_write():
    matriz = [
        [1,2,3,4,5,6],
        [4,5,6,8,9,9],
        [9,8,8,6,25]    
    ]
        
    with open(ruta + 'nuevo_1.csv', 'w') as csv_writer:  # 'w' seria para escrivir directamente sobrescibiendo lo anterior
        # 'a' seria para escribir sin borrar
        escritor = csv.writer(csv_writer)
        escritor.writerow(['Hola mundo en csv']*10 + ['jueves'])
        escritor.writerow(['nada']*20 + ['fin'])
        escritor.writerows(matriz) # En plural para difierentes lineas

csv_write()


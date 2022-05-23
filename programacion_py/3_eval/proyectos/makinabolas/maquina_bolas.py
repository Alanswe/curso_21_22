"""
Maquina expendedora
"""
import csv
#ruta = '/home/alan/Documentos/proyectos/makinabolas/' # ruta proyecto suelto
ruta = '/home/alan/Documentos/GitHub/makinabolas/' # ruta proyecto en carpeta de repositorios
MONEDA = 'Euro_1'
BOLA = 'Bola entregada'
CAPACIDAD = 100 #Nº de bolas que caben en la máquina

class Maquina():
    """ 
    Clase que representa la máquina 
    """
    def __init__(self) -> None:
        self.deposito = CAPACIDAD
        self.monedero = 0

    def aceptar_moneda(self, moneda_insertada):
        """ 
        Método para aceptar una moneda y
        devuelve T/F dependiendo si es correcta.
        """
        return moneda_insertada == MONEDA

    def girar_manivela(self,giro):
        """
        Simula el giro de la manivela de la máquina,
        Solo funciona con giros de 360º. 
        """
        return giro == 360

    def soltar_bola(self):
        """
        Si se ha insertado una moneda válida y se ha girado la manivela,
        se suelta una bola.
        Se decrementa el número de bolas.
        Se incrementa el número de bolas
        """
        self.deposito -=1
        self.monedero +=1
        return BOLA

    def leer_estado_csv_0(self):  
        archivo = open(ruta + 'num_bolas_monedero.csv')
        return list(archivo)

    def leer_estado_csv_1(self):  
        archivo = open(ruta + 'num_bolas_monedero.csv')
        for x in archivo:
            return(x)
    
    def leer_estado_csv_2(self):
        csv_in = open(ruta + 'num_bolas_monedero.csv')
        lector_dict = csv.reader(csv_in)
        lista_de_linea = list(lector_dict)
        csv_in.close()
        return lista_de_linea

    def salvar_estado_csv_1(self):
        with open(ruta + 'num_bolas_monedero.csv', 'w') as csv_writer:
            escritor = csv.writer(csv_writer)
            escritor.writerow([self.deposito] + [self.monedero])
            
    # def salvar_estado_csv_2(self): # si se ejecuta cambia la disposición del csv
    #     with open(ruta + 'num_bolas_monedero.csv', 'w') as csv_writer:
    #         escritor = csv.writer(csv_writer)
    #         escritor.writerow(['Bolas'] + [self.deposito])
    #         escritor.writerow(['Monedas'] + [self.monedero])

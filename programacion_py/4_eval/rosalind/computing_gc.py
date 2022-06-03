#https://rosalind.info/problems/gc/
"""
Problem
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

Sample Dataset

>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT

Sample Output

Rosalind_0808
60.919540

"""
import operator # Es para usar la funcion max()

archivo = "/home/alan/Documents/GitHub/curso_21_22/programacion_py/4_eval/rosalind/archivo_computing_gc.txt"

def porcentaje(cadena):
    total = cadena.count('C') + cadena.count('G')
    return total / len(cadena) * 100

def gc_content(archivo):
    cadenas = {}
    datos = ''
    clave = ''
    
    with open(archivo, 'r') as manejador:
        for linea in manejador:
            if linea.startswith('>'):
                if clave:
                    cadenas[clave] = datos
                    datos = ''
                clave = linea[1:].replace('\n','')
            else:
                datos += linea.replace('\n','')
        cadenas[clave] = datos
    
    for k, v in cadenas.items():
        cadenas[k] = porcentaje(v)

    max_key = max(cadenas, key = cadenas.get)
    return max_key, cadenas[max_key]
    
resp = gc_content(archivo)
print(f'{resp[0]}\n{resp[1]:.6f}')

"""
import operator

stats = {'key1':20, 'key2':35, 'key3': 44}
max_key = max(stats, key = stats.get)
print(max_key)
"""

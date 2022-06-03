#https://rosalind.info/problems/rna/
"""
Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.

Sample Dataset
GATGGAACTTGACTACGTAAATT

Sample Output
GAUGGAACUUGACUACGUAAAUU

"""
ejemplo='GATGGAACTTGACTACGTAAATT'

def trancriptor(cadena_dna):
    cadena_rna = cadena_dna.replace('T','U')
    return cadena_rna

print(trancriptor(ejemplo))
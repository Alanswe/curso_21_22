#https://rosalind.info/problems/hamm/

"""
Problem

Figure 2. The Hamming distance between these two strings is 7. Mismatched symbols are colored red.
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).

Sample Dataset
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT

Sample Output
7
"""

ejemplo_1 = 'GAGCCTACTAACGGGAT'
ejemplo_2 = 'CATCGTAATGACGGCCT'

def hamming(s,t):
    contador = 0
    for l in range(len(s)):
        if s[l] != t[l]:
            contador += 1
    return contador

print(hamming(ejemplo_1,ejemplo_2))
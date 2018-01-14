# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 22:27:36 2017

@author: Jeff
"""

codonposs = {'F': 2, 'L': 6, 'I': 3, 'M': 1, 'V': 4, 'S': 6,
             'P': 4, 'T': 4, 'A': 4, 'Y': 2, 'H':2, 'Q': 2, 
             'N':2, 'K':2, 'D': 2, 'E':2, 'C': 2,'W':1, 'R':6,
             'G': 4, 'STOP': 3
             }

def infermRNA(proteinseq):
    possiblemRNA = codonposs['STOP']
    for letter in proteinseq:
        possiblemRNA *= codonposs[letter]
    return possiblemRNA

with open('Test-cases/rosalind_mrna.txt','r') as f:
    value = f.readline().strip()    
    print(infermRNA(value) % 1000000)
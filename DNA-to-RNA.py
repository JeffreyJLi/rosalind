# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 17:28:58 2017

@author: Jeff
"""

with open('test-cases/rosalind_rna.txt','r') as f:
    sequence = f.readline().strip()
    
def DNAtoRNA(DNA):
    RNA = ''
    for base in DNA:
        if base == 'T':
            RNA += 'U'
        else:
            RNA += base
    return RNA

print(DNAtoRNA(sequence))
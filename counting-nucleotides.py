# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 16:09:31 2017

@author: Jeff
"""

def nucleotideCounter(sequencefile):
    with open(sequencefile, 'r') as f:
        sequence = f.readline().strip()
        counts = {'A': 0, 'C': 0, 'G':0, 'T': 0}
        for base in sequence:
            counts[base] += 1
        return str(counts['A']) + ' '+ str(counts['C']) + ' '+ str(counts['G']) + ' '+ str(counts['T'])

print(nucleotideCounter('Test-cases/rosalind_dna.txt'))
        
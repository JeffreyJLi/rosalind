# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 18:28:19 2017

@author: Jeff
"""

with open('test-cases/rosalind_hamm.txt', 'r') as f:
    line1 = f.readline().strip()
    line2 = f.readline().strip()
    
def hamming(seq1, seq2):
    assert len(seq1) == len(seq2), "Sequence lengths not equal"
    hamming = 0
    for bp in range(len(seq1)):
        if seq1[bp] != seq2[bp]:
            hamming += 1
    return hamming

print(hamming(line1, line2))
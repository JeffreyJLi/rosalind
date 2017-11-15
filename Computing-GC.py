# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 18:00:39 2017

@author: Jeff
"""

with open('test-cases/rosalind_gc.txt','r') as f:
    seq = {}
    for line in f: #Formats each sequence into a dictionary with the key as its name.
        line = line.strip()
        if line.startswith('>'):
            label = line[1:]
            seq[label] = ''
        else:
            seq[label] = seq[label] + line

def GCcontent(seqdict):
    GCs = {}
    for name, seq in seqdict.items():
        length = len(seq)
        GC = (seq.count('G') + seq.count('C'))/ length *100
        GCs[name] = GC
    return GCs
        
GC = GCcontent(seq)
maxName = max(GC, key= GC.get) 
maxGC = GC[maxName]
print(maxName)
print(maxGC)
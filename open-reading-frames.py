# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 22:33:47 2017

@author: Jeff
"""
codonTable = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
   "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
   "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
   "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
   "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
   "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
   "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
   "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
   "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
   "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
   "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
   "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
   "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
   "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
   "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
   "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}
import Fastaunwrapper
class mRNA:
    def __init__(self, sequence):
        self.seq = sequence
        
    def translate(self):
        protein = []
        possiblestart = []
        posstrans = []
        revcomp = ''
        for base in self.seq:
            if base == 'A':
                revcomp = 'T' + revcomp
            if base == 'C':
                revcomp = 'G' + revcomp
            if base == 'G':
                revcomp = 'C' + revcomp
            if base == 'T':
                revcomp = 'A' + revcomp
        for a in range(3):
            for x in range(a, len(self.seq), 3):
                codon = self.seq[x:x+3]
                if codon == 'ATG':
                    possiblestart.append(self.seq[x:])
        for a in range(3):
            for x in range(a, len(revcomp),3):
                codon = revcomp[x:x+3]
                if codon == 'ATG':
                    possiblestart.append(revcomp[x:])
        for mRNA in possiblestart:
            for i in range(0, len(mRNA),3):
                rawcodon = mRNA[i:i+3].replace('T', 'U')    
                if rawcodon == "UAA" or rawcodon == "UAG" or rawcodon == "UGA":
                    protein.append('STOP')
                    break
                if len(rawcodon) !=3:
                    break
                protein.append(codonTable[rawcodon])
            protein = ''.join(protein)
            if 'STOP' in protein:
                posstrans.append(protein[:-4])
            protein = []
        return posstrans
    

with open('Test-cases/rosalind_orf.txt','r') as f:
    temp = Fastaunwrapper.unwrap_dict(f)
    rawdata = []
    [rawdata.extend([k,v]) for k,v in temp.items()]
    print(rawdata)
    a = mRNA(rawdata[1])
    answer = a.translate()
    for proteinstring in answer:
        while answer.count(proteinstring) > 1:
            answer.remove(proteinstring)
    for protein in answer:
        print(protein)
                
                
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 13:04:15 2017

@author: Jeff
"""

class uniprotID(object):
    def __init__(self, uniprotID):
        self.id = uniprotID.strip(' ')
    
    def __str__(self):
        return 'Uniprot ID: ' + str(self.id)
    
    def getID(self):
        return self.id
    
    def getURL(self):
        uniprotURL = 'http://www.uniprot.org/uniprot/%s.fasta' % self.id
        return uniprotURL
    
    def getfasta(self):
        import urllib
        f = urllib.request.urlopen(self.getURL())
        rawfasta = f.read().decode('utf-8').splitlines()
        fasta = []
        for line in rawfasta:
            if line.startswith('>'):
                fasta.append(line)
                fasta.append('')
            else:
                fasta[-1] += line
        fasta[0] = self.getID()
        fasta = tuple(fasta) # Makes (ID, Protein Sequence) into a tuple, rather than a list
        return fasta
    
    def nglycotest(self):
        testseq = self.getfasta()[1]
        position = []
        found = False
        answer = ''
        for index in range(len(testseq)-3):
            if testseq[index] == 'N' and testseq[index+1] !='P' and \
            (testseq[index+2] == 'S' or testseq[index+2] =='T') and testseq[index+3] !='P':
                position.append(index+1)
                found = True
        if found == True:
            for item in position:
                answer = answer + str(item) + ' '
            return self.getfasta()[0] + '\n' +str(answer[:-1])
        else:
            return '%s does not contain a N-glycosylation motif.' % self.getfasta()[0]
    
    def findSeq(self, target):
        seq = self.getfasta()[1]
        tofind = target
        foundindexes= []
        for x in range(len(seq)):
            test = seq[x:len(tofind)+x]
            if test == tofind:
                foundindexes.append(x+1)
        return 'Position(s) of ' + str(tofind) + ': ' + str(foundindexes)
                
with open('Test-cases/rosalind_mprt.txt','r') as f:
    for proteinID in f:
        proteinID = proteinID.strip()
        protein = uniprotID(proteinID)
        glycotest = protein.nglycotest()
        if glycotest != "%s does not contain a N-glycosylation motif." % proteinID:
            print(glycotest)
    

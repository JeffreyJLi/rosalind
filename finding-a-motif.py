with open('test-cases/rosalind_subs (2).txt','r') as rawdata:
    seq = rawdata.readline().strip()
    motif = rawdata.readline().strip()
answer = []
for i in range(0, len(seq)):
    if seq[i:len(motif)+i] == motif:
        answer.append(str(i+1))
print(' '.join(answer))
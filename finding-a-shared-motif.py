rawdata = open('test-cases/rosalind_lcsm.txt', 'r')
seqs = []
empty = rawdata.readline()
seq = ''
for line in rawdata:
    line = line.strip()
    if line.startswith('>') == True:
        seqs.append(seq)
        seq = ''
        continue
    else:
        seq = seq + line
seqs.append(seq)
sequence = seqs[0]
commons = ''
comlength =[]
def is_substr(find, data):
    for i in range(1, len(data)):
        if find not in data[i]:
            return False
    return True

answer = ''
for x in range(0, len(sequence)):
    for y in range(len(sequence)-x+1):
        common = sequence[x:x+y]
        if len(common)> len(answer) and is_substr(common, seqs):
            answer = common
print(answer)

rawdata.close()

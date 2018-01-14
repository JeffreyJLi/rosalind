def unwrap_dict(file):
    seq = {}
    for line in file: #Formats each sequence into a dictionary with the key as its name.
        line = line.strip()
        if line.startswith('>'):
            label = line[1:]
            seq[label] = ''
        else:
            seq[label] = seq[label] + line
    return seq

def unwrap_list(file):
    names = []
    seq = []
    temp = ''
    final = []
    for line in file:
        line = line.strip()
        if line.startswith('>'):
            names.append(line[1:])
            seq.append(temp)
            temp = ''
        else:
            temp = temp + line
    seq.append(temp)
    del seq[0] #deletes first initial empty temp name
    for i in range(len(names)):
        final.append(names[i])
        final.append(seq[i])
    return final

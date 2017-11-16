with open('test-cases/rosalind_iprb.txt','r') as f:
    data = f.readline().strip().split(' ')
k = int(data[0])
m = int(data[1])
n = int(data[2])
p = k + m + n

probability = (4*k*(k-1)+3*m*(m-1)+4*(2*k*m+2*k*n+m*n))/(4*p*(p-1))
print(probability)

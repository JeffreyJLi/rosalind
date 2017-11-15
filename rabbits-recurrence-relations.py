# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 17:36:16 2017

@author: Jeff
"""

def totalrabbits(months, litter):
    a, b = 1, 1
    for x in range(2, months):
        a, b = b, litter*a + b
    return b

with open('test-cases/rosalind_fib.txt','r') as f:
    line = f.readline().strip().split(' ')
    n = int(line[0])
    k = int(line[1])
    print(totalrabbits(n,k))
        
    
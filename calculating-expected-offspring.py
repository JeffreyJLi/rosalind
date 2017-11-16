# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 21:32:04 2017

@author: Jeff
"""

def dominantOffspring(couplesList):
    intList = []
    for item in couplesList:
        item = int(item)
        intList.append(item)
    a = intList[0] * 2
    b = intList[1] *2
    c = intList[2] *2
    d = intList[3]*2*0.75
    e = intList[4]*2*0.5
    answer =  a + b + c + d + e
    return answer

with open('test-cases/rosalind_iev.txt', 'r') as f:
    rawdata = f.readline().split(' ')
print(dominantOffspring(rawdata))

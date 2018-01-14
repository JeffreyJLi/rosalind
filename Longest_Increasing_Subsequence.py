# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 18:01:11 2018

@author: Jeff
"""
def binarysearchLIS(seq,sub,index):
    low = 0
    high = len(sub)-1
    
    if seq[index] > seq[sub[-1]]:
        return len(sub)
    while high - low >= 1:
        mid = (high+low) //2
        if seq[index] > seq[sub[mid]]:
            low = mid+1
        else:
            high = mid
    return high

def binarysearchLDS(seq,sub,index):
    low = 0
    high = len(sub)-1
    
    if seq[index] < seq[sub[-1]]:
        return len(sub)
    while high - low >= 1:
        mid = (high+low) //2
        if seq[index] < seq[sub[mid]]:
            low = mid+1
        else:
            high = mid
    return high
    
def LIS(sequence):
    lis = []
    parentlis = [None] * len(sequence)
    for i in range(len(sequence)):
#        print(i, lis, parentlis)
        if len(lis) == 0 or sequence[i] > sequence[lis[-1]]:
            if len(lis) > 0:
                parentlis[i] = lis[-1]
            lis.append(i)
        else:
            j = binarysearchLIS(sequence,lis,i)
#            print(i, sub,j)
            if j != 0:
                parentlis[i] = lis[j-1]
            lis[j] = i
    curr_parent = lis[-1]
    longest_increasing_subsequence = []

    while curr_parent is not None:
        longest_increasing_subsequence.append(str(sequence[curr_parent]))
        curr_parent = parentlis[curr_parent]

    longest_increasing_subsequence.reverse()

    return longest_increasing_subsequence


def LDS(sequence):
    sub = []
    parent = [None] * len(sequence)
    for i in range(len(sequence)):
#        print(i, sub, parent)
        if len(sub) == 0 or sequence[i] < sequence[sub[-1]]:
            if len(sub) > 0:
                parent[i] = sub[-1]
            sub.append(i)
        else:
            j = binarysearchLDS(sequence,sub,i)
#            print(i, sub,j)
            if j != 0:
                parent[i] = sub[j-1]
            sub[j] = i
    curr_parent = sub[-1]
    longest_decreasing_subsequence = []

    while curr_parent is not None:
        longest_decreasing_subsequence.append(str(sequence[curr_parent]))
        curr_parent = parent[curr_parent]

    longest_decreasing_subsequence.reverse()
    return longest_decreasing_subsequence

file = 'test-cases/rosalind_lgis.txt'
with open(file, 'r') as f:
    data = f.readlines()
    data = data[1].strip().split(' ')
    for i in range(len(data)):
        data[i] = int(data[i])
    print('Longest increasing subsequence:')
    print(' '.join(LIS(data)))
    print('Longest decreasing subsequence:')
    print(' '.join(LDS(data)))
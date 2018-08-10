# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 14:46:00 2018

@author: lenovo
"""
# not bad, good, my personal iterative dp solution to rod-cutting 20108 08 10 15:50 Friday
def rod_cutting(p, N):
    '''
    input1: price table
    N: length of rod to be cutted
    output: res1: revenue table,
            res2: relative solution
    '''
    record = {}
    r = {}
    r[0] = 0
    for i in p:
        max1 = float('-inf')        
        for j in range(i):
            if max1 < p[j + 1] + r[i- 1 - j]:
                record[i] = j + 1
                max1 = p[j + 1] + r[i - 1 - j]
        r[i] = max1
    return r, record
N = 10
val = list(range(1, N + 1))
p1 = [1,5,8,9,10,17,17,20,24,30] 
p = dict(zip(val,p1))

res1, res2 = rod_cutting(p, N)
def print_solution(res2, length):
    while res2[length] != length:
        print(res2[length])
        length = length - res2[length]
    print(length)
print_solution(res2, 10)

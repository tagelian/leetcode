# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 18:26:36 2018

@author: lenovo
"""

def knapsack(item, W):
    '''
    k: item number
    v: assosiate value
    w: assosiate weight
    W: package Weight
    return:
        res1: optimal value
        res2: associate solution
    '''
    k = len(item)
    res1 = [[float('-inf') for j in range(W + 1)] for i in range(k + 1)]
    keep = [[0 for j in range(W + 1)] for i in range(k + 1)]
    for j in range(W + 1):
        res1[0][j] = 0
    for i in range(1, k + 1):
        res1[i][0] = 0
    for i in range(1, k + 1):
        for j in range(1, W + 1):
            if item[i][1] <= j:
                if item[i][0] +res1[i - 1][j - item[i][1]] > res1[i - 1][j] :
                    res1[i][j] = item[i][0] +res1[i - 1][j - item[i][1]] 
                    keep[i][j] = 1
                else:
                    res1[i][j] = res1[i - 1][j]
                    
                    
            else:
                res1[i][j] = res1[i - 1][j]
    return res1, keep
    
#    print(res1)
k = list(range(1, 6))
value = [1,6,18,22,28]    
weight = [1,2,5,6,7]
item = {}

for i in range(len(k)):
    item[k[i]] = [value[i], weight[i]]
    

    
result, s = knapsack(item, 11)    
WW = 11
for i in range(len(k),0, -1):
    if s[i][WW] == 1:
        print(i)
        WW = WW - item[i][1]

# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 07:51:30 2018

@author: lenovo
"""
#have something wrong
def dfs(A, start, path, res, k):
    if k == 0:
        return res.append(path + [])
    for i in range(start, len(A)):
        path.append(A[i])
        dfs(A, i + 1, path, res, k -1)
        path.pop()
test = [1,2,3, 4]
res1 = []
res = dfs(test, 0, [], res1, 1)
    


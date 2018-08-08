# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 19:30:21 2018

@author: lenovo
"""

def Bsearch(A, key):
    length = len(A)
    if length == 0:
        return -1
    A.sort()
    left = 0
    right = length - 1
    while left <= right:
        mid = int((left + right) / 2)
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1
test = [0, 0]
print(Bsearch(test, 0))
        
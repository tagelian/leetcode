# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Wed Aug  8 19:22:48 2018
# 
# @author: lenovo
# """
# 33. Search in Rotated Sorted Array
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# 
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# 
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# Example 1:
# 
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# 
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# =============================================================================
# =============================================================================
# difficulty: medium
# acceptance: 32.0%
# contributor: LeetCode
# =============================================================================
# have something wrong, however I think my idea is right. 2018 0808 20:23 Wednesday
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        if length < 2:
            return -1
#        nums.sort()
        def findPivotIndex(A):
            length = len(A)
            if length < 2:
                return 0
            left = 0
            right = length - 1
            mid = int((left + right) / 2)
            if A[0] > A[1]:
                return 0
            if A[length - 1] < A[length - 2]:
                return length - 2
            
            while left <= right:
                mid = int((left + right) / 2)
                if 0 < mid < length - 1:
                    
                    if A[mid + 1] < A[mid]  and A[mid] > A[mid - 1]:
                        return mid
                    elif A[mid] > A[0]:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    break
            return -1
        def Bsearch(A, key):
            length = len(A)
            if length == 0:
                return -1
#            A.sort()
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
        pivot_index = findPivotIndex(nums)
#        if pivot_index  == -1:
            
        res = -1
        if nums[pivot_index + 1] < target < nums[0]:
            return -1
        elif target >= nums[0]:
            temp = nums[0:pivot_index + 1]
            res = Bsearch(temp, target)
        else:
            temp = nums[pivot_index + 1 : length]
            res = Bsearch(temp, target)
            res = res + pivot_index + 1
        return res
#------------------------------------------------------------------------------
# note: below is the test code 
test = [1.1,2,3,4,0,1]
S = Solution() 
result = S.search(test, 0)
print(result)
#------------------------------------------------------------------------------
# note: below is the submission detail
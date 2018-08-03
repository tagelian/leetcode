# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Fri Aug  3 08:41:37 2018
# 
# @author: lenovo
# """
# 1. Two Sum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# 
# Example:
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# =============================================================================
# =============================================================================
# difficulty: easy
# acceptance: 38.6%
# contributor: LeetCode
# =============================================================================
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        d = {}
        for index, item in enumerate(nums):
            if target - item in d:
                return [d[target - item], index]
            d[item] = index
#------------------------------------------------------------------------------
# note: below is the test code 
test1 = [2,8,5,7]
test2 = 9
S = Solution() 
result = S.twoSum(test1, test2)
print(result)
#------------------------------------------------------------------------------
# note: below is the submission detail        
# =============================================================================
# Submission Detail
# 29 / 29 test cases passed.
# 	Status: Accepted
# Runtime: 48 ms
# beats 48.74% python3 submissions	
# Submitted: 0 minutes ago
# =============================================================================

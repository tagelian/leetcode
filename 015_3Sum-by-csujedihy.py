# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Fri Aug  3 14:20:13 2018
# 
# @author: lenovo
# """
# 15. 3Sum
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
# 
# Note:
# 
# The solution set must not contain duplicate triplets.
# 
# Example:
# 
# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
# =============================================================================
# =============================================================================
# difficulty: medium
# acceptance: 21.9%
# contributor: LeetCode
# =============================================================================
# have some problems 
# done at 2018 0803 19:24 Friday 
# not: this version is from csujedihy
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length < 3:
            return []
        result = []
        nums.sort()
        for i in range(length):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            start, end = i + 1, length - 1
            target = 0 - nums[i]
            while start < end:
                if nums[start] + nums[end] > target:
                    end -= 1
                elif nums[start] + nums[end] < target:
                    start += 1
                else:
                    result.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start  < end and nums[start] == nums[start - 1]:
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
        return result
#------------------------------------------------------------------------------
# note: below is the test code 
test = [-1,1,2,0,0,0,0, -1, -4]
test1 = [0,0,0,0]
S = Solution() 
result = S.threeSum(test)
print(result)
#------------------------------------------------------------------------------
# note: below is the submission detail
# =============================================================================
# Submission Detail
# 313 / 313 test cases passed.
# Status: Accepted
# Runtime: 1060 ms
# Submitted: 0 minutes ago
# beats 39.98% python3 submissions
# =============================================================================

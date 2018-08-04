# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Sat Aug  4 12:15:42 2018
# 
# @author: cui
# """
# 18. 4Sum
# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
# 
# Note:
# 
# The solution set must not contain duplicate quadruplets.
# 
# Example:
# 
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
# 
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
# =============================================================================
# =============================================================================
# difficulty: medium
# acceptance: 28.0%
# contributor: LeetCode
# =============================================================================
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length < 4:
            return []
        result = []
        nums.sort()
        for i in range(length):
            if i > 0 and nums[i] == nums[i - 1]:
                continue            
            for j in range(i + 1, length):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue            

                start, end = j + 1, length - 1
                T = target - nums[i] - nums[j]
                while start < end:
                    if nums[start] +  nums[end] > T:
                        end -= 1
                    elif nums[start] + nums[end] < T:
                        start += 1
                    else:
                        result.append([nums[i], nums[j], nums[start], nums[end]])
                        start += 1
                        end -= 1
                        while start < end and nums[start] == nums[start - 1]:
                            start += 1
                        while start < end and nums[end] == nums[end + 1]:
                            end -= 1
        return result
#------------------------------------------------------------------------------
# note: below is the test code 
test = [1, 0, -1, 0, -2, 2]
test1 = [0,0,0,0]
S = Solution() 
result = S.fourSum(test1, 0)
print(result)
#------------------------------------------------------------------------------
# note: below is the submission detail
# =============================================================================
# Submission Detail
# 282 / 282 test cases passed.
# Status: Accepted
# Runtime: 768 ms
# Submitted: 0 minutes ago
# beats 48.76% python3 submissions
# =============================================================================

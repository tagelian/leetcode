# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Sat Aug  4 13:01:02 2018
# 
# @author: cui
# """
# 16. 3Sum Closest
# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
# 
# Example:
# 
# Given array nums = [-1, 2, 1, -4], and target = 1.
# 
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# =============================================================================
# =============================================================================
# difficulty: medium
# acceptance: 32.2%
# contributor: LeetCode
# =============================================================================
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        if length < 3:
            return 0
        nums.sort()
        minimum = float('inf')
        result = 0
        for  i in range(length):
            start, end = i + 1, length - 1
            while start < end:
                sum1 = nums[i] + nums[start] + nums[end]
                if  sum1 > target:
                    if abs(sum1 - target) < minimum:
                        minimum = abs(sum1 - target)
                        result = sum1
                    end -= 1
                else:
                    if abs(sum1 - target) < minimum:
                        minimum = abs(sum1 - target)
                        result = sum1
                    start += 1
        return result                
#------------------------------------------------------------------------------
# note: below is the test code 
test = [-4,-1,1,2]
test1 = [0,0,0,0]
S = Solution() 
result = S.threeSumClosest(test, 1)
print(result)
#------------------------------------------------------------------------------
# note: below is the submission detail
# =============================================================================
# Submission Detail
# 125 / 125 test cases passed.
# Status: Accepted
# Runtime: 276 ms
# Submitted: 0 minutes ago
# beats 19.08% python3 submissions
# =============================================================================

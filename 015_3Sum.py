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
# difficulty: easy
# acceptance: 31.8%
# contributor: LeetCode
# =============================================================================
# have some problems
import bisect
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length < 3:
            return []
        nums.sort()
        zero_pos = bisect.bisect_left(nums, 0)
#        zero_pos
        left = zero_pos - 1
#        mid = zero_pos
#        right = zero_pos

        result = []
        x = 0
        while left >= 0:
            x = nums[left]
#            y = nums[mid]
#            z = nums[right]
            mid = zero_pos
            while mid < length:
                right = mid + 1
                temp = abs(x)
                while right < length and nums[mid] + nums[right] < temp:
                    right += 1
                if nums[mid] + nums[length - 1] < temp:
                    mid += 1                    
                elif right < length and nums[mid] + nums[right] == temp:
                    res = [nums[left], nums[mid], nums[right]]
                    res.sort()
                    if res in result:
                        break
                    else:
                        result.append(res)
                        break
                else:
                    break
            left -= 1
        right1 = zero_pos + 1
        x1 = 0
        while right1 < length:
            x1 = nums[right1]
#            y = nums[mid]
#            z = nums[right]
            mid1 = zero_pos
            while mid1 >= 0:
                left1 = mid1 - 1
                while left1 >= 0 and  abs(nums[mid1] + nums[left1]) < x1:
                    left1 -= 1
                if abs(nums[mid1] + nums[0]) < x1:
                    mid1 -= 1                
                elif left1 >= 0 and abs(nums[mid1] + nums[left1]) == x1:
                    res1 = [nums[left1], nums[mid1], nums[right1]]
                    res1.sort()
                    if res1 in result:
                        break
                    else:
                        result.append(res1)
                        break
                else:
                    break
#                    a = 1
                    
            right1 += 1 
            
        return result        
#------------------------------------------------------------------------------
# note: below is the test code 
test = [-1, 1, 2, -1, -4]
test1 = [0,0,0,0]
S = Solution() 
result = S.threeSum(test)
print(result)
#------------------------------------------------------------------------------
# note: below is the submission detail
#beats 15.44% python3 submissions

# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Thu Aug  2 20:24:31 2018
# 
# @author: lenovo
# """
# 11. Container With Most Water
# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
# 
# Note: You may not slant the container and n is at least 2.
# =============================================================================
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0
        left_index = 0
        right_index = len(height) - 1
        left_height = height[left_index]
        right_height = height[right_index]
        result = min(left_height, right_height) * (right_index - left_index)
        while left_index < right_index:
            if left_height <= right_height:
                left_temp = left_index
                while left_index < right_index and height[left_index + 1] <= left_height:
                    left_index += 1
                left_index += 1
                if left_index < right_index and left_temp != left_index:
                    left_height = height[left_index]                     
                    opt = min(left_height, right_height) * (right_index - left_index)
                    result = max(result, opt)
            else:
                right_temp = right_index
                while right_index > left_index and height[right_index - 1] <= right_height:
                    right_index -= 1
                right_index -= 1
                if right_index > left_index and right_temp != right_index:
                    right_height = height[right_index]
                    opt = min(left_height,right_height) * (right_index - left_index)
                    result = max(result, opt)  
        return result
#------------------------------------------------------------------------------
# note: below is the test code 
test =  [1,8,6,2,5,4,8,3,7]
S = Solution()
result = S.maxArea(test)
print(result) 
#------------------------------------------------------------------------------
# note: below is the submission detail 
# =============================================================================
# Submission Detail
# 50 / 50 test cases passed.
# 	Status: Accepted
# Runtime: 60 ms
# 	beats 91.39% python3 submissions
# Submitted: 0 minutes ago        
# =============================================================================

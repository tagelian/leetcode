# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Fri Aug  3 07:43:24 2018
# 
# @author: lenovo
# """
# 4. Median of Two Sorted Arrays
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# 
# You may assume nums1 and nums2 cannot be both empty.
# 
#  
# 
# Example 1:
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# 
# Example 2:
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5
# =============================================================================
# =============================================================================
# difficulty: hrad
# acceptance: 23.5%
#contributor: LeetCode
# =============================================================================
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = []
        inf = float('inf')
        nums1.append(inf)
        nums2.append(inf)
        i = 0
        j = 0
        for k in range(len(nums1) + len(nums2) - 2):
            if  nums1[i] <= nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        if len(nums3) % 2 == 0:
            return (nums3[int(len(nums3) / 2)] + nums3[int(len(nums3) / 2) - 1]) / 2
        else:
            return nums3[int((len(nums3) - 1) / 2)]
#------------------------------------------------------------------------------
# note: below is the test code 
test1 = [1, 2]
test2 = [2, 3] 
S = Solution()            
result = S.findMedianSortedArrays(test1, test2)
print(result)
#------------------------------------------------------------------------------
# note: below is the submission detail
# =============================================================================
# Submission Detail
# 2084 / 2084 test cases passed.
# 	Status: Accepted
# Runtime: 128 ms
# beats 12.78% python3 submissions		
# Submitted: 0 minutes ago
# =============================================================================

# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Thu Aug  2 08:02:53 2018
# 
# @author: lenovo
# """
#5. Longest Palindromic Substring
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
# 
# Example 1:
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# Example 2:
# 
# Input: "cbbd"
# Output: "bb"
# =============================================================================
# =============================================================================
# difficulty: medium
# acceptance: 25.6%
#contributor: LeetCode
# =============================================================================
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''
        length = len(s)
        d1 = {}
        d2 = {}
        res1 = 1
        res2 = 0
        for index in range(length):
            count = 1
            left = index - 1
            right = index + 1
            while left >= 0 and right < length and s[left] == s[right]:
                count += 2
                left -= 1
                right += 1
#            res1 = max(res1, count)
#            d1[res1] = s[left + 1 : right]
            if count >= res1:
                res1 = count
                d1[res1] = s[left + 1 : right]            
            count2 = 0
            left1 = index 
            right1 = index + 1
            while left1 >= 0 and right1 < length and s[left1] == s[right1]:
                count2 += 2
                left1 -= 1
                right1 += 1
#            res2 = max(res2, count2)
            if count2 >= res2:
                res2 = count2
                d2[res2] = s[left1 + 1 : right1]
        if res1 > res2:
            return d1[res1]
        else:
            return d2[res2]
# =============================================================================
#         d1_maximum_key = 0
#         for u in d1:
#             d1_maximum_key = max(d1_maximum_key, u)
#         d2_maximum_key = 0
#         for v in d2:
#             d2_maximum_key = max(d2_maximum_key, v)            
#         
#             
#             
#         if  d1_maximum_key > d2_maximum_key:
#             return d1[d1_maximum_key]
#         else:
#             return d2[d2_maximum_key]
# =============================================================================
#------------------------------------------------------------------------------
# note: below is the test code 
test = 'ababc'
S = Solution()
result = S.longestPalindrome(test)
print(result) 
#------------------------------------------------------------------------------
# note: below is the submission detail         
# =============================================================================
# Submission Detail
# 103 / 103 test cases passed.
# 	Status: Accepted
# Runtime: 1604 ms
# beats 45.08% python3 submissions		
# Submitted: 0 minutes ago            
# =============================================================================

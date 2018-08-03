# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Fri Aug  3 07:51:32 2018
# 
# @author: lenovo
# """
# 3. Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.
# 
# Examples:
# 
# Given "abcabcbb", the answer is "abc", which the length is 3.
# 
# Given "bbbbb", the answer is "b", with the length of 1.
# 
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
# 
# =============================================================================
# =============================================================================
# difficulty: medium
# acceptance: 24.9%
#contributor: LeetCode
# =============================================================================
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        d = {}
        res = 0
        start = 0
        for index, item in enumerate(s):
            if item in d:
                start = max(start, d[item][-1] + 1)
            res = max(res, index - start + 1)
            d[item]=[]
            d[item].append(index)                
        return res
#------------------------------------------------------------------------------
# note: below is the test code 
test = 'ababa'
S = Solution()            
result = S.lengthOfLongestSubstring(test)
print(result)
#------------------------------------------------------------------------------
# note: below is the submission detail
# =============================================================================
# Submission Detail
# 987 / 987 test cases passed.
# 	Status: Accepted
# Runtime: 104 ms
# beats 43.88% python3 submissions	
# Submitted: 0 minutes ago
# =============================================================================

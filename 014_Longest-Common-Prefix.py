# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Fri Aug  3 14:08:22 2018
# 
# @author: lenovo
# """
# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# Input: ["flower","flow","flight"]
# Output: "fl"
# 
# Example 2:
# 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# Note:
# 
# All given inputs are in lowercase letters a-z.
# =============================================================================
# =============================================================================
# difficulty: easy
# acceptance: 31.8%
# contributor: LeetCode
# =============================================================================
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        strs.sort(key = lambda x: len(x))
        res = []
        pivot = strs[0]
        for j in range(len(pivot)):
            i = 1
            while i < len(strs) and pivot[j] == strs[i][j]:
                i += 1
            if i == len(strs):
                res.append(pivot[j])
            else:
                break
        if len(res) == 0:
            return ''
        else:
            return ''.join(res)
# 2018 08 03 14:17 Friday
# This problem is not so meaningful.
# however, i redo this problem on 2018 0808 Wednesday
#------------------------------------------------------------------------------
# note: below is the test code 
test = ['a', 'b']
S = Solution() 
result = S.longestCommonPrefix(test)
print(result)
#------------------------------------------------------------------------------
# note: below is the submission detail
# =============================================================================
# beats 84.98% python3 submissions
# Submission Detail
# 118 / 118 test cases passed.
# Status: Accepted
# Runtime: 40 ms
# Submitted: 0 minutes ago
# =============================================================================

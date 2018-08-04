# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Sat Aug  4 22:01:56 2018
# 
# @author: lenovo
# """
# 20. Valid Parentheses
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
# 
# Note that an empty string is also considered valid.
# 
# Example 1:
# 
# Input: "()"
# Output: true
# 
# Example 2:
# 
# Input: "()[]{}"
# Output: true
# 
# Example 3:
# 
# Input: "(]"
# Output: false
# 
# Example 4:
# 
# Input: "([)]"
# Output: false
# 
# Example 5:
# 
# Input: "{[]}"
# Output: true
# =============================================================================
# =============================================================================
# difficulty: easy
# acceptance: 34.4%
# contributor: LeetCode
# =============================================================================
# have something wrong 22:28
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False
        n = len(s) / 2
        d1 = {'[':1,
            ']':-1,
            '(':2,
            ')':-2,
            '{':3,
            '}':-3}
        def dfs(left, n):
            if left == n:
                return
            if left < n:
                a = d1[s[left]]
                dfs(left + 1, n)
                b = d1[s[left + 1]]
                if a + b != 0:
                    return False
        dfs(0, n)
        return True
#------------------------------------------------------------------------------
# note: below is the test code 
test = [-1, 1,0, 2, -1, -4]
test1 = [0,0,0,0]
S = Solution() 
#result = S.threeSum(test)
#print(result)
#------------------------------------------------------------------------------
# note: below is the submission detail
#beats 15.44% python3 submissions

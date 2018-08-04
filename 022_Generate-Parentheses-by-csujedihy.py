# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Sat Aug  4 20:01:12 2018
# 
# @author: lenovo
# """
# 22. Generate Parentheses
#  Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# 
# For example, given n = 3, a solution set is:
# 
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
# 
# =============================================================================
# =============================================================================
# difficulty: medium
# acceptance: 49.5%
# contributor: LeetCode
# =============================================================================
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def DFS(left, path, result, n):
            if len(path) == 2 * n:
                if left == 0:
                    result.append(''.join(path))
                return
            if left < n:
                path.append("(")
                DFS(left + 1, path, result, n)
                path.pop()
            if left > 0 :
                path.append(")")
                DFS(left - 1, path, result, n)
                path.pop()
        path = []
        result = []
        DFS(0, path, result, n)
        return result
#------------------------------------------------------------------------------
# note: below is the test code 
test = 2
test1 = [0,0,0,0]
S = Solution() 
result = S.generateParenthesis(test)
print(result)
#------------------------------------------------------------------------------
# note: below is the submission detail
# =============================================================================
# Submission Detail
# 8 / 8 test cases passed.
# 	Status: Accepted
# Runtime: 80 ms
# beats 7.59% python3 submissions	
# Submitted: 0 minutes ago
# =============================================================================

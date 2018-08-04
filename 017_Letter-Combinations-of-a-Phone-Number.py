# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Sat Aug  4 19:52:02 2018
# 
# @author: lenovo
# """
# 17. Letter Combinations of a Phone Number
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
# 
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
# 
# Example:
# 
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# Note:
# 
# Although the above answer is in lexicographical order, your answer could be in any order you want.
# =============================================================================
# =============================================================================
# difficulty: medium
# acceptance: 37.6%
# contributor: LeetCode
# =============================================================================
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        d1 = {'2':['a', 'b', 'c'],
              '3':['d', 'e', 'f'],
              '4':['g', 'h', 'i'],
              '5':['j', 'k', 'l'],
              '6':['m', 'n', 'o'],
              '7':['p', 'q', 'r', 's'],
              '8':['t', 'u', 'v'],
              '9':['w', 'x', 'y', 'z']}
        if '1' in digits or '0' in digits:
            return ['']
        length = len(digits)
        res = []
        path = []
        def dfs(left, path, res, n ):
            if left == n:
                res.append(''.join(path))
                return
            if left < n:
                for v in d1[digits[left]]:
                    path.append(v)
                    dfs(left + 1, path, res, n)
                    path.pop()
        dfs(0, path, res, length)
        return res
#------------------------------------------------------------------------------
# note: below is the test code 
test = '23'
test1 = [0,0,0,0]
S = Solution() 
result = S.letterCombinations(test)
print(result)
#------------------------------------------------------------------------------
# note: below is the submission detail
# =============================================================================
# Submission Detail
# 25 / 25 test cases passed.
# 	Status: Accepted
# Runtime: 36 ms
# beats 15.44% python3 submissions	
# Submitted: 0 minutes ago
# =============================================================================


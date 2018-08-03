# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 10:38:41 2018

@author: lenovo
"""
# =============================================================================
# 13. Roman to Integer
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# 
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
# 
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
# 
#     I can be placed before V (5) and X (10) to make 4 and 9. 
#     X can be placed before L (50) and C (100) to make 40 and 90. 
#     C can be placed before D (500) and M (1000) to make 400 and 900.
# 
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
# 
# Example 1:
# 
# Input: "III"
# Output: 3
# 
# Example 2:
# 
# Input: "IV"
# Output: 4
# 
# Example 3:
# 
# Input: "IX"
# Output: 9
# 
# Example 4:
# 
# Input: "LVIII"
# Output: 58
# Explanation: C = 100, L = 50, XXX = 30 and III = 3.
# 
# Example 5:
# 
# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
# =============================================================================
# =============================================================================
# difficulty: easy
# acceptance: 49.0%
# contributor: LeetCode
# =============================================================================
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0:
            return 0
        d1 = {'IV':4,
              'IX':9,
              'XL':40,
              'XC':90,
              'CD':400,
              'CM':900}
        d2 = {'V':5,
             'L':50,
             'D':500,
             'M':1000}  
        d3 = {'I':1,
             'X':10,
             'C':100
             }
        result = 0
        index = 0
        while index < length:
#        for index, item in enumerate(s):
            item = s[index]
            if item in d3:
                i = index
                number = 0
                while i + 1 < length and s[i + 1] == item:
                    i += 1
                j = i + 1
                if j < length and s[i:j + 1] in d1:
                    number = d1[s[i:j + 1]] + (j - index - 1) * d3[item]
                    result += number
                    index = j + 1
                else:
                    number = (j - index) * d3[item]
                    result += number
                    index = j                    
            else:
                i = index
                number = 0
                while i + 1 < length and s[i + 1] == item:
                    i += 1
                j = i + 1
                number = (j - index) * d2[item]
                result += number                
                index = j
        return result
#------------------------------------------------------------------------------
# note: below is the test code 
test = 'IX'
S = Solution() 
result = S.romanToInt(test)
print(result)
#------------------------------------------------------------------------------
# note: below is the submission detail
# =============================================================================
# Submission Detail
# 3999 / 3999 test cases passed.
# 	Status: Accepted
# Runtime: 156 ms
# 	beats 15.44% python3 submissions
# Submitted: 0 minutes ago
# =============================================================================

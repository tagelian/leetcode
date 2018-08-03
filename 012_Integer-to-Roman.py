# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Fri Aug  3 09:45:35 2018
# 
# @author: lenovo
# """
# 12. Integer to Roman
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
# Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
# 
# Example 1:
# 
# Input: 3
# Output: "III"
# 
# Example 2:
# 
# Input: 4
# Output: "IV"
# 
# Example 3:
# 
# Input: 9
# Output: "IX"
# 
# Example 4:
# 
# Input: 58
# Output: "LVIII"
# Explanation: C = 100, L = 50, XXX = 30 and III = 3.
# 
# Example 5:
# 
# Input: 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
# =============================================================================
# =============================================================================
# difficulty: medium
# acceptance: 47.1%
# contributor: LeetCode
# =============================================================================
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        temp1 = []        
        x = num
        q = int(x / 10)
        r = x - q * 10
        temp1.append(r)
        while q:
            x = q
            q = int(x / 10)
            r = x - q * 10
            temp1.append(r)
#        length_temp1 = len(temp1)
        temp2 = []
        d1 = {0:1,
              1:5,
              2:10,
              3:50,
              4:100,
              5:500,
              6:1000}
        d2 = {1:'I',
             5:'V',
             10:'X',
             50:'L',
             100:'C',
             500:'D',
             1000:'M'}
        for index, item in enumerate(temp1):
#            digit_number = item * pow(10, index)
            temp3 = ''
            if 0 <= item <4:
                temp3 = item * d2[d1[2 * index]]
            elif item == 4:
                temp3 = d2[d1[2 * index]] + d2[d1[2 * index + 1]]
            elif item == 5:
                temp3 = d2[d1[2 * index + 1]]
            elif 5 < item < 9:
                temp3 = d2[d1[2 * index + 1]] + (item - 5) * d2[d1[2 * index]]
            else:
                temp3 = d2[d1[2 * index]] + d2[d1[2 * index + 2]]
            temp2.append(temp3)
        result = ''
        for i in range(len(temp2) - 1, -1, -1):
            result += temp2[i] 
        return result
#------------------------------------------------------------------------------
# note: below is the test code 
test = 606
S = Solution() 
result = S.intToRoman(test)
print(result)
#------------------------------------------------------------------------------
# note: below is the submission detail  
# =============================================================================
# Submission Detail
# 3999 / 3999 test cases passed.
# 	Status: Accepted
# Runtime: 136 ms
# beats 36.72% python3 submissions	
# Submitted: 0 minutes ago       
# =============================================================================

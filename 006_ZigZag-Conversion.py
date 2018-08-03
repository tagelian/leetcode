# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Thu Aug  2 08:47:38 2018
# 
# @author: lenovo
# """
# 6. ZigZag Conversion
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# 
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# Write the code that will take a string and make this conversion given a number of rows:
# 
# string convert(string s, int numRows);
# 
# Example 1:
# 
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# 
# Example 2:
# 
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# 
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# =============================================================================
# =============================================================================
# difficulty: medium
# acceptance: 28.1%
#contributor: LeetCode
# =============================================================================
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        result = []
        for i in range(numRows):
            result.append([])
        n = len(s)
        seg1_length = (2 * numRows - 2)
        seg1_nums = int(n / seg1_length)
        seg1_residual = n % seg1_length
        for i in range(seg1_nums):
            for j in range(numRows):
                result[j].append(s[i * seg1_length + j])
            for k in range(numRows, seg1_length):
                result[seg1_length - k].append(s[i * seg1_length + k])
        if seg1_residual > numRows:
            for i in range(numRows):
                result[i].append(s[seg1_length * seg1_nums + i])
            for k in range(numRows, seg1_residual):
                result[seg1_length - k].append(s[seg1_length * seg1_nums + k])
        else:
            for i in range(seg1_residual):
                result[i].append(s[seg1_length * seg1_nums + i])  
        final = ''
        for w in result:
            for s in w:
                final += s
        return final
#------------------------------------------------------------------------------
# note: below is the test code 
test = 'paypalishiring'
S = Solution()            
res = S.convert(test, 2)
print(res)
#------------------------------------------------------------------------------
# note: below is the submission detail  
# =============================================================================
# =============================================================================
# Submission Detail
# 1158 / 1158 test cases passed.
# 	Status: Accepted
# Runtime: 96 ms
# beats 79.73% python3 submissions	
# Submitted: 0 minutes ago
# =============================================================================

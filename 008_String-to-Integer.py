# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Thu Aug  2 18:37:00 2018
# 
# @author: lenovo
# """
# 8. String to Integer (atoi)
# Implement atoi which converts a string to an integer.
# 
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
# 
# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
# 
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
# 
# If no valid conversion could be performed, a zero value is returned.
# 
# Note:
# 
#     Only the space character ' ' is considered as whitespace character.
#     Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
# 
# Example 1:
# 
# Input: "42"
# Output: 42
# 
# Example 2:
# 
# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus sign.
#              Then take as many numerical digits as possible, which gets 42.
# 
# Example 3:
# 
# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
# 
# Example 4:
# 
# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a numerical 
#              digit or a +/- sign. Therefore no valid conversion could be performed.
# 
# Example 5:
# 
# Input: "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
#              Thefore INT_MIN (−231) is returned.
# 
# 
# =============================================================================
# =============================================================================
# difficulty: medium
# acceptance: 14.1%
#contributor: LeetCode
# =============================================================================
class Solution:
    def myAtoi(self, str1):
        """
        :type str: str
        :rtype: int
        """
        if len(str1) == 0:
            return 0
        i = 0
        while i < len(str1) and str1[i] == ' ':
            i += 1
        sign = 1
        temp1 = 0
        temp2 = 0
        if i < len(str1) and (str1[i] == '-' or str1[i] == '+') :
            if str1[i] == '-':
                sign = -1
            temp1 = i
            i += 1
        if i < len(str1) and (str1[i] == '-' or str1[i] == '+') :
            if str1[i] == '-':
                sign = -1
            temp2 = i            
        if temp1 + 1 == temp2:
            return 0
        numerics = ['0','1','2','3','4','5','6','7','8','9']
        if i == len(str1):
            return 0
        if not (str1[i] in numerics):
            return 0
        else:
            result = 0
            j = i
            while j < len(str1) and str1[j] in numerics:
                j += 1
            for k in range(i, j):
                result += (ord(str1[k]) - ord('0')) * pow(10, (j - k - 1))
            result = sign * result
            minimum = -1 * pow(2, 31)
            if result < minimum:
                return minimum
            maximum = pow(2, 31) - 1
            if result > maximum:
                return maximum
            return result
#------------------------------------------------------------------------------
# note: below is the test code 
S = Solution()
test = '  -606'
#print(test[0] in ['3', '2'])
result = S.myAtoi(test)
print(result)
#------------------------------------------------------------------------------
# note: below is the submission detail 
# =============================================================================
# Submission Detail
# 1079 / 1079 test cases passed.
# 	Status: Accepted
# Runtime: 72 ms
# beats 15.09% python3 submissions	
# Submitted: 0 minutes ago
# =============================================================================

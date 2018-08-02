# =============================================================================
# 7. Reverse Integer
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# Input: 123
# Output: 321
# 
# Example 2:
# 
# Input: -123
# Output: -321
# 
# Example 3:
# 
# Input: 120
# Output: 21
# 
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
# 
# =============================================================================

#------------------------------------------------------------------------------
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        res = []
        quotient = int(abs(x) / 10)
        remainder = abs(x) - quotient * 10
        res.append(remainder)
        while  quotient:
            
            x1 = quotient
            quotient = int(abs(x1) / 10)
            remainder = abs(x1) - quotient * 10
            res.append(remainder)
        result = 0
        for i,d in enumerate(res):
            result += d * pow(10, len(res) - i - 1)  
            

        if x < 0:
            sign = -1


        else:
            sign = 1
        if sign * result < -1 * pow(2,31) or sign * result > pow(2,31) - 1:
            return 0        
        return sign * result
#------------------------------------------------------------------------------
# note: below is the test code 
        
S = Solution()
result = S.reverse(-596)
print(result)            
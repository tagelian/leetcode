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
# =============================================================================
# difficulty: easy
# acceptance: 24.4%
#contributor: LeetCode
# =============================================================================
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = []
        q = int(abs(x) / 10)
        r = abs(x) - q * 10
        res.append(r)
        while  q:
            temp = q
            q = int(temp / 10)
            r = temp - q * 10
            res.append(r)
        result = 0
        length = len(res)
        for i,d in enumerate(res):
            result += d * pow(10, length - i - 1)  
        if x < 0:
            sign = -1
        else:
            sign = 1
        result = sign * result
        if result < -1 * pow(2,31) or result > pow(2,31) - 1:
            return 0        
        return result
#------------------------------------------------------------------------------
# note: below is the test code 
S = Solution()
result = S.reverse(-606)
print(result) 
#------------------------------------------------------------------------------
# note: below is the submission detail  
# =============================================================================
# Submission Detail
# 1032 / 1032 test cases passed.
# 	Status: Accepted
# Runtime: 56 ms
# beats 79.73% python3 submissions		
# Submitted: 0 minutes ago          
# =============================================================================

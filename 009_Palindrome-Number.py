# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Thu Aug  2 19:44:09 2018
# 
# @author: lenovo
# """
# 9. Palindrome Number
# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
# 
# Example 1:
# 
# Input: 121
# Output: true
# 
# Example 2:
# 
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# 
# Example 3:
# 
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Follow up:

# Coud you solve it without converting the integer to a string?
# =============================================================================
# =============================================================================
# difficulty: easy
# acceptance: 37.5%
#contributor: LeetCode
# =============================================================================
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = []
        if x >= 0:
            q = int(x / 10)
            r = abs(x) - q * 10
            temp.append(r)
            while q:
                x = q
                q = int(x / 10)
                r = x - q * 10
                temp.append(r)
            length = len(temp)
            if length % 2 == 1:
                index_mid = int((length- 1) / 2)
                left = index_mid - 1
                right = index_mid + 1
                while left >= 0 and right <= length - 1 and temp[left] == temp[right]:
                    left -= 1
                    right += 1
                if left != -1:
                    return False
                else:
                    return True
            else:
                index_mid = int((length- 1) / 2)
                left = index_mid 
                right = index_mid + 1
                while left >= 0 and right <= length - 1 and temp[left] == temp[right]:
                    left -= 1
                    right += 1
                if left != -1:
                    return False  
                else:
                    return True
        else:
            return False
#------------------------------------------------------------------------------
# note: below is the test code 
test = 121
S = Solution()
result = S.isPalindrome(test)
print(result) 
#------------------------------------------------------------------------------
# note: below is the submission detail  
# =============================================================================
# Submission Detail
# 11508 / 11508 test cases passed.
# 	Status: Accepted
# Runtime: 472 ms
# 	beats 1.37% python3 submissions
# Submitted: 0 minutes ago
# =============================================================================

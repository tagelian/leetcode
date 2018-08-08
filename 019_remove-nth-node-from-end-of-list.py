# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Sat Aug  4 22:29:41 2018
# 
# @author: lenovo
# """
# 19. Remove Nth Node From End of List
# Given a linked list, remove the n-th node from the end of list and return its head.
# 
# Example:
# 
# Given linked list: 1->2->3->4->5, and n = 2.
# 
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# 
# Note:
# 
# Given n will always be valid.
# 
# Follow up:
# 
# Could you do this in one pass?
# =============================================================================
# =============================================================================
# difficulty: easy
# acceptance: 33.8%
# contributor: LeetCode
# =============================================================================
#Definition for singly-linked list.
# have something wrong, however, this problem is not so meaningful. 2018 08 04 22:46 Saturday
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from collections import defaultdict as D
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        d = D(int)
        p = dummy = ListNode(-1)
        dummy.next = head
        count = 0
        while p:
            count += 1
            d[count] = p
            p = p.next
        length = count + 1
        d[length - n - 1].next = d[length - n].next
        return dummy.next
#------------------------------------------------------------------------------
# note: below is the test code 
#test = 'IX'
#S = Solution() 
#result = S.romanToInt(test)
#print(result)
#------------------------------------------------------------------------------
# note: below is the submission detail
# =============================================================================
# Submission Detail
# 208 / 208 test cases passed.
# Status: Accepted
# Runtime: 48 ms
# Submitted: 0 minutes ago
# beats 15.44% python3 submissions
# =============================================================================

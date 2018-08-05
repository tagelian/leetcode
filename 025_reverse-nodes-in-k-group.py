# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Sun Aug  5 08:07:19 2018
# 
# @author: lenovo
# """
# 25. Reverse Nodes in k-Group
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# 
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
# 
# Example:
# 
# Given this linked list: 1->2->3->4->5
# 
# For k = 2, you should return: 2->1->4->3->5
# 
# For k = 3, you should return: 3->2->1->4->5
# 
# Note:
# 
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.
# =============================================================================
# =============================================================================
# difficulty: hard
# acceptance: 32.7%
# contributor: LeetCode
# =============================================================================
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
#------------------------------------------------------------------------------
# note: below is the test code 
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c
test = a
S = Solution() 
result = S.swapPairs(test)
#result = a
while result:
    print(result.val)
    result = result.next
#------------------------------------------------------------------------------
# note: below is the submission detail
# =============================================================================
# Submission Detail
# 55 / 55 test cases passed.
# Status: Accepted
# Runtime: 44 ms
# Submitted: 1 minute ago
# beats 12.10% python3 submissions    
# =============================================================================

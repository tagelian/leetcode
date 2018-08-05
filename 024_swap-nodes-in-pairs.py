# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Sun Aug  5 07:26:35 2018
# 
# @author: lenovo
# """
# 24. Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes and return its head.
# 
# Example:
# 
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# Note:
# 
# Your algorithm should use only constant extra space.
# You may not modify the values in the list's nodes, only nodes itself may be changed.
# =============================================================================
# =============================================================================
# difficulty: medium
# acceptance: 40.2%
# contributor: LeetCode
# =============================================================================
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy2 = ListNode(-1)
        dummy1 = ListNode(-1)
        dummy1.next = dummy2
        dummy2.next = head
        p = dummy1
        res = dummy2
        temp = dummy1
        while p:
            x = p
            y = x.next
            if y:
                temp.next = y
                p = y.next
                y.next = x
                x.next = p
                temp = x
            else:
                temp.next = x
                p = y
        return res.next.next
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

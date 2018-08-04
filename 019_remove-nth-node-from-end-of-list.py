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
# acceptance: 31.8%
# contributor: LeetCode
# =============================================================================
#Definition for singly-linked list.
# have something wrong, however, this problem is not so meaningful. 2018 08 04 22:46 Saturday
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        d = {}
        if head == None:
            return head
        p = head
        index = 1
        while p:
            d[index] = p
            p = p.next
            index += 1
        if  1 < n < index:
            d[index - n].next = d[index - n + 2]
        if n == 1:
            d[index - 1].next = None
        if n == index:
            head = d[2]
        return head
#------------------------------------------------------------------------------
# note: below is the test code 
test = 'IX'
S = Solution() 
#result = S.romanToInt(test)
#print(result)
#------------------------------------------------------------------------------
# note: below is the submission detail
#beats 15.44% python3 submissions
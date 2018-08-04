# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Sat Aug  4 22:47:33 2018
# 
# @author: lenovo
# """
# 21. Merge Two Sorted Lists
# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
# 
# Example:
# 
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
# =============================================================================
# =============================================================================
# difficulty: easy
# acceptance: 42.5%
# contributor: LeetCode
# =============================================================================
#have something wrong with this problem, in border conditions not so bad, so pass
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        p = dummy
        p1 = l1
        while p1:
            p11 = p1
            p1 = p1.next
        if l1:
            p11.next = ListNode(float('inf'))
        p2 = l2
        while p2:
            p22 = p2
            p2 = p2.next
        if l2:
            p22.next = ListNode(float('inf'))
        if l1 == None:
            l1 =ListNode(float('inf')) 
        if l2 == None:
            l2 =ListNode(float('inf'))        
        while (l1.val != float('inf') and l2.val != float('inf'))  and (l1 or l2):
            if l1.val <= l2.val:
                
                p.next = l1
                p = p.next
                l1 = l1.next
            else:
                p.next = l2
                p = p.next
                l2 = l2.next
        return dummy.next
#------------------------------------------------------------------------------
# note: below is the test code 
test = 'IX'
S = Solution() 
#result = S.romanToInt(test)
#print(result)
#------------------------------------------------------------------------------
# note: below is the submission detail
#beats 15.44% python3 submissions
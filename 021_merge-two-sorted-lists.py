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
from collections import defaultdict as D
import heapq as H
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        d = D(int)
        p = dummy = ListNode(-1)
        heap = []
        lists = [l1, l2]
        for u in lists:
            node = u
            if node:
                d[node.val] += 1
                H.heappush(heap, ((node.val, d[node.val]), node))
        while heap:
            val, node = H.heappop(heap)
            p.next = node
            p = p.next
            if node.next:
                node = node.next
                d[node.val] += 1
                H.heappush(heap, ((node.val, d[node.val]), node))
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
# beats 72.54% python3 submissions
# Submission Detail
# 208 / 208 test cases passed.
# Status: Accepted
# Runtime: 48 ms
# Submitted: 0 minutes ago
# =============================================================================

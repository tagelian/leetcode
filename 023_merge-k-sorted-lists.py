# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Tue Aug  7 20:35:41 2018
# 
# @author: cui
# """
# 23. Merge k Sorted Lists
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
# 
# Example:
# 
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6
# =============================================================================
# =============================================================================
# difficulty: hard
# acceptance: 29.5%
# contributor: LeetCode
# =============================================================================
# Definition for singly-linked list.
#import doctest as d
#d.testmod
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
import heapq as h
from collections import defaultdict
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        p = dummy = ListNode(-1)
        dict1 = defaultdict(int)
        for i in range(len(lists)):
            node = lists[i]
            if  not node:
                continue
            else:
                dict1[node.val] += 1
                h.heappush(heap, ((node.val, dict1[node.val]), node))
        while heap:
            val, node = h.heappop(heap)
            p.next = node
            p = p.next
            node = node.next
            if node:
                dict1[node.val] += 1
                h.heappush(heap, ((node.val, dict1[node.val]), node))
        return dummy.next
#d.testmod()
#------------------------------------------------------------------------------
# note: below is the test code 
#a = ListNode(1)
#b = ListNode(2)
#c = ListNode(3)
#a.next = b
#b.next = c
#test = a
#S = Solution() 
#result = S.swapPairs(test)
##result = a
a = ListNode(1)
b = ListNode(4)
c = ListNode(5)

d = ListNode(1)
e = ListNode(3)
f = ListNode(4)

g = ListNode(2)
hh = ListNode(6)

a.next = b
b.next = c

d.next = e
e.next = f

g.next = hh
test = [a, d, g]
s = Solution()
result = s.mergeKLists(test)
#        >print(mergeKLists(test).val)
#        1        
while result:
    print(result.val)
    result = result.next
#------------------------------------------------------------------------------
# note: below is the submission detail
# =============================================================================
# Submission Detail
# 131 / 131 test cases passed.
# Status: Accepted
# Runtime: 84 ms
# Submitted: 0 minutes ago
# beats 12.10% python3 submissions 
# =============================================================================

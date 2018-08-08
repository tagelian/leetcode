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
        def reverseList(head, k):
            pre = None
            cur = head
            while cur and k:
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp
                k -= 1
            return (cur, pre)
        p1 = head
        length = 0
        while p1:
            length += 1
            p1 = p1.next
        if length < k:
            return head
        step = length // k
        p = head
        res = None
        pre = None
        while p and step:
            nextp, newhead = reverseList(p, k)
            if not res:
                res = newhead
            if pre:
                pre.next = newhead
            pre = p
            p = nextp
            step -= 1
        pre.next = p
        return res
#        reverseList(head, k)
# =============================================================================
# def reverseList(head, k):
#     pre = None
#     cur = head
#     while cur and k:
#         temp = cur.next
#         cur.next = pre
#         pre = cur
#         cur = temp
#         k -= 1
#     return (cur, pre)
# =============================================================================
#------------------------------------------------------------------------------
# note: below is the test code 
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d

test = a
S = Solution() 
result = S.reverseKGroup(test, 3)
#result = a
while result:
    print(result.val)
    result = result.next
#------------------------------------------------------------------------------
# note: below is the submission detail
# =============================================================================
# Submission Detail
# 81 / 81 test cases passed.
# Status: Accepted
# Runtime: 56 ms
# Submitted: 0 minutes ago
# beats 93.99% python3 submissions    
# =============================================================================

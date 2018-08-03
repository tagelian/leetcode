# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Fri Aug  3 08:00:29 2018
# 
# @author: lenovo
# """
# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# 
# Example:
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# =============================================================================
#Definition for singly-linked list.
# =============================================================================
# difficulty: medium
# acceptance: 29.0%
#contributor: LeetCode
# =============================================================================
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        add1 = 0
        dummy = ListNode(-1)
        p = dummy
        while p1 or p2:
            if p1 and p2:
                sum1 = p1.val + p2.val + add1
                add1 = 0
                if sum1 >= 10:
                    sum1 = sum1 - 10
                    add1 = 1
                p.next = ListNode(sum1)
                p = p.next
                p1 = p1.next
                p2 = p2.next
            if p1 and not p2:
                sum1 = p1.val + add1
                add1 = 0
                if sum1 >= 10:
                    sum1 -= 10
                    add1 = 1
                p.next = ListNode(sum1)
                p = p.next
                p1 = p1.next
            if p2 and not p1:
                sum1 = p2.val + add1
                add1 = 0
                if sum1 >= 10:
                    sum1 -= 10
                    add1 = 1
                p.next = ListNode(sum1)
                p = p.next
                p2 = p2.next        
            if add1 and p1 == None and p2 == None:
                p.next = ListNode(1)
                p = p.next
                add1 = 0
        return dummy.next
#------------------------------------------------------------------------------
# note: below is the test code 
test1 = ListNode(1)
test2 = ListNode(9)
test2.next = ListNode(9)
S = Solution() 
result = S.addTwoNumbers(test1, test2)
p = result
while p:
    print(p.val)
    p = p.next
#------------------------------------------------------------------------------
# note: below is the submission detail
# =============================================================================
# Submission Detail
# 1563 / 1563 test cases passed.
# 	Status: Accepted
# Runtime: 132 ms
# beats 15.19% python3 submissions		
# Submitted: 0 minutes ago    
# =============================================================================

# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 13:50:47 2018

@author: lenovo
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def reverseLinkList(self, head):
        '''
        input: Node
        return: Node
        '''
        dummy = ListNode(-1)
        dummy.next = head
        if head == None or head.next == None:
            return head
        q = head.next
        p = dummy.next
        q = p.next
        p.next = None
        while q:
            temp = q.next
            q.next = dummy.next
            dummy.next = q
            q = temp
        return dummy.next
def printLinkList(head):
    p = head
    while p:
        print(p.val)
        p = p.next
#------------------------------------------------------------------------------

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
#a.next = b
#b.next = c
#c.next = d
test = a
S = Solution()
res = S.reverseLinkList(test)
printLinkList(res)

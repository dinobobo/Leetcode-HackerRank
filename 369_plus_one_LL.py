# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 16:55:00 2019

@author: DinoBob
"""
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        else:
            if self.carry(head) == 1:
                node = ListNode(1)
                node.next = head
                return node
            else:
                return head
        
        
    def carry(self, head):
        if head == None:
            return 1
        carry = self.carry(head.next)
        if carry == 0:
            return 0
        else:
            carry = (head.val + 1)//10
            head.val = (1 + head.val) % 10
            return carry

x = Solution().plusOne(ListNode(9))
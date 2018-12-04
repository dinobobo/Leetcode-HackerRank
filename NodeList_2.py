# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 17:27:17 2018

@author: DinoBob
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
     def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        cp = ans
        n = 0
        while True:
            if l1 and l2:
                cp.next = ListNode((l1.val + l2.val + n)%10)
                n = (l1.val + l2.val + n)//10
                cp = cp.next
                l1 = l1.next
                l2 = l2.next            
            elif l1 and not l2:
                cp.next = ListNode((l1.val + n)%10)
                cp = cp.next
                n = (l1.val + n)//10
                l1 = l1.next
            elif l2 and not l1:
                cp.next = ListNode((l2.val + n)%10)
                cp = cp.next
                n = (l2.val + n)//10
                l2 = l2.next
            else:
                break
        if n == 1:
            cp.next = ListNode(1)                
        return ans.next 
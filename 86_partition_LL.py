# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 21:37:56 2019

@author: kenzo
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        
        i = head
        while i.next:
            if i.next.val <= x:
                i = i.next
            else:
                j = i.next
                break
                
                
                
        while j and j.next:
            if j.next.val < x:
                node = ListNode(j.next.val)
                i.next, node.next = node, i.next
                j.next = j.next.next
            else:
                j = j.next
        return head
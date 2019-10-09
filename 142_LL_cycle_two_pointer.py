# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:11:04 2019

@author: DinoBob
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #first run to find the node where fast and slow together
        if head == None or head.next == None:
            return None
        f  = head
        s = head
        while f is not None and f.next is not None:
            f = f.next.next
            s = s.next
            if s == f:
                break
        if f == None or f.next == None:
            return None
        f = head
        while f != s:
            f = f.next
            s = s.next
        return f
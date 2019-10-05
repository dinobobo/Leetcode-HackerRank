# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 08:21:40 2019

@author: kenzo
"""

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        rev = ListNode(0)
        sentinel = node = ListNode(0)
        sentinel.next = head
        i = 0
        while i < m - 1:
            node = node.next
            i += 1
        start = node.next
        rev = rev_end = ListNode(start.val)
        j = m
        while j < n:
            j += 1
            rev, rev.next, start = ListNode(start.next.val), rev, start.next            
        node.next = rev
        rev_end.next = start.next
        return sentinel.next
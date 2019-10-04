# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 07:12:24 2019

@author: kenzo
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import deque
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ans = ListNode(None)
        while head:
            remain = ans.next
            ans.next = ListNode(head.val)
            ans.next.next = remain
            head = head.next
        return ans.next